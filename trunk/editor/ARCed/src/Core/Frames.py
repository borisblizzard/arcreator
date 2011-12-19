'''
Created on Sep 11, 2010

Contains all frame classes

Classes in this module
--------------------------------------
CoreEditorMainWindow - main window class

'''
import os
import sys

import wx

import wx.lib.agw.aui as aui
from wx.lib.agw.aui import aui_switcherdialog as ASD

import Kernel
from Kernel import Manager as KM


MinEditorSize = (1000, 500)

class CoreEditorMainWindow(wx.Frame):
    
    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition,
                 size=MinEditorSize, style=wx.DEFAULT_FRAME_STYLE | wx.SUNKEN_BORDER):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)

        #center the frame
        self.CenterOnScreen()
        self.SetMinSize(MinEditorSize)

        self.main_title = title

        #set the frame icon
        IconManager = KM.get_component("IconManager").object
        self.SetIcon(IconManager.getIcon("arcicon"))

        self._mgr = aui.AuiManager()
        # tell AuiManager to manage this frame
        self._mgr.SetManagedWindow(self)
        self.layout_mgr = None

        #add a status bar and menubar
        self.CreateStatusBar()
        self.CreateMenuBar()
        self.CallLayout()
        
        self.SetMinSize(wx.Size(1000, 500))

        KM.get_event("CoreEventRefreshProject").register(self.CallLayout)

        self.Bind(wx.EVT_UPDATE_UI, self.UpdateUI)
        self.Bind(wx.EVT_CLOSE, self.OnClose, self)

        #start The autosave Time
        self.AutoSaveTimer = wx.Timer(self)
        save_intervel = Kernel.GlobalObjects.get_value("ARCed_config").getint("Main", "Autosave")
        self.Bind(wx.EVT_TIMER, self.ProcessAutoSave, self.AutoSaveTimer)
        self.AutoSaveTimer.Start(save_intervel * 60000, False)

        #show the window
        wx.GetApp().SetTopWindow(self)
        self.Show(True)

    def CallLayout(self):
        if self.layout_mgr is not None:
            self.layout_mgr.Refresh()
        else:
            #get the layout component
            layout = KM.get_component("EditorMainWindowLayout").object
            self.layout_mgr = layout(self, self._mgr)

    def CreateMenuBar(self):
        self.menubar = KM.get_component("MainMenuBar").object(self)
        self.SetMenuBar(self.menubar) #Adding the MenuBar to the Frame.
        if Kernel.GlobalObjects.has_key("MainMenuBar"):
            Kernel.GlobalObjects.set_value("MainMenuBar", self.menubar)
        else:
            Kernel.GlobalObjects.request_new_key("MainMenuBar", "CORE", self.menubar)

    def CreateStatusBar(self):
        self.statusbar = (KM.get_component("MainStatusBar").object(self))
        self.SetStatusBar(self.statusbar)
        if Kernel.GlobalObjects.has_key("MainStatusBar"):
            Kernel.GlobalObjects.set_value("MainStatusBar", self.menubar)
        else:
            Kernel.GlobalObjects.request_new_key("MainStatusBar", "CORE", self.statusbar)

    def ClearLayout(self):
        if self.layout_mgr != None:
            self.layout_mgr.ClearLayout
        self._mgr.Update()

    def UpdateUI(self, event):
        if Kernel.GlobalObjects.has_key("Title"):
            if Kernel.GlobalObjects.get_value("Title") != "":
                title = self.main_title + " - " + Kernel.GlobalObjects.get_value("Title")
                if self.GetTitle() !=  title:
                    self.SetTitle(title)
            else:
                if self.GetTitle() !=  self.main_title:
                    self.SetTitle(self.main_title)

    def OnClose(self, event):
        if event.CanVeto():
            dlg = wx.MessageDialog(self, 
                "Do you really want to close ARCed?",
                "Confirm ARCed Exit", wx.YES_NO|wx.NO_DEFAULT|wx.ICON_QUESTION)
            result = dlg.ShowModal()
            dlg.Destroy()
            if result == wx.ID_YES:
                self.ProcessClose()
                self.Destroy()
                event.Skip()
                wx.Exit()
            else:
                event.Veto()
        else:
            self.ProcessClose()
            self.Destroy()
            event.Skip()
            wx.Exit()

    def ProcessClose(self):
        #handle an open project
        KM.raise_event("CoreExitMainWindow")
        if Kernel.GlobalObjects.has_key("ProjectOpen") and (Kernel.GlobalObjects.get_value("ProjectOpen") == True) and Kernel.GlobalObjects.has_key("PROJECT"):
            current_project = Kernel.GlobalObjects.get_value("PROJECT")
            if current_project.hasDataChanged() or current_project.hasInfoChanged():
                message = "There are unsaved changes in the currently open project Do you want to save these changes?"
                caption = "There is an open project"
                dlg = wx.MessageDialog(self, message, caption, style=wx.YES_NO |
                                       wx.YES_DEFAULT)
                result = dlg.ShowModal()
                dlg.Destroy()
                if result == wx.YES:
                    KM.get_component("SaveProjectHandler").object()

    def ProcessAutoSave(self, event):
        KM.raise_event("CoreEventAutoSave")