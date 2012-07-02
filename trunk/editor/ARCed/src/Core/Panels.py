'''
Panels 

Containes the panel classes dispatched by the Panel Manager
'''

import os
import sys
import copy

import wx

import wx.lib.agw.aui as aui
from wx.lib.agw.aui import aui_switcherdialog as ASD

import Kernel
from Kernel import Manager as KM

class PanelBase(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)

        self.bindFocus()
        self.SetFocus()

    def bindFocus(self):
        self.Bind(wx.EVT_SET_FOCUS, self.OnFocus)
        self.Bind(wx.EVT_CHILD_FOCUS, self.OnFocus)


    def OnFocus(self, event):
        if Kernel.GlobalObjects.has_key("PanelManager"):
            PM = Kernel.GlobalObjects.get_value("PanelManager")
            id = PM.getPanelID(self)
            info = PM.getPanelInfo(id)
            if info is not None:
                if info.IsFloating():
                    PM.set_last_active("Shadow Panel")
                else:
                    PM.set_last_active(id)

class MainToolbar(aui.AuiToolBar):

    _arc_panel_info_string = "Name Caption ToolbarP Top Row CloseB"
    _arc_panel_info_data = {"Name": "Toolbar", "Caption": "Main Tool Bar",  "Row": 1, "CloseB": False, }

    def __init__(self, parent):

        aui.AuiToolBar.__init__(self, parent, style=wx.TB_FLAT | wx.TB_HORIZONTAL)
        
        self.parent = parent

        self.SetToolBitmapSize(wx.Size(16, 16))

       
        #build toolbar
        self.AddTools()
        self.Realize()
        self.BindEvents()

    def AddTools(self):
        IconManager = KM.get_component("IconManager").object
        #get bitmaps
        newbmp = IconManager.getBitmap("newicon")
        openbmp = IconManager.getBitmap("openicon")
        savebmp = IconManager.getBitmap("saveicon")
        undobmp = IconManager.getBitmap("undoicon")
        redobmp = IconManager.getBitmap("redoicon")
        copybmp = IconManager.getBitmap("copyicon")
        cutbmp = IconManager.getBitmap("cuticon")
        pastebmp = IconManager.getBitmap("pasteicon")
        #set up ids
        self.newid = wx.NewId()
        self.openid = wx.NewId()
        self.saveid = wx.NewId()
        self.redoid = wx.NewId()
        self.undoid = wx.NewId()
        self.copyid = wx.NewId()
        self.cutid = wx.NewId()
        self.pasteid = wx.NewId()
        #add the tools
        self.AddSimpleTool(self.newid, "New", newbmp,
                           "Create a new project")
        self.AddSimpleTool(self.openid, "Open", openbmp,
                           "Open a ARC Project")
        self.AddSimpleTool(self.saveid, "Save", savebmp,
                           "Save the current Project")
        self.AddSeparator()
        self.AddSimpleTool(self.undoid, "Undo", undobmp,
                                   "Undo last action")
        self.AddSimpleTool(self.redoid, "Redo", redobmp,
                                   "Redo last action")
        self.AddSeparator()
        self.AddSimpleTool(self.cutid, "Cut", cutbmp,
                           "Cut selection and copy to the clipboard")
        self.AddSimpleTool(self.copyid, "Copy", copybmp,
                           "Copy selection to the clipboard")
        self.AddSimpleTool(self.pasteid, "Paste", pastebmp,
                           "Paste data from the clipboard")

    def BindEvents(self):

        self.Bind(wx.EVT_TOOL, self.OnNew, id=self.newid)
        self.Bind(wx.EVT_TOOL, self.OnOpen, id=self.openid)
        self.Bind(wx.EVT_TOOL, self.OnSave, id=self.saveid)
        self.Bind(wx.EVT_UPDATE_UI, self.uiupdate, id=self.saveid)

        self.Bind(wx.EVT_TOOL, self.OnUndo, id=self.undoid)
        self.Bind(wx.EVT_TOOL, self.OnRedo, id=self.redoid)

        self.Bind(wx.EVT_TOOL, self.OnCut, id=self.cutid)
        self.Bind(wx.EVT_TOOL, self.OnCopy, id=self.copyid)
        self.Bind(wx.EVT_TOOL, self.OnPaste, id=self.pasteid)

    def OnNew(self, event):
        newproject = KM.get_component("NewProjectHandler").object
        newproject(self.parent)
        Kernel.GlobalObjects.get_value("FileHistory").Save(Kernel.GlobalObjects.get_value("WX_config"))
        Kernel.GlobalObjects.get_value("WX_config").Flush()

    def OnOpen(self, event):
        openproject = KM.get_component("OpenProjectHandler").object
        openproject(self.parent, Kernel.GlobalObjects.get_value("FileHistory"))
        Kernel.GlobalObjects.get_value("FileHistory").Save(Kernel.GlobalObjects.get_value("WX_config"))
        Kernel.GlobalObjects.get_value("WX_config").Flush()

    def OnSave(self, event):
        saveproject = KM.get_component("SaveProjectHandler").object
        saveproject()
        Kernel.GlobalObjects.get_value("FileHistory").Save(Kernel.GlobalObjects.get_value("WX_config"))
        Kernel.GlobalObjects.get_value("WX_config").Flush()

    def OnUndo(self, event):
        pass

    def OnRedo(self, event):
        pass

    def OnCopy(self, event):
        pass

    def OnCut(self, event):
        pass

    def OnPaste(self, event):
        pass

    def uiupdate(self, event):
        if Kernel.GlobalObjects.has_key("ProjectOpen") and (Kernel.GlobalObjects.get_value("ProjectOpen") == True):
            event.Enable(True)
        else:
            event.Enable(False)

class DatabaseToolbar(aui.AuiToolBar):

    _arc_panel_info_string = "Name Caption ToolbarP Top Row CloseB"
    _arc_panel_info_data = {"Name": "Toolbar", "Caption": "Database Tool Bar",  "Row": 1, "CloseB": False, }

    def __init__(self, parent):

        aui.AuiToolBar.__init__(self, parent, style=wx.TB_FLAT | wx.TB_HORIZONTAL)
        
        self.parent = parent

        self.SetToolBitmapSize(wx.Size(16, 16))

        IconManager = KM.get_component("IconManager").object
        #get bitmaps
        #newbmp = IconManager.getBitmap("newicon")

        #set up ids
        #self.newid = wx.NewId()
        #build toolbar
        self.AddTools()
        self.Realize()
        self.BindEvents()

    def AddTools(self):
        #add the tools
        #self.AddSimpleTool(self.newid, "New", newbmp,
        #                   "Create a new project")

        #self.AddSeparator()
        pass       

    def BindEvents(self):
        #self.Bind(wx.EVT_TOOL, self.OnNew, id=self.newid)

        self.Bind(wx.EVT_UPDATE_UI, self.uiupdate, id=self.saveid)

    def uiupdate(self, event):
        if Kernel.GlobalObjects.has_key("ProjectOpen") and (Kernel.GlobalObjects.get_value("ProjectOpen") == True):
            event.Enable(True)
        else:
            event.Enable(False)

class StartPanel(PanelBase):

    _arc_panel_info_string = "Name Caption Center CloseB CaptionV BestS MinimizeM MinimizeB MaximizeB Floatable Resizable Snappable NotebookD Movable"
    _arc_panel_info_data = {"Name": "Start Panel", "Caption": "Start Panel", "CaptionV": True, "BestS": (32 * 24, 32 * 18), "MinimizeM": ["POS_SMART", "CAPT_SMART",], 
                            "MinimizeB": True, "CloseB": True}
    
    def __init__(self, parent):
        PanelBase.__init__(self, parent)


class ShadowPanel(PanelBase):

    _arc_panel_info_string = "Name Caption CloseB CaptionV BestS MinimizeB Floatable Resizable Snappable NotebookD Movable"
    _arc_panel_info_data = {"Name": "Shadow Panel", "Caption": "Shadow Panel", "CaptionV": False, "BestS": (1000 - 8, 500), "MinimizeB": False, "CloseB": False, "Floatable" : False,}
    
    def __init__(self, parent):
        PanelBase.__init__(self, parent)