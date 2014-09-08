import wx
from wx.lib.scrolledpanel import ScrolledPanel

class ParameterPanel(ScrolledPanel):

    def __init__(self, parent ):
        ScrolledPanel.__init__(self, parent, -1)
        sizer = wx.BoxSizer( wx.VERTICAL )
        self.SetupScrolling( False, True, 10, 10)
        self.SetSizer( sizer )
        self.Bind(wx.EVT_SIZE, self.LayoutVirtualSize)
        self.SetDoubleBuffered(True)

    def LayoutVirtualSize( self, event ):
        self.SetVirtualSizeHints(-1, -1, self.GetClientSize().GetWidth() - 32)