import wx
from wxPython import stc #* TODO: Use stc for now for benefit of IntelliSense
import Kernel
from Database.Dialogs import FindReplace_Dialog

"""
TODO:
	- Consecutive keywords do not colorize, specifically "def self.WORD"
	- The Ruby range operator ".." and "..." do not colorize properly. If the first 
	  value is a number, the first dot inherits the color of a number as if it were
	  a float. This is an inherit problem with the actual Scintilla library that has
	  not been fixed.
"""
#--------------------------------------------------------------------------------------
# ScriptTextCtrl
#--------------------------------------------------------------------------------------

RUBY_KEYWORDS = "BEGIN END __ENCODING__ __END__ __FILE__ __LINE__ alias and begin break case class def defined? do else elsif end ensure false for if in module next nil not or redo rescue retry return self super then true undef unless until when while yield"

class ScriptTextCtrl(stc.wxStyledTextCtrl):

	SCRIPT_UPDATEUI = wx.PyEventBinder(stc.wxEVT_STC_UPDATEUI, 1)

	def __init__(self, parent):
		"""Basic constructor for the ScriptTextCtrl"""
		super(ScriptTextCtrl, self).__init__(parent, 
			style=stc.wxSTC_STYLE_LINENUMBER|stc.wxSTC_STYLE_INDENTGUIDE)
		from Database.ScriptEditor import FindReplaceData
		global Config
		Config = Kernel.GlobalObjects.get_value('ARCed_config').get_section('ScriptEditor')
		self.FindReplaceData = FindReplaceData()
		self.FindDialog = None
		self.ApplySettings()
		self.BindHotKeys()
		self.Bind(wx.EVT_KEY_DOWN, self.KeyPressed)
		self.Bind(wx.EVT_TEXT_PASTE, self.CalculateLineNumberMargin)
		self.Bind(wx.PyEventBinder(stc.wxEVT_STC_MARGINCLICK, 1), self.MarginClicked)
		
	def MarginClicked(self, event ):
		"""Performs code folding functions"""
		line = self.LineFromPosition(event.GetPosition())
		if line == self.GetFoldParent(line + 1):
			self.ToggleFold(line)

	def KeyPressed( self, event ):
		"""Preprocess keystrokes before they are added to the Scintilla control"""
		ch = event.GetKeyCode()
		# Check for hotkey input
		if event.CmdDown():
			if ch == ord('F'):
				self.StartFindReplace(0)
				return
			elif ch == ord('H'):
				self.StartFindReplace(1)
				return
		if ch == wx.WXK_RETURN:
			# Process auto-indentation if the return key was pressed
			thisLine = self.GetCurrentLine()
			nextLine = thisLine + 1
			text = self.GetCurLine()[0]
			indent = self.GetLineIndentation(thisLine)
			indent += self.DetermineIndentChange(text, thisLine, indent)
			self.CmdKeyExecute(stc.wxSTC_CMD_NEWLINE)
			self.SetLineIndentation(nextLine, indent)
			self.GotoPos(self.GetLineEndPosition(nextLine))
			self.CalculateLineNumberMargin()
		else:
			event.Skip()

	def StartFindReplace(self, index=0 ):
		"""Creates if needed, and focuses the Find & Replace window"""
		text = self.SelectedText
		if len(text) > 0:
			self.FindReplaceData.SearchString[index] = text
		if self.FindDialog is None:
			self.FindDialog = dlg = FindReplace_Dialog(self, index, self.FindReplaceData)
		else:
			dlg = self.FindDialog
		dlg.RefreshTab(index)
		dlg.noteBookFindReplace.ChangeSelection(index)
		if index == 0: dlg.textCtrlFindSearch.SetFocus()
		else: dlg.textCtrlReplaceSearch.SetFocus()
		dlg.Show(True)
		dlg.SetFocus()
		
	def DetermineIndentChange( self, text, previousLine, previousIndent ):
		"""Calculates the value to change the indent level by, if at all"""
		tabWidth = self.GetTabWidth()
		currentWords = text.strip().split()
		if len(currentWords) == 0: 
			return 0
		first, last = currentWords[0], currentWords[-1]
		if last == 'end' or last == 'else' or first in ['when', 'elsif', 'rescue', 'ensure']:
			if first == 'when':
				previousText = self.GetLine(previousLine - 1).strip()
				if 'then' in currentWords: return 0
				elif 'case ' in previousText: return tabWidth
				else: return tabWidth
			prePreviousIndent = self.GetLineIndentation(previousLine - 1)
			if previousIndent + tabWidth != prePreviousIndent:
				indent = previousIndent - tabWidth
				self.SetLineIndentation(previousLine, indent)
			elif self.GetLineIndentation(previousLine + 1) == previousIndent + tabWidth:
				return tabWidth
			if last == 'end' : return -tabWidth
			return 0
		if first in ['class', 'module', 'if', 'elsif', 'else', 'begin', 'rescue', 
			'ensure','unless', 'while', 'until', 'def', 'for', 'case']:
			return tabWidth
		return 0

	def CalculateLineNumberMargin( self, event=None ):
		"""Ensure the margin width is large enough to fit the maximum number"""
		self.SetMarginWidth(2, len(str(self.GetLineCount())) * 4)
		
	def BindHotKeys( self ):
		"""Binds hotkey commands to the script control"""
		self.CmdKeyAssign(ord('Z'), stc.wxSTC_SCMOD_ALT, stc.wxSTC_CMD_ZOOMIN)
		self.CmdKeyAssign(ord('X'), stc.wxSTC_SCMOD_ALT, stc.wxSTC_CMD_ZOOMOUT)
		#self.CmdKeyAssign(ord('Q'), stc.wxSTC_SCMOD_CTRL, stc.wxSTC_CMD_

	def ApplySettings( self ):
		"""Applies default setting to the script control"""
		# TODO: Reorganize imports so this doesn't have to be here
		from Database.ScriptEditor import Manager
		self.SetLexer(stc.wxSTC_LEX_RUBY)
		self.SetKeyWords(0, RUBY_KEYWORDS)
		Manager.ApplyUserSettings(self)
		self.SetEdgeMode(stc.wxSTC_EDGE_LINE)
		self.SetMarginType(2, stc.wxSTC_MARGIN_NUMBER)
		if Config.get('folding').lower() == 'true':
			self.SetupMargins()
		
	def SetupMargins( self ):
		"""Sets up the margins for folding"""
		self.SetMarginType(3, stc.wxSTC_MARGIN_SYMBOL)
		self.SetMarginWidth(3, 16)
		self.SetProperty("fold", "3")
		self.SetMarginType(3, stc.wxSTC_MARGIN_SYMBOL)
		self.SetMarginMask(3, stc.wxSTC_MASK_FOLDERS)
		self.SetMarginSensitive(3, True)
		self.SetMarginWidth(3, 12)
		self.MarkerDefine(stc.wxSTC_MARKNUM_FOLDEROPEN, 
			stc.wxSTC_MARK_BOXMINUS, "white", "#808080")
		self.MarkerDefine(stc.wxSTC_MARKNUM_FOLDER,
			stc.wxSTC_MARK_BOXPLUS, "white", "#808080")
		self.MarkerDefine(stc.wxSTC_MARKNUM_FOLDEROPENMID,
			stc.wxSTC_MARK_BOXMINUSCONNECTED, "white", "#808080")
		self.MarkerDefine(stc.wxSTC_MARKNUM_FOLDEREND,
			stc.wxSTC_MARK_BOXPLUSCONNECTED, "white", "#808080")
		self.MarkerDefine(stc.wxSTC_MARKNUM_FOLDERTAIL,
			stc.wxSTC_MARK_LCORNER, "white", "#808080")
		self.MarkerDefine(stc.wxSTC_MARKNUM_FOLDERSUB,
			stc.wxSTC_MARK_VLINE, "white", "#808080")
		self.MarkerDefine(stc.wxSTC_MARKNUM_FOLDERMIDTAIL,
			stc.wxSTC_MARK_TCORNER, "white", "#808080")