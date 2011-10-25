import wx
import matplotlib
import numpy as np
import matplotlib.path as mpath
import matplotlib.patches as mpatches
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import sys

import Kernel
from Kernel import Manager as KM

class ParameterGraph ( wx.Panel ):
	
	def __init__( self, parent, data=None, range=[1,9999], pointmax=10, 
				 interactive=True, color='#44FF44'):
		''' Basic constructor for the Graph panel '''
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 566,428 ), style = wx.GROW|wx.EXPAND )
		# Set attributes
		self.figure = Figure(None)
		self.canvas = FigureCanvasWxAgg( self, -1, self.figure )
		self.ax = self.figure.add_subplot(111)
		self.FillColor = color
		self.RawData = data
		self.Range = range
		self.PointMax = pointmax
		self.AxisLockedX = 0
		self._ind = None
		self.MouseX, self.MouseY = 0, 0
		self.Interactive = interactive
		self.ShowVerts = True
		# Create layout
		MainSizer = wx.BoxSizer( wx.VERTICAL | wx.EXPAND |wx.GROW)
		MainSizer.Add( self.canvas, 1, wx.EXPAND |wx.GROW, 5 )
		self.SetSizer( MainSizer )
		self.Layout()
		# Bind events, omitting unused ones of this panel is not interactive
		if self.Interactive:
			self.canvas.mpl_connect('button_press_event', self.graph_MouseMove)
			self.canvas.mpl_connect('key_press_event', self.key_press_callback)
			self.canvas.mpl_connect('button_release_event', self.graph_MouseUp)
			self.canvas.mpl_connect('motion_notify_event', self.graph_VertexMoved)
		self.canvas.mpl_connect('draw_event', self.OnGraphDraw)
		# Draw the plot of data has been defined
		if self.RawData != None:
			self.CreatePlot()
	   
	def CreatePlot(self):
		''' '''
		try:
			self.Path = mpath.Path
			self.calculateLayout()
			self.pathpatch = self.GetPatch(self.ParameterData)
			self.pathpatch.set_animated(True)
			x, y = zip(*self.pathpatch.get_path().vertices)
			self.line, = self.ax.plot(x,y,marker='p', markerfacecolor='r', animated=True)
			self.ax.fill_between(self.line.get_xdata(), self.line.get_ydata(), color=self.FillColor)
		except:
			print sys.exc_info()

	def SetRawData(self, data=None, range=None, pointmax=None):
		''' Changes the data then recalculates and draws the plot '''
		if data == None:
			data = self.RawData
		if range == None:
			range = self.Range
		if pointmax == None:
			pointmax = self.PointMax
		self.RawData = data
		self.Range = range
		self.PointMax = pointmax
		self.CreatePlot()

	def GetPoints(self):
		''' Returns a set of tuples where each is the x,y coordinate of a point '''
		return self.pathpatch.get_path().vertices


	def setLabels(self):
		self.ax.set_xlabel('Level')
		self.ax.set_ylabel('Parameter Value')

	def calculateLayout(self):
		''' 
		Sets the min/max of the graph, calculates the point coordinates
		and path, and sets the epsilon tolerance for clicking the points
		'''
		self.ParameterData = []
		levels = len(self.RawData)   
		print levels
		step = int(levels / float(self.PointMax))
		self.Epsilon = int(step / 2.5)
		for i in xrange(step, levels - 1, step):
			self.ParameterData.append((self.Path.CURVE4, (i, self.RawData[i])))
		self.ParameterData.append((self.Path.CURVE4, (levels - 1, self.RawData[levels - 1])))
		self.ax.set_xlim(1, levels - 1)
		self.ax.set_ylim(self.Range[0], self.Range[1])
		self.ParameterData.insert(0, (self.Path.MOVETO, (1, self.RawData[1])))
		self.setLabels()
	
	def GetPatch(self, data):
		''' Creates the patch based on the data, then returns it '''
		codes, verts = zip(*data)
		path = mpath.Path(verts, codes)
		patch = mpatches.PathPatch(path, alpha=0.0)
		return patch
		
	def OnGraphDraw(self, event):
		print 'Drawn called'
		self.background = self.canvas.copy_from_bbox(self.ax.bbox)
		self.ax.draw_artist(self.pathpatch)
		self.ax.draw_artist(self.line)
		self.canvas.blit(self.ax.bbox)

	def PathPatch_Changed(self, pathpatch):
		'this method is called whenever the pathpatchgon object is called'
		# only copy the artist props to the line (except visibility)
		print 'FIRED'
		vis = self.line.get_visible()
		Artist.update_from(self.line, pathpatch)
		self.line.set_visible(vis)  # don't use the pathpatch visibility state

	def GetVertexAtCursor(self, event):
		''' Gets the index of the vertex within the Epsilon tolerance on the X-axis '''
		xy = np.asarray(self.pathpatch.get_path().vertices)
		xyt = self.pathpatch.get_transform().transform(xy)
		xt, yt = xyt[:, 0], xyt[:, 1]
		index = None
		for i in xrange(len(xt)):
			if np.abs(xt[i] - event.xdata) <= self.Epsilon:
				index = i
				self.AxisLockedX = xt[i]
		return index

	def graph_MouseMove(self, event):
		'whenever a mouse button is pressed'
		if not self.ShowVerts: return
		if event.inaxes==None: return
		if event.button != 1: return
		self._ind = self.GetVertexAtCursor(event)

	def setVertices(self, vertices):
		''' Sets a new tuple of vertices and replots the data '''
		self.line.set_data(zip(*vertices))
		self.canvas.restore_region(self.background)
		self.ax.draw_artist(self.pathpatch)
		self.ax.draw_artist(self.line)
		self.canvas.blit(self.ax.bbox)

	def graph_MouseUp(self, event):
		'whenever a mouse button is released'
		if not self.ShowVerts: return
		if event.button != 1: return
		self.AxisLockedX = 0
		if self._ind != None:
			self.figure.set_canvas(self.canvas)
			self.ax.cla()
			self.setLabels()
			self.ax.set_xlim(1, len(self.RawData) - 1)
			self.ax.set_ylim(self.Range[0], self.Range[1])
			self.Colorize()
		self._ind = None

	def Colorize(self):
		''' Fills graph with color '''
		x = self.line.get_xdata()
		y = self.line.get_ydata()
		self.ax.fill_between(x, y, color=self.FillColor)
		self.canvas.draw()

	def key_press_callback(self, event):
		'whenever a key is pressed'
		if not event.inaxes: return
		if event.key=='t':
			self.ShowVerts = not self.ShowVerts
			self.line.set_visible(self.ShowVerts)
			if not self.ShowVerts: self._ind = None
		self.canvas.draw()

	def graph_VertexMoved(self, event):
		'''Ensures neighboring points stay with the correct value and applies the coordinate change'''
		if event.inaxes is None: return
		self.MouseX, self.MouseY = int(event.xdata), int(event.ydata)
		if not self.ShowVerts: return
		if self._ind is None: return
		if event.button != 1: return
		x = self.AxisLockedX
		self.MouseX = int(x)
		vertices = self.pathpatch.get_path().vertices
		vertices[self._ind] = x, self.MouseY
		for i in xrange(len(vertices)):
			if i < self._ind and vertices[i][1] > vertices[self._ind][1]:
				vertices[i][1] = vertices[self._ind][1]
			elif i > self._ind and vertices[i][1] < vertices[self._ind][1]:
				vertices[i][1] = vertices[self._ind][1]
		self.setVertices(vertices)
	
	def __del__( self ):
		''' No function. Should be overridden in derived class '''
		pass
'''
app = wx.PySimpleApp( 0 )
frame = wx.Frame( None, wx.ID_ANY, 'Parameter Curve', size=(640,480) )
panel = ParameterGraph_Panel( frame )
frame.CenterOnScreen()
frame.Show()
app.MainLoop()
'''