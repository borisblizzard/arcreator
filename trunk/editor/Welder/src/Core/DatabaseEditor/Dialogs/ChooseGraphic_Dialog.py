import os

import wx
import PIL

from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')
Templates = Core.Database.Welder_Templates
RTPFunctions = Core.Cache.RTPFunctions
PILCache =  Core.Cache.PILCache

class ChooseGraphic_Dialog( Templates.ChooseGraphic_Dialog ):
	def __init__( self, parent, folder, current, hue ):
		Templates.ChooseGraphic_Dialog.__init__( self, parent )
		self.glCanvasGraphic.canvas.Bind(wx.EVT_LEFT_DOWN, 
			Kernel.Protect(self.glCanvas_LeftMouse))
		#self.Centre( wx.BOTH )
		self.glCanvasGraphic.SetDrawMode(5)
		self.ImageList = ['(None)'] 
		self.ImageList.extend(RTPFunctions.GetFileList(os.path.join('Graphics', folder)))
		self.ImageIndex = 0
		if folder == 'Characters': self.cache = PILCache.Character
		elif folder == 'Battlers': self.cache = PILCache.Battler
		# TODO: Implement the rest...
		if current in self.ImageList: 
			self.ImageIndex = self.ImageList.index(current)
		self.listBoxGraphics.AppendItems(self.ImageList)
		self.listBoxGraphics.SetSelection(self.ImageIndex)
		self.sliderHue.SetValue(hue)
		self.RefreshCanvas()

	def RefreshCanvas( self ):
		if self.ImageIndex == 0:
			image = PIL.Image.new('RGBA', (32, 32))
		else:
			filename = self.ImageList[self.ImageIndex]
			hue = self.sliderHue.GetValue()
			image = self.cache(filename, hue)
		self.glCanvasGraphic.ChangeImage(image)
		del (image)

	def glCanvas_LeftMouse( self, event ):

		print('LEFT DOWN')

	def listBoxGraphics_SelectionChanged( self, event ):
		"""Changes the image index and refreshes the canvas"""
		self.ImageIndex = event.GetSelection()
		self.RefreshCanvas()

	def sliderHue_Scrolled( self, event ):
		"""Refreshes the canvas and redraws with the selected hue rotation"""
		self.RefreshCanvas()
		PILCache.CacheLimit()

	def GetSelection( self ):
		"""Returns the filename and hue that was selected by the user"""
		if self.ImageIndex == 0:
			return 0, 0
		return self.ImageList[self.ImageIndex], self.sliderHue.GetValue()
	
	def buttonOK_Clicked( self, event ):
		"""End the dialog and return wx.ID_OK"""
		self.EndModal(wx.ID_OK)
	
	def buttonCancel_Clicked( self, event ):
		"""End the dialog and return wx.ID_CANCEL"""
		self.EndModal(wx.ID_CANCEL)
	
	
