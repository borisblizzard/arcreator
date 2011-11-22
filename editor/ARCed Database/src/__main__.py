import wx
import DatabasePackage
import os
import ConfigParser
import Kernel
from Kernel import Manager as KM
import Main

import sys
dirName = os.path.dirname(os.path.abspath(__file__))
editorDir = os.path.split(os.path.split(dirName)[0])[0]
editorDir = os.path.join(editorDir, 'ARCed', 'src')        

Main.ConfigManager.LoadConfig()

PAGE_INDEX = 0

class ARCedTest(wx.App):

	def __init__(self, redirect=False, filename=None):
		# Initialize global dictionary that contains the pages
		global Panels
		# Create the application and main frame
		wx.App.__init__(self, redirect, filename)
		self.load_project()
		self.frame = wx.Frame(None, wx.ID_ANY, title='ARCed Panel Test', size=(800, 600))
		self.frame.SetExtraStyle(wx.FRAME_EX_CONTEXTHELP)
		self.frame.CenterOnScreen()

	def create_panels(self):
		
		nb = wx.Notebook( self.frame )
		Panels = [None for i in xrange(2)]
		Panels[0] = ('Actors', 'ARCedActors_Panel')
		Panels[1] = ('Audio', 'ARCedAudioPlayer_Panel')
		#Panels[1] = ('Classes', 'ARCedClasses_Panel')
		#Panels[2] = ('Skills', 'ARCedSkills_Panel')
		#Panels[3] = ('Items', 'ARCedItems_Panel')
		#Panels[4] = ('Weapons', 'ARCedWeapons_Panel')
		#Panels[5] = ('Armors', 'ARCedArmors_Panel')
		#Panels[6] = ('Enemies', 'ARCedEnemies_Panel')
		#Panels[7] = ('Troops', 'ARCedTroops_Panel')
		#Panels[8] = ('States', 'ARCedStates_Panel')
		#Panels[9] = ('Animations', 'ARCedAnimations_Panel')
		#Panels[10] = ('Tilesets', 'ARCedTilesets_Panel')
		#Panels[11] = ('Common Events', 'ARCedCommonEvents_Panel')
		#Panels[12] = ('System', 'ARCedSystem_Panel')
		#Panels[13] = ('Configuration', 'Configuration_Panel')

		for data in Panels:
			exec('from ' + data[1] + ' import ' + data[1])
			exec('page = ' + data[1] + '(nb)')
			nb.AddPage(page, data[0])
		nb.SetSelection(PAGE_INDEX)
		self.frame.Show()

	'''
	def load_project(self):
		if Kernel.GlobalObjects.has_key("CurrentProjectDir"):
			Kernel.GlobalObjects.set_value("CurrentProjectDir", TEST_PATH)
		#get a project loader
		projectloader = KM.get_component("ARCProjectLoader").object()
		projectloader.load(TEST_PATH)
		#place the project in the global namespace
		if Kernel.GlobalObjects.has_key("PROJECT"):
			Kernel.GlobalObjects.set_value("PROJECT", projectloader.getProject())
		else:
			Kernel.GlobalObjects.request_new_key("PROJECT", "CORE", projectloader.getProject())
		#set the Project Title
		if Kernel.GlobalObjects.has_key("Title"):
			Kernel.GlobalObjects.set_value("Title", projectloader.getProject().getInfo("Title"))
		else:
			Kernel.GlobalObjects.request_new_key("Title", "CORE", projectloader.getProject().getInfo("Title"))
		#set the current project directory
		if Kernel.GlobalObjects.has_key("CurrentProjectDir"):
			Kernel.GlobalObjects.set_value("CurrentProjectDir", os.path.dirname(TEST_PATH))
		else:
			Kernel.GlobalObjects.request_new_key("CurrentProjectDir", "CORE", os.path.dirname(TEST_PATH))
		#set that there is an open project
		if Kernel.GlobalObjects.has_key("ProjectOpen"):
			Kernel.GlobalObjects.set_value("ProjectOpen", True)
		else:
			Kernel.GlobalObjects.request_new_key("ProjectOpen", "CORE", True)
	'''
	def load_project(self):
		config = Kernel.GlobalObjects.get_value("ARCed_config")
		TEST_PATH = os.path.join(editorDir, "RTP", "Templates", "Chonicles of Sir Lag-A-Lot", "Chronicles of Sir Lag-A-Lot.arcproj")
		print TEST_PATH
		#get a project loader
		projectloader = KM.get_component("ARCProjectLoader").object()
		projectloader.load(TEST_PATH)
		#place the project in the global namespace
		if Kernel.GlobalObjects.has_key("PROJECT"):
			Kernel.GlobalObjects.set_value("PROJECT", projectloader.getProject())
		else:
			Kernel.GlobalObjects.request_new_key("PROJECT", "CORE", projectloader.getProject())
		#set the Project Title
		if Kernel.GlobalObjects.has_key("Title"):
			Kernel.GlobalObjects.set_value("Title", projectloader.getProject().getInfo("Title"))
		else:
			Kernel.GlobalObjects.request_new_key("Title", "CORE", projectloader.getProject().getInfo("Title"))
		#set the current project directory
		if Kernel.GlobalObjects.has_key("CurrentProjectDir"):
			Kernel.GlobalObjects.set_value("CurrentProjectDir", os.path.dirname(TEST_PATH))
		else:
			Kernel.GlobalObjects.request_new_key("CurrentProjectDir", "CORE", os.path.dirname(TEST_PATH))
		#set that there is an open project
		if Kernel.GlobalObjects.has_key("ProjectOpen"):
			Kernel.GlobalObjects.set_value("ProjectOpen", True)
		else:
			Kernel.GlobalObjects.request_new_key("ProjectOpen", "CORE", True)


# Create window and execute the main loop
if __name__ == '__main__':
	provider = wx.SimpleHelpProvider()
	wx.HelpProvider.Set(provider)
	app = ARCedTest()
	app.create_panels()
	app.MainLoop()
	app.Destroy()
