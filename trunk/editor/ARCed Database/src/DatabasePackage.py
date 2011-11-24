from Actors_Panel import Actors_Panel
from Classes_Panel import Classes_Panel
from Skills_Panel import Skills_Panel
from Items_Panel import Items_Panel
from Weapons_Panel import Weapons_Panel
from Armors_Panel import Armors_Panel
from Enemies_Panel import Enemies_Panel
from Troops_Panel import Troops_Panel
from States_Panel import States_Panel
from Animations_Panel import Animations_Panel
from Tilesets_Panel import Tilesets_Panel
from CommonEvents_Panel import CommonEvents_Panel
from System_Panel import System_Panel

import Kernel
from Kernel import Manager, Type, SuperType, Component, Package, Event

#=============================================================================
# * Package Declaration
#=============================================================================
class DatabasePackage(Package):

	def __init__(self):
		Package.__init__(self, "DATABASE", "CORE")
		self.setup_types()
		self.setup_events()
		self.setup_components()

	def setup_types(self):
		#=============================================================================
		# * Type Declaration 
		#=============================================================================
		#------------------------------ functions ------------------------------------

		#---------------------------- Data handlers ----------------------------------

		#------------------------------- frames --------------------------------------


		#-------------------------------- ctrls --------------------------------------

		#-------------------------------- layouts ------------------------------------
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

		#-------------------------------- menus --------------------------------------

		#------------------------------- dialogs -------------------------------------


		#-------------------------------actions---------------------------------------

		#=====================================================================
		# * add the types to be registered 
		#=====================================================================
		#------------------------------ super types ----------------------------------
		#self.add_types()

		#------------------------------- functions -----------------------------------
		#self.add_types()

		#------------------------------ data handlers --------------------------------
		#self.add_types()

		#-------------------------------- frames -------------------------------------
		#self.add_types()

		#-------------------------------- ctrls --------------------------------------
		#self.add_types()

		#-------------------------------- layouts --------------------------------
		self.add_types(MainActorsPanel, MainClassesPanel, MainSkillsPanel, 
				MainItemsPanel, MainWeaponsPanel, MainArmorsPanel, MainEnemiesPanel, 
				MainTroopsPanel, MainStatesPanel, MainAnimationsPanel, MainTilesetsPanel, 
				MainCommonEventsPanel, MainSystemPanel)
		#-------------------------------- menus --------------------------------------
		#self.add_types()

		#-------------------------------- dialogs ------------------------------------
		#self.add_types()

		#-------------------------------actions---------------------------------------
		#self.add_types()

		#self.add_types()

	def setup_events(self):
		pass
		
		#=============================================================================
		# * events
		#=============================================================================

		#=====================================================================
		# * add the events to be registered 
		#=====================================================================

		#self.add_events()

		#=====================================================================
		# * add even hooks to be registered
		#=====================================================================
		#self.add_event_hook()

	def setup_components(self):
		#=====================================================================
		# * add components (main components)
		#=====================================================================

		#--------------------------- functions -------------------------------

		#-------------------------- data Handler -----------------------------

		#---------------------------- frames ---------------------------------


		#----------------------------- ctrls ---------------------------------


		#----------------------------- layouts -------------------------------
		
		self.add_component(Component(Actors_Panel, "MainActorsLayout", 
							   None, "COREMainActorsLayout", "CORE", 1.0, self))
		self.add_component(Component(Classes_Panel, "MainClassesLayout", 
							   None, "COREMainClassesLayout", "CORE", 1.0, self))
		self.add_component(Component(Skills_Panel, "MainSkillsLayout", 
							   None, "COREMainSkillsLayout", "CORE", 1.0, self))
		self.add_component(Component(Items_Panel, "MainItemsLayout", 
							   None, "COREMainItemsLayout", "CORE", 1.0, self))
		self.add_component(Component(Weapons_Panel, "MainWeaponsLayout", 
							   None, "COREMainWeaponsLayout", "CORE", 1.0, self))
		self.add_component(Component(Armors_Panel, "MainArmorsLayout", 
							   None, "COREMainArmorsLayout", "CORE", 1.0, self))
		self.add_component(Component(Enemies_Panel, "MainEnemiesLayout", 
							   None, "COREMainEnemiesLayout", "CORE", 1.0, self))
		self.add_component(Component(Troops_Panel, "MainTroopsLayout", 
							   None, "COREMainTroopsLayout", "CORE", 1.0, self))
		self.add_component(Component(States_Panel, "MainStatesLayout", 
							   None, "COREMainStatesLayout", "CORE", 1.0, self))
		self.add_component(Component(Animations_Panel, "MainAnimationsLayout", 
							   None, "COREMainAnimationsLayout", "CORE", 1.0, self))
		self.add_component(Component(Tilesets_Panel, "MainTilesetsLayout", 
							   None, "COREMainTilesetsLayout", "CORE", 1.0, self))
		self.add_component(Component(CommonEvents_Panel, "MainCommonEventsLayout", 
							   None, "COREMainCommonEventsLayout", "CORE", 1.0, self))
		self.add_component(Component(System_Panel, "MainSystemLayout", 
							   None, "COREMainSystemLayout", "CORE", 1.0, self))

		#----------------------------- menus ---------------------------------

		#---------------------------- dialogs --------------------------------


package = DatabasePackage()
key = Manager.add_package(package)

# this line is only here because it is the core and should be enabled by default, 
# if it was a normal plug-in it would be enabled else where
Manager.enable_packages(key)




