import wx
import numpy as np
from scipy.interpolate import interp1d

import Kernel
from Kernel import Manager as KM

class ParameterGraph ( wx.Panel ):

	def __init__( self, parent, data=[], maxvalue=9999, pointmax=24, 
				 interactive=True, curvecolor='g', linearcolor='r', display = 2):
		"""Basic constructor for the Graph panel"""
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, 
					 size = wx.Size( 566,428 ), style = wx.GROW|wx.EXPAND)
		from matplotlib.pyplot import Figure
		from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
		# Set instance variables
		self.Data = data
		self.DisplayLine = display
		self.SetPointMax(pointmax)
		self.MaxValue = maxvalue
		self.Interactive = interactive
		self.ActivePoint = None
		self.ShowVerts = True
		self.MouseX = self.MouseY = 0
		self.Figure = Figure(None)#plt.figure()
		self.Canvas = FigureCanvasWxAgg(self, -1, self.Figure)
		self.CurveColor = curvecolor
		self.LinearColor = linearcolor

	
		self.Ax = self.Figure.add_subplot(111, animated=True)
		#self.Ax.grid(None) #!
		self.XLock = 0
		self.Epsilon = 5 #!
		# Define bounds of the graph, then plot it out
		self.Ax.axis([1, len(self.Data) - 1, 1, self.MaxValue])
		self.PlotData()

		if self.Interactive:
			self.Canvas.mpl_connect('draw_event', self.OnDraw)
			self.Canvas.mpl_connect('button_press_event', self.OnMouseDown)
			self.Canvas.mpl_connect('key_press_event', self.OnKeyPress)
			self.Canvas.mpl_connect('button_release_event', self.OnMouseUp)
			self.Canvas.mpl_connect('motion_notify_event', self.OnMouseMotion)

	def PlotData(self):

		# Create arrays of coordinates for the vertices, which will define the rough shape
		self.PointYData = self.Data[1::self.SampleSize]
		self.PointXData = np.linspace(1, len(self.Data) - 1, len(self.PointYData))
		# Interpolate the point coordinates and create a curves between them
		f = interp1d(self.PointXData, self.PointYData)
		f2 = interp1d(self.PointXData, self.PointYData, kind='cubic')

		self.xdata = np.linspace(1, len(self.Data) - 1, len(self.Data) - 1)
		ydata = f2(self.xdata)

		self.Lines = self.Ax.plot(self.PointXData, self.PointYData, 'o', 
			self.PointXData, self.PointYData, self.LinearColor,
			self.xdata, ydata, self.CurveColor)

		if self.DisplayLine == 1:
			self.Lines[2].set_visible(False)
		else:
			self.Lines[1].set_visible(False)
		self.Canvas.blit()
		#self.Ax.fill_between(self.xdata, ydata, color=self.CurveColor, alpha=0.5)
		

		# Set the data for the parameter to match the curve values
		#for i in xrange(len(self.Data)):
		#	self.Data[int(xdata[i])] = int(ydata[i])

	def SetPointMax( self, max ):
		"""Ensures the maximum number of points is valid, then sets it"""
		pts = max
		while pts >= len(self.Data): pts -= 1
		self.PointMax = pts
		self.SampleSize = (len(self.Data) - 1) / self.PointMax

	def OnDraw( self, event, setbg=True):
		if setbg:
			self.Background = self.Canvas.copy_from_bbox(self.Ax.bbox)
		else:
			self.Canvas.restore_region(self.Background)
		self.Ax.draw_artist(self.Lines[0])
		self.Ax.draw_artist(self.Lines[2])
		self.Canvas.blit(self.Ax.bbox)
		self.Ax.fill_between(self.PointXData, self.PointYData, color=self.LinearColor, alpha=0.5)

	def GetParameters(self):
		pass

	def OnMouseDown( self, event ):
		if event.inaxes == None or not self.ShowVerts or event.button != 1: return
		self.ActivePoint = self.GetSelectedPoint(event)

	def OnKeyPress( self, event ):
		pass

	def OnMouseUp( self, event ):
		self.ActivePoint = None
		pass

	def OnMouseMotion( self, event=None, refresh=False ):
		if not refresh:
			if event.inaxes == None: return
			if self.ActivePoint == None:
				self.MouseX, self.MouseY = int(event.xdata), int(event.ydata)
				return
			if not self.ShowVerts or event.button != 1: return
			self.PointYData[self.ActivePoint] = event.ydata


		if self.ShowVerts: 
			self.Lines[0].set_ydata(self.PointYData)
		if self.DisplayLine == 1: 
			self.Lines[1].set_ydata(self.PointYData)
			#self.Ax.fill_between(self.PointXData, self.PointYData, color=self.LinearColor, alpha=0.5)
		else: 
			f = interp1d(self.PointXData, self.PointYData, kind='cubic')
			intp = f(self.xdata)
			#self.Ax.fill_between(self.xdata, intp, color=self.CurveColor, alpha=0.5)
			self.Lines[2].set_ydata(intp)
		self.OnDraw(event, False)


	def GetSelectedPoint( self, event ):
		point = None
		data = self.Lines[0].get_xdata()
		for i in xrange(len(data)):
			x = data[i]
			if np.abs(x - event.xdata) <= self.Epsilon:
				point = i
				self.XLock = event.xdata
				break
		return point + 1
