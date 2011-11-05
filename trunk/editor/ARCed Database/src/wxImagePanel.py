import wx
import Kernel

class ImagePanel(wx.Panel):

	def __init__( self, parent, rows, columns ):
		''' Basic constructor for the image panel '''
		wx.Panel.__init__(self, parent=parent, style=wx.SUNKEN_BORDER|wx.CLIP_CHILDREN|wx.GROW|wx.EXPAND)  
		self.frame = parent
		self.ApplySettings()
		self._rows = rows
		self._columns = columns
		self._imagepath = ''
		self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
		self.Bind
		sizer = wx.BoxSizer( wx.VERTICAL )
		self.SetSizer(sizer)
		sizer.Layout()

	def SetImagepath(self, path):
		self._imagepath = path
		self.Refresh()
		
	def ApplySettings( self, coord=(0, 0), rows=4, columns=4, minsize=(32, 32), 
			maxsize=None, bgbrush=wx.LIGHT_GREY_BRUSH): 
		self._coordinates = coord
		self._rows = rows
		self._columns = columns
		self._minsize = minsize
		self._maxsize = maxsize
		self._bgbrush = bgbrush
		self.Refresh()

	def OnEraseBackground( self, event ):
		print 'hello'
		''' Add a picture to the background '''
		if self._imagepath == '':
			return
		try:
			srcBmp = wx.Bitmap(self._imagepath)
			srcDC = wx.MemoryDC(srcBmp)
			dc = event.GetDC()
			if not dc:
				dc = wx.ClientDC(self)
				rect = self.GetUpdateRegion().GetBox()
				dc.SetClippingRect(rect)
			dc.SetBackground(self._bgbrush)
			dc.Clear()
			width = srcBmp.GetWidth()
			height = srcBmp.GetHeight()

			cw = width / self._columns
			ch = height / self._rows

			bx = by = sx = sy = 0
			
			size = self.GetSize()
			

			if self._minsize != None:
				if size.GetWidth() < self._minsize[0]: 
					bx = (self._minsize[0] - cw) / 2
					size.SetWidth(self._minsize[0])
				if size.GetHeight() < self._minsize[1]: 
					by = (self._minsize[1] - ch) / 2
					size.SetHeight(self._minsize[1])

			if self._maxsize != None:
				if size.GetWidth() > self._maxsize[0]: 
					sx = (cw - self._maxsize[0]) / 2
					size.SetWidth(self._maxsize[0])
				if size.GetHeight() > self._maxsize[1]: 
					sy = (ch - self._maxsize[1]) / 2
					size.SetHeight(self._maxsize[1])

			bx = (size.GetWidth() - cw) / 2
			by = (size.GetHeight() - ch) / 2
			dc.Blit(bx, by, cw, ch, srcDC, sx, sy, wx.COPY, True)
			self.GetSizer().SetMinSize(size)
			del (srcDC)
			del (srcBmp)
		except wx.PyAssertionError:
			Kernel.Log('Failed to load Graphic resource', '[Database:ACTOR]', True)