'''
Created on Dec 20, 2010

exports all the core components to the kernel
'''
import Kernel
from Kernel import Manager, Type, SuperType, Component, Package, Event
import RMXP
import Frames, Menues, Dialogs, Controls, Data



#=============================================================================
# * Type Declaration 
#=============================================================================
#------------------------------ functions ------------------------------------
PathOperator = Type("PathOperator")

#---------------------------- Data handlers ----------------------------------
NewProjectHandler = Type("NewProjectHandler")
OpenProjectHandler = Type("OpenProjectHandler")
SaveProjectHandler = Type("SaveProjectHandler")
SaveAsProjectHandler = Type("SaveAsProjectHandler")

#------------------------------- frames --------------------------------------
EditorMainWindow = Type("EditorMainWindow")

#-------------------------------- ctrls --------------------------------------
MainToolbar = Type("MainToolbar")

#-------------------------------- menus --------------------------------------
MainMenuBar = Type("MainMenuBar")
MainStatusBar = Type("MainStatusBar")
ProjectMenuItems = Type("ProjectMenuItems")
PluginMenuItem = Type("PluginMenuItem")

#------------------------------- dialogs -------------------------------------
NewProjectDialog = Type("NewProjectDialog")


#=============================================================================
# * register Types
#=============================================================================
#------------------------------- functions -----------------------------------
Manager.register_types(PathOperator)

#------------------------------ data handlers --------------------------------
Manager.register_types(NewProjectHandler, OpenProjectHandler,
                       SaveProjectHandler, SaveAsProjectHandler)

#-------------------------------- frames -------------------------------------
Manager.register_types(EditorMainWindow)

#-------------------------------- ctrls --------------------------------------
Manager.register_types(MainToolbar)

#-------------------------------- menus --------------------------------------
Manager.register_types(MainMenuBar, MainStatusBar, ProjectMenuItems,
                       PluginMenuItem)

#-------------------------------- dialogs ------------------------------------
Manager.register_types(NewProjectDialog)

#=============================================================================
# * RMXP SuperType Declaration
#=============================================================================
class RMXPType(SuperType):

    #-------------------------- functions ------------------------------------
    HueRotationOperator = Type("HueRotationOperator")
    AdjustAlphaOperator = Type("AdjustAlphaOperator")

    #---------------------------- data holder --------------------------------
    RPG = Type("RPG")
    Table = Type("Table")
    RMXPProject = Type("RMXPProject")
    WxCache = Type("WxCache")
    #PyGameCache = Type("PyGameCache")

    #---------------------------- data handlers ------------------------------
    ProjectLoader = Type("ProjectLoader")
    ProjectSaver = Type("ProjectSaver")
    ProjectImporter = Type("ProjectImporter")
    ProjectExporter = Type("ProjectExporter")
    ProjectCreator = Type("ProjectCreator")
    ProjectImportHandler = Type("ProjectImportHandler")
    ProjectExportHandler = Type("ProjectExportHandler")

    #------------------------------- ctrls -----------------------------------
    MapEditorWindow = Type("MapEditorWindow")
    MainMapTreeCtrl = Type("MainMapTreeCtrl")

    #-------------------------------- layouts --------------------------------
    EditorMainWindowLayout = Type("EditorMainWindowLayout")

    #------------------------------- dialogs ---------------------------------
    DialogImportProject = Type("DialogImportProject")
    DialogExportProject = Type("DialogExportProject")


    def __init__(self):
        SuperType.__init__(self, "RMXP")

        #=====================================================================
        # * add types
        #=====================================================================

        #-------------------------- functions --------------------------------
        self.add_types(self.HueRotationOperator, self.AdjustAlphaOperator)

        #------------------------- data holder -------------------------------
        self.add_types(self.RPG, self.Table, self.RMXPProject, self.WxCache)
        #, self.PyGameCache)

        #------------------------ data handlers ------------------------------
        self.add_types(self.ProjectLoader, self.ProjectSaver,
                       self.ProjectExporter, self.ProjectImporter,
                       self.ProjectCreator, self.ProjectImportHandler,
                       self.ProjectExportHandler)

        #---------------------------- ctrls ----------------------------------
        self.add_types(self.MapEditorWindow, self.MainMapTreeCtrl)

        #---------------------------- layouts --------------------------------
        self.add_types(self.EditorMainWindowLayout)

        #---------------------------- dialogs --------------------------------
        self.add_types(self.DialogImportProject, self.DialogExportProject)


#=============================================================================
# * Package Declaration
#=============================================================================

class CorePackage(Package):
    def __init__(self):
        Package.__init__(self, "CORE")

        #=====================================================================
        # * add the types
        #=====================================================================
        self.add_types(RMXPType())

        #=====================================================================
        # * add components (main components)
        #=====================================================================

        #--------------------------- functions -------------------------------
        self.add_component(Component(RMXP.RPGutil.opj, "PathOperator", None,
                                     "CorePathOperator", "CORE", 1.0,
                                     self))

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


        #---------------------------- frames ---------------------------------
        self.add_component(Component(Frames.CoreEditorMainWindow,
                                     "EditorMainWindow", None,
                                     "CoreEditorMainWindow", "CORE",
                                     1.0, self))

        #----------------------------- ctrls ---------------------------------
        self.add_component(Component(Controls.MainToolbar,
                                     "MainToolbar", None, "CoreMainToolbar",
                                     "CORE", 1.0, self))

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
        #=====================================================================
        # * add components (RMXP)
        #=====================================================================
        #-------------------------- functions --------------------------------
        #pygame
        #=======================================================================
        # self.add_component(Component(RMXP.RPGutil.PySurfaceFunctions.change_hue,
        #                             "HueRotationOperator", "RMXP",
        #                             "RMXPHueRotationOperator", "CORE", 1.0,
        #                             self))
        # self.add_component(Component(RMXP.RPGutil.PySurfaceFunctions.adjust_alpha,
        #                             "AdjustAlphaOperator", "RMXP",
        #                             "RMXPAdjustAlphaOperator", "CORE", 1.0,
        #                             self))
        #=======================================================================
        #------------------------- data holders ------------------------------
        self.add_component(Component(RMXP.RGSS1_RPG.RPG, "RPG", "RMXP",
                                     "RGSS1_RPG", "CORE", 1.0, self))
        self.add_component(Component(RMXP.RPGutil.Table, "Table", "RMXP",
                                     "RMXPTable", "CORE", 1.0, self))
        self.add_component(Component(RMXP.RMXPProject.Project, "RMXPProject",
                                     "RMXP", "CoreRMXPProject", "CORE", 1.0,
                                     self))
        self.add_component(Component(RMXP.Cache.WxCache, "WxCache", "RMXP",
                                     "RMXPWxCache", "CORE", 1.0, self))
        #pygame
        #=======================================================================
        # self.add_component(Component(RMXP.Cache.PyGameCache, "PyGameCache",
        #                             "RMXP",
        #                             "RMXPPyGameCache", "CORE", 1.0, self))
        #=======================================================================

        #-------------------------- data handlers ----------------------------
        self.add_component(Component(RMXP.Data.RMXPProjectLoader,
                                     "ProjectLoader", "RMXP",
                                     "RMXPProjectLoader", "CORE", 1.0, self))
        self.add_component(Component(RMXP.Data.RMXPProjectSaver,
                                     "ProjectSaver", "RMXP",
                                     "RMXPProjectSaver", "CORE", 1.0, self))
        self.add_component(Component(RMXP.Data.RMXPProjectImporter,
                                     "ProjectImporter", "RMXP",
                                     "RMXPProjectImporter", "CORE", 1.0, self))
        self.add_component(Component(RMXP.Data.RMXPProjectExporter,
                                     "ProjectExporter", "RMXP",
                                     "RMXPProjectExporter", "CORE", 1.0, self))
        self.add_component(Component(RMXP.Data.RMXPProjectCreator,
                                     "ProjectCreator", "RMXP",
                                     "RMXPProjectCreator", "CORE", 1.0, self))
        self.add_component(Component(RMXP.Data.ImportRMXPProject,
                                     "ProjectImportHandler", "RMXP",
                                     "RMXPProjectImportHandler", "CORE",
                                     1.0, self))
        self.add_component(Component(RMXP.Data.ExportRMXPProject,
                                     "ProjectExportHandler", "RMXP",
                                     "RMXPProjectExportHandler", "CORE",
                                     1.0, self))

        #----------------------------- ctrls ---------------------------------
        self.add_component(Component(RMXP.Controls.WxRMXPMapPanel,
                                     "MapEditorWindow", "RMXP",
                                     "WxRMXPMapWindow", "CORE", 1.0, self))
        #pygame
        #=======================================================================
        # self.add_component(Component(RMXP.Controls.PyGameRMXPMapPanel,
        #                             "MapEditorWindow", "RMXP",
        #                             "PyGameRMXPMapWindow", "CORE", 1.0, self))
        #=======================================================================
        self.add_component(Component(RMXP.Controls.RMXPMapTreePanel,
                                     "MainMapTreeCtrl", "RMXP",
                                     "RMXPMapTreeCtrl", "CORE", 1.0,
                                     self))

        #----------------------------- layouts -------------------------------
        self.add_component(Component(RMXP.Layouts.RMXPMainWindow,
                                     "EditorMainWindowLayout", "RMXP",
                                     "RMXPEditorMainWindowLayout", "CORE", 1.0,
                                     self))

        #----------------------------- Dialogs -------------------------------
        self.add_component(Component(RMXP.Dialogs.ImportRMXPProjectDialog,
                                     "DialogImportProject", "RMXP",
                                     "RMXPDialogImportProject", "CORE",
                                     1.0, self))
        self.add_component(Component(RMXP.Dialogs.ExportRMXPProjectDialog,
                                     "DialogExportProject", "RMXP",
                                     "RMXPDialogExportProject", "CORE",
                                     1.0, self))


        #=====================================================================
        # * register
        #=====================================================================
        self.register()

#=============================================================================
# * init package
#=============================================================================

package = CorePackage()

#=============================================================================
# * events
#=============================================================================

EventOpenProject = Event("EventOpenProject")
EventRefreshProject = Event("EventRefreshProject")
EventMode = Event("EventMode")
EventUpdateProjectMenu = Event("EventUpdateProjectMenu")

#=============================================================================
# * register events
#=============================================================================

Manager.register_events(EventOpenProject, EventRefreshProject, EventMode,
                        EventUpdateProjectMenu)

#=============================================================================
# * register functions to events
#=============================================================================

EventOpenProject.register(RMXP.Data.Call_RMXP_Import)

#=============================================================================
# * Add the Project modes
#=============================================================================

Kernel.Global.ProjectModes.append("RMXP")
