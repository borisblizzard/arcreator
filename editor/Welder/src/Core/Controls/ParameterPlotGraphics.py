import wx.lib.plot as plot
import numpy as np

#--------------------------------------------------------------------------------------
# ParameterPlotGraphics
#--------------------------------------------------------------------------------------

class ParameterPlotGraphics(plot.PlotGraphics):

	def __init__(self, *args, **kwargs):
		"""Basic constructor for the ParameterPlotGraphics"""
		self._yLim= kwargs.pop('YLimit', None)
		self._xLim = kwargs.pop('XLimit', None)
		plot.PlotGraphics.__init__(self, *args, **kwargs)

	def boundingBox(self):
		"""Calculates the bounds of the box, factoring in custom values"""
		bounds = plot.PlotGraphics.boundingBox(self)
		Min, Max = [bounds[0][0], bounds[1][0]], [bounds[0][1], bounds[1][1]]
		if self._yLim is not None:
			Min[1], Max[1] = self._yLim[0], self._yLim[1]
		if self._xLim is not None:
			Min[0], Max[0] = self._xLim[0], self._xLim[1]
		return np.array(Min), np.array(Max)