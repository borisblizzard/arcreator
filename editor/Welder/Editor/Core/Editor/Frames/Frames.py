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
from PyitectConsumes import IconManager
from PyitectConsumes import MainWindowLayout
from PyitectConsumes import MainStatusBar
from PyitectConsumes import MainMenuBar
from PyitectConsumes import ShadowPanel

MinEditorSize = (1024, 768)


class AuiManager_DCP_ARC(aui.AuiManager_DCP):

    """
    Just in case we ever need to edit the default behavior
    """

    # def _createDummyPane(self):
    #     """ Creates a Dummy Center Pane (**DCP**). """

    #     if self.hasDummyPane:
    #         return

    #     self.hasDummyPane = True
    #     dummy = ShadowPanel(self.GetManagedWindow())
    #     info = (aui.AuiPaneInfo()
    #             .CenterPane()
    #             .NotebookDockable(True)
    #             .Name('ShadowPanel')
    #             .DestroyOnClose(True))
    #     self.AddPane(dummy, info)


class EditorMainWindow(wx.Frame):

    def __init__(
            self,
            parent,
            id=wx.ID_ANY,
            title="",
            pos=wx.DefaultPosition,
            size=MinEditorSize,
            style=wx.DEFAULT_FRAME_STYLE | wx.SUNKEN_BORDER):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)

        # center the frame
        self.CenterOnScreen()
        self.SetMinSize(MinEditorSize)

        self.main_title = title

        # set the frame icon
        self.SetIcon(IconManager.getIcon("welder"))

        self._mgr = AuiManager_DCP_ARC()
        if wx.Platform == "__WXMSW__":
            try:
                import pywin32
                del pywin32
                self._mgr.SetArtProvider(aui.ModernDockArt(self))
            except ImportError:
                pass
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
        self.Bind(aui.EVT_AUI_PANE_FLOATING, self.OnPaneFloating)
        self.Bind(aui.EVT_AUI_PANE_FLOATED, self.OnPaneFloated)
        self.Bind(aui.EVT_AUI_PANE_DOCKING, self.OnPaneDocking)
        self.Bind(aui.EVT_AUI_PANE_DOCKED, self.OnPaneDocked)
        self.Bind(aui.EVT_AUI_PANE_CLOSE, self.OnPaneClosed)

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
            Kernel.GlobalObjects["MainMenuBar"] = self.menubar
        else:
            Kernel.GlobalObjects.newKey("MainMenuBar", "CORE", self.menubar)

    def CreateStatusBar(self):
        self.statusbar = MainStatusBar(self)
        self.SetStatusBar(self.statusbar)
        if "MainStatusBar" in Kernel.GlobalObjects:
            Kernel.GlobalObjects["MainStatusBar"] = self.menubar
        else:
            Kernel.GlobalObjects.newKey("MainStatusBar", "CORE", self.statusbar)

    def ClearLayout(self):
        if self.layout_mgr is not None:
            self.layout_mgr.ClearLayout
        self._mgr.Update()

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
        if ("ProjectOpen" in Kernel.GlobalObjects and
                Kernel.GlobalObjects["ProjectOpen"] and
                "PROJECT" in Kernel.GlobalObjects):
            current_project = Kernel.GlobalObjects["PROJECT"]
            if (current_project.hasDataChanged() or
                    current_project.hasInfoChanged()):
                message = ("There are unsaved changes in the currently "
                           "open project. Do you wish to save these changes?")
                caption = "There is an open project"
                dlg = wx.MessageDialog(
                    self, message, caption, style=wx.YES_NO | wx.YES_DEFAULT)
                result = dlg.ShowModal()
                dlg.Destroy()
                if result == wx.YES:
                    Kernel.System.load("SaveProjectHandler")()

    def ProcessAutoSave(self, event):
        Kernel.System.fire_event("AutoSave")

    def OnPaneFloating(self, event):
        pass

    def OnPaneFloated(self, event):
        # if "PanelManager" in Kernel.GlobalObjects:
        #     PM = Kernel.GlobalObjects["PanelManager"]
        #     if PM.getDockedCenterPanels() <= 1:
        #         wx.CallAfter(PM.dispatchPanel, "ShadowPanel", "ShadowPanel")
        wx.CallAfter(self._mgr.Update)

    def OnPaneDocking(self, event):
        pass

    def OnPaneDocked(self, event):
        # if "PanelManager" in Kernel.GlobalObjects:
        #     PM = Kernel.GlobalObjects["PanelManager"]
        #     if PM.getDockedCenterPanels() >= 0:
        #         wx.CallAfter(PM.removePanel, "ShadowPanel")
        wx.CallAfter(self._mgr.Update)

    def OnPaneClosed(self, event):
        wx.CallAfter(self._mgr.Update)


    def OnFocus(self, event):
        if "PanelManager" in Kernel.GlobalObjects:
            PM = Kernel.GlobalObjects["PanelManager"]
            wid = PM.getPanelID(self)
            info = PM.getPanelInfo(wid)
            if info is not None:
                if info.IsFloating():
                    PM.setLastActive("ShadowPanel")
                else:
                    PM.setLastActive(wid)
