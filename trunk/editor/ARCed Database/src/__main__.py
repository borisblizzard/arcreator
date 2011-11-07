import wx
import DatabasePackage
import os
import ConfigParser
import Kernel
from Kernel import Manager as KM
#import Core
import Main

Main.ConfigManager.LoadConfig()

TEST_PATH = path = 'ARC TestProject\ARC Test Project.arcproj'

class DatabasePage():

	# Dummy class for now, this will not be used in the release version
	def __init__(self, title, page, index):
		self.Title = title
		self.Page = page
		self.DisplayOrder = index

class ARCedTest(wx.App):

	def __init__(self, redirect=False, filename=None):
		# Initialize global dictionary that contains the pages
		global DatabasePages
		DatabasePages = {}
		# Create the application and main frame
		wx.App.__init__(self, redirect, filename)
		self.load_project()
		self.frame = wx.Frame(None, wx.ID_ANY, title='ARCed Panel Test', size=(800, 600))
		self.frame.SetExtraStyle(wx.FRAME_EX_CONTEXTHELP)
		self.frame.CenterOnScreen()

	def create_panels(self):
		# Read and parse the .ini file to determine what tabs will be available
		Config = ConfigParser.SafeConfigParser()
		Config.read('ini\DatabaseTabs.ini')
		# Create Notebook control, and dynamically add the defined controls to it
		nb = wx.Notebook(self.frame, wx.ID_ANY)
		for tabName in Config.sections():
			file = Config.get(tabName, 'file')
			klass = Config.get(tabName, 'class')
			index = Config.getint(tabName, 'index')
			exec('import ' + file)
			exec('page = ' + file + '.' + klass + '(nb)')
			DatabasePages[index] = DatabasePage(tabName, page, index)
		# Sort the list and add each page to the control
		for i in sorted(DatabasePages.keys()):
			nb.AddPage(DatabasePages[i].Page, DatabasePages[i].Title)
		nb.SetSelection(0)
		self.frame.Show()

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


# Create window and execute the main loop
if __name__ == '__main__':
	provider = wx.SimpleHelpProvider()
	wx.HelpProvider.Set(provider)
	app = ARCedTest()
	app.create_panels()
	app.MainLoop()
	app.Destroy()