import os
import wx
import ARCed_Templates
from Core import Cache
import Kernel

# Implementing ChooseGraphic_Dialog
class ARCedChooseGraphic_Dialog( ARCed_Templates.ChooseGraphic_Dialog ):
	def __init__( self, parent, path, current, hue=0 ):
		''' Initializes control using passed "path" argument to populate the list '''
		ARCed_Templates.ChooseGraphic_Dialog.__init__( self, parent )
		self.Images = []
		# TODO: Add method to search nested directories as well, as well as RTP
		for fname in os.listdir(path):
			name, ext = os.path.splitext(fname)
			if ext in ['.png', '.jpg', '.bmp', '.gif']:  
				self.listBoxGraphics.Append(name)
				self.Images.append(path + '/' + fname)
		if current in self.listBoxGraphics.GetStrings():
			index = self.listBoxGraphics.FindString(current)
			self.listBoxGraphics.Select(index)
		elif self.listBoxGraphics.GetStrings().count > 0:
			self.listBoxGraphics.Select(0)
		else:
			self.buttonOK.Disable()
		self.sliderHue.SetValue(hue)
		# TODO: Test if the following is Windows compatible only
		self.bitmapGraphic.SetBitmap(wx.Bitmap(self.Images[self.listBoxGraphics.GetSelection()]))
		if hue != 0:
			# TODO: Apply hue change if necessary
			pass
	
	def listBoxGraphics_SelectionChanged( self, event ):
		""" Refreshes the bitmap to display the image associated with the current selection """
		index = self.listBoxGraphics.GetSelection()
		self.bitmapGraphic.SetBitmap(wx.Bitmap(self.Images[index]))
	
	def sliderHue_Scrolled( self, event ):
		""" Applies hue change to sample displayed bitmap """
		# TODO: Implement sliderHue_Scrolled 
		pass
	
	def buttonOK_Clicked( self, event ):
		""" Closes the dialog and returns wxID_OK """
		self.EndModal(wx.ID_OK)
	
	def buttonCancel_Clicked( self, event ):
		""" Closes the dialog and returns wxID_CANCEL """
		self.EndModal(wx.ID_CANCEL)
	
	
