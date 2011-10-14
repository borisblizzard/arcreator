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

try:
    from agw import aui
    from agw.aui import aui_switcherdialog as ASD
except ImportError: # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.aui as aui
    from wx.lib.agw.aui import aui_switcherdialog as ASD

import Kernel
from Kernel import Manager as KM


class CoreEditorMainWindow(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition,
                 size=wx.Size(1000, 500), style=wx.DEFAULT_FRAME_STYLE | wx.SUNKEN_BORDER):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)

        self._mgr = aui.AuiManager()
        # tell AuiManager to manage this frame
        self._mgr.SetManagedWindow(self)
        # set up default notebook style
        self._notebook_style = aui.AUI_NB_DEFAULT_STYLE | aui.AUI_NB_TAB_EXTERNAL_MOVE | wx.NO_BORDER
        self._notebook_theme = 0
        self._notebook_style ^= aui.AUI_NB_DRAW_DND_TAB
        self.layout_mgr = None
        self.initpanel = wx.Panel(self)
        self._mgr.AddPane(self.initpanel, aui.AuiPaneInfo().CenterPane())

        #add a status bar and menubar
        self.CreateStatusBar()
        self.CreateMenuBar()
        self.CreateToolbar()

        self.SetMinSize(wx.Size(1000, 500))

        KM.get_event("CoreEventRefreshProject").register(self.CallLayout)

        self._mgr.Update()

        #show the window
        self.Show(True)

    def CallLayout(self):
        self.ClearLayout()
        mode = "ARC"
        #get the layout component
        layout = KM.get_component("EditorMainWindowLayout").object
        self.layout_mgr = layout(self, mode)

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

    def CreateToolbar(self):
        self.toolbar = aui.AuiToolBar(self, style=wx.TB_FLAT | wx.TB_HORIZONTAL)
        toolbarlayout = KM.get_component("MainToolbar").object
        self.toolbarlayout = toolbarlayout(self.toolbar, self)
        self._mgr.AddPane(self.toolbar, aui.AuiPaneInfo().
                          Name("Toolbar").Caption("Main Tool Bar").
                          ToolbarPane().Top().Row(1).CloseButton(False))

    def ClearLayout(self):
        if self.initpanel is not None:
            self._mgr.DetachPane(self.initpanel)
            self.initpanel.Destroy()
            self.initpanel = None
        if self.layout_mgr is not None:
            self.layout_mgr.ClearLayout
        self._mgr.Update()



