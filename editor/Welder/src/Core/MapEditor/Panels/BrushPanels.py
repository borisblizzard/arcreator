import wx

import Kernel

from PyitectConsumes import PanelBase

class TilesetPanel(wx.ScrolledWindow, PanelBase):

    _arc_panel_info_string = "Name Caption Left CloseB BestS MinimizeM Layer Row Pos MinimizeB DestroyOC"
    _arc_panel_info_data = {"Name": "Tileset", "Caption": "Tileset", "CloseB": False, "BestS": (
        32 * 8, 32 * 12), "MinimizeM": ["POS_SMART", "CAPT_SMART", ], "Layer": 1, "Row": 1, "Pos": 1, "MinimizeB": True, }

    def __init__(self, parent):
        wx.ScrolledWindow.__init__(self, parent, wx.ID_ANY)
        self.bindFocus()
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.SetScrollbars(32, 32, 8, 50)
