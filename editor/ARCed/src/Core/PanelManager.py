'''
Created on May 30, 2011

PanelManger

TODO: create show and hide methods

'''
import wx
import wx.lib.agw.aui as aui

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
    
    def __init__(self, parent, manager):
        '''
        sets up the Panel Manager
        '''
        self.parent = parent
        self.manager = manager
        self.dispached = {}
        self.IDs = {}
        self.LastActive = {}
        self.LastActive[aui.AUI_DOCK_NOTEBOOK_PAGE] = None
        self.LastActive[aui.AUI_DOCK_BOTTOM] = None
        self.LastActive[aui.AUI_DOCK_TOP] = None
        self.LastActive[aui.AUI_DOCK_LEFT] = None
        self.LastActive[aui.AUI_DOCK_RIGHT] = None
        self.LastActive[aui.AUI_DOCK_CENTER] = None

    def RequestUserAttention(self, window):
        self.manager.RequestUserAttention(window)

    def set_last_active(self, id):
        ''' Sets the last active Center Panel ID so that the next center panel is docked on top of it'''
        info = self.getPanelInfo(id)
        if info is not None:
            self.LastActive[info.dock_direction_get()] = id
    
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
        #build the window instance
        panel = self.get_panel_object(type)
        panel_instance = panel(self.parent, *arguments)
        #generate the AUI info
        info_obj = None
        if hasattr(panel, "_arc_panel_info_string"):
            if hasattr(panel, "_arc_panel_info_data"):
                info_obj = self.generate_info(panel._arc_panel_info_string, panel._arc_panel_info_data, info_obj)
            else:
                info_obj = self.generate_info(panel._arc_panel_info_string, info=info_obj)
        info_obj = self.generate_info(info, data, info_obj)
        #Check to see if we should dock or float this panel
        docktarget = None
        if not info_obj.IsFloating():
            targetid = self.LastActive[info_obj.dock_direction_get()]
            if (self.dispached.has_key(targetid)) and (self.dispached[targetid] != None):
                docktarget = self.getPanelInfo(targetid)
        panel_instance._ARC_Panel_Info = info_obj
        #store the panel
        if self.dispached.has_key(id):
            self.remove_panel(id)
        self.dispached[id] = panel_instance
        self.IDs[panel_instance] = id
        #add the panel to the AUI interface
        self.manager.AddPane(panel_instance, info_obj, target=docktarget)
        self.Update()
        return panel_instance    
    
    def remove_panel(self, id):
        '''
        removes the panel mapped to id from the AUI manager and destroys it
        then removed id from the dispatched dict
        '''
        if (self.dispached.has_key(id)) and (self.dispached[id] != None):
            info = self.getPanelInfo(id)
            if info is not None:
                info.Float()
            self.manager.DetachPane(self.dispached[id])
            self.Update()
            if self.dispached[id]:
                self.dispached[id].Destroy()
            del self.IDs[self.dispached[id]]
            del self.dispached[id]
        
    def Update(self):
        '''
        Updates the AUI Manager to reflect changes
        '''
        self.manager.Update()
    
    def generate_info(self, info, data={}, info_obj=None):
        '''
        generates a AuiPaneInfo object from the info string and data dict. 
        if an existing AuiPaneInfo object is provided it is extended with the information in the info string and data dict.
        commands that contradict previous setting in the provided AuiPaneInfo object overwrite old settings.
        
        @param info: a string of words seperated by a simple space
            where each word corresponds to a method that could be called on the AuiPaneInfo object
            
        @param data: a dict with where the keys are the names provided in the info string and the values 
            are a sequence of parameters that could be expanded to provide the arguments for the methods 
            those names would call on the AuiPaneInfo object
            
        @param info_obj: a AuiPaneInfo object to be extended
        '''
        
        if info_obj == None:
            info_obj = aui.AuiPaneInfo()
        words = info.split(" ")
        for word in words:
            #center
            if "CenterP" in word:
                info_obj.CenterPane()
            elif "Center" in word:
                info_obj.Center()
            #caption
            if "CaptionV" in word:
                if data.has_key("CaptionV"):
                    info_obj.CaptionVisible(data["CaptionV"])
                else:
                    info_obj.CaptionVisible(True)
            elif "Caption" in word:
                if data.has_key("Caption"):
                    info_obj.Caption(data["Caption"])
            #best size
            if "BestS" in word:
                if data.has_key("BestS"):
                    info_obj.BestSize(data["BestS"])
            #close button
            if "CloseB" in word:
                if data.has_key("CloseB"):
                    info_obj.CloseButton(data["CloseB"])
                else:
                    info_obj.CloseButton(True)
            #bottom
            if "BottomD" in word:
                if data.has_key("BottomD"):
                    info_obj.BottomDockable(data["BottomD"])
                else:
                    info_obj.BottomDockable(True)
            elif "BottomS" in word:
                if data.has_key("BottomS"):
                    info_obj.BottomSnappable(data["BottomS"])
                else:
                    info_obj.BottomSnappable(True)
            elif "Bottom" in word:
                info_obj.Bottom()
            #default
            if "DefaultP" in word:
                info_obj.DefaultPane()
            #destroy on close
            if "DestroyOC" in word:
                if data.has_key("DestroyOC"):
                    info_obj.DestroyOnClose(data["DestroyOC"])
                else:
                    info_obj.DestroyOnClose(True)
            #dock
            if "DockF" in word:
                if data.has_key("DockF"):
                    info_obj.DockFixed(data["DockF"])
                else:
                    info_obj.DockFixed(True)
            elif "Dockable" in word:
                if data.has_key("Dockable"):
                    info_obj.Dockable(data["Dockable"])
                else:
                    info_obj.Dockable(True)
            elif "Dock" in word:
                info_obj.Dock()
            #fixed
            if "Fixed" in word:
                info_obj.Fixed()
            #float
            if "Floatable" in word:
                if data.has_key("Floatable"):
                    info_obj.Floatable(data["Floatable"])
                else:
                    info_obj.Floatable(True)
            elif "FloatingP" in word:
                if data.has_key("FloatingP"):
                    info_obj.FloatingPosition(data["FloatingP"])
            elif "FloatingS" in word:
                if data.has_key("FloatingS"):
                    info_obj.FloatingSize(data["FloatingS"])
            elif "Float" in word:
                info_obj.Float()
            #flyout
            if "FlyOut" in word:
                if data.has_key("FlyOut"):
                    info_obj.FlyOut(data["FlyOut"])
                else:
                    info_obj.FlyOut(True)
            #gripper
            if "GripperT" in word:
                if data.has_key("GripperT"):
                    info_obj.GripperTop(data["GripperT"])
                else:
                    info_obj.GripperTop(True)
            elif "Gripper" in word:
                if data.has_key("Gripper"):
                    info_obj.Gripper(data["Gripper"])
                else:
                    info_obj.Gripper()
            #hide
            if "Hide" in word:
                info_obj.Hide()
            #icon
            if "IconARCM" in word:
                if data.has_key("IconARCM"):
                    IconManager = KM.get_component("IconManager").object
                    icon = IconManager.getBitmap(data["IconARCM"])
                    info_obj.Icon(icon)
            elif "Icon" in word:
                if data.has_key("Icon"):
                    info_obj.Icon(data["Icon"])
            #layer
            if "Layer" in word:
                if data.has_key("Layer"):
                    info_obj.Layer(data["Layer"])
            #left
            if "LeftD" in word:
                if data.has_key("LeftD"):
                    info_obj.LeftDockable(data["LeftD"])
                else:
                    info_obj.LeftDockable(True)
            elif "LeftS" in word:
                if data.has_key("LeftS"):
                    info_obj.LeftSnappable(data["LeftS"])
                else:
                    info_obj.LeftSnappable(True)
            elif "Left" in word:
                info_obj.Left()
            #max size
            if "MaxS" in word:
                if data.has_key("MaxS"):
                    info_obj.MaxSize(data["MaxS"])
            #maximize
            if "MaximizeB" in word:
                if data.has_key("MaximizeB"):
                    info_obj.MaximizeButton(data["MaximizeB"])
                else:
                    info_obj.MaximizeButton(True)
            elif "Maximize" in word:
                info_obj.Maximize()
            #min size
            if "MinS" in word:
                if data.has_key("MinS"):
                    info_obj.MinSize(*data["MinS"])
            #minimize
            if "MinimizeB" in word:
                if data.has_key("MinimizeB"):
                    info_obj.MinimizeButton(data["MinimizeB"])
                else:
                    info_obj.MinimizeButton(True)
            elif "MinimizeM" in word:
                if data.has_key("MinimizeM"):
                    mode = 0
                    for flag in data["MinimizeM"]:
                        mode |= self.minmodes[flag]
                    info_obj.MinimizeMode(mode)
            elif "Minimize" in word:
                info_obj.Minimize()
            #movable
            if "Movable" in word:
                if data.has_key("Movable"):
                    info_obj.Movable(data["Movable"])
                else:
                    info_obj.Movable(True)
            #name
            if "Name" in word:
                if data.has_key("Name"):
                    info_obj.Name(data["Name"])
            #notebook
            if "NotebookC" in word:
                if data.has_key("NotebookC"):
                    info_obj.NotebookControl(data["NotebookC"])
            elif "NotebookD" in word:
                if data.has_key("NotebookD"):
                    info_obj.NotebookDockable(data["NotebookD"])
                else:
                    info_obj.NotebookDockable(True)
            elif "NotebookP" in word:
                if data.has_key("NotebookP"):
                    info_obj.NotebookPage(*data["NotebookP"])
            #pane border
            if "PaneB" in word:
                if data.has_key("PaneB"):
                    info_obj.PaneBorder(data["PaneB"])
                else:
                    info_obj.PaneBorder(True)
            #pin
            if "PinB" in word:
                if data.has_key("PinB"):
                    info_obj.PinButton(data["PinB"])
                else:
                    info_obj.PinButton(True)
            #resizeable
            if "Resizable" in word:
                if data.has_key("Resizable"):
                    info_obj.Resizable(data["Resizable"])
                else:
                    info_obj.Resizable(True)
            #right
            if "RightD" in word:
                if data.has_key("RightD"):
                    info_obj.RightDockable(data["RightD"])
                else:
                    info_obj.RightDockable(True)
            elif "RightS" in word:
                if data.has_key("RightS"):
                    info_obj.RightSnappable(data["RightS"])
                else:
                    info_obj.RightSnappable(True)
            elif "Right" in word:
                info_obj.Right()
            #row
            if "Row" in word:
                if data.has_key("Row"):
                    info_obj.Row(data["Row"])
            #show
            if "Show" in word:
                info_obj.Show(True)
            #snappable
            if "Snappable" in word:
                if data.has_key("Snappable"):
                    info_obj.Snappable(data["Snappable"])
                else:
                    info_obj.Snappable(True)
            #toolbar
            if "ToolbarP" in word:
                info_obj.ToolbarPane()
            #top
            if "TopD" in word:
                if data.has_key("TopD"):
                    info_obj.TopDockable(data["TopD"])
                else:
                    info_obj.TopDockable(True)
            elif "TopS" in word:
                if data.has_key("TopS"):
                    info_obj.TopSnappable(data["TopS"])
                else:
                    info_obj.TopSnappable(True)
            elif "Top" in word:
                info_obj.Top()
            #Transparent
            if "Transparent" in word:
                if data.has_key("Transparent"):
                    info_obj.Transparent(data["Transparent"])

        return info_obj
    
    def getPanel(self, id):
        '''
        retrives the Window object of a panel from the idea it was dispatched with, other wise returns None
        '''
        if (self.dispached.has_key(id)) and (self.dispached[id] != None):
            return self.dispached[id]
        return None

    def getPanelInfo(self, id):
        '''
        gets the auiPaneInfo object of the window that was dispatched with ID
        '''
        window = self.getPanel(id)
        if window is not None:
            info = self.manager.GetPane(window)
            if info.IsOk():
                return info
        return None

    def getPanelID(self, window):
        ''' gets the id a panel was dispatched with '''
        if (self.IDs.has_key(window)) and (self.IDs[window] != None):
            return self.IDs[window]
        return None

    def getDispatched(self, id):
        '''
        return true if there is a panel dispached under ID, otherwise returns false
        '''
        return (self.getPanel(id) is not None)

    def showPanel(self, id, show=True):
        '''
        if there is a window dispatched under id it calls show on the window auiPaneInfo object with the pased value 
        which default to True. it then updates the AuiManager
        '''
        info = self.getPanelInfo(id)
        if info is not None:
            info.Show(show)
            self.Update()

    def getDockedCenterPanels(self):
        '''
        returns the number of center direction panels that are still docked
        '''
        i = 0
        for id in self.dispached.iterkeys():
            info = self.getPanelInfo(id)
            if info.dock_direction_get() == aui.AUI_DOCK_CENTER:
                if not info.IsFloating():
                    i += 1
        return i
