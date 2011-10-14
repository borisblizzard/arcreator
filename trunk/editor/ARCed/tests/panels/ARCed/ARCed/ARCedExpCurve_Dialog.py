import wx
import ARCed_Templates

# Implementing ExpCurve_Dialog
class ARCedExpCurve_Dialog( ARCed_Templates.ExpCurve_Dialog ):
	def __init__( self, parent ):
		ARCed_Templates.ExpCurve_Dialog.__init__( self, parent )
		self.refreshExpTable
	
	# Handlers for ExpCurve_Dialog events.
	def sliderBasis_Scrolled( self, event ):
		# Sync the spin control and refresh the experience list
		self.spinCtrlBasis.SetValue(self.sliderBasis.GetValue())
		self.refreshExpTable
	
	def spinCtrlBasis__ValueChanged( self, event ):
		# Sync the slider control and refresh the table
		self.sliderBasis.SetValue(self.spinCtrlBasis.GetValue())
		self.refreshExpTable
	
	def sliderInflation_Scrolled( self, event ):
		# Sync the spin control and refresh the experience list
		self.spinCtrlInflation.SetValue(self.sliderInflation.GetValue())
		self.refreshExpTable
	
	def spinCtrlInflation_ValueChanged( self, event ):
		# Sync the slider control and refresh the table
		self.sliderInflation.SetValue(self.spinCtrlInflation.GetValue())
		self.refreshExpTable
	
	def buttonOK_Clicked( self, event ):
		# End the dialog and return ID_OK
		self.EndModal(wx.ID_OK)
	
	def buttonCancel_Clicked( self, event ):
		# End the dialog and return ID_CANCEL
		self.EndModal(wx.ID_CANCEL)

	def refreshExpTable(self):
		# TODO: Implement generation of experience tables
		print 'Generate experience table...'