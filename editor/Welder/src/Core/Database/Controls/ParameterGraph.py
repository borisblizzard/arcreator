import wx
import wx.lib.plot as plot
from ParameterPlotGraphics import ParameterPlotGraphics	

from Boot import WelderImport
				
Kernel = WelderImport('Kernel')

#--------------------------------------------------------------------------------------
# ParameterGraph
#--------------------------------------------------------------------------------------

class ParameterGraph(plot.PlotCanvas):

	def __init__(self, parent, data=None, color='orange'):
		"""Basic constructor for the ParameterGraph"""
		super(ParameterGraph, self).__init__(parent, style=wx.SUNKEN_BORDER)
		self.SetEnableTitle(False)
		self.SetEnableLegend(False)
		self.SetEnablePointLabel(False)
		self.SetFontSizeAxis(6)
		self.SetXSpec('min')
		self.SetYSpec('min')
		self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
		self.SetEnableAntiAliasing(True)
		self.DrawColor = color
		self.canvas.Bind(wx.EVT_ERASE_BACKGROUND, self.DoNothing)
		if data is not None:
			self.SetData(data)

	def DoNothing( self, event ):
		"""Prevent flickering on Windows"""
		pass

	def SetData(self, data=None, statName='', color=None, maxvalue=None, 
			maxlevel=None, minlevel=1):
		"""Sets the data to plot and draws the graph"""
		if data is None:
			data = [(0, 0), (1, 0)]
		if color is not None:
			self.DrawColor = color
		line = plot.PolyLine(data, colour=self.DrawColor, width=3)
		xLim = yLim = None
		if maxvalue is not None:
			yLim = [0, maxvalue]
		if maxlevel is not None:
			xLim = [minlevel, maxlevel]
		gc = ParameterPlotGraphics([line], xLabel='Level', yLabel=statName,
			XLimit=xLim, YLimit=yLim)
		self.Draw(gc)