import wx

import Kernel

from PyitectConsumes import PanelBase


class MapTreePanel(wx.Panel, PanelBase):

    _arc_panel_info_string = "Name Caption Left CloseB BestS MinimizeM Layer Row Pos MinimizeB IconARCM DestroyOC"
    _arc_panel_info_data = {"Name": "Maps", "Caption": "Maps", "CloseB": False, "BestS": (32 * 8, 32 * 4),
                            "MinimizeM": ["POS_SMART", "CAPT_SMART", ], "Layer": 1, "Row": 1, "Pos": 1, "MinimizeB": True, 'IconARCM': 'project_icon'}

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
            data = self.treectrl.GetItemData(item).GetData()
            if data:
                map_id, name = data
                project = Kernel.GlobalObjects["PROJECT"]
                map = project.getMapData(map_id)
                tilesets = project.getData("Tilesets")
                if "PanelManager" in Kernel.GlobalObjects:
                    Kernel.GlobalObjects["PanelManager"].dispatchPanel("MapEditorPanel", "Map Editor Panel " + str(map_id),
                                                                                  arguments=[
                                                                                      map, tilesets],
                                                                                  info="Name Caption",
                                                                                  data={"Name": "[" + str(map_id) + "] " + name, "Caption": "[" + str(map_id) + "] " + name})
        event.Skip()
