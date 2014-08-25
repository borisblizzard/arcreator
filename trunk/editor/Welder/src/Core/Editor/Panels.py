'''
Panels 

Containes the panel classes dispatched by the Panel Manager
'''

import os
import sys
import copy

import wx

import wx.lib.agw.aui as aui

from Boot import WelderImport

Kernel = WelderImport('Kernel')
KM = Kernel.Manager

class PanelBase(object):

    def BindPanelManager(self):
        self.bindFocus()
        self.SetFocus()

    def bindFocus(self):
        self.Bind(wx.EVT_SET_FOCUS, self.OnFocus)
        self.Bind(wx.EVT_CHILD_FOCUS, self.OnFocus)


    def OnFocus(self, event):
        if Kernel.GlobalObjects.has_key("PanelManager"):
            PM = Kernel.GlobalObjects.get_value("PanelManager")
            if PM is not None:
                id = PM.getPanelID(self)
                info = PM.getPanelInfo(id)
                if info is not None:
                    if info.IsFloating():
                        PM.set_last_active("Shadow Panel")
                    else:
                        PM.set_last_active(id)

class MainToolbar(aui.AuiToolBar):

    _arc_panel_info_string = "Name Caption ToolbarP Top Row CloseB"
    _arc_panel_info_data = {"Name": "MainToolbar", "Caption": "Main Tool Bar",  "Row": 1, "CloseB": False, }

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
    _arc_panel_info_data = {"Name": "DatabaseToolbar", "Caption": "Database Tool Bar",  "Row": 1, "CloseB": False, }

    def __init__(self, parent):

        aui.AuiToolBar.__init__(self, parent, style=wx.TB_FLAT | wx.TB_HORIZONTAL)
        
        self.parent = parent

        self.mgr = Kernel.GlobalObjects.get_value("PanelManager")

        self.SetToolBitmapSize(wx.Size(16, 16))

        self.actorspanel = None
        self.classespanel = None
        self.skillspanel = None
        self.itemspanel = None
        self.weaponspanel = None
        self.armorspanel = None
        self.enemiespanel = None
        self.troopspanel = None
        self.statespanel = None
        self.animationspanel = None
        self.tilesetspanel = None
        self.commoneventspanel = None
        self.systempanel = None
        self.scriptpanel = None
        
        #build toolbar
        self.AddTools()
        self.Realize()
        self.BindEvents()

    def AddTools(self):
        IconManager = KM.get_component("IconManager").object
        #get bitmaps
        actorsbmp = IconManager.getBitmap("actorsicon")
        classesbmp = IconManager.getBitmap("classesicon")
        skillsbmp = IconManager.getBitmap("skillsicon")
        itemsbmp = IconManager.getBitmap("itemsicon")
        weaponsbmp = IconManager.getBitmap("weaponsicon")
        armorsbmp = IconManager.getBitmap("armorsicon")
        enemiesbmp = IconManager.getBitmap("enemiesicon")
        troopsbmp = IconManager.getBitmap("troopsicon")
        statesbmp = IconManager.getBitmap("statesicon")
        animationsbmp = IconManager.getBitmap("animationsicon")
        tilesetsbmp = IconManager.getBitmap("tilesetsicon")
        commoneventsbmp = IconManager.getBitmap("commoneventsicon")
        systembmp = IconManager.getBitmap("systemicon")
        scriptbmp = IconManager.getBitmap("script_icon")

        #set up ids
        self.actorsid = wx.NewId()
        self.classesid = wx.NewId()
        self.skillsid = wx.NewId()
        self.itemsid = wx.NewId()
        self.weaponsid = wx.NewId()
        self.armorsid = wx.NewId()
        self.enemiesid = wx.NewId()
        self.troopsid = wx.NewId()
        self.statesid = wx.NewId()
        self.animationsid = wx.NewId()
        self.tilesetsid = wx.NewId()
        self.commoneventsid = wx.NewId()
        self.systemid = wx.NewId()
        self.scriptid = wx.NewId()

        #add the tools
        self.AddSimpleTool(self.actorsid, "Actors", actorsbmp,
                           "Open the Actors Panel")
        self.AddSimpleTool(self.classesid, "Classes", classesbmp,
                           "Open the Classes Panel")
        self.AddSimpleTool(self.skillsid, "Skills", skillsbmp,
                           "Open the Skills Panel")
        self.AddSimpleTool(self.statesid, "States", statesbmp,
                           "Open the States Panel")
        self.AddSeparator()
        self.AddSimpleTool(self.itemsid, "Items", itemsbmp,
                           "Open the Items Panel")
        self.AddSimpleTool(self.weaponsid, "Weapons", weaponsbmp,
                           "Open the Weapons Panel")
        self.AddSimpleTool(self.armorsid, "Armors", armorsbmp,
                           "Open the Armors Panel")
        self.AddSeparator()
        self.AddSimpleTool(self.enemiesid, "Enemies", enemiesbmp,
                           "Open the Enemies Panel")
        self.AddSimpleTool(self.troopsid, "Troops", troopsbmp,
                           "Open the Troops Panel")
        
        self.AddSeparator()
        self.AddSimpleTool(self.animationsid, "Animations", animationsbmp,
                           "Open the Animations Panel")
        self.AddSimpleTool(self.tilesetsid, "Tilesets", tilesetsbmp,
                           "Open the Tilesets Panel")
        self.AddSeparator()
        self.AddSimpleTool(self.commoneventsid, "Common Events", commoneventsbmp,
                           "Open the Common Events Panel")
        self.AddSimpleTool(self.systemid, "System", systembmp,
                           "Open the System Panel")
        self.AddSimpleTool(self.scriptid, "Scripts", scriptbmp,
                           "Open the Scripts Panel")
    
    def BindEvents(self):
        #self.Bind(wx.EVT_TOOL, self.OnNew, id=self.newid)

        self.Bind(wx.EVT_TOOL, self.paneldispatch, id=self.actorsid)
        self.Bind(wx.EVT_TOOL, self.paneldispatch, id=self.classesid)
        self.Bind(wx.EVT_TOOL, self.paneldispatch, id=self.skillsid)
        self.Bind(wx.EVT_TOOL, self.paneldispatch, id=self.itemsid)
        self.Bind(wx.EVT_TOOL, self.paneldispatch, id=self.weaponsid)
        self.Bind(wx.EVT_TOOL, self.paneldispatch, id=self.armorsid)
        self.Bind(wx.EVT_TOOL, self.paneldispatch, id=self.enemiesid)
        self.Bind(wx.EVT_TOOL, self.paneldispatch, id=self.troopsid)
        self.Bind(wx.EVT_TOOL, self.paneldispatch, id=self.statesid)
        self.Bind(wx.EVT_TOOL, self.paneldispatch, id=self.animationsid)
        self.Bind(wx.EVT_TOOL, self.paneldispatch, id=self.tilesetsid)
        self.Bind(wx.EVT_TOOL, self.paneldispatch, id=self.commoneventsid)
        self.Bind(wx.EVT_TOOL, self.paneldispatch, id=self.systemid)
        self.Bind(wx.EVT_TOOL, self.paneldispatch, id=self.scriptid)

        self.Bind(wx.EVT_UPDATE_UI, self.uiupdate, id=self.actorsid)
        self.Bind(wx.EVT_UPDATE_UI, self.uiupdate, id=self.classesid)
        self.Bind(wx.EVT_UPDATE_UI, self.uiupdate, id=self.skillsid)
        self.Bind(wx.EVT_UPDATE_UI, self.uiupdate, id=self.itemsid)
        self.Bind(wx.EVT_UPDATE_UI, self.uiupdate, id=self.weaponsid)
        self.Bind(wx.EVT_UPDATE_UI, self.uiupdate, id=self.armorsid)
        self.Bind(wx.EVT_UPDATE_UI, self.uiupdate, id=self.enemiesid)
        self.Bind(wx.EVT_UPDATE_UI, self.uiupdate, id=self.troopsid)
        self.Bind(wx.EVT_UPDATE_UI, self.uiupdate, id=self.statesid)
        self.Bind(wx.EVT_UPDATE_UI, self.uiupdate, id=self.animationsid)
        self.Bind(wx.EVT_UPDATE_UI, self.uiupdate, id=self.tilesetsid)
        self.Bind(wx.EVT_UPDATE_UI, self.uiupdate, id=self.commoneventsid)
        self.Bind(wx.EVT_UPDATE_UI, self.uiupdate, id=self.systemid)
        self.Bind(wx.EVT_UPDATE_UI, self.uiupdate, id=self.scriptid)

    def uiupdate(self, event):
        if Kernel.GlobalObjects.has_key("ProjectOpen") and (Kernel.GlobalObjects.get_value("ProjectOpen") == True):
            event.Enable(True)
        else:
            event.Enable(False)

    def paneldispatch(self, event):
        broken = [self.troopsid, self.animationsid, self.tilesetsid, self.commoneventsid, self.systemid]
        if event.Id in broken:
            KM.raise_event("CoreEventBrokenDatabasePanel")
        if event.Id == self.actorsid:
            if self.actorspanel:
                self.mgr.RequestUserAttention(self.actorspanel) 
            else:
                self.actorspanel = self.mgr.dispatch_panel("MainActorsPanel", "Main Actors Panel") 
        elif event.Id == self.classesid:
            if self.classespanel:
                self.mgr.RequestUserAttention(self.classespanel) 
            else:
                self.classespanel = self.mgr.dispatch_panel("MainClassesPanel", "Main Classes Panel")
        elif event.Id == self.skillsid:
            if self.skillspanel:
                self.mgr.RequestUserAttention(self.skillspanel) 
            else:
                self.skillspanel = self.mgr.dispatch_panel("MainSkillsPanel", "Main Skills Panel")
        elif event.Id == self.itemsid:
            if self.itemspanel:
                self.mgr.RequestUserAttention(self.itemspanel) 
            else:
                self.itemspanel = self.mgr.dispatch_panel("MainItemsPanel", "Main Items Panel")
        elif event.Id == self.weaponsid:
            if self.weaponspanel:
                self.mgr.RequestUserAttention(self.weaponspanel) 
            else:
                self.weaponspanel = self.mgr.dispatch_panel("MainWeaponsPanel", "Main Weapons Panel")
        elif event.Id == self.armorsid:
            if self.armorspanel:
                self.mgr.RequestUserAttention(self.armorspanel) 
            else:
                self.armorspanel = self.mgr.dispatch_panel("MainArmorsPanel", "Main Armors Panel")
        elif event.Id == self.enemiesid:
            if self.enemiespanel:
                self.mgr.RequestUserAttention(self.enemiespanel) 
            else:
                self.enemiespanel = self.mgr.dispatch_panel("MainEnemiesPanel", "Main Enemies Panel")
        elif event.Id == self.troopsid:
            if self.troopspanel:
                self.mgr.RequestUserAttention(self.troopspanel) 
            else:
                self.troopspanel = self.mgr.dispatch_panel("MainTroopsPanel", "Main Troops Panel")
        elif event.Id == self.statesid:
            if self.statespanel:
                self.mgr.RequestUserAttention(self.statespanel) 
            else:
                self.statespanel = self.mgr.dispatch_panel("MainStatesPanel", "Main States Panel")
        elif event.Id == self.animationsid:
            if self.animationspanel:
                self.mgr.RequestUserAttention(self.animationspanel) 
            else:
                self.animationspanel = self.mgr.dispatch_panel("MainAnimationsPanel", "Main Animations Panel")
        elif event.Id == self.tilesetsid:
            if self.tilesetspanel:
                self.mgr.RequestUserAttention(self.tilesetspanel) 
            else:
                self.tilesetspanel = self.mgr.dispatch_panel("MainTilesetsPanel", "Main Tilesets Panel")
        elif event.Id == self.commoneventsid:
            if self.commoneventspanel:
                self.mgr.RequestUserAttention(self.commoneventspanel) 
            else:
                self.commoneventspanel = self.mgr.dispatch_panel("MainCommonEventsPanel", "Main Common Events Panel")
        elif event.Id == self.systemid:
            if self.systempanel:
                self.mgr.RequestUserAttention(self.systempanel) 
            else:
                self.systempanel = self.mgr.dispatch_panel("MainSystemPanel", "Main System Panel")
        elif event.Id == self.scriptid:
            if self.scriptpanel:
                self.mgr.RequestUserAttention(self.scriptpanel) 
            else:
                self.scriptpanel = self.mgr.dispatch_panel("MainScriptEditorPanel", "Main Script Editor Panel")
            

class StartPanel(wx.Panel, PanelBase):

    _arc_panel_info_string = "Name Caption Center CloseB CaptionV BestS MinimizeM MinimizeB MaximizeB Floatable Resizable Snappable NotebookD Movable DestroyOC"
    _arc_panel_info_data = {"Name": "Start Panel", "Caption": "Start Panel", "CaptionV": True, "BestS": (32 * 24, 32 * 18), "MinimizeM": ["POS_SMART", "CAPT_SMART",], 
                            "MinimizeB": True, "CloseB": True}
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.BindPanelManager()


class ShadowPanel(wx.Panel, PanelBase):

    _arc_panel_info_string = "Name Caption CloseB CaptionV BestS MinimizeB Floatable Resizable Snappable NotebookD Movable DestroyOC"
    _arc_panel_info_data = {"Name": "Shadow Panel", "Caption": "Shadow Panel", "CaptionV": False, "BestS": (1000 - 8, 500), "MinimizeB": False, "CloseB": False, "Floatable" : False,}
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.BindPanelManager()