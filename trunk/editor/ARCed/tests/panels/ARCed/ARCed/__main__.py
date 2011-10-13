import wx
import ConfigParser
import ARCed_Templates
import ARCedActors_Panel
import ARCedArmors_Panel
import ARCedAnimations_Panel
import ARCedClasses_Panel
import ARCedCommonEvents_Panel
import ARCedEnemies_Panel
import ARCedItems_Panel
import ARCedSkills_Panel
import ARCedStates_Panel
import ARCedSystem_Panel
import ARCedTilesets_Panel
import ARCedTroops_Panel
import ARCedWeapons_Panel

class DatabasePage():

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
		self.frame = wx.Frame(None, wx.ID_ANY, title='ARCed Panel Test', size=(800, 600))
		self.frame.CenterOnScreen()
		# Read and parse the .ini file to determine what tabs will be available
		Config = ConfigParser.SafeConfigParser()
		Config.read('ini\DatabaseTabs.ini')
		# Create Notebook control, and dynamically add the defined controls to it
		nb = wx.Notebook(self.frame, wx.ID_ANY)
		for tabName in Config.sections():
			file = Config.get(tabName, 'file')
			klass = Config.get(tabName, 'class')
			index = Config.getint(tabName, 'index')
			exec('page = ' + file + '.' + klass + '(nb)')
			DatabasePages[index] = DatabasePage(tabName, page, index)
		# Sort the list and add each page to the control
		for i in sorted(DatabasePages.keys()):
			nb.AddPage(DatabasePages[i].Page, DatabasePages[i].Title)
		self.frame.Show()

# Create window and execute the main loop
if __name__ == '__main__':
	app = ARCedTest()
	app.MainLoop()
	app.Destroy()