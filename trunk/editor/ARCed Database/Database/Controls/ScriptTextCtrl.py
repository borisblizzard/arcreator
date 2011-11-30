import wx
from wxPython import stc
#--------------------------------------------------------------------------------------
# ScriptTextCtrl
#--------------------------------------------------------------------------------------

"""
TODO:
	- Consecutive keywords do not colorize, specifically "def self.WORD"
	- The Ruby range operator ".." and "..." do not colorize properly. If the first 
	  value is a number, the first dot inherits the color of a number as if it were
	  a float
"""

# For now, this works. The finished product can load the fonts, etc. from the cfg file.

if wx.Platform == '__WXMSW__':
    faces = { 'times': 'Times New Roman',
              'mono' : 'Consolas',
              'helv' : 'Arial',
              'other': 'Comic Sans MS',
              'size' : 10,
              'size2': 8,
            }
else:
    faces = { 'times': 'Times',
              'mono' : 'Courier',
              'helv' : 'Helvetica',
              'other': 'new century schoolbook',
              'size' : 10,
              'size2': 8,
            }

# Tabs/Indents
TAB_WIDTH = 2
INDENT_GUIDES = True
AUTO_INDENT = True
EDGE_COLUMN = 80
FOLDING = True

# Line Highlighting
SHOW_CARET = True
CARET_FORE = wx.Color(40, 40, 40)
CARET_BACK = wx.Color(0, 0, 0)
CARET_ALPHA = 40

# Keywords
RUBY_KEYWORDS = "BEGIN END __ENCODING__ __END__ __FILE__ __LINE__ alias and begin break case class def defined? do else elsif end ensure false for if in module next nil not or redo rescue retry return self super then true undef unless until when while yield"

# Styles unrelated to syntax
GLOBAL_STYLES = {
					stc.wxSTC_STYLE_DEFAULT     : "face:%(mono)s,size:%(size)d" % faces,
					stc.wxSTC_STYLE_DEFAULT     : "face:%(mono)s,size:%(size)d" % faces,
					stc.wxSTC_STYLE_LINENUMBER  : "back:#C0C0C0,face:%(helv)s,size:8" % faces,
					stc.wxSTC_STYLE_CONTROLCHAR : "face:%(other)s" % faces,
					stc.wxSTC_STYLE_BRACELIGHT  : "fore:#FFFFFF,back:#0000FF,bold",
					stc.wxSTC_STYLE_BRACEBAD    : "fore:#000000,back:#FF0000,bold"
				}

# Syntax highlighting
RUBY_STYLES = {
				# Default
				stc.wxSTC_RB_DEFAULT      : "fore:#000000,face:%(mono)s,size:%(size)d" % faces,
				# Comment Block (No block comment for Ruby, but setting global works for it)
				stc.wxSTC_ST_COMMENT      : "fore:#008000,face:%(other)s,size:%(size2)d" % faces,
				# Comment
				stc.wxSTC_RB_COMMENTLINE  : "fore:#008000,face:%(other)s,size:%(size2)d" % faces,
				# Numbers
				stc.wxSTC_RB_NUMBER       : "fore:#800000,face:%(mono)s,size:%(size)d" % faces,
				# Double-Quoted Strings
				stc.wxSTC_RB_STRING       : "fore:#800080,italic,face:%(times)s,size:%(size)d" % faces,
				# Single-Quoted Strings
				stc.wxSTC_RB_CHARACTER    : "fore:#C80080,italic,face:%(times)s,size:%(size)d" % faces,
				# Keywords
				stc.wxSTC_RB_WORD         : "fore:#0000FF,bold,size:%(size)d" % faces,
				# Class Name
				stc.wxSTC_RB_CLASSNAME    : "fore:#000000,bold,size:%(size)d" % faces,
				# Module Name
				stc.wxSTC_RB_MODULE_NAME  : "fore:#000000,bold,size:%(size)d" % faces,
				# Method/Function Name
				stc.wxSTC_RB_DEFNAME      : "fore:#000000,bold,size:%(size)d" % faces,
				# Operators
				stc.wxSTC_RB_OPERATOR     : "fore:#2B91AF,bold,size:%(size)d" % faces,
				# Normal Text/Local Variables
				stc.wxSTC_RB_IDENTIFIER   : "fore:#000000,face:%(mono)s,size:%(size)d" % faces,
				# Global Variable
				stc.wxSTC_RB_GLOBAL       : "fore:#000000,face:%(mono)s,size:%(size)d" % faces,
				# Instance Variable
				stc.wxSTC_RB_INSTANCE_VAR : "fore:#000000,face:%(mono)s,size:%(size)d" % faces,
				# Class Variable
				stc.wxSTC_RB_CLASS_VAR    : "fore:#000000,face:%(mono)s,size:%(size)d" % faces,
				# Regular Expressions
				stc.wxSTC_RB_REGEX        : "fore:#9370DB,face:%(mono)s,size:%(size)d" % faces,
				# Symbol
				stc.wxSTC_RB_SYMBOL       : "fore:#000000,face:%(mono)s,size:%(size)d" % faces,
				# Backticks
				stc.wxSTC_RB_BACKTICKS    : "fore:#808080,face:%(mono)s,size:%(size)d" % faces,
				# Data Section
				stc.wxSTC_RB_DATASECTION  : "fore:#000000,face:%(mono)s,size:%(size)d" % faces,
				# Error
				stc.wxSTC_RB_ERROR        : "fore:#FF0000,face:%(mono)s,bold,size:%(size)d" % faces
			  }

#--------------------------------------------------------------------------------------
# ScriptTextCtrl
#--------------------------------------------------------------------------------------

class ScriptTextCtrl(stc.wxStyledTextCtrl):

	def __init__(self, parent):
		"""Basic constructor for the ScriptTextCtrl"""
		super(ScriptTextCtrl, self).__init__(parent, 
			style=stc.wxSTC_STYLE_LINENUMBER|stc.wxSTC_STYLE_INDENTGUIDE)
		self.ApplyDefaults()
		self.BindHotKeys()
		self.Bind(wx.EVT_KEY_DOWN, self.KeyPressed)
		self.Bind(wx.EVT_TEXT_PASTE, self.CalculateLineNumberMargin)

	def KeyPressed( self, event ):
		"""Preprocess keystrokes before they are added to the Scintilla control"""
		ch = event.GetKeyCode()
		if ch == wx.WXK_RETURN and AUTO_INDENT:
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
		
	def DetermineIndentChange( self, text, previousLine, previousIndent ):
		"""Calculates the value to change the indent level by, if at all"""
		tabWidth = self.GetTabWidth()
		currentWords = text.strip().split()
		if len(currentWords) == 0: 
			return 0
		first, last = currentWords[0], currentWords[-1]
		if last == 'end' or last == 'else' or first in ['elsif', 'rescue', 'ensure']:
			prePreviousIndent = self.GetLineIndentation(previousLine - 1)
			if previousIndent + tabWidth != prePreviousIndent:
				indent = previousIndent - tabWidth
				self.SetLineIndentation(previousLine, indent)
			elif self.GetLineIndentation(previousLine + 1) == previousIndent + tabWidth:
				return tabWidth
			if last == 'end' : return -tabWidth
			return 0
		if first in ['class', 'module', 'if', 'elsif', 'else', 'begin', 'rescue', 
			'ensure','unless', 'while', 'until', 'def', 'for', 'case', 'when']:
			return tabWidth
		return 0

	def CalculateLineNumberMargin( self, event=None ):
		"""Ensure the margin width is large enough to fit the maximum number"""
		digits = len(str(self.GetLineCount()))
		self.SetMarginWidth(2, digits * 4)
		
	def BindHotKeys( self ):
		"""Binds hotkey commands to the script control"""
		self.CmdKeyAssign(ord('Z'), stc.wxSTC_SCMOD_ALT, stc.wxSTC_CMD_ZOOMIN)
		self.CmdKeyAssign(ord('X'), stc.wxSTC_SCMOD_ALT, stc.wxSTC_CMD_ZOOMOUT)

	def ApplyDefaults( self ):
		"""Applies default setting to the script control"""
		self.SetLexer(stc.wxSTC_LEX_RUBY)
		self.SetKeyWords(0, RUBY_KEYWORDS)
		for key, value in GLOBAL_STYLES.iteritems():
			self.StyleSetSpec(key, value)
		for key, value in RUBY_STYLES.iteritems():
			self.StyleSetSpec(key, value)
		self.SetTabWidth(TAB_WIDTH)
		self.SetCaretLineVisible(SHOW_CARET)
		self.SetCaretLineBack(CARET_BACK)
		self.SetCaretForeground(CARET_FORE)
		self.SetCaretLineBackAlpha(CARET_ALPHA)
		self.SetIndentationGuides(INDENT_GUIDES)
		self.SetEdgeColumn(EDGE_COLUMN)
		self.SetEdgeMode(stc.wxSTC_EDGE_LINE)
		if FOLDING:
			self.SetupMargins()

	def SetupMargins( self ):
		"""Sets up the margins for folding"""
		self.SetMarginType(2, stc.wxSTC_MARGIN_NUMBER)
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
			stc.wxSTC_MARK_VLINE, "white", "#808080")