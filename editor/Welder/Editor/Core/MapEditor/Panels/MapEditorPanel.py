import wx

import numpy


import Kernel

from PyitectConsumes import PanelBase, MapEditorToolbar, TilemapPanel


class MapEditorPanel(wx.Panel, PanelBase):

    _arc_panel_info = {
        "Name": "MapEditor",
        "Caption": "Map Editor",
        "BestS": (32 * 24, 32 * 18),
        "CaptionV": True,
        "Center": None,
        "CloseB": True,
        "DestroyOC": True,
        "Floatable": True,
        "IconARCM": 'mapedit',
        "MaximizeB": True,
        "MinimizeB": True,
        "MinimizeM": ["POS_SMART", "CAPT_SMART"],
        "Movable": True,
        "NotebookD": True,
        "Resizable": True,
        "Snappable": True
    }

    def __init__(self, parent, map, tilesets):
        '''lays out a toolbar and the map window'''
        super(MapEditorPanel, self).__init__(parent)
        self.Show(False)
        # set data
        self.map = map
        self.caption = "Map Editor:"
        self.panel_name = "Map Editor:"
        self.tilesets = tilesets
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        # toolbar
        self.Create_Toolbar()
        # map
        self.mapwin = TilemapPanel(self, self.map, self.tilesets, self.toolbar)
        self.sizer.Add(self.mapwin, 1, wx.EXPAND | wx.ALL, 1)
        # set the sizer and layout the panel
        self.SetSizer(self.sizer)
        self.Layout()

        self.Bind(wx.EVT_UPDATE_UI, self.updateUI)
        self.Show()

    def Create_Toolbar(self):
        '''creates the toolbar and adds tools'''
        self.toolbar = MapEditorToolbar(self, self.map)
        self.sizer.Add(self.toolbar, 0, wx.EXPAND | wx.ALL, 0)

    def updateUI(self, event):
        pass
