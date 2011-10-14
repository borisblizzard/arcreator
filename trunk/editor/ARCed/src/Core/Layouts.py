'''
Created on Jan 14, 2011

'''
import wx

try:
    from agw import aui
    from agw.aui import aui_switcherdialog as ASD
except ImportError: # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.aui as aui
    from wx.lib.agw.aui import aui_switcherdialog as ASD

import Kernel
from Kernel import Manager as KM

class MainWindowLayout(object):

    def __init__(self, parent, mode):

        self.parent = parent
        self.layout = KM.get_component("ARCModeLayout").object(parent)
        
    def ClearLayout(self):
        self.layout.ClearLayout()
        
class ARCModeLayout(object):
    
    def __init__(self, parent):

        self.parent = parent
        self._mgr = self.parent._mgr
        self.windows = []
        self.BuildPanes()


    def BuildPanes(self):

        self.parent.SetMinSize(wx.Size(1000, 500))
        self.CreateMapEditor()
        self.CreateTilesetView()
        self.CreateTreeCtrl()

        self.regesterParts()

        # "commit" all changes made to AuiManager
        self.parent._mgr.Update()

    def regesterParts(self):
        pluginmenuitem = KM.get_component("PluginMenuItem").object
        self.importmenuitem = pluginmenuitem(self.OnImportMenu,
                                             "Import RMXP Data...")
        self.importmenuitem.add_to_menu()
        self.exportmenuitem = pluginmenuitem(self.OnExportMenu,
                                             "Export RMXP Data...")
        self.exportmenuitem.add_to_menu()

    def OnImportMenu(self, event):
        function = KM.get_component("ProjectImportHandler", "RMXP").object
        function(self.parent)

    def OnExportMenu(self, event):
        function = KM.get_component("ProjectExportHandler", "RMXP").object
        function(self.parent)

    def CreateMapEditor(self):
        mappanel = KM.get_component("MapEditorWindow").object
        self.parent.mapEditerPanel = mappanel(self.parent,
                                              self.parent._notebook_style)
        self._mgr.AddPane(self.parent.mapEditerPanel, aui.AuiPaneInfo().
                                 Name("Map Editor").Caption("Map Editor").
                                 CenterPane().MinimizeButton(True).
                                 CaptionVisible(True).
                                 BestSize(wx.Size(32 * 24, 32 * 18)))
        self.windows.append(self.parent.mapEditerPanel)

    def CreateTilesetView(self):
        self.parent.tilesetscroll = wx.ScrolledWindow(self.parent, wx.ID_ANY)
        self.parent.tilesetpanel = wx.Panel(self.parent.tilesetscroll, wx.ID_ANY)
        self.parent.tilesetscroll.SetScrollbars(32, 32, 8, 50)
        self._mgr.AddPane(self.parent.tilesetscroll, aui.AuiPaneInfo().
                          Name("Tileset").Caption("Tileset").
                          Left().Layer(1).Position(1).
                          MinimizeButton(True).
                          CloseButton(False).
                          BestSize(wx.Size(32 * 8, 32 * 12)))
        self.windows.append(self.parent.tilesetscroll)

    def CreateTreeCtrl(self):
        treectrl = KM.get_component("MainMapTreeCtrl").object
        self.parent.maptree = treectrl(self.parent, self.parent.mapEditerPanel)
        self._mgr.AddPane(self.parent.maptree, aui.
                          AuiPaneInfo().Name("Maps").Caption("Maps").
                          Left().Layer(1).Position(1).
                          MinimizeButton(True).CloseButton(False).
                          BestSize(wx.Size(32 * 8, 32 * 4)))
        self.windows.append(self.parent.maptree)

    def ClearLayout(self):
        for window in self.windows:
            self.parent._mgr.DetachPane(window)
            window.Destroy()
        self.importmenuitem.remove_from_menu()
        self.exportmenuitem.remove_from_menu()