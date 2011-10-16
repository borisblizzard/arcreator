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
        if (self.dispached.has_key(id)) and (self.dispached[id] != None):
            self.manager.DetachPane(self.dispached[id])
            self.dispached[id].Destroy()
            del self.dispached[id]
    
    def generate_info(self, info, data={}, info_obj=None):
        '''
        generates a AuiPaneInfo object from the info string and data dict. 
        if an existing AuiPaneInfo object is provided it is extended with the information in the info string and data dict.
        commands that contradict previous setting in the provided AuiPaneInfo object overwrite old settings.
        
        @param info: a string of words seperated by some character be it a , a . a | a / or a simple space
            where each word corresponds to a method that could be called on the AuiPaneInfo object
            
        @param data: a dict with where the keys are the names provided in the info string and the values 
            are a sequence of parameters that could be expanded to provide the arguments for the methods 
            those names would call on the AuiPaneInfo object
            
        @param info_obj: a AuiPaneInfo object to be extended
        '''
        if info_obj == None:
            info_obj = aui.AuiPaneInfo()
        if "Caption" in info:
            if data.has_key("Caption"):
                info_obj.Caption(data["Caption"])
        if "Center" in info:
            info_obj.Center()
        if "CenterP" in info:
            info_obj.CenterPane()
        if "CaptionV" in info:
            if data.has_key("CaptionV"):
                info_obj.CaptionVisible(*data["CaptionV"])
            else:
                info_obj.CaptionVisible(True)
        if "BestS" in info:
            if data.has_key("BestS"):
                info_obj.BestSize(*data["BestS"])
        if "CloseB" in info:
            if data.has_key("CloseB"):
                info_obj.CloseButton(data["CloseB"])
            else:
                info_obj.CloseButton(True)
        if "Bottom" in info:
            info_obj.Bottom()
        if "BottomD" in info:
            if data.has_key("BottomD"):
                info_obj.BottomDockable(data["BottomD"])
            else:
                info_obj.BottomDockable(True)
        if "BottomS" in info:
            if data.has_key("BottomS"):
                info_obj.BottomSnappable(data["BottomS"])
            else:
                info_obj.BottomSnappable(True)
        if "DefaultP" in info:
            info_obj.DefaultPane()
        if "DestroyOC" in info:
            if data.has_key("DestroyOC"):
                info_obj.DestroyOnClose(data["DestroyOC"])
            else:
                info_obj.DestroyOnClose(True)
        if "Dock" in info:
            info_obj.Dock()
        if "DockF" in info:
            if data.has_key("DockF"):
                info_obj.DockFixed(data["DockF"])
            else:
                info_obj.DockFixed(True)
        if "Dockable" in info:
            if data.has_key("Dockable"):
                info_obj.Dockable(data["Dockable"])
            else:
                info_obj.Dockable(True)
        if "Fixed" in info:
            info_obj.Fixed()
        if "Float" in info:
            info_obj.Float()
        if "Floatable" in info:
            if data.has_key("Floatable"):
                info_obj.Floatable(data["Floatable"])
            else:
                info_obj.Floatable(True)
        if "FloatingP" in info:
            if data.has_key("FloatingP"):
                info_obj.FloatingPosition(data["FloatingP"])
        if "FloatingS" in info:
            if data.has_key("FloatingS"):
                info_obj.FloatingSize(data["FloatingS"])
        if "FlyOut" in info:
            if data.has_key("FlyOut"):
                info_obj.FlyOut(data["FlyOut"])
            else:
                info_obj.FlyOut(True)
        if "Gripper" in info:
            if data.has_key("Gripper"):
                info_obj.Gripper(data["Gripper"])
            else:
                info_obj.Gripper()
        if "GripperT" in info:
            if data.has_key("GripperT"):
                info_obj.GripperTop(data["GripperT"])
            else:
                info_obj.GripperTop(True)
        if "Hide" in info:
            info_obj.Hide()
        if "Icon" in info:
            if data.has_key("Icon"):
                info_obj.Icon(data["Icon"])
        if "Layer" in info:
            if data.has_key("Layer"):
                info_obj.Layer(data["Layer"])
        if "Left" in info:
            info_obj.Left()
        if "LeftD" in info:
            if data.has_key("LeftD"):
                info_obj.LeftDockable(data["LeftD"])
            else:
                info_obj.LeftDockable(True)
        if "LeftS" in info:
            if data.has_key("LeftS"):
                info_obj.LeftSnappable(data["LeftS"])
            else:
                info_obj.LeftSnappable(True)
        if "MaxS" in info:
            if data.has_key("MaxS"):
                info_obj.MaxSize(*data["MaxS"])
        if "Maximize" in info:
            info_obj.Maximize()
        if "MaximizeB" in info:
            if data.has_key("MaximizeB"):
                info_obj.MaximizeButton(data["MaximizeB"])
            else:
                info_obj.MaximizeButton(True)
        if "MinS" in info:
            if data.has_key("MinS"):
                info_obj.MinSize(*data["MinS"])
        if "Minimize" in info:
            info_obj.Minimize()
        if "MinimizeB" in info:
            if data.has_key("MinimizeB"):
                info_obj.MinimizeButton(data["MinimizeB"])
            else:
                info_obj.MinimizeButton(True)
        if "MinimizeM" in info:
            if data.has_key("MinimizeM"):
                mode = 0
                for flag in data["MinimizeM"]:
                    mode |= self.minmodes[flag]
                info_obj.MinimizeMode(mode)
        if "Movable" in info:
            if data.has_key("Movable"):
                info_obj.Movable(data["Movable"])
            else:
                info_obj.Movable(True)
        if "Name" in info:
            if data.has_key("Name"):
                info_obj.Name(data["Name"])
        if "NotebookC" in info:
            if data.has_key("NotebookC"):
                info_obj.NotebookControl(data["NotebookC"])
        if "NotebookD" in info:
            if data.has_key("NotebookD"):
                info_obj.NotebookDockable(data["NotebookD"])
            else:
                info_obj.NotebookDockable(True)
        if "NotebookP" in info:
            if data.has_key("NotebookP"):
                info_obj.NotebookPage(*data["NotebookP"])
        if "PaneB" in info:
            if data.has_key("PaneB"):
                info_obj.PaneBorder(data["PaneB"])
            else:
                info_obj.PaneBorder(True)
        if "PinB" in info:
            if data.has_key("PinB"):
                info_obj.PinButton(data["PinB"])
            else:
                info_obj.PinButton(True)
        if "Resizable" in info:
            if data.has_key("Resizable"):
                info_obj.Resizable(data["Resizable"])
            else:
                info_obj.Resizable(True)
        if "Right" in info:
            info_obj.Right()
        if "RightD" in info:
            if data.has_key("RightD"):
                info_obj.RightDockable(data["RightD"])
            else:
                info_obj.RightDockable(True)
        if "RightS" in info:
            if data.has_key("RightS"):
                info_obj.RightSnappable(data["RightS"])
            else:
                info_obj.RightSnappable(True)
        if "Row" in info:
            if data.has_key("Row"):
                info_obj.Row(data["Row"])
        if "Show" in info:
            info_obj.Show(True)
        if "Snappable" in info:
            if data.has_key("Snappable"):
                info_obj.Snappable(data["Snappable"])
            else:
                info_obj.Snappable(True)
        if "ToolbarPane" in info:
            info_obj.ToolbarPane()
        if "Top" in info:
            info_obj.Top()
        if "TopD" in info:
            if data.has_key("TopD"):
                info_obj.TopDockable(data["TopD"])
            else:
                info_obj.TopDockable(True)
        if "TopS" in info:
            if data.has_key("TopS"):
                info_obj.TopSnappable(data["TopS"])
            else:
                info_obj.TopSnappable(True)
        if "Transparent" in info:
            if data.has_key("Transparent"):
                info_obj.Transparent(data["Transparent"])
        return info_obj
    