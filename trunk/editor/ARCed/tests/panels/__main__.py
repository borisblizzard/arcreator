import wx
import noname

class MyApp(wx.App):

	def __init__(self, redirect=False, filename=None):
	
		_test_panel = 3
		# Set the value of _test_panel to the appropriate integer below
		# ACTORS = 1
		# CLASSES = 2
		# SKILLS = 3
		# ITEMS = 4
		# WEAPONS = 5
		# ARMORS = 6
		# ENEMIES = 7
		# TROOPS = 8
		# STATES = 9
		# ANIMATIONS = 10
		# TILESETS = 11
		# COMMON EVENETS = 12
		# SYSTEM = 13
	
		wx.App.__init__(self, redirect, filename)
		self.frame = wx.Frame(None, wx.ID_ANY, title='Database Panel Test')
		panels = {1 : noname.Actors_Panel,
				2 : noname.Classes_Panel,
				3 : noname.Skills_Panel,
				4 : noname.Items_Panel,
				5 : noname.Weapons_Panel,
				6 : noname.Armors_Panel,
				7 : noname.Enemies_Panel,
				8 : noname.Troops_Panel,
				9 : noname.States_Panel,
				10 : noname.Animations_Panel,
				11 : noname.Tilesets_Panel,
				12 : noname.CommonEvents_Panel,
				13 : noname.System_Panel
			}
		self.panel = panels[_test_panel](self.frame)
		self.frame.Show()

if __name__ == '__main__':
   app = MyApp()
   app.MainLoop()