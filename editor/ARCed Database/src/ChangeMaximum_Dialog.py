import wx
import ARCed_Templates 

class ChangeMaximum_Dialog(ARCed_Templates.ChangeMaximum_Dialog ):
	"""Initialize dialog, setting using pass argument to set the initial value."""
	def __init__( self, parent, currentMaximum, minValue, maxValue):
		ARCed_Templates.ChangeMaximum_Dialog.__init__( self, parent )
		self.spinCtrlMaximum.SetRange(minValue, maxValue)
		self.spinCtrlMaximum.SetValue(currentMaximum)

	def buttonOK_Clicked( self, event ):
		"""Closes the dialog and returns wxID_OK"""
		self.EndModal(wx.ID_OK)

	def buttonCancel_Clicked( self, event ):
		"""Closes the dialog and returns wxID_CANCEL"""
		self.EndModal(wx.ID_CANCEL)