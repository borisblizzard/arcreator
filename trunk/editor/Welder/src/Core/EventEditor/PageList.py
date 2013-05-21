
from Boot import WelderImport

Kernel = WelderImport('Kernel')
KM = Kernel.Manager

import wx

class EventListCtrl(wx.HtmlListBox):

    def __init__(self, parent, list):
        wx.HtmlListBox.__init__(parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize)
        self.list = list

