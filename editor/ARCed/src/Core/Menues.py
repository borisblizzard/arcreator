'''
Created on Dec 21, 2010

'''
import os
import sys
import wx
import Kernel
from Kernel import Manager as KM
import ConfigParser



class CoreMainMenuBar(wx.MenuBar):
    """the main menu bar for the application"""
    def __init__(self, mainwindow):
        wx.MenuBar.__init__(self)
        self.mainwindow = mainwindow
        self.AddMenus()


    def AddMenus(self):
        self.filemenu = FileMenu(self.mainwindow)
        self.Append(self.filemenu, "&File")
        self.projectmenu = ProjectMenu(self.mainwindow)
        self.Append(self.projectmenu, "&Project")

class FileMenu(wx.Menu):

    def __init__(self, mainwindow):
        wx.Menu.__init__(self)
        config = Kernel.GlobalObjects.get_value("ARCed_config")
        file_history_length = None
        try:
            file_history_length = config.getint("Main", "FileHistory")
        except:
            Kernel.Log("Invalid setting for FileHistory in configuration", "[FileHistory]", error=True)
        if file_history_length  is None:
            file_history_length = 5
        self.filehistory = wx.FileHistory(file_history_length)
        self.filehistory.Load(Kernel.GlobalObjects.get_value("WX_config"))

        if Kernel.GlobalObjects.has_key("FileHistory"):
            Kernel.GlobalObjects.set_value("FileHistory", self.filehistory)
        else:
            Kernel.GlobalObjects.request_new_key("FileHistory", "CORE", self.filehistory)
          
        self.mainwindow = mainwindow

        self.AddMenuItems()

    def AddMenuItems(self):

        recent = wx.Menu()
        self.filehistory.UseMenu(recent)
        self.filehistory.AddFilesToMenu()

        self.AppendMenu(wx.ID_ANY, "&Recent Files", recent)

        #add items
        self.new = self.Append(wx.ID_NEW, "&New\tCtrl+N")
        self.open = self.Append(wx.ID_OPEN, "&Open\tCtrl+O")
        self.save = self.Append(wx.ID_SAVE, "&Save\tCtrl+S")
        self.saveas = self.Append(wx.ID_SAVEAS, "S&ave As\tShift+Ctrl+S")
        self.exit = self.Append(wx.ID_EXIT, "E&xit\tCtrl+Q")

        #bind items
        self.mainwindow.Bind(wx.EVT_MENU, self.NewProject, self.new)
        self.mainwindow.Bind(wx.EVT_MENU, self.OpenProject, self.open)
        self.mainwindow.Bind(wx.EVT_MENU, self.SaveProject, self.save)
        self.mainwindow.Bind(wx.EVT_MENU, self.SaveProjectAs, self.saveas)
        self.mainwindow.Bind(wx.EVT_MENU, self.Exit, self.exit)
        self.mainwindow.Bind(wx.EVT_MENU_RANGE, self.on_file_history,
                             id=wx.ID_FILE1, id2=wx.ID_FILE9)
        self.mainwindow.Bind(wx.EVT_UPDATE_UI, self.update, self.save)
        self.mainwindow.Bind(wx.EVT_UPDATE_UI, self.update, self.saveas)

    def NewProject(self, event):
        newproject = KM.get_component("NewProjectHandler").object
        newproject(self.mainwindow)
        self.filehistory.Save(Kernel.GlobalObjects.get_value("WX_config"))
        Kernel.GlobalObjects.get_value("WX_config").Flush()

    def OpenProject(self, event):
        openproject = KM.get_component("OpenProjectHandler").object
        openproject(self.mainwindow, self.filehistory)
        self.filehistory.Save(Kernel.GlobalObjects.get_value("WX_config"))
        Kernel.GlobalObjects.get_value("WX_config").Flush()

    def SaveProject(self, event):
        saveproject = KM.get_component("SaveProjectHandler").object
        saveproject(self.mainwindow)
        self.filehistory.Save(Kernel.GlobalObjects.get_value("WX_config"))
        Kernel.GlobalObjects.get_value("WX_config").Flush()

    def SaveProjectAs(self, event):
        saveprojectas = KM.get_component("SaveAsProjectHandler").object
        saveprojectas(self.mainwindow, self.filehistory)
        self.filehistory.Save(Kernel.GlobalObjects.get_value("WX_config"))
        Kernel.GlobalObjects.get_value("WX_config").Flush()

    def on_file_history(self, event):
        fileNum = event.GetId() - wx.ID_FILE1
        path = self.filehistory.GetHistoryFile(fileNum)
        self.filehistory.AddFileToHistory(path)
        self.filehistory.Save(Kernel.GlobalObjects.get_value("WX_config"))
        Kernel.GlobalObjects.get_value("WX_config").Flush()
        openproject = KM.get_component("OpenProjectHandler").object
        openproject(self.mainwindow, self.filehistory, path)

    def update(self, event):
        if Kernel.GlobalObjects.has_key("ProjectOpen") and (Kernel.GlobalObjects.get_value("ProjectOpen") == True):
            event.Enable(True)
        else:
            event.Enable(False)

    def Exit(self, event):
        self.mainwindow.Close()

class ProjectMenu(wx.Menu):

    object = None

    def __init__(self, mainwindow):
        wx.Menu.__init__(self)
        self.mainwindow = mainwindow
        ProjectMenu.object = self
        self.items = {}

    def AddMenuItem(self, name, function):
        self.items[name] = self.Append(wx.ID_ANY, name)
        self.mainwindow.Bind(wx.EVT_MENU, function, self.items[name])

    def RemoveMenuItem(self, name):
        self.RemoveItem(self.items[name])

class PluginMenuItem(object):

    Menu = ProjectMenu

    def __init__(self, function, name):
        self.function = function
        self.name = name

    def add_to_menu(self):
        PluginMenuItem.Menu.object.AddMenuItem(self.name, self.function)

    def remove_from_menu(self):
        PluginMenuItem.Menu.object.RemoveMenuItem(self.name)

