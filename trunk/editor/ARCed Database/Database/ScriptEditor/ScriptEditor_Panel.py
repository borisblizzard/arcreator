import wx
import os
import Database.ARCed_Templates as Templates
import Database.Manager as DM
import re
import Kernel
#--------------------------------------------------------------------------------------
# ScriptEditor_Panel
#--------------------------------------------------------------------------------------

class ScriptEditor_Panel( Templates.ScriptEditor_Panel ):

	def __init__( self, parent, index=0 ):
		"""Basic constructor for the ScriptEditor_Panel"""
		Templates.ScriptEditor_Panel.__init__( self, parent )
		# TODO: Alter import order to allow importing this globally in header
		import Database.ScriptEditor.Manager as SM
		self.CreateToolBar()
		self.CreateStatusBar(parent)
		DM.DrawHeaderBitmap(self.bitmapScripts, 'Scripts')
		# TODO: Get path by using project path + Data/Scripts/
		path = r"C:\Users\Eric\Desktop\ARC\editor\ARCed\src\RTP\Templates\Chonicles of Sir Lag-A-Lot\Data\Scripts"
		#path = os.path.join(Kernel.GlobalObjects.get_value("CurrentProjectDir"), 'Data', 'Scripts')
		try:
			SM.LoadScripts(path)
		except:
			Kernel.Log('Failed to successfully load all scripts.', '[ScriptEditor]', True, True)
		global Scripts
		Scripts = Kernel.GlobalObjects.get_value('Scripts')
		self.listBoxScripts.AppendItems([script.GetName() for script in Scripts])
		self.listBoxScripts.SetSelection(index)
		self.scriptControl.Bind(wx.EVT_KEY_DOWN, Kernel.Protect(self.RefreshStatus))
		self.RefreshScript(index)

	def CreateToolBar( self ):
		"""Creates the toolbar and binds events to it"""
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
		self.textCtrlSearch = wx.TextCtrl(self.toolBar, -1, 'Search...', style=wx.TE_RIGHT)
		self.toolBar.AddControl(self.textCtrlSearch)
		self.toolBar.AddSimpleTool(10, art.GetBitmap(wx.ART_GO_BACK), 'Previous', '')
		self.toolBar.AddSimpleTool(11, art.GetBitmap(wx.ART_GO_FORWARD), 'Next', '')
		self.toolBar.Realize()
		self.Bind(wx.EVT_TOOL, self.OnCopy, id=0)
		self.Bind(wx.EVT_TOOL, self.OnCut, id=1)
		self.Bind(wx.EVT_TOOL, self.OnPaste, id=2)
		self.Bind(wx.EVT_TOOL, self.OnUndo, id=3)
		self.Bind(wx.EVT_TOOL, self.OnRedo, id=4)
		self.Bind(wx.EVT_TOOL, self.OnFind, id=5)
		self.Bind(wx.EVT_TOOL, self.OnReplace, id=6)
		self.Bind(wx.EVT_TOOL, Kernel.Protect(self.OnSettings), id=7)
		self.Bind(wx.EVT_TOOL, Kernel.Protect(self.OnHelp), id=8)
		self.Bind(wx.EVT_TOOL, Kernel.Protect(self.OnRun), id=9)
		self.Bind(wx.EVT_TOOL, Kernel.Protect(self.FindPrevious), id=10)
		self.Bind(wx.EVT_TOOL, Kernel.Protect(self.FindNext), id=11)

	def CreateStatusBar( self, frame ):
		self.statusBar = frame.CreateStatusBar()
		self.statusBar.SetFieldsCount(4)

	def DoNothing( self, event ):
		"""Prevents flickering on MSW"""
		pass

	def RefreshScript( self, index ):
		"""Refreshes the displayed text"""
		self.scriptControl.ClearAll()
		self.scriptControl.SetTextUTF8(Scripts[index].GetText())
		self.textCtrlScriptName.ChangeValue(Scripts[index].GetName())
		self.scriptControl.CalculateLineNumberMargin()
		self.RefreshStatus()
		
	def RefreshStatus( self, event=None ):
		"""Refreshes the status bar text"""
		sctrl = self.scriptControl
		chars = len(re.sub(r'\s', '', sctrl.Text))
		length = str.format('Lines: {0}   Characters: {1}', sctrl.LineCount, chars)
		self.statusBar.SetStatusText(length, 1)
		pos = str.format('Position: {}', self.scriptControl.GetCurrentPos())
		self.statusBar.SetStatusText(pos, 2)
		path = Scripts[self.listBoxScripts.GetSelection()].GetName()
		self.statusBar.SetStatusText(path, 3)
		if event is not None:
			event.Skip()
		pass
		
	def OnCopy( self, event ):
		"""Sets the scripts selected text to the clipboard"""
		self.statusBar.SetStatusText('Copied selected text', 0)
		self.scriptControl.Copy()

	def OnCut( self, event ):
		"""Sets the scripts selected text to the clipboard"""
		self.statusBar.SetStatusText('Cut selected text', 0)
		self.scriptControl.Cut()

	def OnPaste( self, event ):
		"""Pastes the clipboard text to the script"""
		self.statusBar.SetStatusText('Text pasted', 0)
		self.scriptControl.Paste()

	def OnUndo( self, event ):
		"""Performs script Undo action"""
		self.statusBar.SetStatusText('Undo applied', 0)
		self.scriptControl.Undo()

	def OnRedo( self, event ):
		"""Performs script Redo action"""
		self.statusBar.SetStatusText('Redo applied', 0)
		self.scriptControl.Redo()

	def OnFind( self, event ):
		"""Opens FindReplace window with Find tab focused"""
		self.scriptControl.StartFindReplace(0)

	def OnReplace( self, event ):
		"""Opens FindReplace window with Replace tab focused"""
		self.scriptControl.StartFindReplace(1)

	def OnSettings( self, event ):
		print 'Settings'

	def OnHelp( self, event ):
		self.statusBar.SetStatusText('Opening Help...', 0)

	def OnRun( self, event ):
		self.statusBar.SetStatusText('Play test starting...', 0)
		
		foldingLines = []
		for i, line in enumerate(self.scriptControl.GetText().split()):
			parent = self.scriptControl.GetFoldParent(i)
			if parent not in foldingLines:
				foldingLines.append(parent)
		print foldingLines
		for i in foldingLines:
			
			self.scriptControl.ToggleFold(i)


	def listBoxScripts_SelectionChanged( self, event ):
		self.RefreshScript(event.GetInt())

	def buttonApply_Clicked( self, event ):
		"""Applies the text modifications to all the scripts"""
		for script in Scripts:
			script.ApplyChanges()
		self.statusBar.SetStatusText('Modifications applied!', 0)

	def buttonCancel_Clicked( self, event ):
		print 'Cancel'

	#--------------------------------------------------------------
	# Find/Replace Functions
	#--------------------------------------------------------------
	def GetSearchLocations(self, searchString, matchcase, wholeword, scope, regex=None):
		results = {}
		if scope == 0:
			scripts = [Scripts[self.listBoxScripts.GetSelection()]]
		else:
			scripts = Scripts
		if not matchcase:
			searchString = searchString.lower()
		for i, script in enumerate(scripts):
			if not matchcase: text = script.GetText().lower()
			else: text = script.GetText()
			if searchString in text:
				lines, found = text.splitlines(), []
				for j in xrange(len(lines)):
					if searchString in lines[j] and j not in found:
						found.append(j)
				results[i] = found
		return results

	def FindPrevious( self, event ):
		pass

	def FindNext( self, event ):
		pass
