import wx
import os
import Main
import Kernel
from Kernel import Manager as KM
Main.ConfigManager.LoadConfig()
import DatabasePackage

dirName = os.path.dirname(os.path.abspath(__file__))
editorDir = os.path.split(os.path.split(dirName)[0])[0]
editorDir = os.path.join(editorDir, 'ARCed', 'src')     
PAGE_INDEX = 0

class Test(wx.App):

	def __init__(self, redirect=False, filename=None):
		# Initialize global dictionary that contains the pages
		global Panels
		# Create the application and main frame
		wx.App.__init__(self, redirect, filename)
		self.load_project()
		self.frame = wx.Frame(None, wx.ID_ANY, title='ARCed Database', size=(800, 600))
		self.frame.SetExtraStyle(wx.FRAME_EX_CONTEXTHELP)
		self.frame.CenterOnScreen()

	def create_panels(self):
		
		nb = wx.Notebook( self.frame )
		Panels = [None for i in xrange(15)]
		Panels[0] = ('Actors', 'Actors_Panel')
		Panels[14] = ('Audio', 'AudioPlayer_Panel')
		Panels[1] = ('Classes', 'Classes_Panel')
		Panels[2] = ('Skills', 'Skills_Panel')
		Panels[3] = ('Items', 'Items_Panel')
		Panels[4] = ('Weapons', 'Weapons_Panel')
		Panels[5] = ('Armors', 'Armors_Panel')
		Panels[6] = ('Enemies', 'Enemies_Panel')
		Panels[7] = ('Troops', 'Troops_Panel')
		Panels[8] = ('States', 'States_Panel')
		Panels[9] = ('Animations', 'Animations_Panel')
		Panels[10] = ('Tilesets', 'Tilesets_Panel')
		Panels[11] = ('Common Events', 'CommonEvents_Panel')
		Panels[12] = ('System', 'System_Panel')
		Panels[13] = ('Configuration', 'Configuration_Panel')

		for data in Panels:
			exec('from ' + data[1] + ' import ' + data[1])
			exec('page = ' + data[1] + '(nb)')
			nb.AddPage(page, data[0])
		nb.SetSelection(PAGE_INDEX)
		self.frame.Show()

	def load_project(self):
		config = Kernel.GlobalObjects.get_value("ARCed_config")
		TEST_PATH = os.path.join(editorDir, "RTP", "Templates", "Chonicles of Sir Lag-A-Lot", "Chronicles of Sir Lag-A-Lot.arcproj")
		TEST_PATH = r"C:\Users\Eric\Desktop\ARC\editor\ARCed Database\ARC TestProject\ARC Test Project.arcproj"
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

		# Add RMXP RTP for testing
		common = os.path.expandvars('%COMMONPROGRAMFILES%')
		rtpDir = os.path.join(common, 'Enterbrain', 'RGSS', 'Standard')
		rtps = Kernel.GlobalObjects.get_value("ARCed_config").get_section("RTPs")
		Kernel.GlobalObjects.get_value("ARCed_config").get_section("RTPs").set('RMXP', rtpDir)

# Create window and execute the main loop
if __name__ == '__main__':
	provider = wx.SimpleHelpProvider()
	wx.HelpProvider.Set(provider)
	app = Test()
	app.create_panels()
	app.MainLoop()
	app.Destroy()
