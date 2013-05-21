import wx
from PIL import Image
import pyglet
import pyglet.gl as gl

from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

PygletGLPanel = Core.PygletWX.PygletGLPanel
#--------------------------------------------------------------------------------------
# EditorGLPanel
#--------------------------------------------------------------------------------------

class EditorGLPanel(PygletGLPanel):

	def __init__(self, parent, id=wx.ID_ANY, rows=1, columns=1, coord=(0,0), drawmode=1):
		"""Basic constructor for the wxGLCanvas

		Arguments:
		parent -- The wxWindow instance to set as this panel's parent
		id -- The ID of the panel
		rows -- The number of horizontal rows used for tiles
		columns -- The number of vertical columns used for tiles
		coord -- The coordinate of the tile that the image will draw from the source
		drawmode -- An integer to decide what drawing mode will be used. 
			0: CropAndShrink -- Images will be both scaled down and cropped to fit
			1: Shrink -- Scales image down if too large, else the image is simply centered
			2: StretchAspect -- The image will be stretched to fill panel while maintaining aspect ratio
			3: Cropped -- Oversized images too large for the panel will simply be cropped
			4: Stretch -- The entire image is stretched, and aspect ratio is ignored
			5: TopLeft -- Image is anchored to top left corner and cropped
		Returns:
		None

		"""
		super(EditorGLPanel, self).__init__(parent, id)
		self._rows = rows
		self._columns = columns
		self._coord = coord
		self._drawmode = drawmode
		self._image = None
		self.draw_objects()
		self._contextMenu = None
		self.canvas.Bind( wx.EVT_RIGHT_DOWN, self.canvas_RightClicked )

	def canvas_RightClicked( self, event ):
		"""Creates the context menu if necessary, then displays it"""
		if self._contextMenu is None:
			self._createContextMenu()
		self._contextMenu.Check(self._drawmode, True)
		self.canvas.PopupMenu(self._contextMenu, event.GetPosition())

	def menuItem_SelectionChanged( self, event ):
		"""Updates the draw mode"""
		self.SetDrawMode(event.GetId())

	def _createContextMenu( self ):
		"""Creates the context menu on demand"""
		self._contextMenu = wx.Menu()
		self.menuItemCropAndShrink = wx.MenuItem( self._contextMenu, 0, u"Crop and Shrink", u"Oversized images will be scaled and cropped evenly", wx.ITEM_RADIO  )
		self._contextMenu.AppendItem( self.menuItemCropAndShrink )
		self.menuItemCropAndShrink.Check( True )
		self.menuItemShrink = wx.MenuItem( self._contextMenu, 1, u"Shrink", u"Oversized images will scale to the windows size while maintaining aspect ratio", wx.ITEM_RADIO  )
		self._contextMenu.AppendItem( self.menuItemShrink )
		self.menuItemStretchAspect = wx.MenuItem( self._contextMenu, 2, u"Stretch Aspect", u"Images will expand to fill the window while maintaining aspect ratio", wx.ITEM_RADIO  )
		self._contextMenu.AppendItem( self.menuItemStretchAspect )
		self.menuItemCrop = wx.MenuItem( self._contextMenu, 3, u"Crop", u"Image will be cropped to the window's size", wx.ITEM_RADIO  )
		self._contextMenu.AppendItem( self.menuItemCrop )
		self.menuItemStretch = wx.MenuItem( self._contextMenu, 4, u"Stretch", u"Image will be stretched to fill the window and ignore the aspect ratio", wx.ITEM_RADIO  )
		self._contextMenu.AppendItem( self.menuItemStretch )
		self.menuItemNone = wx.MenuItem( self._contextMenu, 5, u"None", u"No resizing, cropping, or centering will be performed", wx.ITEM_RADIO  )
		self._contextMenu.AppendItem( self.menuItemNone )
		self.Bind( wx.EVT_MENU, self.menuItem_SelectionChanged, id = self.menuItemCropAndShrink.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItem_SelectionChanged, id = self.menuItemShrink.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItem_SelectionChanged, id = self.menuItemStretchAspect.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItem_SelectionChanged, id = self.menuItemCrop.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItem_SelectionChanged, id = self.menuItemStretch.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItem_SelectionChanged, id = self.menuItemNone.GetId() )

	def ChangeImage(self, pilImage):
		"""Changes the displayed image"""
		self._image = pilImage
		del (pilImage)
		self.PrepareGL()
		self.OnDraw()

	def GetDrawMode( self ):
		"""Returns the integer value that represents the current drawing mode"""
		return self._drawmode

	def SetDrawMode( self, drawmode ):
		"""Sets the drawing mode and refreshes the display"""
		self._drawmode = drawmode
		self.PrepareGL()
		self.OnDraw()

	def draw_objects( self ):
		"""Draws the objects on the canvas"""
		if not self.GLinitialized:
			return

		gl.glClearColor(0.93, 0.93, 0.93, 1)
		if self._image is None:
			return
		# Convert PIL image to pyglet image
		srcImage = pyglet.image.create(*self._image.size).get_image_data()
		pitch = -len('RGBA') * srcImage.width
		data = self._image.tostring()
		srcImage.set_data('RGBA', pitch, data)
		# Clear the canvas and calculate the region to draw
		tile_width = srcImage.width / self._rows
		tile_height = srcImage.height / self._columns
		x = self._coord[0] * tile_width
		y = self._coord[1] * tile_height
		y = srcImage.height - y - tile_height
		subimage = srcImage.get_region(x, y, tile_width, tile_height)
		subimage.align_x = subimage.align_y = 0
		# Branch by what mode is selected to draw
		if self._drawmode == 0: self.CropAndShrink(subimage)
		elif self._drawmode == 1: self.Shrink(subimage)
		elif self._drawmode == 2: self.StretchAspect(subimage)
		elif self._drawmode == 3: self.Cropped(subimage)
		elif self._drawmode == 4: self.Stretch(subimage)
		else: self.TopLeft(subimage)
		del (srcImage)

	#---------------------------------------------------------------
	# Draw Modes
	#---------------------------------------------------------------
	def CropAndShrink( self, pygletimage ):
		"""Images will be both scaled down and cropped to fit"""
		width, height = self.GetClientSize()
		w, h = pygletimage.width, pygletimage.height
		x, y, = (width - w) / 2, (height - h) / 2
		if width < w or height < h: 
			diff_w = (w - width) / 2
			diff_h = (h - height) / 2
			pygletimage.blit(x / 2, y / 2, 0, w - diff_w, h - diff_h)
		else:
			pygletimage.blit(x, y, 0, w, h)
		del (pygletimage)

	def Shrink( self, pygletimage ):
		"""Scales image down if too large, else the image is simply centered"""
		width, height = self.GetClientSize()
		w, h = pygletimage.width, pygletimage.height
		x, y, = (width - w) / 2, (height - h) / 2
		if width < w or height < h: 
			self.StretchAspect( pygletimage )
		else:
			pygletimage.blit(x, y, 0, w, h)
		del (pygletimage)

	def StretchAspect( self, pygletimage ):
		"""The image will be stretched to fill panel while maintaining aspect ratio"""
		width, height = self.GetClientSize()
		w, h = pygletimage.width, pygletimage.height
		x_ratio = float(width) / w
		y_ratio = float(height) / h
		if y_ratio > x_ratio:
			ch = h * x_ratio
			pygletimage.blit(0, (height - ch) / 2, 0, width, ch)
		else:
			cw = w * y_ratio
			pygletimage.blit((width - cw) / 2, 0, 0, cw, height)
		del (pygletimage)

	def Cropped( self, pygletimage ):
		"""Oversized images too large for the panel will simply be cropped"""
		width, height = self.GetClientSize()
		w, h = pygletimage.width, pygletimage.height
		x, y = (width - w) / 2, (height - h) / 2
		if w > width: x = (width - w) / 2
		if h > height: y = (height - h) / 2
		pygletimage.blit(x, y, 0, w, h)
		del (pygletimage)

	def Stretch( self, pygletimage ):
		"""The entire image is stretched, and aspect ratio is ignored"""
		width, height = self.GetClientSize()
		pygletimage.blit(0, 0, 0, width, height)

	def TopLeft( self, pygletimage ):
		"""Image is anchored to top left corner and cropped"""
		y = self.GetClientSize()[1] - pygletimage.height
		pygletimage.blit(0, y, 0, pygletimage.width, pygletimage.height)
		del (pygletimage)