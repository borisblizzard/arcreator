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
    
    def __init__(self, manager, parent):
        
        self.manager = manager
        self.parent = parent
        self.dispached = {}
    
    def get_panel_object(self, type_name):
        '''
        gets the default component panel class form the plugin framework
        '''
        return KM.get_type("PanelManagerType").get_type(type_name).get_default_component().object
    
    def dispatch_panel(self, type, id, arguments=[], info="", data={}):
        '''
        gets a panel instance and dispatches it to the window storing it in the dispatched array mapped to id, 
        if id already exists the panel currently mapped to id is removed before the new panel is dispatched
        '''
        panel = self.get_panel_object(type)
        panel_instance = panel(self.parent, *arguments)
        info_obj = self.generate_info(info, data)
        if hasattr(panel, "_arc_panel_info_string"):
            if hasattr(panel, "_arc_panel_info_data"):
                info_obj = self.generate_info(panel._arc_panel_info_string, panel._arc_panel_info_data, info_obj)
            else:
                info_obj = self.generate_info(panel._arc_panel_info_string, info=info_obj)
        if self.dispached.has_key(id):
            self.remove_panel(id)
        self.dispached[id] = panel_instance
        self.manager.AddPane(panel_instance, info_obj)
            
    
    def remove_panel(self, id):
        '''
        removes the panel mapped to id from the AUI manager and destroys it
        then removed id from the dispatched dict
        '''
        if (self.dispached.has_key(id)) and (self.dispached[id] is not None):
            self.manager.DetachPane(self.dispached[id])
            self.dispached[id].Destroy()
            del self.dispached[id]
    
    def generate_info(self, info, data={}, info=None):
        '''
        generates a AuiPaneInfo object from the info string and data dict. 
        if an existing AuiPaneInfo object is provided it is extended with the information in the info string and data dict.
        commands that contradict previous setting in the provided AuiPaneInfo object overwrite old settings.
        
        @param info: a string of words seperated by some character be it a , a . a | a / or a simple space
            where each word corresponds to a method that could be called on the AuiPaneInfo object
            
        @param data: a dict with where the keys are the names provided in the info string and the values 
            are a sequence of parameters that could be expanded to provide the arguments for the methods 
            those names would call on the AuiPaneInfo object
            
        @param info: a AuiPaneInfo object to be extended
        '''
        if info is None:
            info = aui.AuiPaneInfo()
        if "Caption" in info:
            if data.has_key("Caption"):
                info.Caption(data["Caption"])
        if "Center" in info:
            info.Center()
        if "CenterP" in info:
            info.CenterPane()
        if "CaptionV" in info:
            if data.has_key("CaptionV"):
                info.CaptionVisible(*data["CaptionV"])
            else:
                info.CaptionVisible(True)
        if "BestS" in info:
            if data.has_key("BestS"):
                info.BestSize(*data["BestS"])
        if "CloseB" in info:
            if data.has_key("CloseB"):
                info.CloseButton(data["CloseB"])
            else:
                info.CloseButton(True)
        if "Bottom" in info:
            info.Bottom()
        if "BottomD" in info:
            if data.has_key("BottomD"):
                info.BottomDockable(data["BottomD"])
            else:
                info.BottomDockable(True)
        if "BottomS" in info:
            if data.has_key("BottomS"):
                info.BottomSnappable(data["BottomS"])
            else:
                info.BottomSnappable(True)
        if "DefaultP" in info:
            info.DefaultPane()
        if "DestroyOC" in info:
            if data.has_key("DestroyOC"):
                info.DestroyOnClose(data["DestroyOC"])
            else:
                info.DestroyOnClose(True)
        if "Dock" in info:
            info.Dock()
        if "DockF" in info:
            if data.has_key("DockF"):
                info.DockFixed(data["DockF"])
            else:
                info.DockFixed(True)
        if "Dockable" in info:
            if data.has_key("Dockable"):
                info.Dockable(data["Dockable"])
            else:
                info.Dockable(True)
        if "Fixed" in info:
            info.Fixed()
        if "Float" in info:
            info.Float()
        if "Floatable" in info:
            if data.has_key("Floatable"):
                info.Floatable(data["Floatable"])
            else:
                info.Floatable(True)
        if "FloatingP" in info:
            if data.has_key("FloatingP"):
                info.FloatingPosition(data["FloatingP"])
        if "FloatingS" in info:
            if data.has_key("FloatingS"):
                info.FloatingSize(data["FloatingS"])
        if "FlyOut" in info:
            if data.has_key("FlyOut"):
                info.FlyOut(data["FlyOut"])
            else:
                info.FlyOut(True)
        if "Gripper" in info:
            if data.has_key("Gripper"):
                info.Gripper(data["Gripper"])
            else:
                info.Gripper()
        if "GripperT" in info:
            if data.has_key("GripperT"):
                info.GripperTop(data["GripperT"])
            else:
                info.GripperTop(True)
        if "Hide" in info:
            info.Hide()
        if "Icon" in info:
            if data.has_key("Icon"):
                info.Icon(data["Icon"])
        if "Layer" in info:
            if data.has_key("Layer"):
                info.Layer(data["Layer"])
        if "Left" in info:
            info.Left()
        if "LeftD" in info:
            if data.has_key("LeftD"):
                info.LeftDockable(data["LeftD"])
            else:
                info.LeftDockable(True)
        if "LeftS" in info:
            if data.has_key("LeftS"):
                info.LeftSnappable(data["LeftS"])
            else:
                info.LeftSnappable(True)
        if "MaxS" in info:
            if data.has_key("MaxS"):
                info.MaxSize(*data["MaxS"])
        if "Maximize" in info:
            info.Maximize()
        if "MaximizeB" in info:
            if data.has_key("MaximizeB"):
                info.MaximizeButton(data["MaximizeB"])
            else:
                info.MaximizeButton(True)
        if "MinS" in info:
            if data.has_key("MinS"):
                info.MinSize(*data["MinS"])
        if "Minimize" in info:
            info.Minimize()
        if "MinimizeB" in info:
            if data.has_key("MinimizeB"):
                info.MinimizeButton(data["MinimizeB"])
            else:
                info.MinimizeButton(True)
        if "MinimizeM" in info:
            if data.has_key("MinimizeM"):
                mode = 0
                for flag in data["MinimizeM"]:
                    mode |= self.minmodes[flag]
                info.MinimizeMode(mode)
        if "Movable" in info:
            if data.has_key("Movable"):
                info.Movable(data["Movable"])
            else:
                info.Movable(True)
        if "Name" in info:
            if data.has_key("Name"):
                info.Name(data["Name"])
        if "NotebookC" in info:
            if data.has_key("NotebookC"):
                info.NotebookControl(data["NotebookC"])
        if "NotebookD" in info:
            if data.has_key("NotebookD"):
                info.NotebookDockable(data["NotebookD"])
            else:
                info.NotebookDockable(True)
        if "NotebookP" in info:
            if data.has_key("NotebookP"):
                info.NotebookPage(*data["NotebookP"])
        if "PaneB" in info:
            if data.has_key("PaneB"):
                info.PaneBorder(data["PaneB"])
            else:
                info.PaneBorder(True)
        if "PinB" in info:
            if data.has_key("PinB"):
                info.PinButton(data["PinB"])
            else:
                info.PinButton(True)
        if "Resizable" in info:
            if data.has_key("Resizable"):
                info.Resizable(data["Resizable"])
            else:
                info.Resizable(True)
        if "Right" in info:
            info.Right()
        if "RightD" in info:
            if data.has_key("RightD"):
                info.RightDockable(data["RightD"])
            else:
                info.RightDockable(True)
        if "RightS" in info:
            if data.has_key("RightS"):
                info.RightSnappable(data["RightS"])
            else:
                info.RightSnappable(True)
        if "Row" in info:
            if data.has_key("Row"):
                info.Row(data["Row"])
        if "Show" in info:
            info.Show(True)
        if "Snappable" in info:
            if data.has_key("Snappable"):
                info.Snappable(data["Snappable"])
            else:
                info.Snappable(True)
        if "ToolbarPane" in info:
            info.ToolbarPane()
        if "Top" in info:
            info.Top()
        if "TopD" in info:
            if data.has_key("TopD"):
                info.TopDockable(data["TopD"])
            else:
                info.TopDockable(True)
        if "TopS" in info:
            if data.has_key("TopS"):
                info.TopSnappable(data["TopS"])
            else:
                info.TopSnappable(True)
        if "Transparent" in info:
            if data.has_key("Transparent"):
                info.Transparent(data["Transparent"])
        return info
    