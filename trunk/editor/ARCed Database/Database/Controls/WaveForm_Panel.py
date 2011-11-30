import wx
import wx.lib.plot as plot
import numpy as np
 
class WaveFormPanel(plot.PlotCanvas):

	def __init__(self, parent, sound_array=None, color=wx.BLUE):
		super(WaveFormPanel, self).__init__(parent, style=wx.SUNKEN_BORDER)
		self.SetEnableTitle(False)
		self.SetEnableLegend(False)
		self.SetEnablePointLabel(False)
		self.SetXSpec('none')
		self.SetYSpec('none')
		self.DrawColor = color
		if sound_array is not None:
			self.SetSoundArray(sound_array)
		
	def SetSoundArray(self, sndarray):
		self.Clear()
		line = plot.PolyLine(sndarray, colour=self.DrawColor, width=1)
		gc = plot.PlotGraphics([line])
		self.Draw(gc)
'''
import wx
import matplotlib
matplotlib.interactive(False)
matplotlib.use('WXAgg')

class WaveFormPanel( wx.Panel ):

	def __init__(self, parent, sound_array=None, color=(.0, .25, .5)):
		super(WaveFormPanel, self).__init__(parent)
		"""Basic constructor for the WaveForm_Panel"""
		from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
		self.figure = matplotlib.figure.Figure()
		self.canvas = FigureCanvasWxAgg(self, -1, self.figure)
		self.subplot = self.figure.add_subplot(111)
		self.color = color
		self.SetSoundArray(sound_array)
		self.Bind(wx.EVT_SIZE, self.SizeHandler)

	def SizeHandler(self, *args, **kwargs):
		"""Updates the graph size with the parent panel"""
		self.canvas.SetSize(self.GetSize())

	def SetSoundArray( self, array, index=None ):
		"""Updates the data for the graph and redraws"""
		self.sndarray = array
		self.figure.delaxes(self.subplot)
		self.subplot = self.figure.add_subplot(111)
		self.Draw()

	def Draw( self ):
		"""Draws the graph"""
		nullLocator = matplotlib.ticker.NullLocator()
		self.subplot.xaxis.set_major_locator( nullLocator )
		self.subplot.yaxis.set_major_locator( nullLocator )
		self.subplot.xaxis.set_minor_locator( nullLocator )
		self.subplot.yaxis.set_minor_locator( nullLocator )
		self.figure.subplots_adjust(left=0., right=1.0, top=1.0, bottom=0.)
		if self.sndarray is None:
			x, y = [0, 1], [0, 0]
			print x, y
		else:
			y = zip(*self.sndarray)[1]
			x = [i for i in xrange(len(y))]
		print min(x), max(x)
		print min(y), max(y)
		self.subplot.plot(x, y, color=self.color, linewidth=1)
		self.canvas.draw()

import pygame
pygame.mixer.init()
sound = pygame.mixer.Sound("C:/Users/Eric/Desktop/111-Heal07.wav")
array = pygame.sndarray.array(sound)
app = wx.PySimpleApp( 0 )
frame = wx.Frame( None, wx.ID_ANY, 'TEST', size=(500, 200))
panel = WaveFormPanel(frame)
sizer = wx.BoxSizer( wx.HORIZONTAL )
sizer.Add( panel, 1, wx.ALL|wx.GROW, 5 )
frame.SetSizer(sizer)
frame.Layout()
frame.CenterOnScreen()
frame.Show()
app.MainLoop()
'''