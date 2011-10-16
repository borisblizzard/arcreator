import wx
import ARCed_Templates

# Implementing GenerateCurve_Dialog
class ARCedGenerateCurve_Dialog( ARCed_Templates.GenerateCurve_Dialog ):
	def __init__( self, parent, parameterIndex ):
		ARCed_Templates.GenerateCurve_Dialog.__init__( self, parent )
		self.ParameterIndex = parameterIndex

	def buttonOK_Clicked( self, event ):
		# End the dialog and return ID_OK
		self.EndModal(wx.ID_OK)

	def buttonCancel_Clicked( self, event ):
		# End the dialog and return ID_CANCEL
		self.EndModal(wx.ID_CANCEL)