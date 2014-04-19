"""Subclass of ChangePictureColorTone_Dialog, which is generated by wxFormBuilder."""

import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates

# Implementing ChangePictureColorTone_Dialog
class ChangePictureColorTone_Dialog( Templates.ChangePictureColorTone_Dialog ):
	def __init__( self, parent ):
		Templates.ChangePictureColorTone_Dialog.__init__( self, parent )
	
	# Handlers for ChangePictureColorTone_Dialog events.
	def sliderRed_ScrollChanged( self, event ):
		# TODO: Implement sliderRed_ScrollChanged
		pass
	
	def spinCtrlRed_ValueChanged( self, event ):
		# TODO: Implement spinCtrlRed_ValueChanged
		pass
	
	def sliderGreen_ScrollChanged( self, event ):
		# TODO: Implement sliderGreen_ScrollChanged
		pass
	
	def spinCtrGreenl_ValueChanged( self, event ):
		# TODO: Implement spinCtrGreenl_ValueChanged
		pass
	
	def sliderBlue_ScrollChanged( self, event ):
		# TODO: Implement sliderBlue_ScrollChanged
		pass
	
	def spinCtrlBlue_ValueChanged( self, event ):
		# TODO: Implement spinCtrlBlue_ValueChanged
		pass
	
	def sliderStrGray_ScrollChanged( self, event ):
		# TODO: Implement sliderStrGray_ScrollChanged
		pass
	
	def spinCtrlStrGray_ValueChanged( self, event ):
		# TODO: Implement spinCtrlStrGray_ValueChanged
		pass
	
	def buttonOK_Clicked( self, event ):
		# TODO: Implement buttonOK_Clicked
		pass
	
	def buttonCancel_Clicked( self, event ):
		# TODO: Implement buttonCancel_Clicked
		pass
	
	