
import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates

# Implementing CallCommonEvent_Dialog
class CallCommonEvent_Dialog( Templates.CallCommonEvent_Dialog ):
	def __init__( self, parent ):
		Templates.CallCommonEvent_Dialog.__init__( self, parent )

	# Handlers for CallCommonEvent_Dialog events.
	def buttonOK_Clicked( self, event ):
		# TODO: Implement buttonOK_Clicked
		pass

	def buttonCancel_Clicked( self, event ):
		# TODO: Implement buttonCancel_Clicked
		pass


