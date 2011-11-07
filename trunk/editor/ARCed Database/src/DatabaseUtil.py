import wx
from Core.Cache import PILCache as Cache
import os
import Kernel

class DatabaseUtil(object):

	ARC_FORMAT = False
	
	TEXT_COLOR = wx.Color(241, 243, 248)
	GRADIENT_LEFT = wx.Color(100, 100, 100)
	GRADIENT_RIGHT = wx.Color(60, 60, 60)

	_ALPHA_BRUSH = None

	# TODO: Remove this. Use RTP path from Kernel via the Cache
	GraphicsDir = os.path.abspath(os.environ['COMMONPROGRAMFILES'] + '\Enterbrain\RGSS\Standard\Graphics')

	@staticmethod
	def DrawBitmap( staticBitmap, filename, hue=0, type='battler', rows=1, columns=1, tile=(0,0)):
		''' Draws the character graphic to the static bitmap using a blit '''
		if DatabaseUtil._ALPHA_BRUSH is None:
			DatabaseUtil._ALPHA_BRUSH = wx.Brush(wx.Color(228, 228, 228), wx.SOLID)

		if type == 'character':
			# TODO: Load data from cache
			srcBmp = wx.Bitmap(DatabaseUtil.GraphicsDir + '\\Characters\\' + filename + '.png')
			#srcBmp = Cache.Character(filename, hue)
		elif type == 'battler':
			# TODO: Load data from cache
			srcBmp = wx.Bitmap(DatabaseUtil.GraphicsDir + '\\Battlers\\' + filename + '.png')
			#srcBmp = Cache.Battler(filename, hue)

		tile_width = srcBmp.GetWidth() / columns
		tile_height = srcBmp.GetHeight() / rows
		srcDC = wx.MemoryDC()
		srcDC.Clear()
		srcDC.SelectObjectAsSource(srcBmp)
		cSize = [48, 64]
		if tile_width > cSize[0]: cSize[0] = tile_width + 8
		if tile_height > cSize[1]: cSize[1] = tile_height + 8
		destBmp = wx.EmptyBitmap(cSize[0], cSize[1])
		destDC = wx.MemoryDC()
		destDC.SelectObject(destBmp)
		destDC.SetBackground(DatabaseUtil._ALPHA_BRUSH)
		destDC.Clear()
		x = tile_width * tile[0]
		y = tile_height * tile[1]
		destX = (cSize[0] - tile_width) / 2
		destY = (cSize[1] - tile_height) / 2
		destDC.Blit(destX, destY, tile_width, tile_height, srcDC, x, y, wx.COPY, True)
		destDC.SelectObject(wx.NullBitmap)
		staticBitmap.SetSize(destBmp.GetSize())
		staticBitmap.SetBitmap(destBmp)
		del (destDC)
		del (srcDC)
		del (destBmp)



	@staticmethod
	def DrawHeaderBitmap( staticBitmap, text, font=None, textcolor=None, 
			gradient1=None, gradient2=None ):
		''' Draws text on a static bitmap control and applies a gradient color fill '''
		memDC = wx.MemoryDC()
		bmpsize = staticBitmap.GetClientSize()
		bmp = wx.EmptyBitmap(bmpsize[0], bmpsize[1])
		memDC.SelectObject(bmp)
		memDC.Clear()	
		if textcolor == None: textcolor = DatabaseUtil.TEXT_COLOR
		if gradient1 == None: gradient1 = DatabaseUtil.GRADIENT_LEFT
		if gradient2 == None: gradient2 = DatabaseUtil.GRADIENT_RIGHT
		if font == None: font = wx.Font(10, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, 
					wx.FONTWEIGHT_NORMAL, faceName='Ethnocentric') # TODO: Change this?
		memDC.SetFont(font)	
		memDC.SetTextForeground(textcolor)
		textsize = memDC.GetTextExtent(text)
		x = (bmpsize[0] - textsize[0]) / 2
		y = (bmpsize[1] - textsize[1]) / 2
		rect = wx.Rect(0, 0, bmpsize[0], bmpsize[1])
		memDC.GradientFillLinear(rect, gradient1, gradient2)
		memDC.DrawText(text, x, y)
		staticBitmap.SetBitmap(bmp)
		del (memDC)
		del (bmp)

	@staticmethod
	def FixedIndex( index ):
		''' Returns the correct starting index for game data structure depending on the current format '''
		if DatabaseUtil.ARC_FORMAT: return index
		else: return index + 1