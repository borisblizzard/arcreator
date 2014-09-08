#!/usr/bin/env python
"""
The main Boot code,
shows a splash screen during load 
loads genral and plugin configuration
builds the plugin system
loads the main window
"""
import os
import json
from pathlib import Path


import wx

import Kernel
import Welder

import wx.lib.inspection


class ARCSplashScreen(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Welder",
                style = wx.FRAME_SHAPED | wx.NO_BORDER)

        self.hasShape = False
        self.delta = wx.Point(0,0)

        # Load the image
        splash = Path(Kernel.GlobalObjects["Program_Dir"], 'splash.png')
        image = wx.Image(str(splash), wx.BITMAP_TYPE_PNG)         
        self.bmp = wx.Bitmap(image)

        self.SetClientSize((self.bmp.GetWidth(), self.bmp.GetHeight()))
        self.CenterOnScreen()

        dc = wx.ClientDC(self)
        self.Paint(dc)

        self.SetWindowShape()

        self.textctl_size = (self.bmp.GetWidth() / 2 + 32, self.bmp.GetHeight() / 4 - 32)
        self.textctl_pos = (16, self.bmp.GetHeight() / 4 * 3 + 16)


        self.logctl = wx.TextCtrl(self, wx.ID_ANY, "", self.textctl_pos, self.textctl_size, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_DONTWRAP )
        self.logctl.SetSize(self.textctl_size)
        self.logctl.SetPosition(self.textctl_pos)
        
        self.Bind(wx.EVT_LEFT_DCLICK, self.OnDoubleClick)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)
        self.Bind(wx.EVT_RIGHT_UP, self.OnExit)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_WINDOW_CREATE, self.SetWindowShape)

    def SetWindowShape(self, evt=None):
        r = wx.Region(self.bmp)
        self.hasShape = self.SetShape(r)

    def OnDoubleClick(self, evt):
        if self.hasShape:
            self.SetShape(wx.Region())
            self.hasShape = False
        else:
            self.SetWindowShape()

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        self.Paint(dc)
        self.logctl.SetSize(self.textctl_size)
        self.logctl.SetPosition(self.textctl_pos)

    def Paint(self, dc):
        
        dc.DrawBitmap(self.bmp, 0,0, True)

        string1 = "Version: %s" % Welder.VERSION
        string2 = "\n %s %s (%s)" % (Welder.COPYRIGHT, Welder.AUTHOR, Welder.EMAIL)

        dc.SetFont(wx.Font(wx.FontInfo(10)))
        dc.SetTextBackground(wx.Colour(0, 0, 0))
        dc.SetTextForeground(wx.Colour(255, 255, 255))

        text_size1 = dc.GetFullMultiLineTextExtent(string2)
        text_x = self.bmp.GetWidth() - text_size1[0] - 2
        text_y = self.bmp.GetHeight() - text_size1[1] - 2

        dc.DrawText(string2, text_x, text_y)

        text_size2 = dc.GetFullMultiLineTextExtent(string1)
        text_x = self.bmp.GetWidth() - text_size2[0] - 2
        text_y = self.bmp.GetHeight() - text_size2[1] -  text_size1[2] - 2

        dc.DrawText(string1, text_x, text_y)
        

    def OnExit(self, evt):
        self.Close()

    def OnLeftDown(self, evt):
        self.CaptureMouse()
        pos = self.ClientToScreen(evt.GetPosition())
        origin = self.GetPosition()
        self.delta = wx.Point(pos.x - origin.x, pos.y - origin.y)

    def OnMouseMove(self, evt):
        if evt.Dragging() and evt.LeftIsDown():
            pos = self.ClientToScreen(evt.GetPosition())
            newPos = (pos.x - self.delta.x, pos.y - self.delta.y)
            self.Move(newPos)

    def OnLeftUp(self, evt):
        if self.HasCapture():
            self.ReleaseMouse()

    def Do_Setup(self):
        #load up the editor

        wx_config = wx.FileConfig(appName="Welder", vendorName="arc@chaos-project.com", 
                                    localFilename=os.path.join(Kernel.GetConfigFolder(), "filehistory.cfg"))
        if "WX_config" in Kernel.GlobalObjects:
            Kernel.GlobalObjects["WX_config"] = wx_config
        else:
            Kernel.GlobalObjects.request_new_key("WX_config", "CORE", wx_config)

        #load the plugin configuration
        try:
            programpath = Path(Kernel.GlobalObjects["Program_Dir"], "Plugins.cfg")
            userpath = Path(Kernel.GetConfigFolder(), "Plugins.cfg")
            
            if programpath.exists():
                with programpath.open() as f:
                    Kernel.PluginCFG.updateProgram(json.load(f))
            if userpath.exists():
                with userpath.open() as f:
                    Kernel.PluginCFG.updateUser(json.load(f))
        except:
            #we can theoreticly continue even with out plugin defaults, log and continue
            Kernel.Log("Error Loading Plugin Configuration", "[Main]", True, True)

        #load the genral configuration
        try:
            programpath = Path(Kernel.GlobalObjects["Program_Dir"], "Welder.cfg")
            userpath = Path(Kernel.GetConfigFolder(), "Welder.cfg")
            
            if programpath.exists():
                with programpath.open() as f:
                    Kernel.Config.updateProgram(json.load(f))
            if userpath.exists():
                with userpath.open() as f:
                    Kernel.Config.updateUser(json.load(f))
        except:
            Kernel.Log("Error Loading Configuration", "[Main]", True, True)
            #sadly there is also a ton of things that won't work if the genral configuration didn't load properly so we have to exit
            wx.Exit()

        #build the plugin system
        try:
            #build the system setting up the plugin configuration
            Kernel.buildSystem(Kernel.PluginCFG.getUnified())

            #bind some plugin system informative events
            Kernel.System.bind_event('plugin_found', self.onPluginFound)
            Kernel.System.bind_event('plugin_loaded', self.onPluginLoad)
            Kernel.System.bind_event('component_loaded', self.onComponentLoad)

            #search the Core for all Core plugins
            Kernel.System.search(str(Path(Kernel.GlobalObjects["Program_Dir"], "Core")))
            #search the user Plugin folder for plugins
            Kernel.System.search(Kernel.GetPluginFolder())
        except:
            Kernel.Log("Error Loading Plugins", "[Main]", True, True)
            #we can't recover from this so exit out
            wx.Exit()



        #ok first bind our close method to a system event to be fired when the main editor is fully loaded
        Kernel.System.bind_event("EditorReady", self.Close)
            
        #load up the main editor component and show the window
        MainWindow = Kernel.System.load("EditorMainWindow")
        editor = MainWindow(None, wx.ID_ANY, 'Welder')
        if "EditorMainWindow" in Kernel.GlobalObjects:
            Kernel.GlobalObjects["EditorMainWindow"] = editor
        else:
            Kernel.GlobalObjects.request_new_key("EditorMainWindow", "CORE", editor)

    def onPluginFound (self, path, plugin):
        self.log("Plugin '%s' found at '%s'" % (plugin, path))

    def onPluginLoad (self, plugin, plugin_required, component_needed):
        self.log("Plugin '%s' was loaded by plugin '%s' during a request for the '%s' component" % (plugin, plugin_required, component_needed))

    def onComponentLoad (self, component, plugin_required, plugin_loaded):
        self.log("Component '%s' loaded, required by plugin '%s', loaded from plugin '%s'" % (component, plugin_required, plugin_loaded) )

    def log(self, message):
        self.logctl.AppendText(message + "\n")
        wx.SafeYield()
        print("[Pyitect] %s" % message)

    def BindPyXAL(self):
        PyXAL = KM.get_component("PyXAL").object
        if PyXAL is not None:
            PyXAL.Init(self.frame.GetHandle(), True)
        
        #wx.lib.inspection.InspectionTool().Show()

class ARC_App(wx.App):

    def OnInit(self):
        self.SetAppName("Welder")

        self.SplashScreen = ARCSplashScreen()
        self.SplashScreen.Show()
        self.fc = wx.CallLater(1, Kernel.Protect(self.SplashScreen.Do_Setup, exit_on_fail=True))

        self.keepGoing = True
        return True

def Run(programDir, argv):
    if "ARGV" in Kernel.GlobalObjects:
        Kernel.GlobalObjects["ARGV"] = argv
    else:
        Kernel.GlobalObjects.request_new_key("ARGV", "CORE", argv)

    if "Program_Dir" in Kernel.GlobalObjects:
        Kernel.GlobalObjects["Program_Dir"] = programDir
    else:
        Kernel.GlobalObjects.request_new_key("Program_Dir", "CORE", programDir)

    print("[BOOT] Programming running in %s" % programDir)
    print("[BOOT] Running with arguments: %s" % argv)
    
    provider = wx.SimpleHelpProvider()
    wx.HelpProvider.Set(provider)

    app = ARC_App(False)
    #start up the app, we wont be comming back till the app is closed
    app.MainLoop()

    Kernel.GlobalObjects["WX_config"].Flush()
    # we want to clean up PyXAL as much as we can, it's dead now anyway as the window it was bound to is gone
    # try:
    #     PyXAL = KM.get_component("PyXAL").object
    #     if PyXAL is not None:
    #         PyXAL.Destroy()
    # except:
    #     Kernel.Log("Error destroying PyXAL Binding", "[Main]", error=True)
    # #lets try to save the user's current config before we leave
    # try:
    #     ConfigManager.SaveConfig()
    # except:
    #     Kernel.Log("Error saving Configs", "[Main]", error=True)
