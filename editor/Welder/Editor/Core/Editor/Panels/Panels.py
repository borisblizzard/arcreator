'''
Panels 

Containes the panel classes dispatched by the Panel Manager
'''

import wx

import wx.lib.agw.aui as aui

import Kernel

from PyitectConsumes import IconManager


class PanelBase(object):

    def bindPanelManager(self):
        self.bindFocus()
        self.SetFocus()

    def bindFocus(self):
        self.Bind(wx.EVT_SET_FOCUS, self.OnFocus)
        self.Bind(wx.EVT_CHILD_FOCUS, self.OnFocus)

    def OnFocus(self, event):
        if "PanelManager" in Kernel.GlobalObjects:
            PM = Kernel.GlobalObjects["PanelManager"]
            if PM is not None:
                id = PM.getPanelID(self)
                info = PM.getPanelInfo(id)
                if info is not None:
                    if info.IsFloating():
                        PM.setLastActive("Shadow Panel")
                    else:
                        PM.setLastActive(id)


class MainToolbar(aui.AuiToolBar):

    _arc_panel_info_string = "Name Caption ToolbarP Top Row CloseB"
    _arc_panel_info_data = {"Name": "MainToolbar", "Caption": "Main Tool Bar", "Row": 1, "CloseB": False, }

    def __init__(self, parent):

        aui.AuiToolBar.__init__(self, parent, style=wx.TB_FLAT | wx.TB_HORIZONTAL)

        self.parent = parent

        self.SetToolBitmapSize(wx.Size(16, 16))

        # build toolbar
        self.AddTools()
        self.Realize()
        self.BindEvents()

    def AddTools(self):

        # get bitmaps
        newbmp = IconManager.getBitmap("new")
        openbmp = IconManager.getBitmap("open")
        savebmp = IconManager.getBitmap("save")
        undobmp = IconManager.getBitmap("undo")
        redobmp = IconManager.getBitmap("redo")
        copybmp = IconManager.getBitmap("copy")
        cutbmp = IconManager.getBitmap("cut")
        pastebmp = IconManager.getBitmap("paste")
        # set up ids
        self.newid = wx.NewId()
        self.openid = wx.NewId()
        self.saveid = wx.NewId()
        self.redoid = wx.NewId()
        self.undoid = wx.NewId()
        self.copyid = wx.NewId()
        self.cutid = wx.NewId()
        self.pasteid = wx.NewId()
        # add the tools
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
        newproject = Kernel.System.load("NewProjectHandler")
        newproject(self.parent)
        Kernel.GlobalObjects["FileHistory"].Save(Kernel.GlobalObjects["WX_config"])
        Kernel.GlobalObjects["WX_config"].Flush()

    def OnOpen(self, event):
        openproject = Kernel.System.load("OpenProjectHandler")
        openproject(self.parent, Kernel.GlobalObjects["FileHistory"])
        Kernel.GlobalObjects["FileHistory"].Save(Kernel.GlobalObjects["WX_config"])
        Kernel.GlobalObjects["WX_config"].Flush()

    def OnSave(self, event):
        saveproject = Kernel.System.load("SaveProjectHandler")
        saveproject()
        Kernel.GlobalObjects["FileHistory"].Save(Kernel.GlobalObjects["WX_config"])
        Kernel.GlobalObjects["WX_config"].Flush()

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
        if "ProjectOpen" in Kernel.GlobalObjects and (Kernel.GlobalObjects["ProjectOpen"] is True):
            event.Enable(True)
        else:
            event.Enable(False)


class DatabaseToolbar(aui.AuiToolBar):

    _arc_panel_info_string = "Name Caption ToolbarP Top Row CloseB"
    _arc_panel_info_data = {"Name": "DatabaseToolbar", "Caption": "Database Tool Bar", "Row": 1, "CloseB": False, }

    def __init__(self, parent):

        aui.AuiToolBar.__init__(self, parent, style=wx.TB_FLAT | wx.TB_HORIZONTAL)

        self.parent = parent

        self.mgr = Kernel.GlobalObjects["PanelManager"]

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

        # build toolbar
        self.AddTools()
        self.Realize()
        self.BindEvents()

    def AddTools(self):
        # get bitmaps
        actorsbmp = IconManager.getBitmap("actors")
        classesbmp = IconManager.getBitmap("classes")
        skillsbmp = IconManager.getBitmap("skills")
        itemsbmp = IconManager.getBitmap("items")
        weaponsbmp = IconManager.getBitmap("weapons")
        armorsbmp = IconManager.getBitmap("armors")
        enemiesbmp = IconManager.getBitmap("enemies")
        troopsbmp = IconManager.getBitmap("troops")
        statesbmp = IconManager.getBitmap("states")
        animationsbmp = IconManager.getBitmap("animations")
        tilesetsbmp = IconManager.getBitmap("tilesets")
        commoneventsbmp = IconManager.getBitmap("commonEvents")
        systembmp = IconManager.getBitmap("system")
        scriptbmp = IconManager.getBitmap("script")

        # set up ids
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

        # add the tools
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
        # self.Bind(wx.EVT_TOOL, self.OnNew, id=self.newid)

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
        if "ProjectOpen" in Kernel.GlobalObjects and (Kernel.GlobalObjects["ProjectOpen"] is True):
            event.Enable(True)
        else:
            event.Enable(False)

    def paneldispatch(self, event):
        broken = [self.troopsid, self.animationsid, self.tilesetsid, self.commoneventsid, self.systemid]
        # TODO: refactor to get rid of the gigantic elif branch
        if event.Id in broken:
            Kernel.System.fire_event("BrokenDatabasePanel")
        if event.Id == self.actorsid:
            if self.actorspanel:
                self.mgr.RequestUserAttention(self.actorspanel)
            else:
                self.actorspanel = self.mgr.dispatchPanel("Actors_Panel", "Actors")
        elif event.Id == self.classesid:
            if self.classespanel:
                self.mgr.RequestUserAttention(self.classespanel)
            else:
                self.classespanel = self.mgr.dispatchPanel("Classes_Panel", "Classes")
        elif event.Id == self.skillsid:
            if self.skillspanel:
                self.mgr.RequestUserAttention(self.skillspanel)
            else:
                self.skillspanel = self.mgr.dispatchPanel("Skills_Panel", "Skills")
        elif event.Id == self.itemsid:
            if self.itemspanel:
                self.mgr.RequestUserAttention(self.itemspanel)
            else:
                self.itemspanel = self.mgr.dispatchPanel("Items_Panel", "Items")
        elif event.Id == self.weaponsid:
            if self.weaponspanel:
                self.mgr.RequestUserAttention(self.weaponspanel)
            else:
                self.weaponspanel = self.mgr.dispatchPanel("Weapons_Panel", "Weapons")
        elif event.Id == self.armorsid:
            if self.armorspanel:
                self.mgr.RequestUserAttention(self.armorspanel)
            else:
                self.armorspanel = self.mgr.dispatchPanel("Armors_Panel", "Armors")
        elif event.Id == self.enemiesid:
            if self.enemiespanel:
                self.mgr.RequestUserAttention(self.enemiespanel)
            else:
                self.enemiespanel = self.mgr.dispatchPanel("Enemies_Panel", "Enemies")
        elif event.Id == self.troopsid:
            if self.troopspanel:
                self.mgr.RequestUserAttention(self.troopspanel)
            else:
                self.troopspanel = self.mgr.dispatchPanel("Troops_Panel", "Troops")
        elif event.Id == self.statesid:
            if self.statespanel:
                self.mgr.RequestUserAttention(self.statespanel)
            else:
                self.statespanel = self.mgr.dispatchPanel("States_Panel", "States")
        elif event.Id == self.animationsid:
            if self.animationspanel:
                self.mgr.RequestUserAttention(self.animationspanel)
            else:
                self.animationspanel = self.mgr.dispatchPanel("Animations_Panel", "Animations")
        elif event.Id == self.tilesetsid:
            if self.tilesetspanel:
                self.mgr.RequestUserAttention(self.tilesetspanel)
            else:
                self.tilesetspanel = self.mgr.dispatchPanel("Tilesets_Panel", "Tilesets")
        elif event.Id == self.commoneventsid:
            if self.commoneventspanel:
                self.mgr.RequestUserAttention(self.commoneventspanel)
            else:
                self.commoneventspanel = self.mgr.dispatchPanel("CommonEvents_Panel", "Common Events")
        elif event.Id == self.systemid:
            if self.systempanel:
                self.mgr.RequestUserAttention(self.systempanel)
            else:
                self.systempanel = self.mgr.dispatchPanel("System_Panel", "System")
        elif event.Id == self.scriptid:
            if self.scriptpanel:
                self.mgr.RequestUserAttention(self.scriptpanel)
            else:
                self.scriptpanel = self.mgr.dispatchPanel("ScriptEditor_Panel", "Script Editor")


class StartPanel(wx.Panel, PanelBase):

    _arc_panel_info_string = "Name Caption CloseB Center Fixed MinimizeB Maximize MaximizeB Resizable NotebookD DestroyOC Floatable Movable"
    _arc_panel_info_data = {"Name": "Start Panel", "Caption": "Start Panel", "CaptionV": True, "Movable": False,
                            "MinimizeB": False, "MaximizeB": False, "CloseB": False, "Floatable": False}

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.bindPanelManager()


# class ShadowPanel(wx.Panel, PanelBase):

#     _arc_panel_info_string = "Name Caption CloseB CaptionV BestS MinimizeB Floatable Resizable Snappable NotebookD Movable DestroyOC"
#     _arc_panel_info_data = {"Name": "Shadow Panel", "Caption": "Shadow Panel", "CaptionV": False, "BestS": (1000 - 8, 500), "MinimizeB": False, "CloseB": False, "Floatable" : False,}

#     def __init__(self, parent):
#         wx.Panel.__init__(self, parent)
#         self.bindPanelManager()