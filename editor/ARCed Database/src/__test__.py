import wx
import numpy as np
from scipy.interpolate import interp1d

import Kernel
from Kernel import Manager as KM

class ParameterGraph ( wx.Panel ):

	def __init__( self, parent, data=[], maxvalue=9999, pointmax=24, 
				 interactive=True, curvecolor='g', linearcolor='r'):
		''' Basic constructor for the Graph panel '''
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, 
					 size = wx.Size( 566,428 ), style = wx.GROW|wx.EXPAND )
		from matplotlib.pyplot import Figure
		from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
		# Set instance variables
		self.Data = data
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
		self.Ax.grid(None) #!
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
		print len(self.PointXData), len(self.PointYData)
		
		print self.Data
		f = interp1d(self.PointXData, self.PointYData)
		f2 = interp1d(self.PointXData, self.PointYData, kind='cubic')
		xdata = np.linspace(1, len(self.Data) - 1, len(self.Data) - 1)
		ydata = f2(xdata)
		self.Lines = self.Ax.plot(self.PointXData, self.PointYData, 'o', xdata, f(xdata), 
			self.LinearColor, xdata, ydata, self.CurveColor)
		#self.Ax.fill_between(xdata, ydata, color=self.CurveColor, alpha=0.5)
		# Set the data for the parameter to match the curve values
		#for i in xrange(len(self.Data)):
		#	self.Data[int(xdata[i])] = int(ydata[i])

	def SetPointMax( self, max ):
		''' Ensures the maximum number of points is valid, then sets it '''
		pts = max
		while pts >= len(self.Data): pts -= 1
		self.PointMax = pts
		self.SampleSize = (len(self.Data) - 1) / self.PointMax

	def OnDraw( self, event ):
		self.Background = self.Canvas.copy_from_bbox(self.Ax.bbox)
		self.Ax.draw_artist(self.Lines[0])
		self.Ax.draw_artist(self.Lines[1])
		self.Ax.draw_artist(self.Lines[2])
		self.Canvas.blit(self.Ax.bbox)

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

	def OnMouseMotion( self, event ):
		if event.inaxes == None: return
		self.MouseX, self.MouseY = int(event.xdata), int(event.ydata)
		if not self.ShowVerts or self.ActivePoint == None or event.button != 1: return
		
		
		self.Data[int(event.xdata) - 1] = event.ydata
		self.PointYData = self.Data[1::self.SampleSize]
		# Interpolate the point coordinates and create a curves between them
		f = interp1d(self.PointXData, self.PointYData)
		f2 = interp1d(self.PointXData, self.PointYData, kind='cubic')
		xdata = np.linspace(1, len(self.Data) - 1, len(self.Data) - 1)
		ydata = f2(xdata)

		self.Lines[0].set_ydata(self.PointYData)
		self.Lines[1].set_ydata(f(xdata))
		self.Lines[2].set_ydata(ydata)



		#self.Lines[1]

		#self.PlotData()
		#self.Canvas.restore_region(self.Background)
		#self.ax.draw_artist(self.pathpatch)
		#self.Ax.draw_artist(self.Lines[0])
		#self.Ax.draw_artist(self.Lines[1])
		#self.Ax.draw_artist(self.Lines[2])
		#self.Canvas.blit(self.Ax.bbox)
		self.Canvas.draw()


	def GetSelectedPoint( self, event ):
		pt = None
		for x in self.Lines[0].get_xdata():
			if np.abs(x - event.xdata) <= self.Epsilon:
				pt = x
				self.XLock = event.xdata
				break
		return pt
		












data = [0,769,769,769,769,814,814,814,859,859,904,904,950,950,995,1040,1131,1221,1266,1266,1266,1266,1266,1266,1266,1312,1357,1402,1447,1493,1538,1583,1628,1674,1674,1764,1945,1945,1990,1990,1990,1990,1990,2036,2036,2081,2171,2217,2262,2262,2307,2307,2352,2443,2443,2443,2443,2443,2488,2533,2533,2624,2669,2714,2760,2850,2895,3031,3167,3257,3484,3574,3891,4027,4208,4524,4751,4932,5203,5475,5746,6018,6334,6606,6877,7194,7511,7963,8325,8642,9049,9366,9638,9864,9999,9999,9999,9999,9999,9999]
data = [0,950,1131,1357,1900,2217,2533,2714,2714,2714,2714,2624,2398,1628,1402,1312,1221,1221,1266,1583,1809,2081,2579,3212,3891,4751,4977,5067,5158,5203,5203,5203,5022,4796,4479,3800,3438,3122,2895,2714,2488,2307,2126,2036,2036,2081,2262,2850,3800,4524,4886,4932,4932,4932,4932,4886,4615,4298,3710,3438,3257,3076,2941,2850,2805,2760,2760,2760,2805,3076,3393,3800,4343,4932,5520,6515,7013,7330,7647,7873,7873,7782,7692,7601,7420,7285,7194,7058,7013,7013,7104,7375,7601,8009,8371,8778,9095,9502,9819,9954]
app = wx.PySimpleApp( 0 )
frame = wx.Frame( None, wx.ID_ANY, 'Parameter Graph', size=(640,480) )
panel = ParameterGraph( frame, data )
frame.Show()
app.MainLoop()

"""
class ParameterGraph ( wx.Panel ):

	def __init__( self, parent, data=None, range=[1,9999], pointmax=10, 
				 interactive=True, color='#44FF44'):
		''' Basic constructor for the Graph panel '''
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, 
					 size = wx.Size( 566,428 ), style = wx.GROW|wx.EXPAND )
		# Set attributes
		global Path, Ax
		Path = mpath.Path
		self.PointMax = pointmax
		self.RawData = data
		self.ShowVerts = True
		self.ElasticPower = 0
		self.Figure = plt.figure()
		self.Canvas = FigureCanvasWxAgg( self, -1, self.Figure )
		self.Figure.set_canvas(self.Canvas)
		self.XLock = 0
		self.ActivePoint = None
		self.MouseX, self.MouseY = 0, 0
		Ax = self.Figure.add_subplot(111)
		# Generate the layout of the graph
		pathdata = []
		levels = len(self.RawData)   
		self.Step = int(levels / float(self.PointMax))
		self.StretchLength = range[1] / self.Step


		for i in xrange(self.Step, levels - 1, self.Step):
			th = interp1d([i], self.RawData[i])
			pathdata.append((Path.CURVE3, (i, self.RawData[i], th)))
		pathdata.append((Path.CURVE3, (levels - 1, self.RawData[levels - 1])))
		pathdata.insert(0, (Path.MOVETO, (1, self.RawData[1])))
		pathdata.append((Path.LINETO, (levels - 1, 0)))
		pathdata.append((Path.LINETO, (1, range[0])))
		pathdata.append((Path.CLOSEPOLY, (1, self.RawData[1])))

		self.Epsilon = int(self.Step / 2.5)
		Ax.set_xlim(1, levels - 1)
		Ax.set_ylim(range[0], range[1])
		codes, verts = zip(*pathdata)
		print 'Codes', codes, 'Verts', verts
		path = mpath.Path(verts, codes)
		patch = mpatches.PathPatch(path, facecolor=color, alpha=1.0)
		Ax.add_patch(patch)
		self.ax = patch.axes
		self.pathpatch = patch
		self.pathpatch.set_animated(True)
		x, y = zip(*self.pathpatch.get_path().vertices)
		self.Line, = self.ax.plot(x, y, marker='o', markerfacecolor='r', animated=True)
		# Bind Events
		self.Canvas.mpl_connect('draw_event', self.OnDraw)
		if interactive:
			self.Canvas.mpl_connect('button_press_event', self.OnMouseDown)
			self.Canvas.mpl_connect('key_press_event', self.OnKeyPress)
			self.Canvas.mpl_connect('button_release_event', self.OnMouseUp)
			self.Canvas.mpl_connect('motion_notify_event', self.OnMouseMove)
		# Create layout
		MainSizer = wx.BoxSizer( wx.VERTICAL | wx.EXPAND |wx.GROW)
		MainSizer.Add( self.Canvas, 1, wx.EXPAND |wx.GROW, 5 )
		self.SetSizer( MainSizer )
		self.Layout()

	def OnDraw(self, event):
		''' Raised when the canvas is re-drawn '''
		self.background = self.Canvas.copy_from_bbox(self.ax.bbox)
		self.ax.draw_artist(self.pathpatch)
		self.ax.draw_artist(self.Line)
		self.Canvas.blit(self.ax.bbox)

	def GetSelectedPoint(self, event):
		''' Gets the index of the vertex within the Epsilon tolerance on the X-axis '''
		index = None
		xdata = self.Line.get_xdata()
		for i, x in enumerate(xdata):
			if np.abs(x - event.xdata) <= self.Epsilon:
				index = i
				self.XLock = x
				break
		return index

	def OnMouseDown(self, event):
		''' Called when a the left mouse button is pressed. Looks for a point to select '''
		if not self.ShowVerts: return
		if event.inaxes==None: return
		if event.button != 1: return
		self.ActivePoint = self.GetSelectedPoint(event)

	def OnMouseUp(self, event):
		''' Called when a the left mouse button is released'''
		if not self.ShowVerts: return
		if event.button != 1: return
		self.ActivePoint = None

	def OnMouseMove(self, event):
		''' Raised when mouse is moved over the graph '''
		if event.inaxes is None: 
			return
		if self.ActivePoint == None:
			self.MouseX = int(event.xdata)
			self.MouseY = int(event.ydata)
			return
		if not self.ShowVerts or event.button != 1:
			return
		x,y = self.XLock, event.ydata
		vertices = self.pathpatch.get_path().vertices
		vertices[self.ActivePoint] = x,y
		ydata = self.Line.get_ydata() 
		'''
		for i in xrange(len(ydata) - 3):
			if i < self.ActivePoint and y < ydata[i]:
				vertices[i][1] = y
			elif i > self.ActivePoint and ydata[i] < y:
				vertices[i][1] = y
			if self.ElasticPower > 0:
		'''
# TODO: IMPLEMENT

				
		self.MouseX = int(self.XLock)
		self.MouseY = int(y)
		self.Line.set_data(zip(*vertices))
		self.Canvas.restore_region(self.background)
		self.ax.draw_artist(self.pathpatch)
		self.ax.draw_artist(self.Line)
		self.Canvas.blit(self.ax.bbox)

	def OnKeyPress(self, event):
		''' Raised when a key is pressed '''
		if not event.inaxes: return
		if event.key=='s':
			pass

			"""