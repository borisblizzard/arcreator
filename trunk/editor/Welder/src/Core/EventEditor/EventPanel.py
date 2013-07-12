from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')
KM = Kernel.Manager

import wx
Panels = Core.Panels


class EventPanel(wx.Panel, Panels.PanelBase):

    _arc_panel_info_string = "Name Caption Center CloseB CaptionV BestS MinimizeM MinimizeB MaximizeB Floatable Resizable Snappable NotebookD Movable IconARCM DestroyOC"
    _arc_panel_info_data = {"Name": "Event Editor:", "Caption": "Event Editor:", "CaptionV": True, "BestS": (32 * 10, 32 * 18), "MinimizeM": ["POS_SMART", "CAPT_SMART"], 
                            "MinimizeB": True, "CloseB": True, "NotebookP" : [1], 'IconARCM': 'eventlayericon'}

    def __init__(self, parent, event):
        wx.Panel.__init__(self, parent)