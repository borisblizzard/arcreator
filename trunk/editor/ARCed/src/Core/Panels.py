import os
import sys
import copy

import wx

import wx.lib.agw.aui as aui
from wx.lib.agw.aui import aui_switcherdialog as ASD

import Kernel
from Kernel import Manager as KM

class MainToolbar(aui.AuiToolBar):

    _arc_panel_info_string = "Name Caption ToolbarP Top Row CloseB"
    _arc_panel_info_data = {"Name": "Toolbar", "Caption": "Main Tool Bar",  "Row": 1, "CloseB": False, }

    def __init__(self, parent):

        aui.AuiToolBar.__init__(self, parent, style=wx.TB_FLAT | wx.TB_HORIZONTAL)
        
        self.parent = parent

        self.SetToolBitmapSize(wx.Size(16, 16))

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
        self.Realize()

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
        Kernel.GlobalObjects.get_value("FileHistory").Save(Kernel.GlobalObjects.get_value("programconfig"))

    def OnOpen(self, event):
        openproject = KM.get_component("OpenProjectHandler").object
        openproject(self.parent, Kernel.GlobalObjects.get_value("FileHistory"))
        Kernel.GlobalObjects.get_value("FileHistory").Save(Kernel.GlobalObjects.get_value("programconfig"))

    def OnSave(self, event):
        saveproject = KM.get_component("SaveProjectHandler").object
        saveproject()
        Kernel.GlobalObjects.get_value("FileHistory").Save(Kernel.GlobalObjects.get_value("programconfig"))

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

class StartPanel(wx.Panel):

    _arc_panel_info_string = "Name Caption CenterP CloseB CaptionV BestS MinimizeM Layer MinimizeB"
    _arc_panel_info_data = {"Name": "Start Panel", "Caption": "Start Panel", "BestS": (32 * 24, 32 * 18), "MinimizeM": ["POS_SMART", "CAPT_SMART",], "Layer": 1, "MinimizeB": True, "CloseB": True,}
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)

class TilesetPanel(wx.ScrolledWindow):
    
    _arc_panel_info_string = "Name Caption Left CloseB BestS MinimizeM Layer Row Pos MinimizeB"
    _arc_panel_info_data = {"Name": "Tileset", "Caption": "Tileset", "CloseB": False, "BestS": (32 * 8, 32 * 12), "MinimizeM": ["POS_SMART", "CAPT_SMART",], "Layer": 1, "Row": 1, "Pos": 1, "MinimizeB": True,}

    def __init__(self, parent):
        wx.ScrolledWindow.__init__(self, parent, wx.ID_ANY)
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.SetScrollbars(32, 32, 8, 50)

class MapTreePanel(wx.Panel):

    _arc_panel_info_string = "Name Caption Left CloseB BestS MinimizeM Layer Row Pos MinimizeB"
    _arc_panel_info_data = {"Name": "Maps", "Caption": "Maps", "CloseB": False, "BestS": (32 * 8, 32 * 4), "MinimizeM": ["POS_SMART", "CAPT_SMART",], "Layer": 1, "Row": 1, "Pos": 1, "MinimizeB": True,}

    def __init__(self, parent, mapEditerPanel=None):
        wx.Panel.__init__(self, parent)

        self.mapEditerPanel = mapEditerPanel

        #set up Sizer
        box = wx.BoxSizer(wx.VERTICAL)
        #set up tree
        mapTreeCtrl = KM.get_component("MapTreeCtrl").object
        self.treectrl =  mapTreeCtrl(self, -1, wx.Point(0, 0),
                                        wx.Size(160, 250),
                                        wx.TR_DEFAULT_STYLE | wx.NO_BORDER)
        #add ctrls to sizer
        box.Add(self.treectrl, 1, wx.ALL | wx.EXPAND)
        #set sizer
        self.SetSizerAndFit(box)

        #bind events
        self.treectrl.Bind(wx.EVT_LEFT_DCLICK, self.TreeLeftDClick)

    def TreeLeftDClick(self, event):
        pt = event.GetPosition();
        item, flags = self.treectrl.HitTest(pt)
        if item:
            data = self.treectrl.GetItemData(item).GetData()
            if data:
                map_id, name = data
                self.mapEditerPanel.add_page(map_id, name)
        event.Skip()