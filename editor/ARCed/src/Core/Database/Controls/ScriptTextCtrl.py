import wx
from wxPython.stc import *
import Kernel
from Core.Database.ScriptEditor import Manager as SM
from Core.Database.Dialogs import FindReplace_Dialog

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
BRACES = ['(', ')', '[', ']', '{', '}', '<', '>']
INDENT_WORDS = ['if', 'unless', 'def', 'module', 'class', 'begin', 'while', 'until', 'for']
UNINDENT_WORDS = ['elsif', 'else', 'when', 'rescue', 'ensure']

class ScriptTextCtrl(wxStyledTextCtrl):

	SCRIPT_UPDATEUI = wx.PyEventBinder(wxEVT_STC_UPDATEUI, 1)

	def __init__(self, parent):
		"""Basic constructor for the ScriptTextCtrl"""
		super(ScriptTextCtrl, self).__init__(parent, 
			style=wxSTC_STYLE_LINENUMBER|wxSTC_STYLE_INDENTGUIDE)
		from Core.Database.ScriptEditor import FindReplaceData
		global Config
		Config = Kernel.GlobalObjects.get_value('ARCed_config').get_section('ScriptEditor')
		self.FindReplaceData = FindReplaceData()
		self.FindDialog = None
		self.ApplySettings()
		self.BindHotKeys()
		self.Bind(wx.EVT_KEY_DOWN, self.KeyPressed)
		self.Bind(wx.EVT_TEXT_PASTE, self.CalculateLineNumberMargin)
		self.Bind(self.SCRIPT_UPDATEUI, self.UpdateUI)
		self.Bind(wx.PyEventBinder(wxEVT_STC_MARGINCLICK, 1), self.MarginClicked)
		
	def UpdateUI( self, event ):
		"""Updates brace matching"""
		if Config.get('brace_match').lower() == 'true':
			pos = self.GetCurrentPos() - 1
			chr = unichr(self.GetCharAt(pos))
			if chr in BRACES:
				has_match = self.BraceMatch(pos)
				if  has_match > -1:
					self.BraceHighlight(has_match, pos)
				else:
					self.BraceBadLight(pos)
			else:
				pos += 1
				chr = unichr(self.GetCharAt(pos))
				if chr in BRACES:
					has_match = self.BraceMatch(pos)
					if  has_match > -1:
						self.BraceHighlight(has_match, pos)
					else:
						self.BraceBadLight(pos)
				else:
					self.BraceHighlight(-1, -1)
		else:
			self.BraceHighlight(-1, -1)

	def MarginClicked(self, event ):
		"""Performs code folding functions"""
		line = self.LineFromPosition(event.GetPosition())
		if line == self.GetFoldParent(line + 1):
			self.ToggleFold(line)

	def KeyPressed( self, event ):
		"""Preprocess keystrokes before they are added to the Scintilla control"""
		ch = event.GetKeyCode()
		if event.CmdDown():
			if ch == ord('F'): # Find
				self.StartFindReplace(0)
				return
			elif ch == ord('H'): # Replace
				self.StartFindReplace(1) 
				return
			elif ch == ord('S'): # Save
				pass
				return
		if ch == wx.WXK_RETURN:
			thisLine = self.GetCurrentLine()
			nextLine = thisLine + 1
			text = self.GetCurLine()[0]
			indent = self.GetLineIndentation(thisLine)
			indent += self.DetermineIndentChange(text, thisLine, indent)
			self.CmdKeyExecute(wxSTC_CMD_NEWLINE)
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
		if last == 'end' or first in UNINDENT_WORDS:
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
		if first in INDENT_WORDS:
			return tabWidth
		return 0

	def CalculateLineNumberMargin( self, event=None ):
		"""Ensure the margin width is large enough to fit the maximum number"""
		self.SetMarginWidth(2, len(str(self.GetLineCount())) * 4)
		
	def BindHotKeys( self ):
		"""Binds hotkey commands to the script control"""
		self.CmdKeyAssign(ord('Z'), wxSTC_SCMOD_ALT, wxSTC_CMD_ZOOMIN)
		self.CmdKeyAssign(ord('X'), wxSTC_SCMOD_ALT, wxSTC_CMD_ZOOMOUT)

	def ApplySettings( self ):
		"""Applies default setting to the script control"""
		self.SetLexer(wxSTC_LEX_RUBY)
		self.SetKeyWords(0, RUBY_KEYWORDS)
		SM.ApplyUserSettings(self)
		self.SetEdgeMode(wxSTC_EDGE_LINE)
		self.SetMarginType(2, wxSTC_MARGIN_NUMBER)
		if Config.get('folding').lower() == 'true':
			self.SetupMargins()
		
	def SetupMargins( self ):
		"""Sets up the margins for folding"""
		self.SetMarginType(3, wxSTC_MARGIN_SYMBOL)
		self.SetMarginWidth(3, 16)
		self.SetProperty("fold", "3")
		self.SetMarginType(3, wxSTC_MARGIN_SYMBOL)
		self.SetMarginMask(3, wxSTC_MASK_FOLDERS)
		self.SetMarginSensitive(3, True)
		self.SetMarginWidth(3, 12)
		self.MarkerDefine(wxSTC_MARKNUM_FOLDEROPEN, wxSTC_MARK_BOXMINUS, "white", "#808080")
		self.MarkerDefine(wxSTC_MARKNUM_FOLDER, wxSTC_MARK_BOXPLUS, "white", "#808080")
		self.MarkerDefine(wxSTC_MARKNUM_FOLDEROPENMID, wxSTC_MARK_BOXMINUSCONNECTED, "white", "#808080")
		self.MarkerDefine(wxSTC_MARKNUM_FOLDEREND, wxSTC_MARK_BOXPLUSCONNECTED, "white", "#808080")
		self.MarkerDefine(wxSTC_MARKNUM_FOLDERTAIL, wxSTC_MARK_LCORNER, "white", "#808080")
		self.MarkerDefine(wxSTC_MARKNUM_FOLDERSUB, wxSTC_MARK_VLINE, "white", "#808080")
		self.MarkerDefine(wxSTC_MARKNUM_FOLDERMIDTAIL, wxSTC_MARK_TCORNER, "white", "#808080")

	def NormalizeIndenting( self ):
		"""Automatically applies conventional indent levels to the script"""
		new_text = ''
		flag = False
		currentIndent = 0
		for i in xrange(self.LineCount):
			line = self.GetLine(i).strip()
			words = line.split()
			if line.startswith('=begin') or line.startswith('=end'):
				flag = line.startswith('=begin')
				new_text += u'\t' * currentIndent + line + '\r\n'
			elif line.startswith('#') or flag:
				new_text += u'\t' * currentIndent + line + '\r\n'
			elif len(words) > 0 and not line.startswith('#') and not flag:
				first_word = words[0]
				if first_word in INDENT_WORDS or 'do' in words or 'case' in words:
					new_text += u'\t' * currentIndent + line + '\r\n'
					if not 'end' in words or not ';end' in words:
						currentIndent += 1
				elif first_word in UNINDENT_WORDS:
					new_text += u'\t' * (currentIndent - 1)  + line + '\r\n'
				elif first_word.strip(';)}') == 'end':
					currentIndent -= 1
					new_text += u'\t' * currentIndent + line + '\r\n'
				else:
					new_text += u'\t' * currentIndent + line + '\r\n'
			else:
				new_text += '\r\n'
		self.ClearAll()
		self.SetText(new_text)

	def Find(self, text, matchcase, wholeword, regex, wildcards, up, second_pass=False):
		if up:
			find = self.SearchPrev
			self.SetCurrentPos(self.SelectionStart)
			if second_pass:
				self.SetSelection(self.Length, self.Length)
		else:
			find = self.SearchNext
			self.SetCurrentPos(self.SelectionEnd)
			if second_pass:
				self.SetCurrentPos(0)
		self.SearchAnchor()
		flags = 0
		if matchcase: flags |= wxSTC_FIND_MATCHCASE
		if wholeword: flags |= wxSTC_FIND_WHOLEWORD
		if regex: 
			flags |= wxSTC_FIND_REGEXP
			if wildcards:
				text = text.replace('*', '.')
		pos = find(flags, text)
		if pos != -1:
			second_pass = False
			self.EnsureCaretVisible()
		elif not second_pass:
			# This effectively enables looping the search
			self.Find(text, matchcase, wholeword, regex, wildcards, up, True)