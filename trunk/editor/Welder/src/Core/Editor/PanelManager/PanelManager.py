'''
Created on May 30, 2011

PanelManger

TODO: create show and hide methods

'''

import wx.lib.agw.aui as aui

import Kernel

from PyitectConsumes import IconManager
    
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
    
    def get_panel_object(self, component_name):
        '''
        gets the default component panel class form the plugin framework
        '''
        return Kernel.System.load(component_name)
    
    def dispatch_panel(self, type, id, arguments=[], info="", data={}, overwrite=False):
        '''
        gets a panel instance and dispatches it to the window storing it in the dispatched array mapped to id, 
        if id already exists the panel currently mapped to id is removed before the new panel is dispatched
        '''
        panel = self.get_panel_object(type)
        #generate the AUI info
        info_obj = None
        if hasattr(panel, "_arc_panel_info_string"):
            if hasattr(panel, "_arc_panel_info_data"):
                info_obj = self.generate_info(panel._arc_panel_info_string, panel._arc_panel_info_data, info_obj)
            else:
                info_obj = self.generate_info(panel._arc_panel_info_string, info=info_obj)
        info_obj = self.generate_info(info, data, info_obj)
        
        #find were we might be docking this pane
        docktarget = None
        #Check to see if we should dock or float this panel
        if not info_obj.IsFloating():
            targetid = self.LastActive[info_obj.dock_direction_get()]
            if (targetid in self.dispached) and (self.dispached[targetid] != None):
                docktarget = self.getPanelInfo(targetid)

        #check to see if the pane exists already
        pane_info = self.manager.GetPane(info_obj.name)
        if pane_info.IsOk() and not overwrite:
            info_obj.Show()
            panel_instance = pane_info.window
            self.manager.DetachPane(panel_instance)
            self.manager.AddPane(panel_instance, info_obj, target=docktarget)
            self.manager.RequestUserAttention(panel_instance)
        else:
            
            # prevent duplicates
            if id in self.dispached:
                self.remove_panel(id)
            #build the window instance
            panel_instance = panel(self.parent, *arguments)
            
            panel_instance._ARC_Panel_Info = info_obj
            #store the panel
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
        if (id in self.dispached) and (self.dispached[id] != None):
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
                if "CaptionV" in data:
                    info_obj.CaptionVisible(data["CaptionV"])
                else:
                    info_obj.CaptionVisible(True)
            elif "Caption" in word:
                if "Caption" in data:
                    info_obj.Caption(data["Caption"])
            #best size
            if "BestS" in word:
                if "BestS" in data:
                    info_obj.BestSize(data["BestS"])
            #close button
            if "CloseB" in word:
                if "CloseB" in data:
                    info_obj.CloseButton(data["CloseB"])
                else:
                    info_obj.CloseButton(True)
            #bottom
            if "BottomD" in word:
                if "BottomD" in data:
                    info_obj.BottomDockable(data["BottomD"])
                else:
                    info_obj.BottomDockable(True)
            elif "BottomS" in word:
                if "BottomS" in data:
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
                if "DestroyOC" in data:
                    info_obj.DestroyOnClose(data["DestroyOC"])
                else:
                    info_obj.DestroyOnClose(True)
            #dock
            if "DockF" in word:
                if "DockF" in data:
                    info_obj.DockFixed(data["DockF"])
                else:
                    info_obj.DockFixed(True)
            elif "Dockable" in word:
                if "Dockable" in data:
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
                if "Floatable" in data:
                    info_obj.Floatable(data["Floatable"])
                else:
                    info_obj.Floatable(True)
            elif "FloatingP" in word:
                if "FloatingP" in data:
                    info_obj.FloatingPosition(data["FloatingP"])
            elif "FloatingS" in word:
                if "FloatingS" in data:
                    info_obj.FloatingSize(data["FloatingS"])
            elif "Float" in word:
                info_obj.Float()
            #flyout
            if "FlyOut" in word:
                if "FlyOut" in data:
                    info_obj.FlyOut(data["FlyOut"])
                else:
                    info_obj.FlyOut(True)
            #gripper
            if "GripperT" in word:
                if "GripperT" in data:
                    info_obj.GripperTop(data["GripperT"])
                else:
                    info_obj.GripperTop(True)
            elif "Gripper" in word:
                if "Gripper" in data:
                    info_obj.Gripper(data["Gripper"])
                else:
                    info_obj.Gripper()
            #hide
            if "Hide" in word:
                info_obj.Hide()
            #icon
            if "IconARCM" in word:
                if "IconARCM" in data:
                    icon = IconManager.getBitmap(data["IconARCM"])
                    info_obj.Icon(icon)
            elif "Icon" in word:
                if "Icon" in data:
                    info_obj.Icon(data["Icon"])
            #layer
            if "Layer" in word:
                if "Layer" in data:
                    info_obj.Layer(data["Layer"])
            #left
            if "LeftD" in word:
                if "LeftD" in data:
                    info_obj.LeftDockable(data["LeftD"])
                else:
                    info_obj.LeftDockable(True)
            elif "LeftS" in word:
                if "LeftS" in data:
                    info_obj.LeftSnappable(data["LeftS"])
                else:
                    info_obj.LeftSnappable(True)
            elif "Left" in word:
                info_obj.Left()
            #max size
            if "MaxS" in word:
                if "MaxS" in data:
                    info_obj.MaxSize(data["MaxS"])
            #maximize
            if "MaximizeB" in word:
                if "MaximizeB" in data:
                    info_obj.MaximizeButton(data["MaximizeB"])
                else:
                    info_obj.MaximizeButton(True)
            elif "Maximize" in word:
                info_obj.Maximize()
            #min size
            if "MinS" in word:
                if "MinS" in data:
                    info_obj.MinSize(*data["MinS"])
            #minimize
            if "MinimizeB" in word:
                if "MinimizeB" in data:
                    info_obj.MinimizeButton(data["MinimizeB"])
                else:
                    info_obj.MinimizeButton(True)
            elif "MinimizeM" in word:
                if "MinimizeM" in data:
                    mode = 0
                    for flag in data["MinimizeM"]:
                        mode |= self.minmodes[flag]
                    info_obj.MinimizeMode(mode)
            elif "Minimize" in word:
                info_obj.Minimize()
            #movable
            if "Movable" in word:
                if "Movable" in data:
                    info_obj.Movable(data["Movable"])
                else:
                    info_obj.Movable(True)
            #name
            if "Name" in word:
                if "Name" in data:
                    info_obj.Name(data["Name"])
            #notebook
            if "NotebookC" in word:
                if "NotebookC" in data:
                    info_obj.NotebookControl(data["NotebookC"])
            elif "NotebookD" in word:
                if "NotebookD" in data:
                    info_obj.NotebookDockable(data["NotebookD"])
                else:
                    info_obj.NotebookDockable(True)
            elif "NotebookP" in word:
                if "NotebookP" in data:
                    info_obj.NotebookPage(*data["NotebookP"])
            #pane border
            if "PaneB" in word:
                if "PaneB" in data:
                    info_obj.PaneBorder(data["PaneB"])
                else:
                    info_obj.PaneBorder(True)
            #pin
            if "PinB" in word:
                if "PinB" in data:
                    info_obj.PinButton(data["PinB"])
                else:
                    info_obj.PinButton(True)
            #resizeable
            if "Resizable" in word:
                if "Resizable" in data:
                    info_obj.Resizable(data["Resizable"])
                else:
                    info_obj.Resizable(True)
            #right
            if "RightD" in word:
                if "RightD" in data:
                    info_obj.RightDockable(data["RightD"])
                else:
                    info_obj.RightDockable(True)
            elif "RightS" in word:
                if "RightS" in data:
                    info_obj.RightSnappable(data["RightS"])
                else:
                    info_obj.RightSnappable(True)
            elif "Right" in word:
                info_obj.Right()
            #row
            if "Row" in word:
                if "Row" in data:
                    info_obj.Row(data["Row"])
            #show
            if "Show" in word:
                info_obj.Show(True)
            #snappable
            if "Snappable" in word:
                if "Snappable" in data:
                    info_obj.Snappable(data["Snappable"])
                else:
                    info_obj.Snappable(True)
            #toolbar
            if "ToolbarP" in word:
                info_obj.ToolbarPane()
            #top
            if "TopD" in word:
                if "TopD" in data:
                    info_obj.TopDockable(data["TopD"])
                else:
                    info_obj.TopDockable(True)
            elif "TopS" in word:
                if "TopS" in data:
                    info_obj.TopSnappable(data["TopS"])
                else:
                    info_obj.TopSnappable(True)
            elif "Top" in word:
                info_obj.Top()
            #Transparent
            if "Transparent" in word:
                if "Transparent" in data:
                    info_obj.Transparent(data["Transparent"])

        return info_obj
    
    def getPanel(self, id):
        '''
        retrives the Window object of a panel from the idea it was dispatched with, other wise returns None
        '''
        if (id in self.dispached) and (self.dispached[id] != None):
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
        if (window in self.IDs) and (self.IDs[window] != None):
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
        for id in self.dispached.keys():
            info = self.getPanelInfo(id)
            if info.dock_direction_get() == aui.AUI_DOCK_CENTER:
                if not info.IsFloating():
                    i += 1
        return i
