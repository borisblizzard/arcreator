import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates
#--------------------------------------------------------------------------------------
# AnimationCellProperties_Dialog
#--------------------------------------------------------------------------------------

# Implementing AnimationCellProperties_Dialog
class AnimationCellProperties_Dialog( Templates.AnimationCellProperties_Dialog ):
	def __init__( self, parent ):
		Templates.AnimationCellProperties_Dialog.__init__( self, parent )
	
	# Handlers for AnimationCellProperties_Dialog events.
	def buttonOK_Clicked( self, event ):
		# TODO: Implement buttonOK_Clicked
		pass
	
	def buttonCancel_Clicked( self, event ):
		# TODO: Implement buttonCancel_Clicked
		pass
	
	
