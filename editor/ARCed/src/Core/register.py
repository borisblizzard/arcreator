'''
Created on Dec 20, 2010

exports all the core components to the kernel
'''
import Kernel
from Kernel import Manager, Type, SuperType, Component, Package, Event
import RMXP
import Frames, Menues, Dialogs, Controls, Layouts, Data, Project, ARC_Data, Actions
import DatabaseActions, RPGutil, Icons, PanelManager, Panels


#=============================================================================
# * RMXP SuperType Declaration
#=============================================================================
class RMXPType(SuperType):

    #-------------------------- functions ------------------------------------
    #HueRotationOperator = Type("HueRotationOperator")
    #AdjustAlphaOperator = Type("AdjustAlphaOperator")

    #---------------------------- data holder --------------------------------
    RPG = Type("RPG")
    WxCache = Type("WxCache")
    #PyGameCache = Type("PyGameCache")

    #---------------------------- data handlers ------------------------------

    #------------------------------- ctrls -----------------------------------
    
    #-------------------------------- layouts --------------------------------

    #------------------------------- dialogs ---------------------------------
    DialogImportProject = Type("DialogImportProject")
    DialogExportProject = Type("DialogExportProject")


    def __init__(self):
        SuperType.__init__(self, "RMXP")

        #=====================================================================
        # * add types
        #=====================================================================

        #-------------------------- functions --------------------------------
        #self.add_types(self.HueRotationOperator, self.AdjustAlphaOperator)

        #------------------------- data holder -------------------------------
        self.add_types(self.RPG, self.WxCache)
        #, self.PyGameCache)

        #------------------------ data handlers ------------------------------

        #---------------------------- ctrls ----------------------------------

        #---------------------------- layouts --------------------------------

        #---------------------------- dialogs --------------------------------
        self.add_types(self.DialogImportProject, self.DialogExportProject)

#=============================================================================
# * PanelManager SuperType Declaration
#=============================================================================
class PanelManagerType(SuperType):

    #----------------------------- Panels ------------------------------------
    StartPanel = Type("StartPanel")
    TilesetPanel = Type("TilesetPanel")
    MapTreePanel = Type("MapTreePanel")
    MainToolbar = Type("MainToolbar")
    
    def __init__(self):
        SuperType.__init__(self, "PanelManagerType")

        #----------------------------- Panels --------------------------------
        self.add_types(self.StartPanel, self.TilesetPanel, self.MapTreePanel, self.MainToolbar)

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
      
        #------------------------------- frames --------------------------------------
        EditorMainWindow = Type("EditorMainWindow")
        
        #-------------------------------- ctrls --------------------------------------
        MainToolbar = Type("MainToolbar")
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

        #=====================================================================
        # * add the types to be registered 
        #=====================================================================
        #------------------------------ super types ----------------------------------
        self.add_types(RMXPType(), PanelManagerType())
        
        #------------------------------- functions -----------------------------------
        self.add_types(ARCDataDumpFunction, ARCDataLoadFunction, ARCProjectSaveFunction, 
                       ARCProjectLoadFunction)
        
        #------------------------------ data handlers --------------------------------
        self.add_types(Project, NewProjectHandler, OpenProjectHandler, SaveProjectHandler, 
                               SaveAsProjectHandler, ARCProjectCreator, ARCProjectHolder,
                               ARCProjectSaver, ARCProjectLoader)

        #------------------------- data holders ------------------------------
        self.add_types(Table, IconManager)
        
        #-------------------------------- frames -------------------------------------
        self.add_types(EditorMainWindow)
        
        #-------------------------------- ctrls --------------------------------------
        self.add_types(MainToolbar, MapEditorWindow, MapTreeCtrl)
        
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
        
        #=====================================================================
        # * add the events to be registered 
        #=====================================================================
        
        self.add_events(CoreEventOpenProject, CoreEventRefreshProject, CoreEventUpdateProjectMenu,
                        CoreEventARCRedirectClassPathsOnSave, CoreEventARCRedirectClassPathsOnLoad,
                        CoreEventARCExtendNamespaceOnLoad, CoreExitMainWindow)
        
        #=====================================================================
        # * add even hooks to be registered
        #=====================================================================
        self.add_event_hook("CoreEventARCExtendNamespaceOnLoad", RMXP.RGSS1_RPG.extend_namespace,  RMXP.RGSS1_RPG)

    def setup_components(self):
        #=====================================================================
        # * add components (main components)
        #=====================================================================

        #--------------------------- functions -------------------------------
        self.add_component(Component(ARC_Data.ARC_Data.dump, "ARCDataDumpFunction",
                                     None, "CoreARCDataDumpFunction", "CORE",
                                     1.0, self))
        self.add_component(Component(ARC_Data.ARC_Data.load, "ARCDataLoadFunction",
                                     None, "CoreARCDataLoadFunction", "CORE",
                                     1.0, self))
        self.add_component(Component(Project.ARCProjectSaveFunction, "ARCProjectSaveFunction", 
                                     None, "CoreARCProjctSaveFunction", "CORE", 
                                     1.0, self))
        self.add_component(Component(Project.ARCProjectLoadFunction, "ARCProjectLoadFunction", 
                                     None, "CoreARCProjectLoadFunction", "CORE", 
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
        self.add_component(Component(RPGutil.Table, "Table", None,
                                     "CoreTable", "CORE", 1.0, self))
        self.add_component(Component(Icons.IconManager, "IconManager", None,
                                     "CoreIconManager", "CORE", 1.0, self))

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

        #=====================================================================
        # * add components (RMXP)
        #=====================================================================
        #-------------------------- functions --------------------------------

        #------------------------- data holders ------------------------------
        self.add_component(Component(RMXP.RGSS1_RPG.RPG, "RPG", "RMXP",
                                     "RGSS1_RPG", "CORE", 1.0, self))
        self.add_component(Component(RMXP.Cache.WxCache, "WxCache", "RMXP",
                                     "RMXPWxCache", "CORE", 1.0, self))

        #-------------------------- data handlers ----------------------------


        #----------------------------- ctrls ---------------------------------
        

        #----------------------------- Dialogs -------------------------------

        #=====================================================================
        # * add components (PanelManager)
        #=====================================================================
        self.add_component(Component(Panels.StartPanel, "StartPanel", "PanelManagerType",
                                     "CoreStartPanel", "CORE", 1.0, self))
        self.add_component(Component(Panels.TilesetPanel, "TilesetPanel", "PanelManagerType",
                                     "CoreTilesetPanel", "CORE", 1.0, self))
        self.add_component(Component(Panels.MapTreePanel, "MapTreePanel", "PanelManagerType",
                                     "CoreMapTreePanel", "CORE", 1.0, self))
        self.add_component(Component(Panels.MainToolbar, "MainToolbar", "PanelManagerType",
                                     "CoreMainToolbar", "CORE", 1.0, self))
        
        
package = CorePackage()
key = package.add_to_kernel()

# this line is only here because it is the core and should be enabled by default, 
# if it was a normal plug-in it would be enabled else where
Manager.enable_packages(key)





