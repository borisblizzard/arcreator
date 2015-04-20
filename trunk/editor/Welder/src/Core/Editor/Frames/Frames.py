'''
Created on Sep 11, 2010

Contains all frame classes

Classes in this module
--------------------------------------
CoreEditorMainWindow - main window class

'''
import wx

import wx.lib.agw.aui as aui


import Kernel
from PyitectConsumes import IconManager, MainWindowLayout, MainStatusBar, MainMenuBar

MinEditorSize = (1024, 576)


class AuiManager_DCP_ARC(aui.AuiManager_DCP):

    """

    """

    def _createDummyPane(self):
        """ Creates a Dummy Center Pane (**DCP**). """

        if self.hasDummyPane:
            return

        self.hasDummyPane = True
        #dummy = ShadowPanel(self.GetManagedWindow())
        info = aui.AuiPaneInfo().CenterPane().NotebookDockable(
            True).Name('dummyCenterPane').DestroyOnClose(True)
        #self.AddPane(dummy, info)


class EditorMainWindow(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition,
                 size=MinEditorSize, style=wx.DEFAULT_FRAME_STYLE | wx.SUNKEN_BORDER):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)

        # center the frame
        self.CenterOnScreen()
        self.SetMinSize(MinEditorSize)

        self.main_title = title

        # set the frame icon
        self.SetIcon(IconManager.getIcon("arcicon"))

        self._mgr = AuiManager_DCP_ARC()
        if wx.Platform == "__WXMSW__":
            self._mgr.SetArtProvider(aui.ModernDockArt(self))
        # tell AuiManager to manage this frame
        self._mgr.SetManagedWindow(self)
        self.layout_mgr = None

        # add a status bar and menubar
        self.CreateStatusBar()
        self.CreateMenuBar()
        self.CallLayout()

        self.SetMinSize(MinEditorSize)

        # Kernel.System.bind_event('RefreshProject', )

        self.Bind(wx.EVT_UPDATE_UI, self.updateUI)
        self.Bind(wx.EVT_CLOSE, self.OnClose, self)

        # Bind AUI events
        self.Bind(aui.EVT_AUI_PANE_FLOATING, self.OnFloating)
        self.Bind(aui.EVT_AUI_PANE_FLOATED, self.OnFloated)
        self.Bind(aui.EVT_AUI_PANE_DOCKING, self.OnDocking)
        self.Bind(aui.EVT_AUI_PANE_DOCKED, self.OnDocked)

        # start The autosave Time
        self.AutoSaveTimer = wx.Timer(self)
        # TODO: fix autosave
        #save_intervel = Kernel.Config.getint("Main", "Autosave")
        #self.Bind(wx.EVT_TIMER, self.ProcessAutoSave, self.AutoSaveTimer)
        #self.AutoSaveTimer.Start(save_intervel * 60000, False)

        # show the window
        wx.GetApp().SetTopWindow(self)
        self.Show(True)
        Kernel.System.fire_event("EditorReady")

    def CallLayout(self):
        if self.layout_mgr is not None:
            self.layout_mgr.Refresh()
        else:
            # get the layout component
            self.layout_mgr = MainWindowLayout(self, self._mgr)

    def CreateMenuBar(self):
        self.menubar = MainMenuBar(self)
        self.SetMenuBar(self.menubar)  # Adding the MenuBar to the Frame.
        if "MainMenuBar" in Kernel.GlobalObjects:
            Kernel.GlobalObjects["MainMenuBar"] =  self.menubar
        else:
            Kernel.GlobalObjects.request_new_key(
                "MainMenuBar", "CORE", self.menubar)

    def CreateStatusBar(self):
        self.statusbar = MainStatusBar(self)
        self.SetStatusBar(self.statusbar)
        if "MainStatusBar" in Kernel.GlobalObjects:
            Kernel.GlobalObjects["MainStatusBar"] =  self.menubar
        else:
            Kernel.GlobalObjects.request_new_key(
                "MainStatusBar", "CORE", self.statusbar)

    def ClearLayout(self):
        if self.layout_mgr is not None:
            self.layout_mgr.ClearLayout
        self._mgr.update()

    def updateUI(self, event):
        if "Title" in Kernel.GlobalObjects:
            if Kernel.GlobalObjects["Title"] != "":
                title = self.main_title + " - " + \
                    Kernel.GlobalObjects["Title"]
                if self.GetTitle() != title:
                    self.SetTitle(title)
            else:
                if self.GetTitle() != self.main_title:
                    self.SetTitle(self.main_title)

    def OnClose(self, event):
        self.ProcessClose()
        self.Destroy()
        event.Skip()
        wx.Exit()

    def ProcessClose(self):
        # handle an open project
        Kernel.System.fire_event("CoreExitMainWindow")
        if "ProjectOpen" in Kernel.GlobalObjects and Kernel.GlobalObjects["ProjectOpen"] and "PROJECT" in Kernel.GlobalObjects:
            current_project = Kernel.GlobalObjects["PROJECT"]
            if current_project.hasDataChanged() or current_project.hasInfoChanged():
                message = "There are unsaved changes in the currently open project. Do you want to save these changes?"
                caption = "There is an open project"
                dlg = wx.MessageDialog(self, message, caption, style=wx.YES_NO | wx.YES_DEFAULT)
                result = dlg.ShowModal()
                dlg.Destroy()
                if result == wx.YES:
                    Kernel.System.load("SaveProjectHandler")()

    def ProcessAutoSave(self, event):
        Kernel.System.fire_event("AutoSave")

    def OnFloating(self, event):
        pass

    def OnFloated(self, event):
        # if Kernel.GlobalObjects.has_key("PanelManager"):
        #    PM = Kernel.GlobalObjects["PanelManager"]
        #    if PM.getDockedCenterPanels() <= 1:
        #        PM.dispatchPanel("ShadowPanel", "Shadow Panel")
        pass

    def OnDocking(self, event):
        pass

    def OnDocked(self, event):
        # if Kernel.GlobalObjects.has_key("PanelManager"):
        #    PM = Kernel.GlobalObjects["PanelManager"]
        #    if PM.getDockedCenterPanels() >= 0:
        #        PM.removePanel("Shadow Panel")
        pass

    def OnFocus(self, event):
        if "PanelManager" in Kernel.GlobalObjects:
            PM = Kernel.GlobalObjects["PanelManager"]
            id = PM.getPanelID(self)
            info = PM.getPanelInfo(id)
            if info is not None:
                if info.IsFloating():
                    PM.setLastActive("Shadow Panel")
                else:
                    PM.setLastActive(id)
