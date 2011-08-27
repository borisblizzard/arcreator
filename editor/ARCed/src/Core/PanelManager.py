'''
Created on May 30, 2011

'''
import wx

try:
    from agw import aui
    from agw.aui import aui_switcherdialog as ASD
except ImportError: # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.aui as aui
    from wx.lib.agw.aui import aui_switcherdialog as ASD
    
import Kernel
from Kernel import Manager as KM
    
class PanelManager(object):
    
    minmodes = {}
    #position modes
    minmodes["POS_SMART"]  = aui.AUI_MINIMIZE_POS_SMART 
    minmodes["POS_TOP"]    = aui.AUI_MINIMIZE_POS_TOP
    minmodes["POS_LEFT"]   = aui.AUI_MINIMIZE_POS_LEFT
    minmodes["POS_RIGHT"]  = aui.AUI_MINIMIZE_POS_RIGHT
    minmodes["POS_BOTTOM"] = aui.AUI_MINIMIZE_POS_BOTTOM
    minmodes["POS_MASK"]   = aui.AUI_MINIMIZE_POS_MASK
    #caption modes
    minmodes["CAPT_HIDE"]  = aui.AUI_MINIMIZE_CAPT_HIDE
    minmodes["CAPT_SMART"] = aui.AUI_MINIMIZE_CAPT_SMART
    minmodes["CAPT_HORZ"]  = aui.AUI_MINIMIZE_CAPT_HORZ
    minmodes["CAPT_MASK"]  = aui.AUI_MINIMIZE_CAPT_MASK
    
    def __init__(self, manager):
        
        self.manager = manager
        self.panals = {}
        self.dispached = {}
        types = KM.get_type("PanelManagerType")
        for type in types.types:
            for component in type.components:
                self.regester(component, type)
               
    def regester(self, component):
        pass
    
    def generate_info(self, string, data={}):
        info = aui.AuiPaneInfo()
        if "Caption" in string:
            if data.has_key("Caption"):
                info.Caption(data["Caption"])
        if "Center" in string:
            info.Center()
        if "CenterP" in string:
            info.CenterPane()
        if "CaptionV" in string:
            if data.has_key("CaptionV"):
                info.CaptionVisible(*data["CaptionV"])
            else:
                info.CaptionVisible(True)
        if "BestS" in string:
            if data.has_key("BestS"):
                info.BestSize(*data["BestS"])
        if "CloseB" in string:
            if data.has_key("CloseB"):
                info.CloseButton(data["CloseB"])
            else:
                info.CloseButton(True)
        if "Bottom" in string:
            info.Bottom()
        if "BottomD" in string:
            if data.has_key("BottomD"):
                info.BottomDockable(data["BottomD"])
            else:
                info.BottomDockable(True)
        if "BottomS" in string:
            if data.has_key("BottomS"):
                info.BottomSnappable(data["BottomS"])
            else:
                info.BottomSnappable(True)
        if "DefaultP" in string:
            info.DefaultPane()
        if "DestroyOC" in string:
            if data.has_key("DestroyOC"):
                info.DestroyOnClose(data["DestroyOC"])
            else:
                info.DestroyOnClose(True)
        if "Dock" in string:
            info.Dock()
        if "DockF" in string:
            if data.has_key("DockF"):
                info.DockFixed(data["DockF"])
            else:
                info.DockFixed(True)
        if "Dockable" in string:
            if data.has_key("Dockable"):
                info.Dockable(data["Dockable"])
            else:
                info.Dockable(True)
        if "Fixed" in string:
            info.Fixed()
        if "Float" in string:
            info.Float()
        if "Floatable" in string:
            if data.has_key("Floatable"):
                info.Floatable(data["Floatable"])
            else:
                info.Floatable(True)
        if "FloatingP" in string:
            if data.has_key("FloatingP"):
                info.FloatingPosition(data["FloatingP"])
        if "FloatingS" in string:
            if data.has_key("FloatingS"):
                info.FloatingSize(data["FloatingS"])
        if "FlyOut" in string:
            if data.has_key("FlyOut"):
                info.FlyOut(data["FlyOut"])
            else:
                info.FlyOut(True)
        if "Gripper" in string:
            if data.has_key("Gripper"):
                info.Gripper(data["Gripper"])
            else:
                info.Gripper()
        if "GripperT" in string:
            if data.has_key("GripperT"):
                info.GripperTop(data["GripperT"])
            else:
                info.GripperTop(True)
        if "Hide" in string:
            info.Hide()
        if "Icon" in string:
            if data.has_key("Icon"):
                info.Icon(data["Icon"])
        if "Layer" in string:
            if data.has_key("Layer"):
                info.Layer(data["Layer"])
        if "Left" in string:
            info.Left()
        if "LeftD" in string:
            if data.has_key("LeftD"):
                info.LeftDockable(data["LeftD"])
            else:
                info.LeftDockable(True)
        if "LeftS" in string:
            if data.has_key("LeftS"):
                info.LeftSnappable(data["LeftS"])
            else:
                info.LeftSnappable(True)
        if "MaxS" in string:
            if data.has_key("MaxS"):
                info.MaxSize(*data["MaxS"])
        if "Maximize" in string:
            info.Maximize()
        if "MaximizeB" in string:
            if data.has_key("MaximizeB"):
                info.MaximizeButton(data["MaximizeB"])
            else:
                info.MaximizeButton(True)
        if "MinS" in string:
            if data.has_key("MinS"):
                info.MinSize(*data["MinS"])
        if "Minimize" in string:
            info.Minimize()
        if "MinimizeB" in string:
            if data.has_key("MinimizeB"):
                info.MinimizeButton(data["MinimizeB"])
            else:
                info.MinimizeButton(True)
        if "MinimizeM" in string:
            if data.has_key("MinimizeM"):
                mode = 0
                for flag in data["MinimizeM"]:
                    mode |= self.minmodes[flag]
                info.MinimizeMode(mode)
        if "Movable" in string:
            if data.has_key("Movable"):
                info.Movable(data["Movable"])
            else:
                info.Movable(True)
        if "Name" in string:
            if data.has_key("Name"):
                info.Name(data["Name"])
        if "NotebookC" in string:
            if data.has_key("NotebookC"):
                info.NotebookControl(data["NotebookC"])
        if "NotebookD" in string:
            if data.has_key("NotebookD"):
                info.NotebookDockable(data["NotebookD"])
            else:
                info.NotebookDockable(True)
        if "NotebookP" in string:
            if data.has_key("NotebookP"):
                info.NotebookPage(*data["NotebookP"])
        if "PaneB" in string:
            if data.has_key("PaneB"):
                info.PaneBorder(data["PaneB"])
            else:
                info.PaneBorder(True)
        if "PinB" in string:
            if data.has_key("PinB"):
                info.PinButton(data["PinB"])
            else:
                info.PinButton(True)
        if "Resizable" in string:
            if data.has_key("Resizable"):
                info.Resizable(data["Resizable"])
            else:
                info.Resizable(True)
        if "Right" in string:
            info.Right()
        if "RightD" in string:
            if data.has_key("RightD"):
                info.RightDockable(data["RightD"])
            else:
                info.RightDockable(True)
        if "RightS" in string:
            if data.has_key("RightS"):
                info.RightSnappable(data["RightS"])
            else:
                info.RightSnappable(True)
        if "Row" in string:
            if data.has_key("Row"):
                info.Row(data["Row"])
        if "Show" in string:
            info.Show(True)
        if "Snappable" in string:
            if data.has_key("Snappable"):
                info.Snappable(data["Snappable"])
            else:
                info.Snappable(True)
        if "ToolbarPane" in string:
            info.ToolbarPane()
        if "Top" in string:
            info.Top()
        if "TopD" in string:
            if data.has_key("TopD"):
                info.TopDockable(data["TopD"])
            else:
                info.TopDockable(True)
        if "TopS" in string:
            if data.has_key("TopS"):
                info.TopSnappable(data["TopS"])
            else:
                info.TopSnappable(True)
        if "Transparent" in string:
            if data.has_key("Transparent"):
                info.Transparent(data["Transparent"])
        return info
    
 
    
        
        
    