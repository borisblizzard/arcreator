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

    def __init__(self, parent, aui_mgr):

        self.parent = parent
        self.aui_mgr = aui_mgr
        self.PanelManager = KM.get_component("PanelManager").object(self.parent, self.aui_mgr)
        if Kernel.GlobalObjects.has_key("PanelManager"):
            Kernel.GlobalObjects.set_value("PanelManager", self.PanelManager)
        else:
            Kernel.GlobalObjects.request_new_key("PanelManager", "CORE", self.PanelManager)
        self.layout = KM.get_component("ARCModeLayout").object()
        
    def ClearLayout(self):
        self.layout.ClearLayout()
        
class ARCModeLayout(object):
    
    def __init__(self):

        if Kernel.GlobalObjects.has_key("PanelManager"):
            self.mgr = Kernel.GlobalObjects.get_value("PanelManager")
        else:
            raise RuntimeError("The Panel Manager hasn't been created yet")
        self.windows = []
        self.BuildPanes()


    def BuildPanes(self):
        self.CreateStartPanel()
        self.CreateTilesetView()
        self.CreateTreeCtrl()
        #self.regesterParts()
        # "commit" all changes made to PanelManager
        self.mgr.Update()

    #def regesterParts(self):
    #    pluginmenuitem = KM.get_component("PluginMenuItem").object
    #    self.importmenuitem = pluginmenuitem(self.OnImportMenu,
    #                                         "Import RMXP Data...")
    #    self.importmenuitem.add_to_menu()
    #    self.exportmenuitem = pluginmenuitem(self.OnExportMenu,
    #                                         "Export RMXP Data...")
    #    self.exportmenuitem.add_to_menu()

    #def OnImportMenu(self, event):
    #    function = KM.get_component("ProjectImportHandler", "RMXP").object
    #    function(self.parent)

    #def OnExportMenu(self, event):
    #    function = KM.get_component("ProjectExportHandler", "RMXP").object
    #    function(self.parent)

    def CreateStartPanel(self):
        self.startPanel = self.mgr.dispatch_panel("StartPanel", "Start Panel")
        self.windows.append("Start Panel")

    def CreateTilesetView(self):
        self.tilesetPanel = self.mgr.dispatch_panel("TilesetPanel", "Tileset Panel")
        self.windows.append("Tileset Panel")

    def CreateTreeCtrl(self):
        self.tilesetPanel = self.mgr.dispatch_panel("MapTreePanel", "Map Tree Panel")
        self.windows.append("Map Tree Panel")

    def ClearLayout(self):
        for window in self.windows:
            self.mgr.remove_panel(window)
        #self.importmenuitem.remove_from_menu()
        #self.exportmenuitem.remove_from_menu()
        self.mgr.Update()