import wx
import Database.ARCed_Templates as Templates
#--------------------------------------------------------------------------------------
# BattleTestActor_Panel
#--------------------------------------------------------------------------------------

# Implementing BattleTestActor_Panel
class BattleTestActor_Panel( Templates.BattleTestActor_Panel ):
	def __init__( self, parent ):
		ARCed_Templates.BattleTestActor_Panel.__init__( self, parent )
	
	# Handlers for BattleTestActor_Panel events.
	def comboBoxActor_SelectionChanged( self, event ):
		# TODO: Implement comboBoxActor_SelectionChanged
		pass
	
	def spinCtrlLevel_ValueChanged( self, event ):
		# TODO: Implement spinCtrlLevel_ValueChanged
		pass
	
	def buttonInitialize_Clicked( self, event ):
		# TODO: Implement buttonInitialize_Clicked
		pass
	
	
