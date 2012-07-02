import wx
import Database.ARCed_Templates as Templates
#--------------------------------------------------------------------------------------
# AddParameter_Dialog
#--------------------------------------------------------------------------------------

# Implementing AddParameter_Dialog
class AddParameter_Dialog( Templates.AddParameter_Dialog ):
	def __init__( self, parent ):
		Templates.AddParameter_Dialog.__init__( self, parent )
	
	def buttonOK_Clicked( self, event ):
		"""End the dialog and return wx.ID_OK"""
		self.EndModal(wx.ID_OK)
	
	def buttonCancel_Clicked( self, event ):
		"""End the dialog and return wx.ID_CANCEL"""
		self.EndModal(wx.ID_CANCEL)
	
	
