'''
Created on Jan 14, 2011

'''
import Kernel

from PyitectConsumes import PanelManager

class MainWindowLayout(object):

    def __init__(self, parent, aui_mgr):

        self.parent = parent
        self.aui_mgr = aui_mgr
        self.mgr = PanelManager(self.parent, self.aui_mgr)
        if "PanelManager" in Kernel.GlobalObjects:
            Kernel.GlobalObjects["PanelManager"] =  self.mgr
        else:
            Kernel.GlobalObjects.request_new_key("PanelManager", "CORE", self.mgr)

        self.CreateToolbars()
        self.CreateStartPanel()
        self.layout = ARCModeLayout()
        

    def CreateToolbars(self):
        self.maintoolbar = self.mgr.dispatchPanel("MainToolbar", "Main Toolbar")
        self.databasetoolbar = self.mgr.dispatchPanel("DatabaseToolbar", "Database Toolbar")

    def CreateStartPanel(self):
        self.startPanel = self.mgr.dispatchPanel("StartPanel", "Start Panel")

    def ClearLayout(self):
        self.mgr.removePanel("Main Tool bar")
        self.mgr.removePanel("Start Panel")
        self.layout.ClearLayout()

    def Refresh(self):
        self.layout.Refresh()
        
class ARCModeLayout(object):
    
    def __init__(self):

        if "PanelManager" in Kernel.GlobalObjects:
            self.mgr = Kernel.GlobalObjects["PanelManager"]
        else:
            raise RuntimeError("The Panel Manager hasn't been created yet")
        self.windows = []
        self.BuildPanes()


    def BuildPanes(self):
        if "ProjectOpen" in Kernel.GlobalObjects and (Kernel.GlobalObjects["ProjectOpen"] == True) and "PROJECT" in Kernel.GlobalObjects:
            self.CreateTilesetView()
            self.CreateTreeCtrl()
            #self.regesterParts()
        # "commit" all changes made to PanelManager
        self.mgr.update()

    def Refresh(self):
        self.ClearLayout()
        self.BuildPanes()

    def CreateTilesetView(self):
        self.tilesetPanel = self.mgr.dispatchPanel("TilesetPanel", "Tileset Panel")
        self.windows.append("Tileset Panel")

    def CreateTreeCtrl(self):
        self.tilesetPanel = self.mgr.dispatchPanel("MapTreePanel", "Map Tree Panel")
        self.windows.append("Map Tree Panel")

    def ClearLayout(self):
        for window in self.windows:
            self.mgr.removePanel(window)
        #self.importmenuitem.remove_from_menu()
        #self.exportmenuitem.remove_from_menu()
        self.mgr.update()