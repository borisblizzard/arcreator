'''
Created on Dec 2, 2010

the extend-able backend to the main program

Classes in this module
-------------------------------------------
Component - holds a registered extension
Function - holds a registered extension (methods and functions)
Event - container for organizing events and calling attached functions
Type - container for organizing extensions that do the same thing
Package - container for organizing and registering groups of extensions
Manager - the main processor of the Kernel
'''
import os
import sys
import time
import traceback
import inspect
import platform

import pyitect

import configparser
import re

import wx
import wx.lib.agw.pycollapsiblepane as PCP
import collections

#====================================================================================
# Plugin System
#====================================================================================
global System

System = None

def buildSystem(cfg):
    global System
    System = pyitect.System(cfg)

#====================================================================================
# Global Object Storage
#====================================================================================

class GlobalObjectsContainer(object):
    '''
    a storage for global objects where a key is mapped to a list where the first value is a name that represents what created the key and the 
    second value is an object
    '''

    def __init__(self):
        self._objects = {
        }


    def __iter__(self):
        for item in self._objects:
            yield item


    def has_key(self, key):
        if key in self._objects:
            return True
        return False

    def request_new_key(self, key, name="PLUGIN", value=None):
        '''
        find out if a key exits if it does it return a tuple of (False, name) where name is an id for what 
        made the key. if it is made by a CORE component the name is "CORE"
        if the key didn't already exist it makes it and store the provided name and value then returns a tuple (True, name)
        '''
        if key in self._objects:
            return (False, self._objects[key][0])
        else:
            self._objects[key] = [name, value]
            return (True, name)

    def get_name(self, key):
        '''
        gets a name stored with a key key if a key exists other wise returns None
        '''
        if key in self._objects:
            return self._objects[key][0]
        else:
            return None
        
    def get_value(self, key):
        '''
        gets a value stored with a key if a key exists
        '''
        if key in self._objects:
            return self._objects[key][1]

    def __getitem__(self, key):
        if key in self._objects:
            return self._objects[key][1]
        
    def set_value(self, key, value):
        '''
        sets a vlaue stored with a key if a key exists
        '''
        if key in self._objects:
            self._objects[key][1] = value

    def __setitem__(self, key, value):
        if key in self._objects:
            self._objects[key][1] = value

    def remove_key(self, key):
        '''
        removes a key if it exists
        '''
        if key in self._objects:
            del self._objects[key]

    def __delitem__(self, key):
        if key in self._objects:
            del self._objects[key]

    def __len__(self):
        return len(self._objects)


global GlobalObjects
GlobalObjects = GlobalObjectsContainer()

#====================================================================================
# Global Config Storage
#====================================================================================
class ConfigContainer(object):
    '''
    a container to store the config
    '''

    def __init__(self):
        self.user = {}
        self.program = {}

    def updateUser(self, cfg):
        self.user.update(cfg)

    def updateProgram(self, cfg):
        self.program.update(cfg)

    def getUser(self):
        return self.user

    def getProgram(self):
        return self.program

    def getUnified(self):
        '''return the program and user cfg's unified'''
        unif = {}
        unif.update(self.program)
        unif.update(self.user)
        return unif

global Config, PluginCFG
Config = ConfigContainer()
PluginCFG = ConfigContainer()


#====================================================================================
# Status Bar Manager (move to plugin?)
#====================================================================================
class StatusBar(object):
    ''' Manages the interface to the Status Bar '''

    TaskRunning = False
    _status_bar = None
    _previousRanges = []
    _previousSteps = []
    _previousStatus = []
    _tasks_running = 0


    @staticmethod
    def BeginTask(range=10, status=""):
        flag = False
        StatusBar.TaskRunning = True
        if StatusBar._tasks_running > 0:
            flag = True
        wx.BeginBusyCursor()
        StatusBar._tasks_running += 1
        if StatusBar._status_bar is not None:
            StatusBar._status_bar.UpdateProgressBarShow() 
            if flag:
                StatusBar._previousRanges.append(StatusBar._status_bar.GetProgressRange())
                StatusBar._previousSteps.append(StatusBar._status_bar.GetProgress())
                StatusBar._previousStatus.append(StatusBar._status_bar.GetExtraStatus())
            StatusBar._status_bar.SetProgressRange(range)
            StatusBar._status_bar.UpdateProgress(0)
            StatusBar._status_bar.SetExtraStatus(status)
            if range <= 0:
                StatusBar._status_bar.PulseProgress()
        wx.SafeYield(onlyIfNeeded=True)

    @staticmethod
    def EndTask():
        wx.EndBusyCursor()
        StatusBar._tasks_running -= 1
        if StatusBar._tasks_running == 0:
            StatusBar.TaskRunning = False
        if StatusBar._status_bar is not None:
            StatusBar._status_bar.UpdateProgressBarShow() 
            if len(StatusBar._previousRanges) > 0:
                StatusBar._status_bar.SetProgressRange(StatusBar._previousRanges.pop())
            if len(StatusBar._previousSteps) > 0:
                StatusBar._status_bar.UpdateProgress(StatusBar._previousSteps.pop())
            if len(StatusBar._previousStatus) > 0:
                StatusBar._status_bar.SetExtraStatus(StatusBar._previousStatus.pop())
            if StatusBar._tasks_running == 0:
                StatusBar._status_bar.SetExtraStatus("Idle")
        wx.SafeYield(onlyIfNeeded=True)

    @staticmethod
    def UpdateTask(step=0, status=""):
        if StatusBar._status_bar is not None:
            StatusBar._status_bar.UpdateProgressBarShow()
            StatusBar._status_bar.UpdateProgress(step)
            StatusBar._status_bar.SetExtraStatus(status)
            if step < 0:
                StatusBar._status_bar.PulseProgress()
        wx.SafeYield(onlyIfNeeded=True)

    @staticmethod
    def SetTaskSteps(steps=10):
        if StatusBar._status_bar is not None:
            StatusBar._status_bar.UpdateProgressBarShow() 
            StatusBar._status_bar.SetProgressRange(steps)
        wx.SafeYield(onlyIfNeeded=True)

    @staticmethod
    def SetMainStatusText(text):
        if StatusBar._status_bar is not None:
            StatusBar._status_bar.SetMainStatus(text)

    @staticmethod
    def SetStatusBar(bar):
        StatusBar._status_bar = bar
#====================================================================================
# Kernel classes
#====================================================================================

class Manager(object):
    '''The main Kernel processor'''
    events = {}

    @staticmethod
    def register_events(*args):
        '''add passed events to the 'events' dict mapped their their name'''
        for event in args:
            if str(event.name) not in Manager.events:
                Manager.events[str(event.name)] = event

    @staticmethod
    def raise_event(name, *args, **kwargs):
        '''call the event mapped to 'name' and pass extra arguments'''
        Manager.events[str(name)].call(*args, **kwargs)

    @staticmethod
    def has_event(name):
        return str(name) in Manager.events

    @staticmethod
    def get_event(name):
        try:
            return Manager.events[str(name)]
        except KeyError:
            Log("Event '%s' not registered with Kernel" % name)
            return Event("None")



class Event(object):
    '''A data class used as a container for organizing events as their 
    registered methods and methods'''

    def __init__(self, name=""):
        '''initializes a Kernel.Event object
        
        name - a string that uniquely identifies the event, used for retrieval
        '''
        self.name = name
        self.registered = []

    def register(self, function=None, master=None):
        '''registers a function or method to the event
        
        function - the Function or Method object
        master - for methods the objects that is passed as the self parameter
        '''
        if function != None and isinstance(function, collections.Callable):
            self.registered.append([function, master])
        else: raise TypeError("'function' must be a call-able object")

    def unregister(self, function=None, master=None):
        '''removes a function from the list of function to be called'''
        if function != None and isinstance(function, collections.Callable):
            self.registered.remove([function, master])

    def call(self, *args, **kwargs):
        '''calls all the registered function passing all the arguments and 
        keyword arguments passed with the 
        call'''
        for function in self.registered:
            if function[1] != None:
                Protect(function[0], True)(function[1], *args, **kwargs)
            else:
                Protect(function[0], True)(*args, **kwargs)


#====================================================================================
# * Protect (a class to wrap around functions like event handlers to catch errors)
#====================================================================================

class Protect(object):
     def __init__(self, fn, exit_on_fail=False):
         self.fn = fn
         self.exit_on_fail = exit_on_fail

     def __call__(self, *args, **kwargs):
        try:
            result = self.fn(*args, **kwargs)
            return result
        except Exception as excp:
            if inspect.ismethod(self.fn):
                message = "Exception in protected method  '%s' bound to class '%s'" % (self.fn.__name__, self.fn.__self__.__class__.__name__ )
            elif inspect.isfunction(self.fn):
                message = "Exception in protected function %s" % self.fn.__name__
            else:
                message = "Exception in protected call"
            Log(message, inform=True, error=True)
            if self.exit_on_fail:
                wx.Exit()
            return None

#====================================================================================
# * Kernel Functions
#====================================================================================
def GetDataFolder(): 
    path = "" 
    if sys.platform.startswith('win32'): 
        path = os.path.expandvars("%APPDATA%")
    elif sys.platform.startswith('linux'): 
        path = os.path.expanduser(os.path.join("~", ".arc_config"))
    elif sys.platform.startswith('darwin'): 
        path = os.path.expanduser(os.path.join("~", "Library", "Application Support"))
    else:
        raise RuntimeError("Unknown Platform: %s" % sys.platform)
    path = os.path.join(path, "ARC", "Welder")
    if (not os.path.exists(path) or not os.path.isdir(path)):
        os.makedirs(path) 
    return path

def GetConfigFolder():
    path = GetDataFolder()
    path = os.path.join(path, "Config")
    if not os.path.exists(path) or not os.path.isdir(path):
        os.makedirs(path)
    return path

def GetLogFolder():
    path = GetDataFolder()
    path = os.path.join(path, "Logs")
    if not os.path.exists(path) or not os.path.isdir(path):
        os.makedirs(path)
    return path

def GetPluginFolder():
    path = GetDataFolder()
    path = os.path.join(path, "Plugins")
    if not os.path.exists(path) or not os.path.isdir(path):
        os.makedirs(path)
    return path

def Log(message=None, prefix="[Kernel]", inform=False, error=False):
    '''
    time stamps a message and writes it to a log file, it can also attach a trace back of the latest error. 
    always adds a new line at the end of the message
    '''
    try:
        if message == None:
            error = True
            message = ""
        logdir = GetLogFolder()
        f = open(os.path.join(logdir, "Welder.log"), "ab")
        time_str = time.strftime("%a %d %b %Y %H:%M:%S [%Z] ")
        if error:
            error_text = " [Error] " + traceback.format_exc()
        else:
            error_text = ""
        f.write(bytes(time_str + prefix + " " + message + error_text + "\n", 'UTF-8'))
        print(prefix + " " + message + error_text)
        f.close()
        if inform:
            Inform(prefix, message, error)
    except Exception:
        #if this failed then we have no choice but to print the exception and hope for the best. perhaps wx will cache it and print to it's stdout window
        print("There has been an error")
        print(traceback.format_exc())

class ErrorDialog (wx.Dialog):
    
    def __init__(self, prefix, message, error_text):
        wx.Dialog.__init__ (self, None, -1, "Welder Error " + str(prefix), wx.DefaultPosition, (480, -1), wx.DEFAULT_DIALOG_STYLE)

        mainsizer = wx.BoxSizer(wx.VERTICAL)
        message_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.cp = PCP.PyCollapsiblePane(self, label="Details",
                                             agwStyle= wx.CP_NO_TLW_RESIZE|wx.CP_USE_STATICBOX)
        self.btn = wx.Button(self.cp, -1, "Details")
        self.cp.SetButton(self.btn)
        self.Bind(wx.EVT_COLLAPSIBLEPANE_CHANGED, self.OnPaneChanged, self.cp)

        self.error_bmp = wx.StaticBitmap(self, wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_ERROR, wx.ART_OTHER), wx.DefaultPosition, wx.DefaultSize, 0)
        message_sizer.Add(self.error_bmp, 0, wx.ALL, 5)
        
        self.message = wx.StaticText(self, wx.ID_ANY, str(message), wx.DefaultPosition, wx.DefaultSize, 0)
        self.message.Wrap(-1)
        message_sizer.Add(self.message, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 16)
        
        mainsizer.Add(message_sizer, 0, wx.EXPAND, 5)
        
        self.details_tb = wx.TextCtrl(self.cp.GetPane(), wx.ID_ANY, str(error_text), wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
       
        details_sizer = wx.BoxSizer(wx.VERTICAL)
        details_sizer.Add(self.details_tb, 1, wx.EXPAND|wx.ALL, 2)
        self.cp.GetPane().SetSizer(details_sizer)

        mainsizer.Add(self.cp, 1, wx.ALL|wx.EXPAND, 5)
        
        dilg_btn_sizer = wx.StdDialogButtonSizer()
        self.dilg_btn_sizerOK = wx.Button(self, wx.ID_OK)
        dilg_btn_sizer.AddButton(self.dilg_btn_sizerOK)
        dilg_btn_sizer.Realize();
        mainsizer.Add(dilg_btn_sizer, 0, wx.EXPAND, 5)
        
        self.SetSizer(mainsizer)
        self.Layout()
        
        self.Centre(wx.BOTH)

    def OnPaneChanged(self, event=None):

        # redo the layout
        self.Layout()
        
        # and also change the labels
        if self.cp.IsExpanded():
            self.cp.SetLabel("Details <<")
            self.btn.SetLabel("Details <<")
        else:
            self.cp.SetLabel("Details >>")
            self.btn.SetLabel("Details >>")
            
        self.btn.SetInitialSize()

def Inform(title, message, error=False):
    try:
        if wx.GetApp() is not None:
            if error:
                dlg = ErrorDialog(title, message, traceback.format_exc())
                dlg.ShowModal()
            else:
                style = wx.OK|wx.STAY_ON_TOP|wx.ICON_INFORMATION
                dlg = wx.MessageDialog(None, message, caption="Welder "+ title, style=style)
                dlg.ShowModal()
    except Exception:
        #if this fails lets log it with out an inform
        Log("Inform failed: [Message] %s  [Error?] %s" % (message, error), "[Kernel Inform]", error=True)

def parseInt(string):
    hitint = False
    ints = []
    for x in string:
        
        if x.isdigit():
            ints.append(x)
            hitint = True
        else:
            if hitint: break
    return int(''.join(ints))

def parseFloat(string):
    hitint = False
    chars = []
    for x in string:
        if x.isdigit() or x == ".":
            chars.append(x)
            hitint = True
        else:
            if hitint: break
    return float(''.join(chars))

def escapeHTML(string):
    return (
        string
        .replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        .replace("'", "&#39;").replace('"', "&quot;")
    )

def normConfigPath(path):
    return path.replace('/', os.sep)