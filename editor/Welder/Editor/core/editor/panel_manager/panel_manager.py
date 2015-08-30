'''
Created on May 30, 2011

PanelManger

TODO: create show and hide methods

'''

import wx.lib.agw.aui as aui

import welder_kernel as kernel

from PyitectConsumes import IconManager


class PanelManager(object):

    minmodes = {}
    # position modes
    minmodes["POS_SMART"] = aui.AUI_MINIMIZE_POS_SMART
    minmodes["POS_TOP"] = aui.AUI_MINIMIZE_POS_TOP
    minmodes["POS_LEFT"] = aui.AUI_MINIMIZE_POS_LEFT
    minmodes["POS_RIGHT"] = aui.AUI_MINIMIZE_POS_RIGHT
    minmodes["POS_BOTTOM"] = aui.AUI_MINIMIZE_POS_BOTTOM
    minmodes["POS_MASK"] = aui.AUI_MINIMIZE_POS_MASK
    # caption modes
    minmodes["CAPT_HIDE"] = aui.AUI_MINIMIZE_CAPT_HIDE
    minmodes["CAPT_SMART"] = aui.AUI_MINIMIZE_CAPT_SMART
    minmodes["CAPT_HORZ"] = aui.AUI_MINIMIZE_CAPT_HORZ
    minmodes["CAPT_MASK"] = aui.AUI_MINIMIZE_CAPT_MASK

    info_methods = {
        "CenterP": "CenterPane",
        "Center": "Center",
        "CaptionV": "CaptionVisible",
        "Caption": "Caption",
        "BestS": "BestSize",
        "BottomD": "BottomDockable",
        "BottomS": "BottomSnappable",
        "Bottom": "Bottom",
        "CloseB": "CloseButton",
        "DefaultP": "DefaultPane",
        "DestroyOC": "DestroyOnClose",
        "DockF": "DockFixed",
        "Dockable": "Dockable",
        "Dock": "Dock",
        "Fixed": "Fixed",
        "Floatable": "Floatable",
        "FloatingP": "FloatingPosition",
        "FloatingS": "FloatingSize",
        "Float": "Float",
        "FlyOut": "FlyOut",
        "GripperT": "GripperTop",
        "Gripper": "Gripper",
        "Hide": "Hide",
        "Icon": "Icon",
        "Layer": "Layer",
        "LeftD": "LeftDockable",
        "LeftS": "LeftSnappable",
        "Left": "Left",
        "MaxS": "MaxSize",
        "MaximizeB": "MaximizeButton",
        "Maximize": "Maximize",
        "MinimizeB": "MinimizeButton",
        "MinimizeM": "MinimizeMode",
        "Minimize": "Minimize",
        "Movable": "Movable",
        "Name": "Name",
        "NotebookC": "NotebookControl",
        "NotebookD": "NotebookDockable",
        "NotebookP": "NotebookPage",
        "PaneB": "PaneBorder",
        "PinB": "PinButton",
        "Resizable": "Resizable",
        "Restore": "Restore",
        "RightD": "RightDockable",
        "RightS": "RightSnappable",
        "Right": "Right",
        "Row": "Row",
        "Show": "Show",
        "Snappable": "Snappable",
        "ToolbarP": "ToolbarPane",
        "TopD": "TopDockable",
        "TopS": "TopSnappable",
        "Top": "Top",
        "Transparent": "Transparent"
    }

    info_specials = ["IconARCM"]

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

    def setLastActive(self, wid):
        '''
        Sets the last active Center Panel ID
        so that the next center panel is docked on top of it
        '''
        info = self.getPanelInfo(wid)
        if info is not None:
            self.LastActive[info.dock_direction_get()] = wid

    def getPanelObject(self, component_name):
        '''
        gets the default component panel class form the plugin framework
        '''
        return kernel.System.load(component_name)

    def dispatchPanel(self, type, wid, arguments=[], info={}, overwrite=False):
        '''
        gets a panel instance and dispatches it to the window
        storing it in the dispatched array mapped to id,
        if id already exists the panel currently mapped to id is
        removed before the new panel is dispatched
        '''
        panel = self.getPanelObject(type)
        # generate the AUI info
        info_obj = None
        if hasattr(panel, "_arc_panel_info"):
            # if we have priority keys
            if hasattr(panel, "_arc_panel_info_priority"):
                for key in panel._arc_panel_info_priority:
                    if key in panel._arc_panel_info:
                        # pull the key out of info and run it special
                        info = {}
                        info[key] = panel._arc_panel_info[key]
                        info_obj = self.generateInfo(info, info_obj)
                        del panel._arc_panel_info[key]
            # run the keys remaining in panel_info
            info_obj = self.generateInfo(panel._arc_panel_info, info_obj)
        # run the keys pprovided to the dispatch method
        info_obj = self.generateInfo(info, info_obj)

        # find were we might be docking this pane
        docktarget = None
        # Check to see if we should dock or float this panel
        if not info_obj.IsFloating() and not info_obj.IsToolbar():
            targetid = self.LastActive[info_obj.dock_direction_get()]
            if ((targetid in self.dispached)
                    and (self.dispached[targetid] is not None)):
                target_info = self.getPanelInfo(targetid)
                if target_info is not None and target_info.IsOk():
                    docktarget = target_info

        # check to see if the pane exists already
        pane_info = self.manager.GetPane(info_obj.name)
        if pane_info.IsOk() and not overwrite:
            info_obj.Show()
            panel_instance = pane_info.window
            self.manager.DetachPane(panel_instance)
            self.manager.AddPane(panel_instance, info_obj, target=docktarget)
            self.manager.RequestUserAttention(panel_instance)
            self.setLastActive(wid)
        else:

            # prevent duplicates
            if wid in self.dispached:
                self.removePanel(wid)
            # build the window instance
            panel_instance = panel(self.parent, *arguments)

            panel_instance._ARC_Panel_Info = info_obj
            # store the panel
            self.dispached[wid] = panel_instance
            self.IDs[panel_instance] = wid
            # add the panel to the AUI interface

            self.manager.AddPane(panel_instance, info_obj, target=docktarget)
            self.setLastActive(wid)
        self.update()
        return panel_instance

    def removePanel(self, wid):
        '''
        removes the panel mapped to id from the AUI manager and destroys it
        then removed id from the dispatched dict
        '''
        if (wid in self.dispached) and (self.dispached[wid] is not None):
            info = self.getPanelInfo(wid)
            if info is not None:
                info.Float()
            self.manager.DetachPane(self.dispached[wid])
            self.update()
            if self.dispached[wid]:
                self.dispached[wid].Destroy()
            del self.IDs[self.dispached[wid]]
            del self.dispached[wid]

    def update(self):
        '''
        updates the AUI Manager to reflect changes
        '''
        self.manager.Update()

    def generateInfo(self, info, info_obj=None):
        '''
        generates a AuiPaneInfo object from the info string and data dict.
        if an existing AuiPaneInfo object is provided
        it is extended with the information in the info string and data dict.
        commands that contradict previous setting in the provided AuiPaneInfo
        object overwrite old settings.

        @param info: a dict of keys where each key corresponds
            to a method that could be called on the AuiPaneInfo object

        @param info_obj: a AuiPaneInfo object to be extended
        '''

        if info_obj is None:
            info_obj = aui.AuiPaneInfo()
            info_obj.DefaultPane()

        for key in info:

            if key in self.info_specials:

                if key == "IconARCM":
                    icon = IconManager.getBitmap(info["IconARCM"])
                    info_obj.Icon(icon)
                else:
                    raise KeyError(
                        "'%s' is a invalid _arc_panel_info key" % key
                    )
            elif key in self.info_methods:
                method = getattr(info_obj, self.info_methods[key])
                if info[key] is None:
                    method()
                else:
                    method(info[key])
            else:
                raise KeyError(
                    "'%s' is a invalid _arc_panel_info key" % key
                )

        return info_obj

    def getPanel(self, wid):
        '''
        retrives the Window object of a panel from the
        id it was dispatched with, other wise returns None
        '''
        if (wid in self.dispached) and (self.dispached[wid] is not None):
            return self.dispached[wid]
        return None

    def getPanelInfo(self, wid):
        '''
        gets the auiPaneInfo object of the window that was dispatched with ID
        '''
        window = self.getPanel(wid)
        if window is not None:
            info = self.manager.GetPane(window)
            if info.IsOk():
                return info
        return None

    def getPanelID(self, window):
        ''' gets the id a panel was dispatched with '''
        if (window in self.IDs) and (self.IDs[window] is not None):
            return self.IDs[window]
        return None

    def getDispatched(self, wid):
        '''
        return true if there is a panel dispached under ID,
        otherwise returns false
        '''
        return (self.getPanel(wid) is not None)

    def showPanel(self, wid, show=True):
        '''
        if there is a window dispatched under id it calls show on the
        window auiPaneInfo object with the pased value
        which default to True. it then updates the AuiManager
        '''
        info = self.getPanelInfo(wid)
        if info is not None:
            info.Show(show)
            self.update()

    def getDockedCenterPanels(self):
        '''
        returns the number of center direction panels that are still docked
        '''
        i = 0
        for wid in self.dispached.keys():
            info = self.getPanelInfo(wid)
            if info.dock_direction_get() == aui.AUI_DOCK_CENTER:
                if not info.IsFloating():
                    i += 1
        return i
