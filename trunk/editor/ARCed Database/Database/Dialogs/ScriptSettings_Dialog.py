import wx
import Database.ARCed_Templates as Templates
from Database.ScriptEditor import Manager as SM
import Kernel
#--------------------------------------------------------------------------------------
# ScriptSettings_Dialog
#--------------------------------------------------------------------------------------

class ScriptSettings_Dialog( Templates.ScriptSettings_Dialog ):
	def __init__( self, parent, scriptcontrol ):
		Templates.ScriptSettings_Dialog.__init__( self, parent )
		global Config
		Config = Kernel.GlobalObjects.get_value('ARCed_config').get_section('ScriptEditor')
		self.ScriptControl = scriptcontrol
		self.InstalledFonts = sorted(wx.FontEnumerator.GetFacenames())
		self.comboBoxFont.AppendItems(self.InstalledFonts)
		self.listBoxDisplayItems.SetSelection(0)
		self.panelForeColor.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
		self.panelBackColor.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
		self.RefreshFontPage()

	def GetStyle( self, index ):
		"""Returns the associated style at the passed index"""
		return SM.GetStyles()[index]

	def ParseFormatString( self, index ):
		"""Parses the user defined format string for the style, and returns it"""
		key = self.GetStyle(index)[1]
		fstring = Config.get(key)
		style = ScintillaStyle()
		for format in fstring.split(','):
			if format.startswith('fore:'):	style.fore = SM.ParseColor(format.split(':')[1])
			elif format.startswith('back:'): style.back = SM.ParseColor(format.split(':')[1])
			elif format.startswith('face:'): style.face = format.split(':')[1]
			elif format.startswith('size:'): style.size = int(format.split(':')[1])
			elif format.lower() == 'bold': style.bold = True
			elif format.lower() == 'italic': style.italic = True
		if style.face is None:
			if index == 0: style.face = self.GetSystemFont()
			else: style.face = self.ParseFormatString(0).face
		if style.size is None:
			if index == 0: style.size = 10
			else: style.size = self.ParseFormatString(0).size
		return style

	def GetSystemFont( self ):
		"""Returns a default mono-spaced font for the system"""
		return wx.Font(10, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, 
			wx.FONTWEIGHT_NORMAL).GetFaceName()

	def RefreshFontPage( self ):
		"""Refreshes the controls to reflect the selected style"""
		itemIndex = self.listBoxDisplayItems.GetSelection()
		if itemIndex < 0:
			return
		style = self.ParseFormatString(itemIndex)
		try:
			index = self.InstalledFonts.index(style.face)
		except:
			index = self.InstalledFonts.index(style.GetSystemFont())
			Kernel.Log(str.format('Font \"{}\" not found on system.', style.face), 
			'[Script Editor]', True, False)
		self.comboBoxFont.SetSelection(index)
		self.textCtrlForeColor.ChangeValue(style.GetForeColorAsString())
		self.textCtrlBackColor.ChangeValue(style.GetBackColorAsString())
		self.checkBoxBold.SetValue(style.bold)
		self.checkBoxItalic.SetValue(style.italic)
		style.size = max(6, min(style.size, 24))
		self.comboBoxSize.SetSelection(style.size - 6)
		self.panelForeColor.SetBackgroundColour(style.fore)
		self.panelBackColor.SetBackgroundColour(style.back)
		self.panelForeColor.Refresh()
		self.panelBackColor.Refresh()

	def RefreshEditorPage( self ):
		pass

	def noteBookSettings_PageChanged( self, event ):
		"""Refreshes the page then displays and switches control to it"""
		index = event.GetSelection()
		if index == 0: self.RefreshFontPage()
		else: self.RefreshEditorPage()
		self.noteBookSettings.ChangeSelection(index)
	
	def comboBoxFont_SelectionChanged( self, event ):
		

		print event.GetString()


		pass

	
	def comboBoxSize_SelectionChanged( self, event ):
		# TODO: Implement comboBoxSize_SelectionChanged
		pass
	
	def listBoxDisplayItems_SelectionChanged( self, event ):
		
		# START HERE
		self.RefreshFontPage()
	
	def textCtrlForeColor_TextChanged( self, event ):
		# TODO: Implement textCtrlForeColor_TextChanged
		pass
	
	def buttonForeColor_Clicked( self, event ):
		# TODO: Implement buttonForeColor_Clicked
		pass
	
	def textCtrlBackColor_TextChanged( self, event ):
		# TODO: Implement textCtrlBackColor_TextChanged
		pass
	
	def buttonBackColor_Clicked( self, event ):
		# TODO: Implement buttonBackColor_Clicked
		pass
	
	def checkBoxBold_CheckChanged( self, event ):
		# TODO: Implement checkBoxBold_CheckChanged
		pass
	
	def checkBoxItalic_CheckChanged( self, event ):
		# TODO: Implement checkBoxItalic_CheckChanged
		pass
	
	def spinCtrlTabWidth_ValueChanged( self, event ):
		# TODO: Implement spinCtrlTabWidth_ValueChanged
		pass
	
	def spinCtrlEdgeColumn_ValueChanged( self, event ):
		# TODO: Implement spinCtrlEdgeColumn_ValueChanged
		pass
	
	def checkBoxIndentGuide_CheckChanged( self, event ):
		# TODO: Implement checkBoxIndentGuide_CheckChanged
		pass
	
	def checkBoxCaret_CheckChanged( self, event ):
		# TODO: Implement checkBoxCaret_CheckChanged
		pass
	
	def textCtrlCaretColor_TextChanged( self, event ):
		# TODO: Implement textCtrlCaretColor_TextChanged
		pass
	
	def buttonCaretColor_Clicked( self, event ):
		# TODO: Implement buttonCaretColor_Clicked
		pass
	
	def spinCtrlCaretAlpha_ValueChanged( self, event ):
		# TODO: Implement spinCtrlCaretAlpha_ValueChanged
		pass
	
	


#--------------------------------------------------------------------------------------
# ScintillaStyle
#--------------------------------------------------------------------------------------

class ScintillaStyle(object):

	def __init__(self, fore=wx.BLACK, back=wx.WHITE, face=None, size=None, 
			 bold=False, italic=False):
		self.fore = fore
		self.back = back
		self.face = face
		self.size = size
		self.bold = bold
		self.italic = italic

	def GetForeColorAsString( self ):
		return self.fore.GetAsString(wx.C2S_HTML_SYNTAX)

	def GetBackColorAsString( self ):
		return self.back.GetAsString(wx.C2S_HTML_SYNTAX)

	def GetFormatString( self ):
		"""Returns a formatted string to be used with the configuration"""
		fstring = str.format('fore:{0},back:{1},face:{2},size:{3}', 
			self.GetForeColorAsString(), self.GetBackColorAsString(),
			self.face, self.size)
		if self.bold: fstring = str.format('{},bold', fstring)
		if self.italic: fstring = str.format('{},italic', fstring)
		return fstring