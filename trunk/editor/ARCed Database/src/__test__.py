import wx
import wx.aui
import matplotlib as mpl
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as Canvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2Wx as Toolbar

class Plot(wx.Panel):
    def __init__(self, parent, id = wx.ID_ANY, dpi = None, **kwargs):
        wx.Panel.__init__(self, parent, id=id, **kwargs)
        self.figure = mpl.figure.Figure(dpi=dpi, figsize=(2,2))
        self.canvas = Canvas(self, -1, self.figure)
        sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
        self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        sizerOKCancel.Add( self.buttonOK, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
        self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        sizerOKCancel.Add( self.buttonCancel, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas,1,wx.EXPAND)
        sizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
        self.SetSizer(sizer)

class PlotNotebook(wx.Panel):
    def __init__(self, parent, id = -1):
        wx.Panel.__init__(self, parent, id=id)
        self.nb = wx.aui.AuiNotebook(self)
        sizer = wx.BoxSizer()
        sizer.Add(self.nb, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def add(self, name="plot"):
       page = Plot(self.nb)
       self.nb.AddPage(page,name)
       return page.figure


def demo():
    app = wx.PySimpleApp()
    frame = wx.Frame(None,-1,'Curve')
    plotter = PlotNotebook(frame)
    axes1 = plotter.add('figure 1').gca()
    axes1.plot([1,2,3],[2,1,4])
    axes2 = plotter.add('figure 2').gca()
    axes2.plot([1,2,3,4,5],[2,1,4,2,3])
    #axes1.figure.canvas.draw()
    #axes2.figure.canvas.draw()
    frame.Show()
    app.MainLoop()

if __name__ == "__main__": demo()