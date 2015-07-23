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
        self.bindEvents()
        self.SetFocus()

    def bindEvents(self):
        self.Bind(wx.EVT_SET_FOCUS, self.OnFocus)
        self.Bind(wx.EVT_CHILD_FOCUS, self.OnFocus)

    def OnFocus(self, event):
        if "PanelManager" in Kernel.GlobalObjects:
            PM = Kernel.GlobalObjects["PanelManager"]
            if PM is not None:
                wid = PM.getPanelID(self)
                info = PM.getPanelInfo(wid)
                if info is not None:
                    if info.IsFloating():
                        PM.setLastActive("ShadowPanel")
                    else:
                        PM.setLastActive(wid)


class MainToolbar(aui.AuiToolBar):

    _arc_panel_info = {
        "Name": "MainToolbar",
        "Caption": "Main Tool Bar",
        "ToolbarP": None,
        "Top": None,
        "Row": 1,
        "CloseB": False
    }

    def __init__(self, parent):

        aui.AuiToolBar.__init__(
            self,
            parent,
            style=wx.TB_FLAT | wx.TB_HORIZONTAL
        )

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


class EditorToolbar(aui.AuiToolBar):

    _arc_panel_info = {
        "Name": "EditorToolbar",
        "Caption": "Editor Tool Bar",
        "ToolbarP": None,
        "Top": None,
        "Row": 1,
        "CloseB": False
    }

    def __init__(self, parent):

        aui.AuiToolBar.__init__(self, parent, style=wx.TB_FLAT | wx.TB_HORIZONTAL)

        self.parent = parent

        self.mgr = Kernel.GlobalObjects["PanelManager"]

        self.SetToolBitmapSize(wx.Size(16, 16))

        self.mapeditpanel = None
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
        mapeditbmp = IconManager.getBitmap("mapedit")
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
        self.mapeditid = wx.NewId()
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
        self.AddSimpleTool(
            self.mapeditid,
            "Map Editor",
            mapeditbmp,
            "Open the Map Editor"
        )
        self.AddSeparator()
        self.AddSimpleTool(
            self.actorsid,
            "Actors",
            actorsbmp,
            "Open the Actors Panel"
        )
        self.AddSimpleTool(
            self.classesid,
            "Classes",
            classesbmp,
            "Open the Classes Panel"
        )
        self.AddSimpleTool(
            self.skillsid,
            "Skills",
            skillsbmp,
            "Open the Skills Panel"
        )
        self.AddSimpleTool(
            self.statesid,
            "States",
            statesbmp,
            "Open the States Panel"
        )
        self.AddSeparator()
        self.AddSimpleTool(
            self.itemsid,
            "Items",
            itemsbmp,
            "Open the Items Panel"
        )
        self.AddSimpleTool(
            self.weaponsid,
            "Weapons",
            weaponsbmp,
            "Open the Weapons Panel"
        )
        self.AddSimpleTool(
            self.armorsid,
            "Armors",
            armorsbmp,
            "Open the Armors Panel"
        )
        self.AddSeparator()
        self.AddSimpleTool(
            self.enemiesid,
            "Enemies",
            enemiesbmp,
            "Open the Enemies Panel"
        )
        self.AddSimpleTool(
            self.troopsid,
            "Troops",
            troopsbmp,
            "Open the Troops Panel"
        )
        self.AddSeparator()
        self.AddSimpleTool(
            self.animationsid,
            "Animations",
            animationsbmp,
            "Open the Animations Panel"
        )
        self.AddSimpleTool(
            self.tilesetsid,
            "Tilesets",
            tilesetsbmp,
            "Open the Tilesets Panel"
        )

        self.AddSeparator()
        self.AddSimpleTool(
            self.commoneventsid,
            "Common Events",
            commoneventsbmp,
            "Open the Common Events Panel"
        )
        self.AddSimpleTool(
            self.systemid,
            "System",
            systembmp,
            "Open the System Panel"
        )
        self.AddSimpleTool(
            self.scriptid,
            "Scripts",
            scriptbmp,
            "Open the Scripts Panel"
        )

    def BindEvents(self):
        # self.Bind(wx.EVT_TOOL, self.OnNew, id=self.newid)
        tool_ids = [
            self.mapeditid,
            self.actorsid,
            self.classesid,
            self.skillsid,
            self.itemsid,
            self.weaponsid,
            self.armorsid,
            self.enemiesid,
            self.troopsid,
            self.statesid,
            self.animationsid,
            self.tilesetsid,
            self.commoneventsid,
            self.systemid,
            self.scriptid
        ]
        for tool_id in tool_ids:
            self.Bind(wx.EVT_TOOL, self.paneldispatch, id=tool_id)
            self.Bind(wx.EVT_UPDATE_UI, self.uiupdate, id=tool_id)

    def uiupdate(self, event):
        if ("ProjectOpen" in Kernel.GlobalObjects
                and (Kernel.GlobalObjects["ProjectOpen"] is True)):
            event.Enable(True)
        else:
            event.Enable(False)

    def paneldispatch(self, event):
        # TODO: refactor to get rid of the gigantic elif branch
        panel_infos = {
            self.mapeditid: ["mapeditpanel", "MapManagerPanel", "MapManager"],
            self.actorsid: ["actorspanel", "Actors_Panel", "ActorsPanel"],
            self.classesid: ["classespanel", "Classes_Panel", "ClassesPanel"],
            self.skillsid: ["skillspanel", "Skills_Panel", "SkillsPanel"],
            self.itemsid: ["itemspanel", "Items_Panel", "ItemsPanel"],
            self.weaponsid: ["weaponspanel", "Weapons_Panel", "WeaponsPanel"],
            self.armorsid: ["armorspanel", "Armors_Panel", "ArmorsPanel"],
            self.enemiesid: ["enemiespanel", "Enemies_Panel", "EnemiesPanel"],
            self.troopsid: ["troopspanel", "Troops_Panel", "TroopsPanel"],
            self.statesid: ["statespanel", "States_Panel", "StatesPanel"],
            self.animationsid: [
                "animationspanel",
                "Animations_Panel",
                "Animations"
            ],
            self.tilesetsid: ["tilesetspanel", "Tilesets_Panel", "Tilesets"],
            self.commoneventsid: [
                "commoneventspanel",
                "CommonEvents_Panel",
                "Common Events"
            ],
            self.systemid: ["systempanel", "System_Panel", "System"],
            self.scriptid: [
                "scriptpanel",
                "ScriptEditor_Panel",
                "Script Editor"
            ]
        }
        info = panel_infos[event.Id]
        panel = getattr(self, info[0])
        if panel:
            self.mgr.RequestUserAttention(panel)
        else:
            panel = self.mgr.dispatchPanel(info[1], info[2])
            setattr(self, info[0], panel)


class StartPanel(wx.Panel, PanelBase):

    _arc_panel_info_priority = ["CenterP"]
    _arc_panel_info = {
        #"CenterP": None,
        "Name": "Start Panel",
        "Caption": "Start Panel",
        "CaptionV": True,
        "CloseB": True,
        "Center": None,
        "MinimizeB": True,
        "Restore": None,
        "MaximizeB": True,
        "Movable": True,
        "Resizable": True,
        "NotebookD": True,
        "DestroyOC": True,
        "Floatable": True,
        "IconARCM": 'arca'
    }

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.bindPanelManager()


class ShadowPanel(wx.Panel, PanelBase):

    _arc_panel_info_priority = ["CenterP"]
    _arc_panel_info = {
        #"CenterP": None,
        "Name": "ShadowPanel",
        "CaptionV": False,
        "CloseB": False,
        "Center": None,
        "MinimizeB": False,
        "MaximizeB": False,
        "Movable": False,
        "Resizable": True,
        "NotebookD": True,
        "DestroyOC": True,
        "Floatable": False,
    }

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.bindPanelManager()
