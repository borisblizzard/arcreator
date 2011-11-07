
import wx
import ARCed_Templates
import ARCedChangeMaximum_Dialog
import ARCedEventCommands1_Panel
import ARCedEventCommands2_Panel
import ARCedEventCommands3_Panel
import ARCedChooseSwitchVariable_Dialog
from DatabaseUtil import DatabaseUtil as util

# Implementing CommonEvents_Panel
class ARCedCommonEvents_Panel( ARCed_Templates.CommonEvents_Panel ):
	def __init__( self, parent ):
		ARCed_Templates.CommonEvents_Panel.__init__( self, parent )

		util.DrawHeaderBitmap(self.bitmapCommonEvents, 'Common Events')

	# Handlers for CommonEvents_Panel events.
	def listBoxCommonEvents_SelectionChanged( self, event ):
		# TODO: Implement listBoxCommonEvents_SelectionChanged
		pass

	def buttonMaximum_Clicked( self, event ):
		# TODO: Implement buttonMaximum_Clicked
		pass

	def textCtrlName_ValueChanged( self, event ):
		# TODO: Implement textCtrlName_ValueChanged
		pass

	def comboBoxTrigger_SelectionChanged( self, event ):
		# TODO: Implement comboBoxTrigger_SelectionChanged
		pass

	def comboBoxCondition_Clicked( self, event ):
		# TODO: Implement comboBoxCondition_Clicked
		pass

	def listBoxEvents_DoubleClicked( self, event ):
		# TODO: Implement listBoxEvents_DoubleClicked
		pass

	def listBoxPage_SelectionChanged( self, event ):
		# TODO: Implement listBoxPage_SelectionChanged
		pass


