import wx

import Kernel

from PyitectConsumes import PanelBase


class MapManagerPanel(wx.Panel, PanelBase):

    _arc_panel_info = {
        "Name": "MapManager",
        "Caption": "Map Manager",
        "BestS": (32 * 8, 32 * 4),
        "Left": None,
        "CloseB": True,
        "TopD": False,
        "BottomD": False,
        "RightD": True,
        "LeftD": True,
        "MinimizeM": ["POS_SMART", "CAPT_SMART", ],
        "MinimizeB": True,
        'IconARCM': 'project',
        "DestroyOC": True

    }

    def __init__(self, parent, mapEditerPanel=None):
        wx.Panel.__init__(self, parent)

        self.mapEditerPanel = mapEditerPanel

        # set up Sizer
        box = wx.BoxSizer(wx.VERTICAL)
        # set up tree
        mapTreeCtrl = Kernel.System.load("MapTreeCtrl")
        self.treectrl = mapTreeCtrl(
            self, -1, wx.Point(0, 0), wx.Size(160, 250), True)
        # add ctrls to sizer
        box.Add(self.treectrl, 1, wx.ALL | wx.EXPAND)
        # set sizer
        self.SetSizerAndFit(box)

        # bind events
        self.treectrl.Bind(wx.EVT_LEFT_DCLICK, self.TreeLeftDClick)

    def TreeLeftDClick(self, event):
        pt = event.GetPosition()
        item, flags = self.treectrl.HitTest(pt)
        if item:
            data = self.treectrl.GetItemData(item)
            if data:
                map_id, name = data
                self.dispatchMapPanel(map_id, name)
        event.Skip()

    def dispatchMapPanel(self, map_id, name):
        project = Kernel.GlobalObjects["PROJECT"]
        map_data = project.getMapData(map_id)
        tilesets = project.getData("Tilesets")
        if "PanelManager" in Kernel.GlobalObjects:
            Kernel.GlobalObjects["PanelManager"].dispatchPanel(
                "MapEditorPanel",
                "MapEditorPanel" + str(map_id),
                arguments=[map_data, tilesets],
                info={
                    "Name": "MapEditorPanel" + str(map_id),
                    "Caption": "[" + str(map_id) + "] " + name
                }
            )
