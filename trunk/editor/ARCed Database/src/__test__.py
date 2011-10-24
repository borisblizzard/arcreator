import wx
import wx.xrc
import wx.combo
import matplotlib
import sys
import numpy as np
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

class ParameterGraph_Panel ( wx.Panel ):
    
    ShowVerts = True
    
    def __init__( self, parent, data=None, range=[1,500], pointmax=10, interactive=True):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 566,428 ), style = wx.GROW|wx.EXPAND )
        from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
        from matplotlib.figure import Figure
        self.figure = Figure(None)
        self.canvas = FigureCanvasWxAgg( self, -1, self.figure )
        self.ax = self.figure.add_subplot(111)
        self.Path = mpath.Path
        MainSizer = wx.BoxSizer( wx.VERTICAL | wx.EXPAND |wx.GROW)
        sizerGraph = wx.BoxSizer( wx.VERTICAL | wx.EXPAND |wx.GROW )
        sizerGraph.Add( self.canvas, 1, wx.EXPAND |wx.GROW, 5 )
        MainSizer.Add( sizerGraph, 1, wx.EXPAND, 5 )

        self.Interactive = interactive

        if False:#self.Interactive:
            # Draw the controls and bind events if the panel is set to be interactive
            sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
            self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
            sizerOKCancel.Add( self.buttonOK, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
            self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
            sizerOKCancel.Add( self.buttonCancel, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
            MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
            self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
            self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )

        self.canvas.mpl_connect('button_press_event', self.graph_MouseMove)
        self.canvas.mpl_connect('key_press_event', self.key_press_callback)
        self.canvas.mpl_connect('button_release_event', self.graph_MouseUp)
        self.canvas.mpl_connect('motion_notify_event', self.graph_VertexMoved)
        self.canvas.mpl_connect('draw_event', self.draw_callback)
        self.SetSizer( MainSizer )
        self.Layout()
        
        
        self.RawData = data
        self.Range = range
        self.PointMax = pointmax
        self.ParameterData = []
        self.AxisLockedX = 0
        self._ind = None
        
        
        # TODO: REMOVE THIS --------------
        if self.RawData == None:
            print 'CREATING'
            levels = 100
            self.RawData = [ i * 2 + 30 for i in xrange(levels)]
        # --------------------------------
        
        
        
        if self.RawData != None:
            self.CreatePlot()
       
    def CreatePlot(self):
        try:
            self.calculateLayout()
            self.pathpatch = self.getPatch(self.ParameterData)
            self.pathpatch.set_animated(True)
            x, y = zip(*self.pathpatch.get_path().vertices)
            self.line, = self.ax.plot(x,y,marker='p', markerfacecolor='r', animated=True)
        except:
            print sys.exc_info()
        
    def SetRawData(self, data, range, pointmax=10):
        self.RawData = data
        self.Range = range
        self.PointMax = pointmax
        self.CreatePLot()

    def calculateLayout(self):
        levels = len(self.RawData)   
        print levels 
        step = int(levels / float(self.PointMax))
        self.Epsilon = int(step / 2.5)
        print step, self.Epsilon
        for i in xrange(0, levels - 1, step):
            self.ParameterData.append((self.Path.CURVE4, (i, self.RawData[i])))
        self.ParameterData.append((self.Path.CURVE4, (levels - 1, self.RawData[levels - 1])))
        self.ax.set_xlim(1, levels - 1)
        self.ax.set_ylim(self.Range[0], self.Range[1])
        self.ParameterData.insert(0, (self.Path.MOVETO, (1, self.RawData[1])))
    
    def getPatch(self, data):
        codes, verts = zip(*data)
        path = mpath.Path(verts, codes)
        patch = mpatches.PathPatch(path, alpha=0.0)
        return patch
        
    def draw_callback(self, event):
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        self.ax.draw_artist(self.pathpatch)
        self.ax.draw_artist(self.line)
        self.canvas.blit(self.ax.bbox)

    def pathpatch_changed(self, pathpatch):
        'this method is called whenever the pathpatchgon object is called'
        # only copy the artist props to the line (except visibility)
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

    def graph_MouseUp(self, event):
        'whenever a mouse button is released'
        if not self.ShowVerts: return
        if event.button != 1: return
        self.AxisLockedX = 0
        self._ind = None

    def key_press_callback(self, event):
        'whenever a key is pressed'
        if not event.inaxes: return
        if event.key=='t':
            self.ShowVerts = not self.ShowVerts
            self.line.set_visible(self.ShowVerts)
            if not self.ShowVerts: self._ind = None
        self.canvas.draw()

    def graph_VertexMoved(self, event):
        'on mouse movement'
        if not self.ShowVerts: return
        if self._ind is None: return
        if event.inaxes is None: return
        if event.button != 1: return
        x,y = self.AxisLockedX, event.ydata
        
        vertices = self.pathpatch.get_path().vertices

        vertices[self._ind] = x,y
        self.line.set_data(zip(*vertices))

        self.canvas.restore_region(self.background)
        self.ax.draw_artist(self.pathpatch)
        self.ax.draw_artist(self.line)
        self.canvas.blit(self.ax.bbox)
    
    def __del__( self ):
        pass
    
    def buttonOK_Clicked( self, event ):
        print "OK"
        self.Close()
    
    def buttonCancel_Clicked( self, event ):
        print "Cancel"
        self.Close()
'''
app = wx.PySimpleApp( 0 )
frame = wx.Frame( None, wx.ID_ANY, 'Parameter Curve', size=(640,480) )
panel = ParameterGraph_Panel( frame )
frame.CenterOnScreen()
frame.Show()
app.MainLoop()
'''