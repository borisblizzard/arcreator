'''
Created on Jan 14, 2011

'''
import wx
import wx.lib.agw.aui as aui

from Boot import WelderImport

Kernel = WelderImport('Kernel')
KM = Kernel.Manager

class MainWindowLayout(object):

    def __init__(self, parent, aui_mgr):

        self.parent = parent
        self.aui_mgr = aui_mgr
        self.mgr = KM.get_component("PanelManager").object(self.parent, self.aui_mgr)
        if "PanelManager" in Kernel.GlobalObjects:
            Kernel.GlobalObjects.set_value("PanelManager", self.mgr)
        else:
            Kernel.GlobalObjects.request_new_key("PanelManager", "CORE", self.mgr)

        self.CreateToolbars()
        self.CreateStartPanel()
        self.layout = KM.get_component("ARCModeLayout").object()
        

    def CreateToolbars(self):
        self.maintoolbar = self.mgr.dispatch_panel("MainToolbar", "Main Toolbar")
        self.databasetoolbar = self.mgr.dispatch_panel("DatabaseToolbar", "Database Toolbar")

    def CreateStartPanel(self):
        self.startPanel = self.mgr.dispatch_panel("StartPanel", "Start Panel")

    def ClearLayout(self):
        self.mgr.remove_panel("Main Tool bar")
        self.mgr.remove_panel("Start Panel")
        self.layout.ClearLayout()

    def Refresh(self):
        self.layout.Refresh()
        
class ARCModeLayout(object):
    
    def __init__(self):

        if "PanelManager" in Kernel.GlobalObjects:
            self.mgr = Kernel.GlobalObjects.get_value("PanelManager")
        else:
            raise RuntimeError("The Panel Manager hasn't been created yet")
        self.windows = []
        self.BuildPanes()


    def BuildPanes(self):
        if "ProjectOpen" in Kernel.GlobalObjects and (Kernel.GlobalObjects.get_value("ProjectOpen") == True) and "PROJECT" in Kernel.GlobalObjects:
            self.CreateTilesetView()
            self.CreateTreeCtrl()
            #self.regesterParts()
        # "commit" all changes made to PanelManager
        self.mgr.Update()

    def Refresh(self):
        self.ClearLayout()
        self.BuildPanes()

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