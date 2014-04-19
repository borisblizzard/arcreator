"""Subclass of ChangePartyMember_Dialog, which is generated by wxFormBuilder."""

import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates

# Implementing ChangePartyMember_Dialog
class ChangePartyMember_Dialog( Templates.ChangePartyMember_Dialog ):
	def __init__( self, parent ):
		Templates.ChangePartyMember_Dialog.__init__( self, parent )
	
	# Handlers for ChangePartyMember_Dialog events.
	def buttonOK_Clicked( self, event ):
		# TODO: Implement buttonOK_Clicked
		pass
	
	def buttonCancel_Clicked( self, event ):
		# TODO: Implement buttonCancel_Clicked
		pass
	
	