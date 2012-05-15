import wx
import Database.ARCed_Templates as Templates
#--------------------------------------------------------------------------------------
# FindReplace_Dialog
#--------------------------------------------------------------------------------------

class FindReplace_Dialog( Templates.FindReplace_Dialog ):
	def __init__( self, parent, index, data ):
		Templates.FindReplace_Dialog.__init__( self, parent )
		self.Data = data

	def RefreshTab(self, index=0 ):
		if index == 0:
			self.textCtrlFindSearch.ChangeValue(self.Data.SearchString[0])
			self.comboBoxLook.SetSelection(self.Data.Scope)
			self.checkBoxFindMatchCase.SetValue(self.Data.MatchCase)
			self.checkBoxFindWholeWord.SetValue(self.Data.WholeWord)
			self.checkBoxFindSearchUp.SetValue(self.Data.SearchUp)
			self.checkBoxFindFlags.SetValue(self.Data.RegExSearch)
			self.comboBoxFindFlags.SetSelection(self.Data.RegExMode)
			self.comboBoxFindFlags.Enable(self.Data.RegExSearch)
		else:
			self.textCtrlReplaceSearch.ChangeValue(self.Data.SearchString[1])
			self.textCtrlReplace.ChangeValue(self.Data.ReplaceString)
			self.comboBoxLookReplace.SetSelection(self.Data.Scope)
			self.checkBoxReplaceMatchCase.SetValue(self.Data.MatchCase)
			self.checkBoxReplaceWholeWord.SetValue(self.Data.WholeWord)
			self.checkBoxReplaceSearchUp.SetValue(self.Data.SearchUp)
			self.checkBoxReplaceFlags.SetValue(self.Data.RegExSearch)
			self.comboBoxReplaceFlags.SetSelection(self.Data.RegExMode)
			self.comboBoxReplaceFlags.Enable(self.Data.RegExSearch)						  

	def noteBookFindReplace_PageChanged( self, event ):
		"""Changes the current page"""
		# I don't know if it is a bug, or a problem with the Windows, but the pages
		# do not change automatically, and must be done this way...
		index = event.GetSelection()
		self.RefreshTab(index)
		self.noteBookFindReplace.ChangeSelection(index)
		
	def comboBoxLook_SelectionChanged( self, event ):
		self.Data.Scope = event.GetInt()
	
	def checkBoxMatchCase_CheckChanged( self, event ):
		self.Data.MatchCase = event.Checked()
	
	def checkBoxWholeWord_CheckChanged( self, event ):
		self.Data.WholeWord = event.Checked()
	
	def checkBoxSearchUP_CheckChanged( self, event ):
		self.Data.SearchUp = event.Checked()
	
	def checkBoxFlags_CheckChanged( self, event ):
		# TODO: Implement checkBoxFlags_CheckChanged
		pass
	
	def comboBoxFlags_SelectionChanged( self, event ):
		# TODO: Implement comboBoxFlags_SelectionChanged
		pass
	
	def buttonFindNext_Clicked( self, event ):
		# TODO: Implement buttonFindNext_Clicked
		pass
	
	def buttonReplace_Clicked( self, event ):
		# TODO: Implement buttonReplace_Clicked
		pass
	
	def buttonReplaceAll_Clicked( self, event ):
		# TODO: Implement buttonReplaceAll_Clicked
		pass