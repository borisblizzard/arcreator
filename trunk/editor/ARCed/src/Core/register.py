'''
Created on Dec 20, 2010

exports all the core components to the kernel
'''
import Kernel
from Kernel import Manager, Type, SuperType, Component, Package, Event
import RMXP
from Core import Frames
from Core import Menues
from Core import Dialogs
from Core import Controls
from Core import Layouts
from Core import Data
from Core import Project
from Core import ARC_Data
from Core import Actions
from Core import DatabaseActions
from Core import RPGutil
from Core import Icons
from Core import PanelManager
from Core import Panels
from Core import Cache
from Core import PyXAL
from Core import MapEditor
from Core.Database import Actors_Panel
from Core.Database import Classes_Panel
from Core.Database import Skills_Panel
from Core.Database import Items_Panel
from Core.Database import Weapons_Panel
from Core.Database import Armors_Panel
from Core.Database import Enemies_Panel
from Core.Database import Troops_Panel
from Core.Database import States_Panel
from Core.Database import Animations_Panel
from Core.Database import Tilesets_Panel
from Core.Database import CommonEvents_Panel
from Core.Database import System_Panel
from Core.Database import EventEditor_Panel
from Core.Database.ScriptEditor import ScriptEditor_Panel

#=============================================================================
# * RMXP SuperType Declaration
#=============================================================================
class RMXPType(SuperType):

    #---------------------------- data holder --------------------------------
    RPG = Type("RPG")

    def __init__(self):
        SuperType.__init__(self, "RMXP")

        #=====================================================================
        # * add types
        #=====================================================================
        #------------------------- data holder -------------------------------
        self.add_types(self.RPG)



#=============================================================================
# * PanelManager SuperType Declaration
#=============================================================================
class PanelManagerType(SuperType):

    #--------------------------------- Toolbars ----------------------------------
    MainToolbar = Type("MainToolbar")
    DatabaseToolbar = Type("DatabaseToolbar")
    #----------------------------- Panels ------------------------------------
    StartPanel = Type("StartPanel")
    ShadowPanel = Type("ShadowPanel")
    TilesetPanel = Type("TilesetPanel")
    MapTreePanel = Type("MapTreePanel")
    MapEditorPanel = Type("MapEditorPanel")
    #Database
    MainActorsPanel = Type("MainActorsPanel")
    MainClassesPanel = Type("MainClassesPanel")
    MainSkillsPanel = Type("MainSkillsPanel")
    MainItemsPanel = Type("MainItemsPanel")
    MainWeaponsPanel = Type("MainWeaponsPanel")
    MainArmorsPanel = Type("MainArmorsPanel")
    MainEnemiesPanel = Type("MainEnemiesPanel")
    MainTroopsPanel = Type("MainTroopsPanel")
    MainStatesPanel = Type("MainStatesPanel")
    MainAnimationsPanel = Type("MainAnimationsPanel")
    MainTilesetsPanel = Type("MainTilesetsPanel")
    MainCommonEventsPanel = Type("MainCommonEventsPanel")
    MainSystemPanel = Type("MainSystemPanel")
    # Event Editor
    MainEventEditor = Type("MainEventEditor")
    # ScriptEditor
    MainScriptEditorPanel = Type("MainScriptEditorPanel")
    
    def __init__(self):
        SuperType.__init__(self, "PanelManagerType")

        #----------------------------- Panels --------------------------------
        self.add_types(self.StartPanel, self.ShadowPanel, self.TilesetPanel, self.MapTreePanel, self.MainToolbar, 
                       self.MapEditorPanel)
        #Database
        self.add_types(self.MainActorsPanel, self.MainClassesPanel, self.MainSkillsPanel, 
                       self.MainItemsPanel, self.MainWeaponsPanel, self.MainArmorsPanel, self.MainEnemiesPanel, 
                       self.MainTroopsPanel, self.MainStatesPanel, self.MainAnimationsPanel, self.MainTilesetsPanel, 
                       self.MainCommonEventsPanel, self.MainSystemPanel)
        #Event Editor
        self.add_types(self.MainEventEditor)
        #Script Editor
        self.add_types(self.MainScriptEditorPanel)
        #--------------------------------- Toolbars ----------------------------------
        self.add_types(self.MainToolbar, self.DatabaseToolbar)

#=============================================================================
# * Package Declaration
#=============================================================================

class CorePackage(Package):
    def __init__(self):
        Package.__init__(self, "CORE", "CORE")
        self.setup_types()
        self.setup_events()
        self.setup_components()
        

    def setup_types(self):
        #=============================================================================
        # * Type Declaration 
        #=============================================================================
        #------------------------------ functions ------------------------------------
        ARCDataDumpFunction = Type("ARCDataDumpFunction")
        ARCDataLoadFunction = Type("ARCDataLoadFunction")
        ARCProjectSaveFunction = Type("ARCProjectSaveFunction")
        ARCProjectLoadFunction = Type("ARCProjectLoadFunction")

        ARCImageFunctions = Type("ARCImageFunctions")
        ARCRTPFunctions = Type("ARCRTPFunctions")

        #---------------------------- Data handlers ----------------------------------
        Project = Type("Project")
        NewProjectHandler = Type("NewProjectHandler")
        OpenProjectHandler = Type("OpenProjectHandler")
        SaveProjectHandler = Type("SaveProjectHandler")
        SaveAsProjectHandler = Type("SaveAsProjectHandler")
        ARCProjectCreator = Type("ARCProjectCreator")
        ARCProjectHolder = Type("ARCProjectHolder")
        ARCProjectSaver = Type("ARCProjectSaver")
        ARCProjectLoader = Type("ARCProjectLoader")

        #------------------------- data holders ------------------------------
        Table = Type("Table")
        IconManager = Type("IconManager")
        RTPCache = Type("RTPCache")
        RTPPygletCache = Type("RTPPygletCache")
      
        #------------------------------- frames --------------------------------------
        EditorMainWindow = Type("EditorMainWindow")
        
        #-------------------------------- ctrls --------------------------------------
        MapEditorWindow = Type("MapEditorWindow")
        MapTreeCtrl = Type("MapTreeCtrl")
        
        #-------------------------------- layouts ------------------------------------
        EditorMainWindowLayout = Type("EditorMainWindowLayout")
        ARCModeLayout = Type("ARCModeLayout")
        PanelManager = Type("PanelManager")
            
        #-------------------------------- menus --------------------------------------
        MainMenuBar = Type("MainMenuBar")
        MainStatusBar = Type("MainStatusBar")
        ProjectMenuItems = Type("ProjectMenuItems")
        PluginMenuItem = Type("PluginMenuItem")
        
        #------------------------------- dialogs -------------------------------------
        NewProjectDialog = Type("NewProjectDialog")
        
        #-------------------------------actions---------------------------------------
        ActionManager = Type("ActionManager")
        ActionTemplate = Type("ActionTemplate")

        TableEditAction = Type("TableEditAction")
        ARCActorEditAction = Type("ARCActorEditAction")

        #------------------------------ utilities ------------------------------------
        PyXAL = Type("PyXAL")

        #=====================================================================
        # * add the types to be registered 
        #=====================================================================
        #------------------------------ super types ----------------------------------
        self.add_types(RMXPType(), PanelManagerType())
        
        #------------------------------- functions -----------------------------------
        self.add_types(ARCDataDumpFunction, ARCDataLoadFunction, ARCProjectSaveFunction, 
                       ARCProjectLoadFunction, ARCImageFunctions, ARCRTPFunctions)
        
        #------------------------------ data handlers --------------------------------
        self.add_types(Project, NewProjectHandler, OpenProjectHandler, SaveProjectHandler, 
                               SaveAsProjectHandler, ARCProjectCreator, ARCProjectHolder,
                               ARCProjectSaver, ARCProjectLoader)

        #------------------------- data holders ------------------------------
        self.add_types(Table, IconManager, RTPCache, RTPPygletCache)
        
        #-------------------------------- frames -------------------------------------
        self.add_types(EditorMainWindow)

        #-------------------------------- ctrls --------------------------------------
        self.add_types(MapEditorWindow, MapTreeCtrl)
        
        #-------------------------------- layouts --------------------------------
        self.add_types(EditorMainWindowLayout, ARCModeLayout, PanelManager)
        
        #-------------------------------- menus --------------------------------------
        self.add_types(MainMenuBar, MainStatusBar, ProjectMenuItems,
                               PluginMenuItem)
        
        #-------------------------------- dialogs ------------------------------------
        self.add_types(NewProjectDialog)
        
        #-------------------------------actions---------------------------------------
        self.add_types(ActionManager, ActionTemplate)

        self.add_types(TableEditAction)

        self.add_types(ARCActorEditAction)

        #------------------------------ utilities ------------------------------------
        self.add_types(PyXAL)
        
    def setup_events(self):
        #=============================================================================
        # * events
        #=============================================================================
       
        CoreEventOpenProject = Event("CoreEventOpenProject")
        CoreEventRefreshProject = Event("CoreEventRefreshProject")
        CoreEventUpdateProjectMenu = Event("CoreEventUpdateProjectMenu")
        CoreEventARCRedirectClassPathsOnSave = Event("CoreEventARCRedirectClassPathsOnSave")
        CoreEventARCRedirectClassPathsOnLoad = Event("CoreEventARCRedirectClassPathsOnLoad")
        CoreEventARCExtendNamespaceOnLoad = Event("CoreEventARCExtendNamespaceOnLoad")
        CoreExitMainWindow = Event("CoreExitMainWindow")
        CoreEventAutoSave = Event("CoreEventAutoSave")
        
        #=====================================================================
        # * add the events to be registered 
        #=====================================================================
        
        self.add_events(CoreEventOpenProject, CoreEventRefreshProject, CoreEventUpdateProjectMenu,
                        CoreEventARCRedirectClassPathsOnSave, CoreEventARCRedirectClassPathsOnLoad,
                        CoreEventARCExtendNamespaceOnLoad, CoreExitMainWindow, CoreEventAutoSave)
        
        #=====================================================================
        # * add event hooks to be registered
        #=====================================================================
        self.add_event_hook("CoreEventARCExtendNamespaceOnLoad", RMXP.RGSS1_RPG.extend_namespace,  RMXP.RGSS1_RPG)

    def setup_components(self):
        #=====================================================================
        # * add components (main components)
        #=====================================================================

        #--------------------------- functions -------------------------------
        self.add_component(Component(ARC_Data.ARC_Dump.dump, "ARCDataDumpFunction",
                                     None, "CoreARCDataDumpFunction", "CORE",
                                     1.0, self))
        self.add_component(Component(ARC_Data.ARC_Dump.load, "ARCDataLoadFunction",
                                     None, "CoreARCDataLoadFunction", "CORE",
                                     1.0, self))
        self.add_component(Component(Project.ARCProjectSaveFunction, "ARCProjectSaveFunction", 
                                     None, "CoreARCProjctSaveFunction", "CORE", 
                                     1.0, self))
        self.add_component(Component(Project.ARCProjectLoadFunction, "ARCProjectLoadFunction", 
                                     None, "CoreARCProjectLoadFunction", "CORE", 
                                     1.0, self))
        self.add_component(Component(Cache.ImageFunctions, "ARCImageFunctions", 
                                     None, "CoreARCImageFunctions", "CORE", 
                                     1.0, self))
        self.add_component(Component(Cache.RTPFunctions, "ARCRTPFunctions", 
                                     None, "CoreARCRTPFunctions", "CORE",
                                     1.0, self))

        #-------------------------- data Handler -----------------------------
        self.add_component(Component(Data.NewProject, "NewProjectHandler",
                                     None, "CoreNewProjectHandler", "CORE",
                                     1.0, self))
        self.add_component(Component(Data.OpenProject, "OpenProjectHandler",
                                     None, "CoreOpenProjectHandler", "CORE",
                                     1.0, self))
        self.add_component(Component(Data.SaveProject, "SaveProjectHandler",
                                     None, "CoreSaveProjectHandler", "CORE",
                                     1.0, self))
        self.add_component(Component(Data.SaveProjectAS, "SaveAsProjectHandler",
                                     None, "CoreSaveAsProjectHandler", "CORE",
                                     1.0, self))
        self.add_component(Component(Project.ARCProjectCreator, "ARCProjectCreator",
                                     None, "CoreARCProjectCreator", "CORE",
                                     1.0, self))
        self.add_component(Component(Project.Project, "ARCProjectHolder",
                                     None, "CoreARCProjectHolder", "CORE",
                                     1.0, self))
        self.add_component(Component(Project.ARCProjectSaver, "ARCProjectSaver",
                                     None, "CoreARCProjectSaver", "CORE",
                                     1.0, self))
        self.add_component(Component(Project.ARCProjectLoader, "ARCProjectLoader",
                                     None, "CoreARCProjectLoader", "CORE",
                                     1.0, self))

        #------------------------- data holders ------------------------------
        self.add_component(Component(RPGutil.Table, "Table", 
                                     None, "CoreTable", "CORE", 
                                     1.0, self))
        self.add_component(Component(Icons.IconManager, "IconManager",
                                     None, "CoreIconManager", "CORE", 
                                     1.0, self))
        self.add_component(Component(Cache.PILCache, "RTPCache",
                                     None, "CoreRTPCache", "CORE",
                                     1.0, self))
        self.add_component(Component(Cache.PygletCache, "RTPPygletCache",
                                     None, "CoreRTPPygletCache", "CORE",
                                     1.0, self))

        #---------------------------- frames ---------------------------------
        self.add_component(Component(Frames.CoreEditorMainWindow,
                                     "EditorMainWindow", None,
                                     "CoreEditorMainWindow", "CORE",
                                     1.0, self))

        #----------------------------- ctrls ---------------------------------
        self.add_component(Component(Controls.WxRMXPMapPanel,
                                     "MapEditorWindow", None,
                                     "WxRMXPMapWindow", "CORE", 1.0, self))
        self.add_component(Component(Controls.MapTreeCtrl,
                                     "MapTreeCtrl", None,
                                     "CoreMapTreeCtrl", "CORE", 1.0,
                                     self))
        

        #----------------------------- layouts -------------------------------
        self.add_component(Component(Layouts.MainWindowLayout,
                                     "EditorMainWindowLayout", None,
                                     "CoreEditorMainWindowLayout", "CORE", 1.0, self))
        self.add_component(Component(Layouts.ARCModeLayout,
                                     "ARCModeLayout", None,
                                     "CoreARCModeLayout", "CORE", 1.0, self))
        self.add_component(Component(PanelManager.PanelManager,
                                     "PanelManager", None,
                                     "CorePanelManager", "CORE", 1.0, self))

        #----------------------------- menus ---------------------------------
        self.add_component(Component(Menues.CoreMainMenuBar, "MainMenuBar",
                                     None, "CoreMainMenuBar", "CORE", 1.0,
                                     self))
        self.add_component(Component(Controls.MainStatusBar,
                                     "MainStatusBar", None, "CoreStatusBar",
                                     "CORE", 1.0, self))
        self.add_component(Component(Menues.PluginMenuItem, "PluginMenuItem",
                                     None, "CorePluginMenuItem", "CORE",
                                     1.0, self))

        #---------------------------- dialogs --------------------------------
        self.add_component(Component(Dialogs.NewProjectDialog,
                                     "NewProjectDialog", None,
                                     "CoreNewProjectDialog", "CORE", 1.0, self))

        #-------------------------------actions---------------------------------------
        self.add_component(Component(Actions.ActionManager, "ActionManager",
                                     None, "CoreActionManager", "CORE", 1.0, self))
        self.add_component(Component(Actions.ActionTemplate, "ActionTemplate",
                                     None, "CoreActionTemplate", "CORE", 1.0, self))
        
        self.add_component(Component(DatabaseActions.TableEditAction, "TableEditAction",
                                     None, "CoreTableEditAction", "CORE", 1.0, self))

        self.add_component(Component(DatabaseActions.ActorEditAction, "ARCActorEditAction",
                                     None, "CoreARCActorEditAction", "CORE", 1.0, self))

        #------------------------------ utilities ------------------------------------
        self.add_component(Component(PyXAL, "PyXAL", None, "CorePyXAL", "CORE", 1.0, self))

        #=====================================================================
        # * add components (RMXP)
        #=====================================================================
        #-------------------------- functions --------------------------------

        #------------------------- data holders ------------------------------
        self.add_component(Component(RMXP.RGSS1_RPG.RPG, "RPG", "RMXP",
                                     "RGSS1_RPG", "CORE", 1.0, self))

        #-------------------------- data handlers ----------------------------


        #----------------------------- ctrls ---------------------------------
        

        #----------------------------- Dialogs -------------------------------

        #=====================================================================
        # * add components (PanelManager)
        #=====================================================================
        #------------------------------ Panels--------------------------------
        self.add_component(Component(Panels.StartPanel, "StartPanel", "PanelManagerType",
                                     "CoreStartPanel", "CORE", 1.0, self))
        self.add_component(Component(Panels.ShadowPanel, "ShadowPanel", "PanelManagerType",
                                     "CoreShadowPanel", "CORE", 1.0, self))

        self.add_component(Component(MapEditor.BrushPanels.TilesetPanel, "TilesetPanel", "PanelManagerType",
                                     "CoreTilesetPanel", "CORE", 1.0, self))
        self.add_component(Component(MapEditor.BrushPanels.MapTreePanel, "MapTreePanel", "PanelManagerType",
                                     "CoreMapTreePanel", "CORE", 1.0, self))
        self.add_component(Component(MapEditor.MapEditorPanel.MapPanel, "MapEditorPanel", "PanelManagerType",
                                     "CoreMapEditorPanel", "CORE", 1.0, self))

        self.add_component(Component(Panels.MainToolbar, "MainToolbar", "PanelManagerType",
                                     "CoreMainToolbar", "CORE", 1.0, self))
        self.add_component(Component(Panels.DatabaseToolbar, "DatabaseToolbar", "PanelManagerType",
                                     "CoreDatabaseToolbar", "CORE", 1.0, self))

        # Database
        self.add_component(Component(Actors_Panel, "MainActorsPanel", "PanelManagerType", 
                                     "COREMainActorsPanel", "CORE", 1.0, self))
        self.add_component(Component(Classes_Panel, "MainClassesPanel", "PanelManagerType", 
                                     "COREMainClassesPanel", "CORE", 1.0, self))
        self.add_component(Component(Skills_Panel, "MainSkillsPanel", "PanelManagerType", 
                                     "COREMainSkillsPanel", "CORE", 1.0, self))
        self.add_component(Component(Items_Panel, "MainItemsPanel", "PanelManagerType", 
                                     "COREMainItemsPanel", "CORE", 1.0, self))
        self.add_component(Component(Weapons_Panel, "MainWeaponsPanel", "PanelManagerType", 
                                     "COREMainWeaponsPanel", "CORE", 1.0, self))
        self.add_component(Component(Armors_Panel, "MainArmorsPanel", "PanelManagerType", 
                                     "COREMainArmorsPanel", "CORE", 1.0, self))
        self.add_component(Component(Enemies_Panel, "MainEnemiesPanel", "PanelManagerType", 
                                     "COREMainEnemiesPanel", "CORE", 1.0, self))
        self.add_component(Component(Troops_Panel, "MainTroopsPanel", "PanelManagerType", 
                                     "COREMainTroopsPanel", "CORE", 1.0, self))
        self.add_component(Component(States_Panel, "MainStatesPanel", "PanelManagerType", 
                                     "COREMainStatesPanel", "CORE", 1.0, self))
        self.add_component(Component(Animations_Panel, "MainAnimationsPanel", "PanelManagerType", 
                                     "COREMainAnimationsPanel", "CORE", 1.0, self))
        self.add_component(Component(Tilesets_Panel, "MainTilesetsPanel", "PanelManagerType", 
                                     "COREMainTilesetsPanel", "CORE", 1.0, self))
        self.add_component(Component(CommonEvents_Panel, "MainCommonEventsPanel", "PanelManagerType", 
                                     "COREMainCommonEventsPanel", "CORE", 1.0, self))
        self.add_component(Component(System_Panel, "MainSystemPanel", "PanelManagerType", 
                                     "COREMainSystemPanel", "CORE", 1.0, self))

        #Event Editor
        self.add_component(Component(EventEditor_Panel, "MainEventEditorPanel", "PanelManagerType",
                                     "COREMainEventEditorPanel", "CORE", 1.0, self))

        #Script Editor
        self.add_component(Component(ScriptEditor_Panel, "MainScriptEditorPanel", "PanelManagerType", 
                                     "COREMainScriptEditorPanel", "CORE", 1.0, self))
        
        



package = CorePackage()
key = package.add_to_kernel()

# this line is only here because it is the core and should be enabled by default, 
# if it was a normal plug-in it would be enabled else where
Manager.enable_packages(key)





