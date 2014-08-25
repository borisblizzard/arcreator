import wx
import wx.lib.plot as plot
import numpy as np
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
		self.DrawColor = color
		if sound_array is not None:
			self.SetSoundArray(sound_array)
		
	def SetSoundArray(self, sndarray):
		self.Clear()
		line = plot.PolyLine(sndarray, colour=self.DrawColor, width=1)
		gc = plot.PlotGraphics([line])
		self.Draw(gc)