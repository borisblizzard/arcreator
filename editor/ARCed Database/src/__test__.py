import wx
import wx.lib.plot as plot
import numpy as np
import pygame
import os

# Set dummy video driver to prevent malfunction on certain platforms
os.environ['SDL_VIDEODRIVER'] = 'dummy'

#--------------------------------------------------------------------------------------
# WaveFormPanel
#--------------------------------------------------------------------------------------

class WaveFormPanel(plot.PlotCanvas):

	def __init__(self, parent, sound_array=None, color=wx.BLUE):
		super(WaveFormPanel, self).__init__(parent, style=wx.SUNKEN_BORDER)
		self.SetEnableTitle(False)
		self.SetEnableLegend(False)
		self.SetEnablePointLabel(False)
		self.SetXSpec('none')
		self.SetYSpec('none')
		self.SetFontSizeAxis(1)
		self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
		self.DrawColor = color
		self.SetEnableAntiAliasing(True)
		self.SetEnableHiRes(True)
		if sound_array is not None:
			self.SetSoundArray(sound_array)
		
	def SetSoundArray(self, data):
		# Draw a static straight line if no sound is defined
		if data is None:
			return
		line = plot.PolyLine(data, colour=self.DrawColor, width=1)
		gc = plot.PlotGraphics([line])
		self.Draw(gc)


pygame.mixer.init()
sound = pygame.mixer.Sound("myaudiofile.ogg")

x = np.array([1, 45, 100])
y = np.array([1, 45, 100])

y = np.polyfit(x, y, 3)
data = np.column_stack((x, y))

app = wx.PySimpleApp( 0 )
frame = wx.Frame( None, wx.ID_ANY, 'WaveForm', size=(500, 200))
panel = WaveFormPanel(frame, data)

sizer = wx.BoxSizer( wx.HORIZONTAL )
sizer.Add( panel, 1, wx.ALL|wx.GROW, 5 )
frame.SetSizer(sizer)
frame.Layout()
frame.CenterOnScreen()
frame.Show()
app.MainLoop()
