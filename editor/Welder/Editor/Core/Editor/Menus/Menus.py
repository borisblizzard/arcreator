'''
Created on Dec 21, 2010

'''
import wx

import Kernel

class MainMenuBar(wx.MenuBar):
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
        config = Kernel.Config.getUnified()
        filehistory = None
        if "filehistory" in config:
            if isinstance(config["filehistory"], int):
                filehistory = config["filehistory"]
            else:
                Kernel.Log("Invalid setting for FileHistory in configuration", "[FileHistory]", error=True)
        if filehistory is None:
            filehistory = 5
        self.filehistory = wx.FileHistory(filehistory)
        self.filehistory.Load(Kernel.GlobalObjects["WX_config"])

        if "FileHistory" in Kernel.GlobalObjects:
            Kernel.GlobalObjects["FileHistory"] =  self.filehistory
        else:
            Kernel.GlobalObjects.request_new_key("FileHistory", "CORE", self.filehistory)
          
        self.mainwindow = mainwindow

        self.AddMenuItems()

    def AddMenuItems(self):

        recent = wx.Menu()
        self.filehistory.UseMenu(recent)
        self.filehistory.AddFilesToMenu()

        self.Append(wx.ID_ANY, "&Recent Files", recent)

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
        self.mainwindow.Bind(wx.EVT_MENU_RANGE, self.onFileHistory,
                             id=wx.ID_FILE1, id2=wx.ID_FILE9)
        self.mainwindow.Bind(wx.EVT_UPDATE_UI, self.update, self.save)
        self.mainwindow.Bind(wx.EVT_UPDATE_UI, self.update, self.saveas)

    def NewProject(self, event):
        newproject = Kernel.System.load("NewProjectHandler")
        newproject(self.mainwindow)
        self.filehistory.Save(Kernel.GlobalObjects["WX_config"])
        Kernel.GlobalObjects["WX_config"].Flush()

    def OpenProject(self, event):
        openproject = Kernel.System.load("OpenProjectHandler")
        openproject(self.mainwindow, self.filehistory)
        self.filehistory.Save(Kernel.GlobalObjects["WX_config"])
        Kernel.GlobalObjects["WX_config"].Flush()

    def SaveProject(self, event):
        saveproject = Kernel.System.load("SaveProjectHandler")
        saveproject(self.mainwindow)
        self.filehistory.Save(Kernel.GlobalObjects["WX_config"])
        Kernel.GlobalObjects["WX_config"].Flush()

    def SaveProjectAs(self, event):
        saveprojectas = Kernel.System.load("SaveAsProjectHandler")
        saveprojectas(self.mainwindow, self.filehistory)
        self.filehistory.Save(Kernel.GlobalObjects["WX_config"])
        Kernel.GlobalObjects["WX_config"].Flush()

    def onFileHistory(self, event):
        fileNum = event.GetId() - wx.ID_FILE1
        path = self.filehistory.GetHistoryFile(fileNum)
        self.filehistory.AddFileToHistory(path)
        self.filehistory.Save(Kernel.GlobalObjects["WX_config"])
        Kernel.GlobalObjects["WX_config"].Flush()
        openproject = Kernel.System.load("OpenProjectHandler")
        openproject(self.mainwindow, self.filehistory, path)

    def update(self, event):
        if "ProjectOpen" in Kernel.GlobalObjects and Kernel.GlobalObjects["ProjectOpen"]:
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

