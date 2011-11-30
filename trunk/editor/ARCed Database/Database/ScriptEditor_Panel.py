import wx
import Database.ARCed_Templates as Templates
#--------------------------------------------------------------------------------------
# ScriptEditor_Panel
#--------------------------------------------------------------------------------------

# Implementing ScriptEditor_Panel
class ScriptEditor_Panel( Templates.ScriptEditor_Panel ):
	def __init__( self, parent ):
		ARCed_Templates.ScriptEditor_Panel.__init__( self, parent )
		self.CreateToolBar()


	def CreateToolBar( self ):
		art = wx.ArtProvider()
		self.toolBar.AddSimpleTool(0, art.GetBitmap(wx.ART_COPY), 'Copy', 'Copies the selected text')
		self.toolBar.AddSimpleTool(1, art.GetBitmap(wx.ART_CUT), 'Cut', 'Cuts the selected text')
		self.toolBar.AddSimpleTool(2, art.GetBitmap(wx.ART_PASTE), 'Paste', 'Pastes previously copied/cut text')
		self.toolBar.AddSeparator()
		self.toolBar.AddSimpleTool(3, art.GetBitmap(wx.ART_UNDO), 'Undo', 'Undoes the previous action')
		self.toolBar.AddSimpleTool(4, art.GetBitmap(wx.ART_REDO), 'Redo', 'Redoes the previous Undo')
		self.toolBar.AddSeparator()
		self.toolBar.AddSimpleTool(5, art.GetBitmap(wx.ART_FIND), 'Find', 'Opens Find window for searching text')
		self.toolBar.AddSimpleTool(6, art.GetBitmap(wx.ART_FIND_AND_REPLACE), 'Find and Replace', 'Open Find & Replace window for replacing text')
		self.toolBar.AddSeparator()
		self.toolBar.AddSimpleTool(7, art.GetBitmap(wx.ART_HELP_SETTINGS), 'Settings', 'Opens the settings window')
		self.toolBar.AddSimpleTool(8, art.GetBitmap(wx.ART_HELP_BOOK), 'Help', 'Opens the compiled HTML help doc')
		self.toolBar.AddSimpleTool(9, art.GetBitmap(wx.ART_EXECUTABLE_FILE), 'Test Run', 'Starts play testing')
		self.toolBar.AddSeparator()
		label = wx.StaticText(self.toolBar, wx.ID_ANY, u"\tSearch:")
		self.textCtrlSearch = wx.TextCtrl(self.toolBar)
		self.toolBar.AddControl(label)
		self.toolBar.AddControl(self.textCtrlSearch)
		self.toolBar.Realize()
		self.Bind(wx.EVT_TOOL, self.OnCopy, id=0)
		self.Bind(wx.EVT_TOOL, self.OnCut, id=1)
		self.Bind(wx.EVT_TOOL, self.OnPaste, id=2)
		self.Bind(wx.EVT_TOOL, self.OnUndo, id=3)
		self.Bind(wx.EVT_TOOL, self.OnRedo, id=4)
		self.Bind(wx.EVT_TOOL, self.OnFind, id=5)
		self.Bind(wx.EVT_TOOL, self.OnFindReplace, id=6)
		self.Bind(wx.EVT_TOOL, self.OnSettings, id=7)
		self.Bind(wx.EVT_TOOL, self.OnHelp, id=8)
		self.Bind(wx.EVT_TOOL, self.OnRun, id=9)

	def OnCopy( self, event ):
		print 'Copy'

	def OnCut( self, event ):
		print 'Cut'

	def OnPaste( self, event ):
		print 'Paste'

	def OnUndo( self, event ):
		print 'Undo'

	def OnRedo( self, event ):
		print 'Redo'

	def OnFind( self, event ):
		print 'Find'

	def OnFindReplace( self, event ):
		print 'Find and Replace'

	def OnSettings( self, event ):
		print 'Settings'

	def OnHelp( self, event ):
		print 'Help'

	def OnRun( self, event ):
		print 'Run'

#--------------------------------------------------------------------------------------
# TEST
#--------------------------------------------------------------------------------------

app = wx.PySimpleApp( 0 )
frame = wx.Frame( None, wx.ID_ANY, 'ARCed Script Editor', size=(840,630) )
frame.CreateStatusBar()
panel = ScriptEditor_Panel( frame )

try:
	from DatabaseManager import DatabaseManager as DM
	DM.DrawHeaderBitmap(panel.bitmapScripts, 'Scripts')
except:
	pass

frame.Centre( wx.BOTH )
frame.Show()
app.MainLoop()
