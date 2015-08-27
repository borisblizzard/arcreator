# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Jun 17 2015)
# http://www.wxformbuilder.org/
##
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.grid
import wx.dataview

from . import Extras

import gettext
_ = gettext.gettext

###########################################################################
# Class Actors_Panel_Template
###########################################################################


class Actors_Panel_Template (wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(
            742, 559), style=wx.CLIP_CHILDREN | wx.TAB_TRAVERSAL)

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        ActorListSizer = wx.BoxSizer(wx.VERTICAL)

        self.bitmapActors = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(
            150, 26), wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)
        self.bitmapActors.SetMinSize(wx.Size(150, 26))
        self.bitmapActors.SetMaxSize(wx.Size(150, 26))

        ActorListSizer.Add(self.bitmapActors, 0, wx.ALL | wx.EXPAND, 5)

        listBoxActorsChoices = []
        self.listBoxActors = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(
            184, -1), listBoxActorsChoices, wx.LB_SINGLE | wx.CLIP_CHILDREN)
        self.listBoxActors.SetHelpText(_("TEST HELP STRING"))

        ActorListSizer.Add(
            self.listBoxActors, 1, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        self.buttonMaximum = wx.Button(self, wx.ID_ANY, _(
            "Change Maximum..."), wx.DefaultPosition, wx.Size(150, -1), 0)
        ActorListSizer.Add(self.buttonMaximum, 0, wx.ALL | wx.EXPAND, 5)

        MainSizer.Add(ActorListSizer, 0, wx.EXPAND, 5)

        staticSizerActors = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.HORIZONTAL)

        sizer1 = wx.BoxSizer(wx.HORIZONTAL)

        sizer3 = wx.BoxSizer(wx.VERTICAL)

        self.labelName = wx.StaticText(staticSizerActors.GetStaticBox(), wx.ID_ANY, _(
            "Name:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelName.Wrap(-1)
        sizer3.Add(self.labelName, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlName = wx.TextCtrl(staticSizerActors.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlName.SetMaxLength(0)
        sizer3.Add(
            self.textCtrlName, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelClass = wx.StaticText(staticSizerActors.GetStaticBox(), wx.ID_ANY, _(
            "Class:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelClass.Wrap(-1)
        sizer3.Add(self.labelClass, 0, wx.ALL, 5)

        comboBoxClassChoices = []
        self.comboBoxClass = wx.Choice(staticSizerActors.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxClassChoices, 0)
        self.comboBoxClass.SetSelection(-1)
        sizer3.Add(
            self.comboBoxClass, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelInitialLevel = wx.StaticText(staticSizerActors.GetStaticBox(
        ), wx.ID_ANY, _("Initial Level:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelInitialLevel.Wrap(-1)
        sizer4.Add(self.labelInitialLevel, 1, wx.EXPAND | wx.ALL, 5)

        self.labelFinalLevel = wx.StaticText(staticSizerActors.GetStaticBox(
        ), wx.ID_ANY, _("Final Level:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelFinalLevel.Wrap(-1)
        sizer4.Add(self.labelFinalLevel, 1, wx.ALL | wx.EXPAND, 5)

        sizer3.Add(sizer4, 0, wx.EXPAND, 5)

        sizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.spinCtrlInitialLevel = wx.SpinCtrl(staticSizerActors.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS | wx.SP_WRAP, 0, 65535, 1)
        sizer5.Add(self.spinCtrlInitialLevel, 1, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.spinCtrlFinalLevel = wx.SpinCtrl(staticSizerActors.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS | wx.SP_WRAP, 0, 999, 99)
        sizer5.Add(self.spinCtrlFinalLevel, 1, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizer3.Add(sizer5, 0, wx.EXPAND, 5)

        self.labelExpCurve = wx.StaticText(staticSizerActors.GetStaticBox(), wx.ID_ANY, _(
            "Experience Curve:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelExpCurve.Wrap(-1)
        sizer3.Add(self.labelExpCurve, 0, wx.ALL, 5)

        self.comboBoxExpCurve = wx.adv.BitmapComboBox(staticSizerActors.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, "", wx.CB_READONLY | wx.CLIP_CHILDREN)
        sizer3.Add(self.comboBoxExpCurve, 0, wx.EXPAND |
                   wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelGraphics = wx.StaticText(staticSizerActors.GetStaticBox(), wx.ID_ANY, _(
            "Actor Graphics:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelGraphics.Wrap(-1)
        sizer3.Add(self.labelGraphics, 0, wx.ALL | wx.EXPAND, 5)

        self.splitterGraphics = wx.SplitterWindow(staticSizerActors.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_BORDER)
        self.splitterGraphics.SetSashGravity(0.5)
        self.splitterGraphics.Bind(wx.EVT_IDLE, self.splitterGraphicsOnIdle)
        self.splitterGraphics.SetMinimumPaneSize(1)

        self.panelCharacter = wx.Panel(
            self.splitterGraphics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        sizerCharacter = wx.BoxSizer(wx.VERTICAL)

        from .Extras import EditorGLPanel
        parent, id = self.panelCharacter, wx.ID_ANY
        self.glCanvasCharacter = EditorGLPanel(parent, id, 4, 4, (0, 0,), 1)
        self.glCanvasCharacter.SetHelpText(
            _("The graphic used for the actor on the map. Double-click to edit."))

        sizerCharacter.Add(self.glCanvasCharacter, 1, wx.ALL | wx.EXPAND, 0)

        self.panelCharacter.SetSizer(sizerCharacter)
        self.panelCharacter.Layout()
        sizerCharacter.Fit(self.panelCharacter)
        self.panelBattler = wx.Panel(
            self.splitterGraphics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        sizerBattler = wx.BoxSizer(wx.VERTICAL)

        from .Extras import EditorGLPanel
        parent, id = self.panelBattler, wx.ID_ANY
        self.glCanvasBattler = EditorGLPanel(parent, id, 1, 1, (0, 0,), 1)
        self.glCanvasBattler.SetHelpText(
            _("The graphic used for the actor in battle. Double-click to edit."))

        sizerBattler.Add(self.glCanvasBattler, 1, wx.ALL | wx.EXPAND, 0)

        self.panelBattler.SetSizer(sizerBattler)
        self.panelBattler.Layout()
        sizerBattler.Fit(self.panelBattler)
        self.splitterGraphics.SplitHorizontally(
            self.panelCharacter, self.panelBattler, 0)
        sizer3.Add(self.splitterGraphics, 1, wx.EXPAND, 5)

        sizer1.Add(sizer3, 25, wx.EXPAND, 5)

        staticSizerActors.Add(sizer1, 35, wx.EXPAND, 5)

        sizer2 = wx.BoxSizer(wx.VERTICAL)

        sizerParameters = wx.BoxSizer(wx.VERTICAL)

        self.noteBookActorParameters = wx.Notebook(staticSizerActors.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 | wx.CLIP_CHILDREN | wx.TAB_TRAVERSAL)
        self.pageParameters = wx.Panel(
            self.noteBookActorParameters, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CLIP_CHILDREN | wx.TAB_TRAVERSAL)
        MainSizerParamter = wx.BoxSizer(wx.VERTICAL)

        sizerConrolsParameter = wx.BoxSizer(wx.HORIZONTAL)

        sizerQuickSettings = wx.StaticBoxSizer(wx.StaticBox(
            self.pageParameters, wx.ID_ANY, _("Quick Settings")), wx.HORIZONTAL)

        self.buttonQuickA = wx.Button(sizerQuickSettings.GetStaticBox(), wx.ID_ANY, _(
            "A"), wx.DefaultPosition, wx.Size(23, 23), 0)
        sizerQuickSettings.Add(self.buttonQuickA, 0, wx.ALL, 5)

        self.buttonQuickB = wx.Button(sizerQuickSettings.GetStaticBox(), wx.ID_ANY, _(
            "B"), wx.DefaultPosition, wx.Size(23, 23), 0)
        sizerQuickSettings.Add(
            self.buttonQuickB, 0, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        self.buttonQuickC = wx.Button(sizerQuickSettings.GetStaticBox(), wx.ID_ANY, _(
            "C"), wx.DefaultPosition, wx.Size(23, 23), 0)
        sizerQuickSettings.Add(
            self.buttonQuickC, 0, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        self.buttonQuickD = wx.Button(sizerQuickSettings.GetStaticBox(), wx.ID_ANY, _(
            "D"), wx.DefaultPosition, wx.Size(23, 23), 0)
        sizerQuickSettings.Add(
            self.buttonQuickD, 0, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        self.buttonQuickE = wx.Button(sizerQuickSettings.GetStaticBox(), wx.ID_ANY, _(
            "E"), wx.DefaultPosition, wx.Size(23, 23), 0)
        sizerQuickSettings.Add(
            self.buttonQuickE, 0, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        sizerConrolsParameter.Add(sizerQuickSettings, 0, wx.ALL, 5)

        sizerLevel = wx.BoxSizer(wx.VERTICAL)

        self.labelLevel = wx.StaticText(self.pageParameters, wx.ID_ANY, _(
            "Level:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelLevel.Wrap(-1)
        sizerLevel.Add(self.labelLevel, 0, wx.ALL | wx.EXPAND, 5)

        self.spinCtrlLevel = wx.SpinCtrl(self.pageParameters, wx.ID_ANY, wx.EmptyString,
                                         wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS | wx.SP_WRAP, 0, 999, 1)
        sizerLevel.Add(
            self.spinCtrlLevel, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerConrolsParameter.Add(sizerLevel, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        sizerValue = wx.BoxSizer(wx.VERTICAL)

        self.labelValue = wx.StaticText(self.pageParameters, wx.ID_ANY, _(
            "Value:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelValue.Wrap(-1)
        sizerValue.Add(self.labelValue, 0, wx.ALL | wx.EXPAND, 5)

        self.spinCtrlValue = wx.SpinCtrl(self.pageParameters, wx.ID_ANY, wx.EmptyString,
                                         wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS | wx.SP_WRAP, 0, 10, 0)
        sizerValue.Add(
            self.spinCtrlValue, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerConrolsParameter.Add(sizerValue, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        MainSizerParamter.Add(sizerConrolsParameter, 0, wx.EXPAND, 5)

        bSizer613 = wx.BoxSizer(wx.HORIZONTAL)

        from Database.Controls import ParameterGraph
        self.parameterGraph = PyitectConsumes.ParameterGraph(
            self.pageParameters)
        bSizer613.Add(
            self.parameterGraph, 1, wx.EXPAND | wx.RIGHT | wx.LEFT, 0)

        bSizer640 = wx.BoxSizer(wx.VERTICAL)

        self.buttonAddParameter = wx.Button(self.pageParameters, wx.ID_ANY, _(
            "Add..."), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer640.Add(
            self.buttonAddParameter, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.buttonRemoveParameter = wx.Button(self.pageParameters, wx.ID_ANY, _(
            "Remove"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.buttonRemoveParameter.Enable(False)

        bSizer640.Add(
            self.buttonRemoveParameter, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        bSizer641 = wx.BoxSizer(wx.VERTICAL)

        self.checkBoxScaled = wx.CheckBox(self.pageParameters, wx.ID_ANY, _(
            "Scaled"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer641.Add(
            self.checkBoxScaled, 1, wx.ALL | wx.ALIGN_RIGHT | wx.EXPAND, 5)

        self.buttonGenerate = wx.Button(self.pageParameters, wx.ID_ANY, _(
            "Generate..."), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer641.Add(self.buttonGenerate, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        bSizer640.Add(bSizer641, 1, wx.ALIGN_RIGHT, 5)

        bSizer613.Add(bSizer640, 0, wx.EXPAND, 5)

        MainSizerParamter.Add(bSizer613, 1, wx.EXPAND, 5)

        self.pageParameters.SetSizer(MainSizerParamter)
        self.pageParameters.Layout()
        MainSizerParamter.Fit(self.pageParameters)
        self.noteBookActorParameters.AddPage(
            self.pageParameters, _("MaxHP"), True)
        self.pageSP = wx.Panel(
            self.noteBookActorParameters, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.noteBookActorParameters.AddPage(self.pageSP, _("MaxSP"), False)

        sizerParameters.Add(
            self.noteBookActorParameters, 1, wx.EXPAND | wx.ALL, 5)

        sizer2.Add(sizerParameters, 45, wx.EXPAND, 5)

        sizerEquipment = wx.StaticBoxSizer(wx.StaticBox(
            staticSizerActors.GetStaticBox(), wx.ID_ANY, _("Initial Equipment")), wx.VERTICAL)

        self.scrolledWindowEquipment = wx.ScrolledWindow(sizerEquipment.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CLIP_CHILDREN | wx.VSCROLL)
        self.scrolledWindowEquipment.SetScrollRate(5, 5)
        scrolledWindowMainSizer = wx.BoxSizer(wx.VERTICAL)

        self.scrolledWindowEquipment.SetSizer(scrolledWindowMainSizer)
        self.scrolledWindowEquipment.Layout()
        scrolledWindowMainSizer.Fit(self.scrolledWindowEquipment)
        sizerEquipment.Add(self.scrolledWindowEquipment, 1, wx.EXPAND, 5)

        sizer2.Add(sizerEquipment, 35, wx.EXPAND | wx.ALL, 5)

        self.labelNotes = wx.StaticText(staticSizerActors.GetStaticBox(), wx.ID_ANY, _(
            "Notes:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelNotes.Wrap(-1)
        sizer2.Add(self.labelNotes, 0, wx.ALL, 5)

        self.textCtrlNotes = wx.TextCtrl(staticSizerActors.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_PROCESS_ENTER | wx.TE_PROCESS_TAB | wx.CLIP_CHILDREN)
        
        sizer2.Add(
            self.textCtrlNotes, 20, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        staticSizerActors.Add(sizer2, 65, wx.EXPAND, 5)

        MainSizer.Add(staticSizerActors, 75, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        # Connect Events
        self.listBoxActors.Bind(
            wx.EVT_LISTBOX, self.listBoxActors_SelectionChanged)
        self.buttonMaximum.Bind(wx.EVT_BUTTON, self.buttonMaximum_Clicked)
        self.textCtrlName.Bind(wx.EVT_TEXT, self.textBoxName_TextChanged)
        self.comboBoxClass.Bind(
            wx.EVT_CHOICE, self.comboBoxClass_SelectionChanged)
        self.spinCtrlInitialLevel.Bind(
            wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.spinCtrlInitialLevel.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlInitialLevel_ValueChanged)
        self.spinCtrlFinalLevel.Bind(
            wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.spinCtrlFinalLevel.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlFinalLevel_ValueChanged)
        self.comboBoxExpCurve.Bind(
            wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.comboBoxExpCurve.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxExperience_Click)
        self.noteBookActorParameters.Bind(
            wx.EVT_NOTEBOOK_PAGE_CHANGED, self.noteBookParameters_PageChanged)
        self.buttonQuickA.Bind(wx.EVT_BUTTON, self.buttonQuickA_Clicked)
        self.buttonQuickB.Bind(wx.EVT_BUTTON, self.buttonQuickB_Clicked)
        self.buttonQuickC.Bind(wx.EVT_BUTTON, self.buttonQuickC_Clicked)
        self.buttonQuickD.Bind(wx.EVT_BUTTON, self.buttonQuickD_Clicked)
        self.buttonQuickE.Bind(wx.EVT_BUTTON, self.buttonQuickE_Clicked)
        self.spinCtrlLevel.Bind(
            wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.spinCtrlLevel.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlParamLevel_ValueChanged)
        self.spinCtrlLevel.Bind(
            wx.EVT_TEXT, self.spinCtrlParamLevel_ValueChanged)
        self.spinCtrlValue.Bind(
            wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.spinCtrlValue.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlValue_ValueChanged)
        self.spinCtrlValue.Bind(wx.EVT_TEXT, self.spinCtrlValue_ValueChanged)
        self.parameterGraph.Bind(
            wx.EVT_ERASE_BACKGROUND, self.ControlOnEraseBackground)
        self.buttonAddParameter.Bind(
            wx.EVT_BUTTON, self.buttonAddParameter_Clicked)
        self.buttonRemoveParameter.Bind(
            wx.EVT_BUTTON, self.buttonRemoveParameter_Clicked)
        self.checkBoxScaled.Bind(
            wx.EVT_CHECKBOX, self.checkBoxScaled_CheckChanged)
        self.buttonGenerate.Bind(
            wx.EVT_BUTTON, self.buttonGenerateCurve_Clicked)
        self.textCtrlNotes.Bind(wx.EVT_TEXT, self.textCtrlNotes_TextChanged)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def listBoxActors_SelectionChanged(self, event):
        event.Skip()

    def buttonMaximum_Clicked(self, event):
        event.Skip()

    def textBoxName_TextChanged(self, event):
        event.Skip()

    def comboBoxClass_SelectionChanged(self, event):
        event.Skip()

    def OnEraseBackground(self, event):
        event.Skip()

    def spinCtrlInitialLevel_ValueChanged(self, event):
        event.Skip()

    def spinCtrlFinalLevel_ValueChanged(self, event):
        event.Skip()

    def comboBoxExperience_Click(self, event):
        event.Skip()

    def noteBookParameters_PageChanged(self, event):
        event.Skip()

    def buttonQuickA_Clicked(self, event):
        event.Skip()

    def buttonQuickB_Clicked(self, event):
        event.Skip()

    def buttonQuickC_Clicked(self, event):
        event.Skip()

    def buttonQuickD_Clicked(self, event):
        event.Skip()

    def buttonQuickE_Clicked(self, event):
        event.Skip()

    def spinCtrlParamLevel_ValueChanged(self, event):
        event.Skip()

    def spinCtrlValue_ValueChanged(self, event):
        event.Skip()

    def ControlOnEraseBackground(self, event):
        event.Skip()

    def buttonAddParameter_Clicked(self, event):
        event.Skip()

    def buttonRemoveParameter_Clicked(self, event):
        event.Skip()

    def checkBoxScaled_CheckChanged(self, event):
        event.Skip()

    def buttonGenerateCurve_Clicked(self, event):
        event.Skip()

    def textCtrlNotes_TextChanged(self, event):
        event.Skip()

    def splitterGraphicsOnIdle(self, event):
        self.splitterGraphics.SetSashPosition(0)
        self.splitterGraphics.Unbind(wx.EVT_IDLE)


###########################################################################
# Class Classes_Panel_Template
###########################################################################

class Classes_Panel_Template (wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(
            800, 600), style=wx.TAB_TRAVERSAL)

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        ClassListSizer = wx.BoxSizer(wx.VERTICAL)

        self.bitmapClasses = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(
            150, 26), wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)
        self.bitmapClasses.SetMinSize(wx.Size(150, 26))
        self.bitmapClasses.SetMaxSize(wx.Size(150, 26))

        ClassListSizer.Add(self.bitmapClasses, 0, wx.ALL | wx.EXPAND, 5)

        listBoxClassesChoices = []
        self.listBoxClasses = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(
            184, -1), listBoxClassesChoices, wx.LB_SINGLE | wx.CLIP_CHILDREN)
        ClassListSizer.Add(
            self.listBoxClasses, 1, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonMaximum = wx.Button(self, wx.ID_ANY, _(
            "Change Maximum..."), wx.DefaultPosition, wx.Size(150, -1), 0)
        ClassListSizer.Add(self.buttonMaximum, 0, wx.ALL | wx.EXPAND, 5)

        MainSizer.Add(ClassListSizer, 0, wx.EXPAND, 5)

        staticSizerClasses = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.HORIZONTAL)

        bSizer616 = wx.BoxSizer(wx.VERTICAL)

        bSizer6171 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer65 = wx.BoxSizer(wx.VERTICAL)

        self.labelName = wx.StaticText(staticSizerClasses.GetStaticBox(), wx.ID_ANY, _(
            "Name:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelName.Wrap(-1)
        bSizer65.Add(self.labelName, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlName = wx.TextCtrl(staticSizerClasses.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlName.SetMaxLength(0)
        bSizer65.Add(
            self.textCtrlName, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelWeapons = wx.StaticText(staticSizerClasses.GetStaticBox(), wx.ID_ANY, _(
            "Equippable Weapons:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelWeapons.Wrap(-1)
        bSizer65.Add(self.labelWeapons, 0, wx.ALL | wx.EXPAND, 5)

        checkListWeaponsChoices = []
        self.checkListWeapons = wx.CheckListBox(staticSizerClasses.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListWeaponsChoices, 0)
        bSizer65.Add(
            self.checkListWeapons, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        bSizer68 = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonWeaponAll = wx.Button(staticSizerClasses.GetStaticBox(), wx.ID_ANY, _(
            "All"), wx.DefaultPosition, wx.Size(-1, 19), 0)
        bSizer68.Add(
            self.buttonWeaponAll, 1, wx.BOTTOM | wx.LEFT | wx.EXPAND, 5)

        self.buttonWeaponNone = wx.Button(staticSizerClasses.GetStaticBox(), wx.ID_ANY, _(
            "None"), wx.DefaultPosition, wx.Size(-1, 19), 0)
        bSizer68.Add(
            self.buttonWeaponNone, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT, 5)

        bSizer65.Add(bSizer68, 0, wx.EXPAND, 5)

        bSizer6171.Add(bSizer65, 27, wx.EXPAND, 5)

        bSizer66 = wx.BoxSizer(wx.VERTICAL)

        bSizer651 = wx.BoxSizer(wx.VERTICAL)

        self.labelPosition = wx.StaticText(staticSizerClasses.GetStaticBox(), wx.ID_ANY, _(
            "Position:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelPosition.Wrap(-1)
        bSizer651.Add(self.labelPosition, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxPositionChoices = []
        self.comboBoxPosition = wx.Choice(staticSizerClasses.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxPositionChoices, 0)
        self.comboBoxPosition.SetSelection(0)
        bSizer651.Add(
            self.comboBoxPosition, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelArmors = wx.StaticText(staticSizerClasses.GetStaticBox(), wx.ID_ANY, _(
            "Equippable Armors:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelArmors.Wrap(-1)
        bSizer651.Add(self.labelArmors, 0, wx.ALL | wx.EXPAND, 5)

        checkListArmorsChoices = []
        self.checkListArmors = wx.CheckListBox(staticSizerClasses.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListArmorsChoices, 0)
        bSizer651.Add(
            self.checkListArmors, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerOKRemove = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonArmorAll = wx.Button(staticSizerClasses.GetStaticBox(), wx.ID_ANY, _(
            "All"), wx.DefaultPosition, wx.Size(-1, 19), 0)
        sizerOKRemove.Add(
            self.buttonArmorAll, 1, wx.EXPAND | wx.BOTTOM | wx.LEFT, 5)

        self.buttonArmorNone = wx.Button(staticSizerClasses.GetStaticBox(), wx.ID_ANY, _(
            "None"), wx.DefaultPosition, wx.Size(-1, 19), 0)
        sizerOKRemove.Add(
            self.buttonArmorNone, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT, 5)

        bSizer651.Add(sizerOKRemove, 0, wx.EXPAND, 5)

        bSizer66.Add(bSizer651, 1, wx.EXPAND, 5)

        bSizer6171.Add(bSizer66, 27, wx.EXPAND, 5)

        bSizer616.Add(bSizer6171, 75, wx.EXPAND, 5)

        self.labelNotes = wx.StaticText(staticSizerClasses.GetStaticBox(), wx.ID_ANY, _(
            "Notes:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelNotes.Wrap(-1)
        bSizer616.Add(self.labelNotes, 0, wx.ALL, 5)

        self.textCtrlNotes = wx.TextCtrl(staticSizerClasses.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_PROCESS_ENTER | wx.TE_PROCESS_TAB | wx.CLIP_CHILDREN)
        
        bSizer616.Add(
            self.textCtrlNotes, 25, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        staticSizerClasses.Add(bSizer616, 54, wx.EXPAND, 5)

        bSizer67 = wx.BoxSizer(wx.VERTICAL)

        bSizer74 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelElements = wx.StaticText(staticSizerClasses.GetStaticBox(), wx.ID_ANY, _(
            "Element Efficiency:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelElements.Wrap(-1)
        bSizer74.Add(self.labelElements, 1, wx.ALL | wx.EXPAND, 5)

        self.labelStates = wx.StaticText(staticSizerClasses.GetStaticBox(), wx.ID_ANY, _(
            "State Efficiency:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelStates.Wrap(-1)
        bSizer74.Add(self.labelStates, 1, wx.ALL | wx.EXPAND, 5)

        bSizer67.Add(bSizer74, 0, wx.EXPAND, 5)

        bSizer75 = wx.BoxSizer(wx.HORIZONTAL)

        listBoxElementsChoices = []
        self.listBoxElements = wx.ListBox(staticSizerClasses.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxElementsChoices, 0)
        bSizer75.Add(
            self.listBoxElements, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        listBoxStatesChoices = []
        self.listBoxStates = wx.ListBox(staticSizerClasses.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxStatesChoices, 0)
        bSizer75.Add(
            self.listBoxStates, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        bSizer67.Add(bSizer75, 30, wx.EXPAND, 5)

        bSizer617 = wx.BoxSizer(wx.HORIZONTAL)

        self.spinCtrlElements = wx.SpinCtrl(staticSizerClasses.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS | wx.SP_WRAP, 0, 10, 0)
        bSizer617.Add(
            self.spinCtrlElements, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlStates = wx.SpinCtrl(staticSizerClasses.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS | wx.SP_WRAP, 0, 10, 0)
        bSizer617.Add(
            self.spinCtrlStates, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        bSizer67.Add(bSizer617, 0, wx.EXPAND, 5)

        self.labelSkills = wx.StaticText(staticSizerClasses.GetStaticBox(), wx.ID_ANY, _(
            "Skills to Learn:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelSkills.Wrap(-1)
        bSizer67.Add(self.labelSkills, 0, wx.ALL, 5)

        self.listCtrlSkills = wx.ListCtrl(staticSizerClasses.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT | wx.LC_SINGLE_SEL)
        bSizer67.Add(
            self.listCtrlSkills, 35, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        bSizer618 = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonSkillAdd = wx.Button(staticSizerClasses.GetStaticBox(), wx.ID_ANY, _(
            "Add"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer618.Add(self.buttonSkillAdd, 0, wx.BOTTOM | wx.LEFT, 5)

        self.buttonSkillRemove = wx.Button(staticSizerClasses.GetStaticBox(), wx.ID_ANY, _(
            "Remove"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer618.Add(self.buttonSkillRemove, 0, wx.BOTTOM | wx.RIGHT, 5)

        bSizer67.Add(bSizer618, 0, wx.ALIGN_RIGHT, 5)

        staticSizerClasses.Add(bSizer67, 44, wx.EXPAND, 5)

        MainSizer.Add(staticSizerClasses, 75, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        # Connect Events
        self.listBoxClasses.Bind(
            wx.EVT_LISTBOX, self.listBoxClasses_SelectionChanged)
        self.buttonMaximum.Bind(wx.EVT_BUTTON, self.buttonMaximum_Clicked)
        self.textCtrlName.Bind(wx.EVT_TEXT, self.textCtrlName_TextChanged)
        self.checkListWeapons.Bind(
            wx.EVT_CHECKLISTBOX, self.checkListWeapons_CheckChanged)
        self.buttonWeaponAll.Bind(wx.EVT_BUTTON, self.buttonWeaponAll_Clicked)
        self.buttonWeaponNone.Bind(
            wx.EVT_BUTTON, self.buttonWeaponNone_Clicked)
        self.comboBoxPosition.Bind(
            wx.EVT_CHOICE, self.comboBoxPosition_SelectionChanged)
        self.checkListArmors.Bind(
            wx.EVT_CHECKLISTBOX, self.checkListArmors_CheckChanged)
        self.buttonArmorAll.Bind(wx.EVT_BUTTON, self.buttonArmorAll_Clicked)
        self.buttonArmorNone.Bind(wx.EVT_BUTTON, self.buttonArmorNone_Clicked)
        self.textCtrlNotes.Bind(wx.EVT_TEXT, self.textCtrlNotes_TextChanged)
        self.listBoxElements.Bind(
            wx.EVT_LISTBOX, self.listBoxElements_SelectionChanged)
        self.listBoxStates.Bind(
            wx.EVT_LISTBOX, self.listBoxStates_SelectionChanged)
        self.spinCtrlElements.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlElements_ValueChanged)
        self.spinCtrlStates.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlStates_ValueChanged)
        self.listCtrlSkills.Bind(wx.EVT_KEY_DOWN, self.listCtrlSkills_KeyDown)
        self.listCtrlSkills.Bind(
            wx.EVT_LEFT_DCLICK, self.listCtrlSkills_DoubleClick)
        self.buttonSkillAdd.Bind(wx.EVT_BUTTON, self.buttonSkillAdd_Clicked)
        self.buttonSkillRemove.Bind(
            wx.EVT_BUTTON, self.buttonSkillRemove_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def listBoxClasses_SelectionChanged(self, event):
        event.Skip()

    def buttonMaximum_Clicked(self, event):
        event.Skip()

    def textCtrlName_TextChanged(self, event):
        event.Skip()

    def checkListWeapons_CheckChanged(self, event):
        event.Skip()

    def buttonWeaponAll_Clicked(self, event):
        event.Skip()

    def buttonWeaponNone_Clicked(self, event):
        event.Skip()

    def comboBoxPosition_SelectionChanged(self, event):
        event.Skip()

    def checkListArmors_CheckChanged(self, event):
        event.Skip()

    def buttonArmorAll_Clicked(self, event):
        event.Skip()

    def buttonArmorNone_Clicked(self, event):
        event.Skip()

    def textCtrlNotes_TextChanged(self, event):
        event.Skip()

    def listBoxElements_SelectionChanged(self, event):
        event.Skip()

    def listBoxStates_SelectionChanged(self, event):
        event.Skip()

    def spinCtrlElements_ValueChanged(self, event):
        event.Skip()

    def spinCtrlStates_ValueChanged(self, event):
        event.Skip()

    def listCtrlSkills_KeyDown(self, event):
        event.Skip()

    def listCtrlSkills_DoubleClick(self, event):
        event.Skip()

    def buttonSkillAdd_Clicked(self, event):
        event.Skip()

    def buttonSkillRemove_Clicked(self, event):
        event.Skip()


###########################################################################
# Class Skills_Panel_Template
###########################################################################

class Skills_Panel_Template (wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(
            800, 600), style=wx.TAB_TRAVERSAL)

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        SkillListSizer = wx.BoxSizer(wx.VERTICAL)

        self.bitmapSkills = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(
            150, 26), wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)
        self.bitmapSkills.SetMinSize(wx.Size(150, 26))
        self.bitmapSkills.SetMaxSize(wx.Size(150, 26))

        SkillListSizer.Add(self.bitmapSkills, 0, wx.ALL | wx.EXPAND, 5)

        listBoxSkillsChoices = []
        self.listBoxSkills = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(
            184, -1), listBoxSkillsChoices, wx.LB_SINGLE | wx.CLIP_CHILDREN)
        SkillListSizer.Add(
            self.listBoxSkills, 100, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonMaximum = wx.Button(self, wx.ID_ANY, _(
            "Change Maximum..."), wx.DefaultPosition, wx.Size(150, -1), 0)
        SkillListSizer.Add(self.buttonMaximum, 0, wx.ALL | wx.EXPAND, 5)

        MainSizer.Add(SkillListSizer, 0, wx.EXPAND, 5)

        staticSizerItems = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.HORIZONTAL)

        sizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer620 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer621 = wx.BoxSizer(wx.VERTICAL)

        self.labelName = wx.StaticText(staticSizerItems.GetStaticBox(), wx.ID_ANY, _(
            "Name:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelName.Wrap(-1)
        bSizer621.Add(self.labelName, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlName = wx.TextCtrl(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlName.SetMaxLength(0)
        bSizer621.Add(
            self.textCtrlName, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        bSizer620.Add(bSizer621, 65, 0, 5)

        bSizer622 = wx.BoxSizer(wx.VERTICAL)

        self.labelIcon = wx.StaticText(staticSizerItems.GetStaticBox(), wx.ID_ANY, _(
            "Icon:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelIcon.Wrap(-1)
        bSizer622.Add(self.labelIcon, 0, wx.ALL | wx.EXPAND, 5)

        self.labelIconName = wx.StaticText(staticSizerItems.GetStaticBox(), wx.ID_ANY, _(
            "(Name of Icon)"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelIconName.Wrap(-1)
        bSizer622.Add(self.labelIconName, 0, wx.ALL | wx.EXPAND, 5)

        bSizer620.Add(bSizer622, 35, wx.EXPAND, 5)

        self.bitmapButtonIcon = wx.BitmapButton(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(32, 32), wx.BU_AUTODRAW)
        bSizer620.Add(self.bitmapButtonIcon, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        sizer1.Add(bSizer620, 0, wx.EXPAND, 5)

        self.labelDescription = wx.StaticText(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, _("Description:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelDescription.Wrap(-1)
        sizer1.Add(self.labelDescription, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlDescription = wx.TextCtrl(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlDescription.SetMaxLength(0)
        sizer1.Add(self.textCtrlDescription, 0, wx.EXPAND |
                   wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizer6 = wx.BoxSizer(wx.HORIZONTAL)

        sizer8 = wx.BoxSizer(wx.VERTICAL)

        self.labelScope = wx.StaticText(staticSizerItems.GetStaticBox(), wx.ID_ANY, _(
            "Scope:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelScope.Wrap(-1)
        sizer8.Add(self.labelScope, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxScopeChoices = [_("None"), _("One Enemy"), _("All Enemies"), _("One Ally"), _("All Allies"), _(
            "One Ally (HP 0)"), _("All Allies (HP 0)"), _("The User"), _("One Ally or Enemy"), _("Everyone")]
        self.comboBoxScope = wx.Choice(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxScopeChoices, 0)
        self.comboBoxScope.SetSelection(0)
        sizer8.Add(
            self.comboBoxScope, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelUserAnimation = wx.StaticText(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, _("User Animation:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelUserAnimation.Wrap(-1)
        sizer8.Add(self.labelUserAnimation, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxUserAnimationChoices = [_("(None)")]
        self.comboBoxUserAnimation = wx.Choice(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxUserAnimationChoices, 0)
        self.comboBoxUserAnimation.SetSelection(0)
        sizer8.Add(self.comboBoxUserAnimation, 1, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        bSizer623 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer624 = wx.BoxSizer(wx.VERTICAL)

        self.labelMenuSE = wx.StaticText(staticSizerItems.GetStaticBox(), wx.ID_ANY, _(
            "Menu Use SE:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelMenuSE.Wrap(-1)
        bSizer624.Add(self.labelMenuSE, 0, wx.ALL | wx.EXPAND, 5)

        self.comboBoxMenuSE = wx.adv.BitmapComboBox(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, "", wx.CB_READONLY | wx.CLIP_CHILDREN)
        bSizer624.Add(
            self.comboBoxMenuSE, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        bSizer623.Add(bSizer624, 1, 0, 5)

        self.bitmapButtonAudioTest = wx.BitmapButton(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        bSizer623.Add(
            self.bitmapButtonAudioTest, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        sizer8.Add(bSizer623, 0, wx.EXPAND, 5)

        sizer6.Add(sizer8, 1, wx.EXPAND, 5)

        sizer9 = wx.BoxSizer(wx.VERTICAL)

        self.labelOccasion = wx.StaticText(staticSizerItems.GetStaticBox(), wx.ID_ANY, _(
            "Occasion:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelOccasion.Wrap(-1)
        sizer9.Add(self.labelOccasion, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxOccasionChoices = [
            _("Always"), _("Only in Battle"), _("Only from Men"), _("Never")]
        self.comboBoxOccasion = wx.Choice(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxOccasionChoices, 0)
        self.comboBoxOccasion.SetSelection(0)
        sizer9.Add(self.comboBoxOccasion, 1, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelTargetAnimation = wx.StaticText(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, _("Target Animation:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelTargetAnimation.Wrap(-1)
        sizer9.Add(self.labelTargetAnimation, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxTargetAnimationChoices = [_("(None)")]
        self.comboBoxTargetAnimation = wx.Choice(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxTargetAnimationChoices, 0)
        self.comboBoxTargetAnimation.SetSelection(0)
        sizer9.Add(self.comboBoxTargetAnimation, 1, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelCommonEvent = wx.StaticText(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, _("Common Event:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelCommonEvent.Wrap(-1)
        sizer9.Add(self.labelCommonEvent, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxCommonEventChoices = [_("(None)")]
        self.comboBoxCommonEvent = wx.Choice(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxCommonEventChoices, 0)
        self.comboBoxCommonEvent.SetSelection(0)
        sizer9.Add(self.comboBoxCommonEvent, 1, wx.EXPAND |
                   wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizer6.Add(sizer9, 1, wx.EXPAND, 5)

        sizer1.Add(sizer6, 0, wx.EXPAND, 5)

        sizerParameters = wx.StaticBoxSizer(wx.StaticBox(
            staticSizerItems.GetStaticBox(), wx.ID_ANY, _("Parameters")), wx.VERTICAL)

        from .Extras import ParameterPanel
        self.panelParameters = ParameterPanel(self)
        sizerParameters.Add(self.panelParameters, 1, wx.EXPAND, 5)

        sizer1.Add(sizerParameters, 1, wx.ALL | wx.EXPAND, 5)

        staticSizerItems.Add(sizer1, 60, wx.EXPAND, 5)

        sizer2 = wx.BoxSizer(wx.VERTICAL)

        sizerEfficiency = wx.BoxSizer(wx.HORIZONTAL)

        sizerElements = wx.BoxSizer(wx.VERTICAL)

        self.labelElements = wx.StaticText(staticSizerItems.GetStaticBox(), wx.ID_ANY, _(
            "Element:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelElements.Wrap(-1)
        sizerElements.Add(self.labelElements, 0, wx.ALL | wx.EXPAND, 5)

        from .Extras import ImageCheckList
        from .Extras import DatabaseManager as DM
        states = [False, True]
        images = DM.GetNormalCheckImageList()
        self.checkListElements = ImageCheckList(self, states, images)

        sizerElements.Add(
            self.checkListElements, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerEfficiency.Add(sizerElements, 1, wx.EXPAND, 5)

        sizerStates = wx.BoxSizer(wx.VERTICAL)

        self.labelStates = wx.StaticText(staticSizerItems.GetStaticBox(), wx.ID_ANY, _(
            "State Change:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelStates.Wrap(-1)
        sizerStates.Add(self.labelStates, 0, wx.ALL | wx.EXPAND, 5)

        states = [0, 1, -1]
        images = DM.GetAddSubImageList()
        self.checkListStates = ImageCheckList(self, states, images)
        sizerStates.Add(
            self.checkListStates, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizerEfficiency.Add(sizerStates, 1, wx.EXPAND, 5)

        sizer2.Add(sizerEfficiency, 60, wx.EXPAND, 5)

        self.labelNotes = wx.StaticText(staticSizerItems.GetStaticBox(), wx.ID_ANY, _(
            "Notes:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelNotes.Wrap(-1)
        sizer2.Add(self.labelNotes, 0, wx.ALL, 5)

        self.textCtrlNotes = wx.TextCtrl(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_PROCESS_ENTER | wx.TE_PROCESS_TAB | wx.CLIP_CHILDREN)
        
        sizer2.Add(
            self.textCtrlNotes, 40, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        staticSizerItems.Add(sizer2, 40, wx.EXPAND, 5)

        MainSizer.Add(staticSizerItems, 75, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        # Connect Events
        self.listBoxSkills.Bind(
            wx.EVT_LISTBOX, self.listBoxSkills_SelectionChanged)
        self.buttonMaximum.Bind(wx.EVT_BUTTON, self.buttonMaximum_Clicked)
        self.textCtrlName.Bind(wx.EVT_TEXT, self.textCtrlName_TextChanged)
        self.bitmapButtonIcon.Bind(
            wx.EVT_BUTTON, self.bitmapButtonIcon_Clicked)
        self.textCtrlDescription.Bind(
            wx.EVT_TEXT, self.textCtrlDescription_TextChange)
        self.comboBoxScope.Bind(
            wx.EVT_CHOICE, self.comboBoxScope_SelectionChanged)
        self.comboBoxUserAnimation.Bind(
            wx.EVT_CHOICE, self.comboBoxUserAnimation_SelectionChanged)
        self.comboBoxMenuSE.Bind(wx.EVT_LEFT_DOWN, self.comboBoxMenuSE_Clicked)
        self.bitmapButtonAudioTest.Bind(
            wx.EVT_BUTTON, self.bitmapButtonAudioTest_Clicked)
        self.comboBoxOccasion.Bind(
            wx.EVT_CHOICE, self.comboBoxOccasion_SelectionChanged)
        self.comboBoxTargetAnimation.Bind(
            wx.EVT_CHOICE, self.comboBoxTargetAnimation_SelectionChanged)
        self.comboBoxCommonEvent.Bind(
            wx.EVT_CHOICE, self.comboBoxCommonEvent_SelectionChanged)
        self.checkListElements.Bind(
            wx.EVT_LEFT_DOWN, self.checkListElements_Clicked)
        self.checkListElements.Bind(
            wx.EVT_RIGHT_DOWN, self.checkListElements_Clicked)
        self.checkListStates.Bind(
            wx.EVT_LEFT_DOWN, self.checkListStates_LeftClicked)
        self.checkListStates.Bind(
            wx.EVT_RIGHT_DOWN, self.checkListStates_RightClicked)
        self.textCtrlNotes.Bind(wx.EVT_TEXT, self.textCtrlNotes_TextChanged)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def listBoxSkills_SelectionChanged(self, event):
        event.Skip()

    def buttonMaximum_Clicked(self, event):
        event.Skip()

    def textCtrlName_TextChanged(self, event):
        event.Skip()

    def bitmapButtonIcon_Clicked(self, event):
        event.Skip()

    def textCtrlDescription_TextChange(self, event):
        event.Skip()

    def comboBoxScope_SelectionChanged(self, event):
        event.Skip()

    def comboBoxUserAnimation_SelectionChanged(self, event):
        event.Skip()

    def comboBoxMenuSE_Clicked(self, event):
        event.Skip()

    def bitmapButtonAudioTest_Clicked(self, event):
        event.Skip()

    def comboBoxOccasion_SelectionChanged(self, event):
        event.Skip()

    def comboBoxTargetAnimation_SelectionChanged(self, event):
        event.Skip()

    def comboBoxCommonEvent_SelectionChanged(self, event):
        event.Skip()

    def checkListElements_Clicked(self, event):
        event.Skip()

    def checkListStates_LeftClicked(self, event):
        event.Skip()

    def checkListStates_RightClicked(self, event):
        event.Skip()

    def textCtrlNotes_TextChanged(self, event):
        event.Skip()


###########################################################################
# Class Items_Panel_Template
###########################################################################

class Items_Panel_Template (wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(
            926, 600), style=wx.TAB_TRAVERSAL)

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        ItemListSizer = wx.BoxSizer(wx.VERTICAL)

        self.bitmapItems = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(
            150, 26), wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)
        self.bitmapItems.SetMinSize(wx.Size(150, 26))
        self.bitmapItems.SetMaxSize(wx.Size(150, 26))

        ItemListSizer.Add(self.bitmapItems, 0, wx.ALL | wx.EXPAND, 5)

        listBoxItemsChoices = []
        self.listBoxItems = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(
            184, -1), listBoxItemsChoices, wx.LB_SINGLE | wx.CLIP_CHILDREN)
        ItemListSizer.Add(
            self.listBoxItems, 1, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        self.buttonMaximum = wx.Button(self, wx.ID_ANY, _(
            "Change Maximum..."), wx.DefaultPosition, wx.Size(150, -1), 0)
        ItemListSizer.Add(self.buttonMaximum, 0, wx.ALL | wx.EXPAND, 5)

        MainSizer.Add(ItemListSizer, 0, wx.EXPAND, 5)

        staticSizerItems = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.HORIZONTAL)

        sizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer620 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer621 = wx.BoxSizer(wx.VERTICAL)

        self.labelName = wx.StaticText(staticSizerItems.GetStaticBox(), wx.ID_ANY, _(
            "Name:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelName.Wrap(-1)
        bSizer621.Add(self.labelName, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlName = wx.TextCtrl(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlName.SetMaxLength(0)
        bSizer621.Add(
            self.textCtrlName, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        bSizer620.Add(bSizer621, 65, 0, 5)

        bSizer622 = wx.BoxSizer(wx.VERTICAL)

        self.labelIcon = wx.StaticText(staticSizerItems.GetStaticBox(), wx.ID_ANY, _(
            "Icon:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelIcon.Wrap(-1)
        bSizer622.Add(self.labelIcon, 0, wx.ALL | wx.EXPAND, 5)

        self.labelIconName = wx.StaticText(staticSizerItems.GetStaticBox(), wx.ID_ANY, _(
            "(Name of Icon)"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelIconName.Wrap(-1)
        bSizer622.Add(self.labelIconName, 0, wx.ALL | wx.EXPAND, 5)

        bSizer620.Add(bSizer622, 35, 0, 5)

        self.bitmapButtonIcon = wx.BitmapButton(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(32, 32), wx.BU_AUTODRAW)
        bSizer620.Add(self.bitmapButtonIcon, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        sizer1.Add(bSizer620, 0, wx.EXPAND, 5)

        self.labelDescription = wx.StaticText(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, _("Description:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelDescription.Wrap(-1)
        sizer1.Add(self.labelDescription, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlDescription = wx.TextCtrl(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlDescription.SetMaxLength(0)
        sizer1.Add(self.textCtrlDescription, 0, wx.EXPAND |
                   wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizer6 = wx.BoxSizer(wx.HORIZONTAL)

        sizer8 = wx.BoxSizer(wx.VERTICAL)

        self.labelScope = wx.StaticText(staticSizerItems.GetStaticBox(), wx.ID_ANY, _(
            "Scope:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelScope.Wrap(-1)
        sizer8.Add(self.labelScope, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxScopeChoices = [_("None"), _("One Enemy"), _("All Enemies"), _("One Ally"), _("All Allies"), _(
            "One Ally (HP 0)"), _("All Allies (HP 0)"), _("The User"), _("One Ally or Enemy"), _("Everyone")]
        self.comboBoxScope = wx.Choice(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxScopeChoices, 0)
        self.comboBoxScope.SetSelection(0)
        sizer8.Add(
            self.comboBoxScope, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelUserAnimation = wx.StaticText(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, _("User Animation:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelUserAnimation.Wrap(-1)
        sizer8.Add(self.labelUserAnimation, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxUserAnimationChoices = [_("(None)")]
        self.comboBoxUserAnimation = wx.Choice(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxUserAnimationChoices, 0)
        self.comboBoxUserAnimation.SetSelection(0)
        sizer8.Add(self.comboBoxUserAnimation, 1, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        bSizer623 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer624 = wx.BoxSizer(wx.VERTICAL)

        self.labelMenuSE = wx.StaticText(staticSizerItems.GetStaticBox(), wx.ID_ANY, _(
            "Menu Use SE:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelMenuSE.Wrap(-1)
        bSizer624.Add(self.labelMenuSE, 0, wx.ALL | wx.EXPAND, 5)

        self.comboBoxMenuSE = wx.adv.BitmapComboBox(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, "", wx.CB_READONLY | wx.CLIP_CHILDREN)
        bSizer624.Add(
            self.comboBoxMenuSE, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        bSizer623.Add(bSizer624, 1, 0, 5)

        self.bitmapButtonAudioTest = wx.BitmapButton(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        bSizer623.Add(
            self.bitmapButtonAudioTest, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        sizer8.Add(bSizer623, 0, wx.EXPAND, 5)

        sizer6.Add(sizer8, 1, wx.EXPAND, 5)

        sizer9 = wx.BoxSizer(wx.VERTICAL)

        self.labelOccasion = wx.StaticText(staticSizerItems.GetStaticBox(), wx.ID_ANY, _(
            "Occasion:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelOccasion.Wrap(-1)
        sizer9.Add(self.labelOccasion, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxOccasionChoices = [
            _("Always"), _("Only in Battle"), _("Only from Men"), _("Never")]
        self.comboBoxOccasion = wx.Choice(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxOccasionChoices, 0)
        self.comboBoxOccasion.SetSelection(0)
        sizer9.Add(self.comboBoxOccasion, 1, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelTargetAnimation = wx.StaticText(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, _("Target Animation:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelTargetAnimation.Wrap(-1)
        sizer9.Add(self.labelTargetAnimation, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxTargetAnimationChoices = [_("(None)")]
        self.comboBoxTargetAnimation = wx.Choice(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxTargetAnimationChoices, 0)
        self.comboBoxTargetAnimation.SetSelection(0)
        sizer9.Add(self.comboBoxTargetAnimation, 1, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelCommonEvent = wx.StaticText(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, _("Common Event:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelCommonEvent.Wrap(-1)
        sizer9.Add(self.labelCommonEvent, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxCommonEventChoices = [_("(None)")]
        self.comboBoxCommonEvent = wx.Choice(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxCommonEventChoices, 0)
        self.comboBoxCommonEvent.SetSelection(0)
        sizer9.Add(self.comboBoxCommonEvent, 1, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizer6.Add(sizer9, 1, wx.EXPAND, 5)

        sizer1.Add(sizer6, 0, wx.EXPAND, 5)

        sizerParameters = wx.StaticBoxSizer(wx.StaticBox(
            staticSizerItems.GetStaticBox(), wx.ID_ANY, _("Parameters")), wx.VERTICAL)

        bSizer651 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelPrice = wx.StaticText(sizerParameters.GetStaticBox(), wx.ID_ANY, _(
            "Price:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelPrice.Wrap(-1)
        bSizer651.Add(self.labelPrice, 1, wx.ALL, 5)

        self.labelConsumable = wx.StaticText(sizerParameters.GetStaticBox(), wx.ID_ANY, _(
            "Consumable:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelConsumable.Wrap(-1)
        bSizer651.Add(self.labelConsumable, 1, wx.ALL, 5)

        self.labelParameter = wx.StaticText(sizerParameters.GetStaticBox(), wx.ID_ANY, _(
            "Parameter:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelParameter.Wrap(-1)
        bSizer651.Add(self.labelParameter, 1, wx.ALL, 5)

        self.labelParameterInc = wx.StaticText(sizerParameters.GetStaticBox(
        ), wx.ID_ANY, _("Param Inc:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelParameterInc.Wrap(-1)
        bSizer651.Add(self.labelParameterInc, 1, wx.ALL, 5)

        sizerParameters.Add(bSizer651, 0, wx.EXPAND, 5)

        bSizer652 = wx.BoxSizer(wx.HORIZONTAL)

        self.spinCtrlPrice = wx.SpinCtrl(sizerParameters.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 999999999, 0)
        bSizer652.Add(self.spinCtrlPrice, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        comboBoxConsumableChoices = [_("Yes"), _("No")]
        self.comboBoxConsumable = wx.Choice(sizerParameters.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxConsumableChoices, 0)
        self.comboBoxConsumable.SetSelection(0)
        bSizer652.Add(
            self.comboBoxConsumable, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        comboBoxParameterChoices = [_("(None)"), _("MaxHP"), _(
            "MaxSP"), _("STR"), _("DEX"), _("AGI"), _("INT")]
        self.comboBoxParameter = wx.Choice(sizerParameters.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxParameterChoices, 0)
        self.comboBoxParameter.SetSelection(0)
        bSizer652.Add(
            self.comboBoxParameter, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlParameterInc = wx.SpinCtrl(sizerParameters.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        bSizer652.Add(
            self.spinCtrlParameterInc, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerParameters.Add(bSizer652, 0, wx.EXPAND, 5)

        bSizer653 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelRecrHPPercent = wx.StaticText(sizerParameters.GetStaticBox(
        ), wx.ID_ANY, _("Rcvr HP %:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelRecrHPPercent.Wrap(-1)
        bSizer653.Add(self.labelRecrHPPercent, 1, wx.ALL, 5)

        self.labelRecrHP = wx.StaticText(sizerParameters.GetStaticBox(), wx.ID_ANY, _(
            "Rcvr HP:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelRecrHP.Wrap(-1)
        bSizer653.Add(self.labelRecrHP, 1, wx.ALL, 5)

        self.labelRcvrRate = wx.StaticText(sizerParameters.GetStaticBox(), wx.ID_ANY, _(
            "Rcvr SP %:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelRcvrRate.Wrap(-1)
        bSizer653.Add(self.labelRcvrRate, 1, wx.ALL, 5)

        self.labelRecrSP = wx.StaticText(sizerParameters.GetStaticBox(), wx.ID_ANY, _(
            "Recr SP:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelRecrSP.Wrap(-1)
        bSizer653.Add(self.labelRecrSP, 1, wx.ALL, 5)

        sizerParameters.Add(bSizer653, 0, wx.EXPAND, 5)

        bSizer654 = wx.BoxSizer(wx.HORIZONTAL)

        self.spinCtrlRecrHPRate = wx.SpinCtrl(sizerParameters.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -10000, 10000, 0)
        bSizer654.Add(
            self.spinCtrlRecrHPRate, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlRecrHP = wx.SpinCtrl(sizerParameters.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        bSizer654.Add(
            self.spinCtrlRecrHP, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlRecrSPRate = wx.SpinCtrl(sizerParameters.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0)
        bSizer654.Add(
            self.spinCtrlRecrSPRate, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlRecrSP = wx.SpinCtrl(sizerParameters.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        bSizer654.Add(
            self.spinCtrlRecrSP, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerParameters.Add(bSizer654, 0, wx.EXPAND, 5)

        bSizer655 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelHitRate = wx.StaticText(sizerParameters.GetStaticBox(), wx.ID_ANY, _(
            "Hit Rate:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelHitRate.Wrap(-1)
        bSizer655.Add(self.labelHitRate, 1, wx.ALL, 5)

        self.labelPDEF = wx.StaticText(sizerParameters.GetStaticBox(), wx.ID_ANY, _(
            "PDEF-F:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelPDEF.Wrap(-1)
        bSizer655.Add(self.labelPDEF, 1, wx.ALL, 5)

        self.labelMDEF = wx.StaticText(sizerParameters.GetStaticBox(), wx.ID_ANY, _(
            "MDEF-F:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelMDEF.Wrap(-1)
        bSizer655.Add(self.labelMDEF, 1, wx.ALL, 5)

        self.labelVariance = wx.StaticText(sizerParameters.GetStaticBox(), wx.ID_ANY, _(
            "Variance:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelVariance.Wrap(-1)
        bSizer655.Add(self.labelVariance, 1, wx.ALL, 5)

        sizerParameters.Add(bSizer655, 0, wx.EXPAND, 5)

        bSizer656 = wx.BoxSizer(wx.HORIZONTAL)

        self.spinCtrlHitRate = wx.SpinCtrl(sizerParameters.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 100)
        bSizer656.Add(
            self.spinCtrlHitRate, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlPDEF = wx.SpinCtrl(sizerParameters.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        bSizer656.Add(self.spinCtrlPDEF, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlMDEF = wx.SpinCtrl(sizerParameters.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        bSizer656.Add(self.spinCtrlMDEF, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlVariance = wx.SpinCtrl(sizerParameters.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0)
        bSizer656.Add(
            self.spinCtrlVariance, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerParameters.Add(bSizer656, 0, wx.EXPAND, 5)

        sizer1.Add(sizerParameters, 0, wx.EXPAND | wx.ALL, 5)

        staticSizerItems.Add(sizer1, 60, wx.EXPAND, 5)

        sizer2 = wx.BoxSizer(wx.VERTICAL)

        sizer14 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelElements = wx.StaticText(staticSizerItems.GetStaticBox(), wx.ID_ANY, _(
            "Element:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelElements.Wrap(-1)
        sizer14.Add(self.labelElements, 1, wx.ALL | wx.EXPAND, 5)

        self.labelStates = wx.StaticText(staticSizerItems.GetStaticBox(), wx.ID_ANY, _(
            "State Change:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelStates.Wrap(-1)
        sizer14.Add(self.labelStates, 1, wx.ALL | wx.EXPAND, 5)

        sizer2.Add(sizer14, 0, wx.EXPAND, 5)

        sizer15 = wx.BoxSizer(wx.HORIZONTAL)

        from .Extras import ImageCheckList
        from .Extras import DatabaseManager as DM
        states = [False, True]
        images = DM.GetNormalCheckImageList()
        self.checkListElements = ImageCheckList(self, states, images)
        sizer15.Add(
            self.checkListElements, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        states = [0, 1, -1]
        images = DM.GetAddSubImageList()
        self.checkListStates = ImageCheckList(self, states, images)
        sizer15.Add(
            self.checkListStates, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizer2.Add(sizer15, 1, wx.EXPAND, 5)

        self.labelNotes = wx.StaticText(staticSizerItems.GetStaticBox(), wx.ID_ANY, _(
            "Notes:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelNotes.Wrap(-1)
        sizer2.Add(self.labelNotes, 0, wx.ALL, 5)

        self.textCtrlNotes = wx.TextCtrl(staticSizerItems.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.CLIP_CHILDREN)
        
        sizer2.Add(
            self.textCtrlNotes, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        staticSizerItems.Add(sizer2, 40, wx.EXPAND, 5)

        MainSizer.Add(staticSizerItems, 75, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        # Connect Events
        self.listBoxItems.Bind(
            wx.EVT_LISTBOX, self.listBoxItems_SelectionChanged)
        self.buttonMaximum.Bind(wx.EVT_BUTTON, self.buttonMaximum_Clicked)
        self.textCtrlName.Bind(wx.EVT_TEXT, self.textCtrlName_TextChanged)
        self.bitmapButtonIcon.Bind(
            wx.EVT_BUTTON, self.bitmapButtonIcon_Clicked)
        self.textCtrlDescription.Bind(
            wx.EVT_TEXT, self.textCtrlDescription_TextChange)
        self.comboBoxScope.Bind(
            wx.EVT_CHOICE, self.comboBoxScope_SelectionChanged)
        self.comboBoxUserAnimation.Bind(
            wx.EVT_CHOICE, self.comboBoxUserAnimation_SelectionChanged)
        self.comboBoxMenuSE.Bind(wx.EVT_LEFT_DOWN, self.comboBoxMenuSE_Clicked)
        self.bitmapButtonAudioTest.Bind(
            wx.EVT_BUTTON, self.bitmapButtonAudioTest_Clicked)
        self.comboBoxOccasion.Bind(
            wx.EVT_CHOICE, self.comboBoxOccasion_SelectionChanged)
        self.comboBoxTargetAnimation.Bind(
            wx.EVT_CHOICE, self.comboBoxTargetAnimation_SelectionChanged)
        self.comboBoxCommonEvent.Bind(
            wx.EVT_CHOICE, self.comboBoxCommonEvent_SelectionChanged)
        self.spinCtrlPrice.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlPrice_ValueChanged)
        self.comboBoxConsumable.Bind(
            wx.EVT_CHOICE, self.comboBoxConsumable_SelectionChanged)
        self.comboBoxParameter.Bind(
            wx.EVT_CHOICE, self.comboBoxParameter_SelectionChanged)
        self.spinCtrlParameterInc.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlParameterInc_ValueChanged)
        self.spinCtrlRecrHPRate.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlRecrHPPercent_ValueChanged)
        self.spinCtrlRecrHP.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlRecrHP_ValueChanged)
        self.spinCtrlRecrSPRate.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlRecrSPPercent_ValueChanged)
        self.spinCtrlRecrSP.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlRecrSP_ValueChanged)
        self.spinCtrlHitRate.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlHitRate_ValueChanged)
        self.spinCtrlPDEF.Bind(wx.EVT_SPINCTRL, self.spinCtrlPDEF_ValueChanged)
        self.spinCtrlMDEF.Bind(wx.EVT_SPINCTRL, self.spinCtrlMDEF_ValueChanged)
        self.spinCtrlVariance.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlVariance_ValueChanged)
        self.checkListElements.Bind(
            wx.EVT_LEFT_DOWN, self.checkListElements_Clicked)
        self.checkListElements.Bind(
            wx.EVT_RIGHT_DOWN, self.checkListElements_Clicked)
        self.checkListStates.Bind(
            wx.EVT_LEFT_DOWN, self.checkListStates_LeftClicked)
        self.checkListStates.Bind(
            wx.EVT_RIGHT_DOWN, self.checkListStates_RightClicked)
        self.textCtrlNotes.Bind(wx.EVT_TEXT, self.textCtrlNotes_TextChanged)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def listBoxItems_SelectionChanged(self, event):
        event.Skip()

    def buttonMaximum_Clicked(self, event):
        event.Skip()

    def textCtrlName_TextChanged(self, event):
        event.Skip()

    def bitmapButtonIcon_Clicked(self, event):
        event.Skip()

    def textCtrlDescription_TextChange(self, event):
        event.Skip()

    def comboBoxScope_SelectionChanged(self, event):
        event.Skip()

    def comboBoxUserAnimation_SelectionChanged(self, event):
        event.Skip()

    def comboBoxMenuSE_Clicked(self, event):
        event.Skip()

    def bitmapButtonAudioTest_Clicked(self, event):
        event.Skip()

    def comboBoxOccasion_SelectionChanged(self, event):
        event.Skip()

    def comboBoxTargetAnimation_SelectionChanged(self, event):
        event.Skip()

    def comboBoxCommonEvent_SelectionChanged(self, event):
        event.Skip()

    def spinCtrlPrice_ValueChanged(self, event):
        event.Skip()

    def comboBoxConsumable_SelectionChanged(self, event):
        event.Skip()

    def comboBoxParameter_SelectionChanged(self, event):
        event.Skip()

    def spinCtrlParameterInc_ValueChanged(self, event):
        event.Skip()

    def spinCtrlRecrHPPercent_ValueChanged(self, event):
        event.Skip()

    def spinCtrlRecrHP_ValueChanged(self, event):
        event.Skip()

    def spinCtrlRecrSPPercent_ValueChanged(self, event):
        event.Skip()

    def spinCtrlRecrSP_ValueChanged(self, event):
        event.Skip()

    def spinCtrlHitRate_ValueChanged(self, event):
        event.Skip()

    def spinCtrlPDEF_ValueChanged(self, event):
        event.Skip()

    def spinCtrlMDEF_ValueChanged(self, event):
        event.Skip()

    def spinCtrlVariance_ValueChanged(self, event):
        event.Skip()

    def checkListElements_Clicked(self, event):
        event.Skip()

    def checkListStates_LeftClicked(self, event):
        event.Skip()

    def checkListStates_RightClicked(self, event):
        event.Skip()

    def textCtrlNotes_TextChanged(self, event):
        event.Skip()


###########################################################################
# Class Weapons_Panel_Template
###########################################################################

class Weapons_Panel_Template (wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(
            800, 600), style=wx.TAB_TRAVERSAL)

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        WeaponsListSizer = wx.BoxSizer(wx.VERTICAL)

        self.bitmapWeapons = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(
            150, 26), wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)
        self.bitmapWeapons.SetMinSize(wx.Size(150, 26))
        self.bitmapWeapons.SetMaxSize(wx.Size(150, 26))

        WeaponsListSizer.Add(self.bitmapWeapons, 0, wx.ALL | wx.EXPAND, 5)

        listBoxWeaponsChoices = []
        self.listBoxWeapons = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(
            184, -1), listBoxWeaponsChoices, wx.LB_SINGLE | wx.CLIP_CHILDREN)
        WeaponsListSizer.Add(
            self.listBoxWeapons, 1, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        self.buttonMaximum = wx.Button(self, wx.ID_ANY, _(
            "Change Maximum..."), wx.DefaultPosition, wx.Size(150, -1), 0)
        WeaponsListSizer.Add(self.buttonMaximum, 0, wx.ALL | wx.EXPAND, 5)

        MainSizer.Add(WeaponsListSizer, 0, wx.EXPAND, 5)

        staticSizerWeapons = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.HORIZONTAL)

        sizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer620 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer621 = wx.BoxSizer(wx.VERTICAL)

        self.labelName = wx.StaticText(staticSizerWeapons.GetStaticBox(), wx.ID_ANY, _(
            "Name:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelName.Wrap(-1)
        bSizer621.Add(self.labelName, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlName = wx.TextCtrl(staticSizerWeapons.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlName.SetMaxLength(0)
        bSizer621.Add(
            self.textCtrlName, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        bSizer620.Add(bSizer621, 65, 0, 5)

        bSizer622 = wx.BoxSizer(wx.VERTICAL)

        self.labelIcon = wx.StaticText(staticSizerWeapons.GetStaticBox(), wx.ID_ANY, _(
            "Icon:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelIcon.Wrap(-1)
        bSizer622.Add(self.labelIcon, 0, wx.ALL | wx.EXPAND, 5)

        self.labelIconName = wx.StaticText(staticSizerWeapons.GetStaticBox(), wx.ID_ANY, _(
            "(Name of Icon)"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelIconName.Wrap(-1)
        bSizer622.Add(self.labelIconName, 0, wx.ALL | wx.EXPAND, 5)

        bSizer620.Add(bSizer622, 35, wx.EXPAND, 5)

        self.bitmapButtonIcon = wx.BitmapButton(staticSizerWeapons.GetStaticBox(
        ), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(32, 32), wx.BU_AUTODRAW)
        bSizer620.Add(self.bitmapButtonIcon, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        sizer1.Add(bSizer620, 0, wx.EXPAND, 5)

        self.labelDescription = wx.StaticText(staticSizerWeapons.GetStaticBox(
        ), wx.ID_ANY, _("Description:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelDescription.Wrap(-1)
        sizer1.Add(self.labelDescription, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlDescription = wx.TextCtrl(staticSizerWeapons.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlDescription.SetMaxLength(0)
        sizer1.Add(self.textCtrlDescription, 0, wx.EXPAND |
                   wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizer6 = wx.BoxSizer(wx.HORIZONTAL)

        sizer8 = wx.BoxSizer(wx.VERTICAL)

        self.labelUserAnimation = wx.StaticText(staticSizerWeapons.GetStaticBox(
        ), wx.ID_ANY, _("User Animation:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelUserAnimation.Wrap(-1)
        sizer8.Add(self.labelUserAnimation, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxUserAnimationChoices = [_("(None)")]
        self.comboBoxUserAnimation = wx.Choice(staticSizerWeapons.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxUserAnimationChoices, 0)
        self.comboBoxUserAnimation.SetSelection(0)
        sizer8.Add(self.comboBoxUserAnimation, 1, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizer6.Add(sizer8, 1, wx.EXPAND, 5)

        sizer9 = wx.BoxSizer(wx.VERTICAL)

        self.labelTargetAnimation = wx.StaticText(staticSizerWeapons.GetStaticBox(
        ), wx.ID_ANY, _("Target Animation:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelTargetAnimation.Wrap(-1)
        sizer9.Add(self.labelTargetAnimation, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxTargetAnimationChoices = [_("(None)")]
        self.comboBoxTargetAnimation = wx.Choice(staticSizerWeapons.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxTargetAnimationChoices, 0)
        self.comboBoxTargetAnimation.SetSelection(0)
        sizer9.Add(self.comboBoxTargetAnimation, 1, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizer6.Add(sizer9, 1, wx.EXPAND, 5)

        sizer1.Add(sizer6, 0, wx.EXPAND, 5)

        sizerParameters = wx.StaticBoxSizer(wx.StaticBox(
            staticSizerWeapons.GetStaticBox(), wx.ID_ANY, _("Parameters")), wx.VERTICAL)

        from .Extras import ParameterPanel
        self.panelParameters = ParameterPanel(self)
        sizerParameters.Add(self.panelParameters, 1, wx.EXPAND, 5)

        sizer1.Add(sizerParameters, 1, wx.EXPAND | wx.ALL, 5)

        staticSizerWeapons.Add(sizer1, 60, wx.EXPAND, 5)

        sizer2 = wx.BoxSizer(wx.VERTICAL)

        sizer14 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelElements = wx.StaticText(staticSizerWeapons.GetStaticBox(), wx.ID_ANY, _(
            "Element:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelElements.Wrap(-1)
        sizer14.Add(self.labelElements, 1, wx.ALL | wx.EXPAND, 5)

        self.labelStates = wx.StaticText(staticSizerWeapons.GetStaticBox(), wx.ID_ANY, _(
            "State Change:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelStates.Wrap(-1)
        sizer14.Add(self.labelStates, 1, wx.ALL | wx.EXPAND, 5)

        sizer2.Add(sizer14, 0, wx.EXPAND, 5)

        sizer15 = wx.BoxSizer(wx.HORIZONTAL)

        from .Extras import ImageCheckList
        from .Extras import DatabaseManager as DM
        states = [False, True]
        images = DM.GetNormalCheckImageList()
        self.checkListElements = ImageCheckList(self, states, images)
        sizer15.Add(
            self.checkListElements, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        states = [0, 1, -1]
        images = DM.GetAddSubImageList()
        self.checkListStates = ImageCheckList(self, states, images)
        sizer15.Add(
            self.checkListStates, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizer2.Add(sizer15, 1, wx.EXPAND, 5)

        self.labelNotes = wx.StaticText(staticSizerWeapons.GetStaticBox(), wx.ID_ANY, _(
            "Notes:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelNotes.Wrap(-1)
        sizer2.Add(self.labelNotes, 0, wx.ALL, 5)

        self.textCtrlNotes = wx.TextCtrl(staticSizerWeapons.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.CLIP_CHILDREN)
        
        sizer2.Add(
            self.textCtrlNotes, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        staticSizerWeapons.Add(sizer2, 40, wx.EXPAND, 5)

        MainSizer.Add(staticSizerWeapons, 75, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        # Connect Events
        self.listBoxWeapons.Bind(
            wx.EVT_LISTBOX, self.listBoxWeapons_SelectionChanged)
        self.buttonMaximum.Bind(wx.EVT_BUTTON, self.buttonMaximum_Clicked)
        self.textCtrlName.Bind(wx.EVT_TEXT, self.textCtrlName_TextChanged)
        self.bitmapButtonIcon.Bind(
            wx.EVT_BUTTON, self.bitmapButtonIcon_Clicked)
        self.textCtrlDescription.Bind(
            wx.EVT_TEXT, self.textCtrlDescription_TextChange)
        self.comboBoxUserAnimation.Bind(
            wx.EVT_CHOICE, self.comboBoxUserAnimation_SelectionChanged)
        self.comboBoxTargetAnimation.Bind(
            wx.EVT_CHOICE, self.comboBoxTargetAnimation_SelectionChanged)
        self.checkListElements.Bind(
            wx.EVT_LEFT_DOWN, self.checkListElements_Clicked)
        self.checkListElements.Bind(
            wx.EVT_RIGHT_DOWN, self.checkListElements_Clicked)
        self.checkListStates.Bind(
            wx.EVT_LEFT_DOWN, self.checkListStates_LeftClicked)
        self.checkListStates.Bind(
            wx.EVT_RIGHT_DOWN, self.checkListStates_RightClicked)
        self.textCtrlNotes.Bind(wx.EVT_TEXT, self.textCtrlNotes_TextChanged)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def listBoxWeapons_SelectionChanged(self, event):
        event.Skip()

    def buttonMaximum_Clicked(self, event):
        event.Skip()

    def textCtrlName_TextChanged(self, event):
        event.Skip()

    def bitmapButtonIcon_Clicked(self, event):
        event.Skip()

    def textCtrlDescription_TextChange(self, event):
        event.Skip()

    def comboBoxUserAnimation_SelectionChanged(self, event):
        event.Skip()

    def comboBoxTargetAnimation_SelectionChanged(self, event):
        event.Skip()

    def checkListElements_Clicked(self, event):
        event.Skip()

    def checkListStates_LeftClicked(self, event):
        event.Skip()

    def checkListStates_RightClicked(self, event):
        event.Skip()

    def textCtrlNotes_TextChanged(self, event):
        event.Skip()


###########################################################################
# Class Armors_Panel_Template
###########################################################################

class Armors_Panel_Template (wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(
            800, 600), style=wx.TAB_TRAVERSAL)

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        ArmorsListSizer = wx.BoxSizer(wx.VERTICAL)

        self.bitmapArmors = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(
            150, 26), wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)
        self.bitmapArmors.SetMinSize(wx.Size(150, 26))
        self.bitmapArmors.SetMaxSize(wx.Size(150, 26))

        ArmorsListSizer.Add(self.bitmapArmors, 0, wx.ALL | wx.EXPAND, 5)

        listBoxArmorsChoices = []
        self.listBoxArmors = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(
            184, -1), listBoxArmorsChoices, wx.LB_SINGLE | wx.CLIP_CHILDREN)
        ArmorsListSizer.Add(
            self.listBoxArmors, 1, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        self.buttonMaximum = wx.Button(self, wx.ID_ANY, _(
            "Change Maximum..."), wx.DefaultPosition, wx.Size(150, -1), 0)
        ArmorsListSizer.Add(self.buttonMaximum, 0, wx.ALL | wx.EXPAND, 5)

        MainSizer.Add(ArmorsListSizer, 0, wx.EXPAND, 5)

        staticSizerArmors = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.HORIZONTAL)

        sizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer620 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer621 = wx.BoxSizer(wx.VERTICAL)

        self.labelName = wx.StaticText(staticSizerArmors.GetStaticBox(), wx.ID_ANY, _(
            "Name:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelName.Wrap(-1)
        bSizer621.Add(self.labelName, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlName = wx.TextCtrl(staticSizerArmors.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlName.SetMaxLength(0)
        bSizer621.Add(
            self.textCtrlName, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        bSizer620.Add(bSizer621, 65, 0, 5)

        bSizer622 = wx.BoxSizer(wx.VERTICAL)

        self.labelIcon = wx.StaticText(staticSizerArmors.GetStaticBox(), wx.ID_ANY, _(
            "Icon:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelIcon.Wrap(-1)
        bSizer622.Add(self.labelIcon, 0, wx.ALL | wx.EXPAND, 5)

        self.labelIconName = wx.StaticText(staticSizerArmors.GetStaticBox(), wx.ID_ANY, _(
            "(Name of Icon)"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelIconName.Wrap(-1)
        bSizer622.Add(self.labelIconName, 0, wx.ALL | wx.EXPAND, 5)

        bSizer620.Add(bSizer622, 35, wx.EXPAND, 5)

        self.bitmapButtonIcon = wx.BitmapButton(staticSizerArmors.GetStaticBox(
        ), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(32, 32), wx.BU_AUTODRAW)
        bSizer620.Add(self.bitmapButtonIcon, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        sizer1.Add(bSizer620, 0, wx.EXPAND | wx.ALIGN_RIGHT, 5)

        self.labelDescription = wx.StaticText(staticSizerArmors.GetStaticBox(
        ), wx.ID_ANY, _("Description:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelDescription.Wrap(-1)
        sizer1.Add(self.labelDescription, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlDescription = wx.TextCtrl(staticSizerArmors.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlDescription.SetMaxLength(0)
        sizer1.Add(self.textCtrlDescription, 0, wx.EXPAND |
                   wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizer6 = wx.BoxSizer(wx.HORIZONTAL)

        sizer8 = wx.BoxSizer(wx.VERTICAL)

        self.labelKindAnimation = wx.StaticText(staticSizerArmors.GetStaticBox(
        ), wx.ID_ANY, _("Kind:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelKindAnimation.Wrap(-1)
        sizer8.Add(self.labelKindAnimation, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxKindChoices = [
            _("Shield"), _("Helmet"), _("Body Armor"), _("Accessory")]
        self.comboBoxKind = wx.Choice(staticSizerArmors.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxKindChoices, 0)
        self.comboBoxKind.SetSelection(0)
        sizer8.Add(
            self.comboBoxKind, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizer6.Add(sizer8, 1, wx.EXPAND, 5)

        sizer9 = wx.BoxSizer(wx.VERTICAL)

        self.labelAutoState = wx.StaticText(staticSizerArmors.GetStaticBox(), wx.ID_ANY, _(
            "Auto State:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelAutoState.Wrap(-1)
        sizer9.Add(self.labelAutoState, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxAutoStateChoices = [_("(None)")]
        self.comboBoxAutoState = wx.Choice(staticSizerArmors.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxAutoStateChoices, 0)
        self.comboBoxAutoState.SetSelection(0)
        sizer9.Add(self.comboBoxAutoState, 1, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizer6.Add(sizer9, 1, wx.EXPAND, 5)

        sizer1.Add(sizer6, 0, wx.EXPAND, 5)

        sizerParameters = wx.StaticBoxSizer(wx.StaticBox(
            staticSizerArmors.GetStaticBox(), wx.ID_ANY, _("Parameters")), wx.VERTICAL)

        from .Extras import ParameterPanel
        self.panelParameters = ParameterPanel(self)
        sizerParameters.Add(self.panelParameters, 1, wx.EXPAND, 5)

        sizer1.Add(sizerParameters, 1, wx.EXPAND | wx.ALL, 5)

        staticSizerArmors.Add(sizer1, 60, wx.EXPAND, 5)

        sizer2 = wx.BoxSizer(wx.VERTICAL)

        sizer14 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelElements = wx.StaticText(staticSizerArmors.GetStaticBox(), wx.ID_ANY, _(
            "Element Defense:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelElements.Wrap(-1)
        sizer14.Add(self.labelElements, 1, wx.ALL | wx.EXPAND, 5)

        self.labelStates = wx.StaticText(staticSizerArmors.GetStaticBox(), wx.ID_ANY, _(
            "State Defense:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelStates.Wrap(-1)
        sizer14.Add(self.labelStates, 1, wx.ALL | wx.EXPAND, 5)

        sizer2.Add(sizer14, 0, wx.EXPAND, 5)

        sizer15 = wx.BoxSizer(wx.HORIZONTAL)

        from .Extras import ImageCheckList
        from .Extras import DatabaseManager as DM
        states = [False, True]
        images = DM.GetNormalCheckImageList()
        self.checkListElements = ImageCheckList(self, states, images)
        sizer15.Add(
            self.checkListElements, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        states = [0, 1, -1]
        images = DM.GetAddSubImageList()
        self.checkListStates = ImageCheckList(self, states, images)
        sizer15.Add(
            self.checkListStates, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizer2.Add(sizer15, 1, wx.EXPAND, 5)

        self.labelNotes = wx.StaticText(staticSizerArmors.GetStaticBox(), wx.ID_ANY, _(
            "Notes:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelNotes.Wrap(-1)
        sizer2.Add(self.labelNotes, 0, wx.ALL, 5)

        self.textCtrlNotes = wx.TextCtrl(staticSizerArmors.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.CLIP_CHILDREN)
        
        sizer2.Add(
            self.textCtrlNotes, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        staticSizerArmors.Add(sizer2, 40, wx.EXPAND, 5)

        MainSizer.Add(staticSizerArmors, 75, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        # Connect Events
        self.listBoxArmors.Bind(
            wx.EVT_LISTBOX, self.listBoxArmors_SelectionChanged)
        self.buttonMaximum.Bind(wx.EVT_BUTTON, self.buttonMaximum_Clicked)
        self.textCtrlName.Bind(wx.EVT_TEXT, self.textCtrlName_TextChanged)
        self.bitmapButtonIcon.Bind(
            wx.EVT_BUTTON, self.bitmapButtonIcon_Clicked)
        self.textCtrlDescription.Bind(
            wx.EVT_TEXT, self.textCtrlDescription_TextChange)
        self.comboBoxKind.Bind(
            wx.EVT_CHOICE, self.comboBoxKind_SelectionChanged)
        self.comboBoxAutoState.Bind(
            wx.EVT_CHOICE, self.comboBoxAutoState_SelectionChanged)
        self.checkListElements.Bind(
            wx.EVT_LEFT_DOWN, self.checkListElements_Clicked)
        self.checkListElements.Bind(
            wx.EVT_RIGHT_DOWN, self.checkListElements_Clicked)
        self.checkListStates.Bind(
            wx.EVT_LEFT_DOWN, self.checkListStates_Clicked)
        self.checkListStates.Bind(
            wx.EVT_RIGHT_DOWN, self.checkListStates_Clicked)
        self.textCtrlNotes.Bind(wx.EVT_TEXT, self.textCtrlNotes_TextChanged)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def listBoxArmors_SelectionChanged(self, event):
        event.Skip()

    def buttonMaximum_Clicked(self, event):
        event.Skip()

    def textCtrlName_TextChanged(self, event):
        event.Skip()

    def bitmapButtonIcon_Clicked(self, event):
        event.Skip()

    def textCtrlDescription_TextChange(self, event):
        event.Skip()

    def comboBoxKind_SelectionChanged(self, event):
        event.Skip()

    def comboBoxAutoState_SelectionChanged(self, event):
        event.Skip()

    def checkListElements_Clicked(self, event):
        event.Skip()

    def checkListStates_Clicked(self, event):
        event.Skip()

    def textCtrlNotes_TextChanged(self, event):
        event.Skip()


###########################################################################
# Class Enemies_Panel_Template
###########################################################################

class Enemies_Panel_Template (wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(
            800, 600), style=wx.TAB_TRAVERSAL)

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        EnemiesListSizer = wx.BoxSizer(wx.VERTICAL)

        self.bitmapEnemies = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(
            150, 26), wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)
        self.bitmapEnemies.SetMinSize(wx.Size(150, 26))
        self.bitmapEnemies.SetMaxSize(wx.Size(150, 26))

        EnemiesListSizer.Add(self.bitmapEnemies, 0, wx.ALL | wx.EXPAND, 5)

        listBoxEnemiesChoices = []
        self.listBoxEnemies = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(
            184, -1), listBoxEnemiesChoices, wx.LB_SINGLE | wx.CLIP_CHILDREN)
        EnemiesListSizer.Add(
            self.listBoxEnemies, 1, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        self.buttonMaximum = wx.Button(self, wx.ID_ANY, _(
            "Change Maximum..."), wx.DefaultPosition, wx.Size(150, -1), 0)
        EnemiesListSizer.Add(self.buttonMaximum, 0, wx.ALL | wx.EXPAND, 5)

        MainSizer.Add(EnemiesListSizer, 0, wx.EXPAND, 5)

        staticSizerEnemies = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        sizer1 = wx.BoxSizer(wx.HORIZONTAL)

        sizer2 = wx.BoxSizer(wx.VERTICAL)

        self.labelName = wx.StaticText(staticSizerEnemies.GetStaticBox(), wx.ID_ANY, _(
            "Name:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelName.Wrap(-1)
        sizer2.Add(self.labelName, 0, wx.ALL, 5)

        self.textCtrlName = wx.TextCtrl(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlName.SetMaxLength(0)
        sizer2.Add(
            self.textCtrlName, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelBattlerGraphic = wx.StaticText(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, _("Battler Graphic:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelBattlerGraphic.Wrap(-1)
        sizer2.Add(self.labelBattlerGraphic, 0, wx.ALL, 5)

        self.panelEnemyGraphic = wx.Panel(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        sizerEnemyGraphic = wx.BoxSizer(wx.VERTICAL)

        from .Extras import EditorGLPanel
        parent = self.panelEnemyGraphic
        self.glCanvasEnemyGraphic = EditorGLPanel(parent, -1, 1, 1, (0, 0,), 1)
        sizerEnemyGraphic.Add(
            self.glCanvasEnemyGraphic, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 0)

        self.panelEnemyGraphic.SetSizer(sizerEnemyGraphic)
        self.panelEnemyGraphic.Layout()
        sizerEnemyGraphic.Fit(self.panelEnemyGraphic)
        sizer2.Add(self.panelEnemyGraphic, 1, wx.EXPAND | wx.ALL, 5)

        self.labelAttackAnimation = wx.StaticText(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, _("Attack Animation:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelAttackAnimation.Wrap(-1)
        sizer2.Add(self.labelAttackAnimation, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxAttackAnimationChoices = [_("(None)")]
        self.comboBoxAttackAnimation = wx.Choice(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxAttackAnimationChoices, 0)
        self.comboBoxAttackAnimation.SetSelection(0)
        sizer2.Add(self.comboBoxAttackAnimation, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelTargetAnimation = wx.StaticText(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, _("Target Animation:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelTargetAnimation.Wrap(-1)
        sizer2.Add(self.labelTargetAnimation, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxTargetAnimationChoices = [_("(None)")]
        self.comboBoxTargetAnimation = wx.Choice(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxTargetAnimationChoices, 0)
        self.comboBoxTargetAnimation.SetSelection(0)
        sizer2.Add(self.comboBoxTargetAnimation, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizer1.Add(sizer2, 30, wx.EXPAND, 5)

        sizer3 = wx.BoxSizer(wx.VERTICAL)

        self.labelDescription = wx.StaticText(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, _("Description:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelDescription.Wrap(-1)
        sizer3.Add(self.labelDescription, 0, wx.ALL, 5)

        self.textCtrlDescription = wx.TextCtrl(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlDescription.SetMaxLength(0)
        sizer3.Add(self.textCtrlDescription, 0, wx.EXPAND |
                   wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerParameters = wx.StaticBoxSizer(wx.StaticBox(
            staticSizerEnemies.GetStaticBox(), wx.ID_ANY, _("Parameters")), wx.VERTICAL)

        from .Extras import ParameterPanel
        self.panelParameters = ParameterPanel(self)
        sizerParameters.Add(self.panelParameters, 1, wx.EXPAND, 5)

        sizer3.Add(sizerParameters, 1, wx.EXPAND | wx.ALL, 5)

        sizerDummyFiller = wx.BoxSizer(wx.VERTICAL)

        sizer3.Add(sizerDummyFiller, 0, wx.EXPAND, 5)

        bSizer628 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer629 = wx.BoxSizer(wx.VERTICAL)

        self.labelExp = wx.StaticText(staticSizerEnemies.GetStaticBox(), wx.ID_ANY, _(
            "Experience:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelExp.Wrap(-1)
        bSizer629.Add(self.labelExp, 0, wx.ALL, 5)

        self.comboBoxExp = wx.adv.BitmapComboBox(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, "", wx.CB_READONLY)
        bSizer629.Add(
            self.comboBoxExp, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        bSizer628.Add(bSizer629, 1, 0, 5)

        bSizer630 = wx.BoxSizer(wx.VERTICAL)

        self.labelGold = wx.StaticText(staticSizerEnemies.GetStaticBox(), wx.ID_ANY, _(
            "Gold:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelGold.Wrap(-1)
        bSizer630.Add(self.labelGold, 0, wx.ALL, 5)

        self.comboBoxGold = wx.adv.BitmapComboBox(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, "", wx.CB_READONLY)
        bSizer630.Add(
            self.comboBoxGold, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        bSizer628.Add(bSizer630, 1, 0, 5)

        sizer3.Add(bSizer628, 0, wx.EXPAND, 5)

        self.labelTreasure = wx.StaticText(staticSizerEnemies.GetStaticBox(), wx.ID_ANY, _(
            "Treasure(s):"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelTreasure.Wrap(-1)
        sizer3.Add(self.labelTreasure, 0, wx.ALL | wx.EXPAND, 5)

        self.comboBoxTreasure = wx.adv.BitmapComboBox(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, "", wx.CB_READONLY)
        sizer3.Add(self.comboBoxTreasure, 0, wx.EXPAND |
                   wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizer1.Add(sizer3, 50, wx.EXPAND, 5)

        sizer4 = wx.BoxSizer(wx.VERTICAL)

        self.labelElements = wx.StaticText(staticSizerEnemies.GetStaticBox(), wx.ID_ANY, _(
            "Element Efficiency:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelElements.Wrap(-1)
        sizer4.Add(self.labelElements, 0, wx.ALL | wx.EXPAND, 5)

        from .Extras import ImageCheckList
        from .Extras import DatabaseManager as DM
        states = [0, 1, -1]
        images = DM.GetAddSubImageList()
        self.checkListElements = ImageCheckList(self, states, images)
        sizer4.Add(self.checkListElements, 1, wx.EXPAND |
                   wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelStates = wx.StaticText(staticSizerEnemies.GetStaticBox(), wx.ID_ANY, _(
            "State Efficiency:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelStates.Wrap(-1)
        sizer4.Add(self.labelStates, 0, wx.ALL | wx.EXPAND, 5)

        states = [0, 1, -1]
        images = DM.GetAddSubImageList()
        self.checkListStates = ImageCheckList(self, states, images)
        sizer4.Add(self.checkListStates, 1, wx.EXPAND |
                   wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizer1.Add(sizer4, 20, wx.EXPAND, 5)

        staticSizerEnemies.Add(sizer1, 70, wx.EXPAND, 5)

        bSizer624 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer625 = wx.BoxSizer(wx.VERTICAL)

        self.labelAction = wx.StaticText(staticSizerEnemies.GetStaticBox(), wx.ID_ANY, _(
            "Action:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelAction.Wrap(-1)
        bSizer625.Add(self.labelAction, 0, wx.ALL | wx.EXPAND, 5)

        self.listCtrlActions = wx.ListCtrl(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        bSizer625.Add(
            self.listCtrlActions, 30, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        bSizer624.Add(bSizer625, 60, wx.EXPAND, 5)

        bSizer626 = wx.BoxSizer(wx.VERTICAL)

        self.labelNotes = wx.StaticText(staticSizerEnemies.GetStaticBox(), wx.ID_ANY, _(
            "Notes:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelNotes.Wrap(-1)
        bSizer626.Add(self.labelNotes, 0, wx.ALL, 5)

        self.textCtrlNotes = wx.TextCtrl(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.CLIP_CHILDREN)
        
        self.textCtrlNotes.SetToolTipString(
            _("Any user notes for this item. These notes can also be referenced via scripts."))

        bSizer626.Add(
            self.textCtrlNotes, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        bSizer624.Add(bSizer626, 40, wx.EXPAND, 5)

        staticSizerEnemies.Add(bSizer624, 30, wx.EXPAND, 5)

        MainSizer.Add(staticSizerEnemies, 75, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        # Connect Events
        self.listBoxEnemies.Bind(
            wx.EVT_LISTBOX, self.listBoxEnemies_SelectionChanged)
        self.buttonMaximum.Bind(wx.EVT_BUTTON, self.buttonMaximum_Clicked)
        self.textCtrlName.Bind(wx.EVT_TEXT, self.textCtrlName_ValueChanged)
        self.comboBoxAttackAnimation.Bind(
            wx.EVT_CHOICE, self.comboBoxAttackAnimation_SelectionChanged)
        self.comboBoxTargetAnimation.Bind(
            wx.EVT_CHOICE, self.comboBoxTargetAnimation_ValueChanged)
        self.textCtrlDescription.Bind(
            wx.EVT_TEXT, self.textCtrlDescription_TextChanged)
        self.comboBoxExp.Bind(wx.EVT_LEFT_DOWN, self.comboBoxExp_Clicked)
        self.comboBoxGold.Bind(wx.EVT_LEFT_DOWN, self.comboBoxGold_Clicked)
        self.comboBoxTreasure.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxTreasure_Clicked)
        self.checkListElements.Bind(
            wx.EVT_LEFT_DOWN, self.checkListStates_LeftClicked)
        self.checkListElements.Bind(
            wx.EVT_RIGHT_DOWN, self.checkListStates_RightClicked)
        self.checkListStates.Bind(
            wx.EVT_LEFT_DOWN, self.checkListStates_LeftClicked)
        self.checkListStates.Bind(
            wx.EVT_RIGHT_DOWN, self.checkListStates_RightClicked)
        self.listCtrlActions.Bind(
            wx.EVT_LEFT_DCLICK, self.listCtrlAction_DoubleClick)
        self.textCtrlNotes.Bind(wx.EVT_TEXT, self.textCtrlNotes_TextChanged)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def listBoxEnemies_SelectionChanged(self, event):
        event.Skip()

    def buttonMaximum_Clicked(self, event):
        event.Skip()

    def textCtrlName_ValueChanged(self, event):
        event.Skip()

    def comboBoxAttackAnimation_SelectionChanged(self, event):
        event.Skip()

    def comboBoxTargetAnimation_ValueChanged(self, event):
        event.Skip()

    def textCtrlDescription_TextChanged(self, event):
        event.Skip()

    def comboBoxExp_Clicked(self, event):
        event.Skip()

    def comboBoxGold_Clicked(self, event):
        event.Skip()

    def comboBoxTreasure_Clicked(self, event):
        event.Skip()

    def checkListStates_LeftClicked(self, event):
        event.Skip()

    def checkListStates_RightClicked(self, event):
        event.Skip()

    def listCtrlAction_DoubleClick(self, event):
        event.Skip()

    def textCtrlNotes_TextChanged(self, event):
        event.Skip()


###########################################################################
# Class Troops_Panel_Template
###########################################################################

class Troops_Panel_Template (wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(
            800, 600), style=wx.TAB_TRAVERSAL)

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        TroopsListSizer = wx.BoxSizer(wx.VERTICAL)

        self.bitmapTroops = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(
            150, 26), wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)
        self.bitmapTroops.SetMinSize(wx.Size(150, 26))
        self.bitmapTroops.SetMaxSize(wx.Size(150, 26))

        TroopsListSizer.Add(self.bitmapTroops, 0, wx.ALL | wx.EXPAND, 5)

        listBoxTroopsChoices = []
        self.listBoxTroops = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(
            184, -1), listBoxTroopsChoices, wx.LB_SINGLE | wx.CLIP_CHILDREN)
        TroopsListSizer.Add(
            self.listBoxTroops, 1, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        self.buttonMaximum = wx.Button(self, wx.ID_ANY, _(
            "Change Maximum..."), wx.DefaultPosition, wx.Size(150, -1), 0)
        TroopsListSizer.Add(self.buttonMaximum, 0, wx.ALL | wx.EXPAND, 5)

        MainSizer.Add(TroopsListSizer, 0, wx.EXPAND, 5)

        staticSizerEnemies = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.labelName = wx.StaticText(staticSizerEnemies.GetStaticBox(), wx.ID_ANY, _(
            "Name:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelName.Wrap(-1)
        staticSizerEnemies.Add(self.labelName, 0, wx.ALL, 5)

        sizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.textCtrlName = wx.TextCtrl(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlName.SetMaxLength(0)
        sizer1.Add(self.textCtrlName, 40, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.buttonAutoname = wx.Button(staticSizerEnemies.GetStaticBox(), wx.ID_ANY, _(
            "Autoname"), wx.DefaultPosition, wx.Size(-1, -1), 0)
        sizer1.Add(self.buttonAutoname, 20, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.buttonBattleback = wx.Button(staticSizerEnemies.GetStaticBox(), wx.ID_ANY, _(
            "[ED] Battleback..."), wx.DefaultPosition, wx.Size(-1, -1), 0)
        sizer1.Add(
            self.buttonBattleback, 20, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.buttonBattleTest = wx.Button(staticSizerEnemies.GetStaticBox(), wx.ID_ANY, _(
            "Battle Test..."), wx.DefaultPosition, wx.Size(-1, -1), 0)
        sizer1.Add(
            self.buttonBattleTest, 20, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        staticSizerEnemies.Add(sizer1, 0, wx.EXPAND, 5)

        sizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.bitmapTroopLayout = wx.StaticBitmap(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER)
        sizer2.Add(self.bitmapTroopLayout, 70, wx.ALL | wx.EXPAND, 5)

        sizer4 = wx.BoxSizer(wx.VERTICAL)

        self.buttonAddEnemy = wx.Button(staticSizerEnemies.GetStaticBox(), wx.ID_ANY, _(
            "<"), wx.DefaultPosition, wx.Size(23, -1), 0)
        sizer4.Add(
            self.buttonAddEnemy, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.buttonRemoveEnemy = wx.Button(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, _(">"), wx.DefaultPosition, wx.Size(23, -1), 0)
        sizer4.Add(
            self.buttonRemoveEnemy, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.buttonClearTroops = wx.Button(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, _("C"), wx.DefaultPosition, wx.Size(23, -1), 0)
        sizer4.Add(
            self.buttonClearTroops, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.buttonAlignTroops = wx.Button(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, _("A"), wx.DefaultPosition, wx.Size(23, -1), 0)
        sizer4.Add(
            self.buttonAlignTroops, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        sizer2.Add(sizer4, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        listBoxEnemiesChoices = []
        self.listBoxEnemies = wx.ListBox(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxEnemiesChoices, 0)
        sizer2.Add(self.listBoxEnemies, 30, wx.ALL | wx.EXPAND, 5)

        staticSizerEnemies.Add(sizer2, 40, wx.EXPAND, 5)

        sizer3 = wx.BoxSizer(wx.HORIZONTAL)

        sizer5 = wx.BoxSizer(wx.VERTICAL)

        self.labelBattleEvent = wx.StaticText(staticSizerEnemies.GetStaticBox(
        ), wx.ID_ANY, _("Battle Event:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelBattleEvent.Wrap(-1)
        sizer5.Add(self.labelBattleEvent, 0, wx.ALL, 5)

        self.buttonNewPage = wx.Button(staticSizerEnemies.GetStaticBox(), wx.ID_ANY, _(
            "New\nEvent Page"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizer5.Add(self.buttonNewPage, 1, wx.ALL, 5)

        self.buttonCopyPage = wx.Button(staticSizerEnemies.GetStaticBox(), wx.ID_ANY, _(
            "Copy\nEvent Page"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizer5.Add(self.buttonCopyPage, 1, wx.ALL, 5)

        self.buttonPastePage = wx.Button(staticSizerEnemies.GetStaticBox(), wx.ID_ANY, _(
            "Paste\nEvent Page"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizer5.Add(self.buttonPastePage, 1, wx.ALL, 5)

        self.buttonDeletePage = wx.Button(staticSizerEnemies.GetStaticBox(), wx.ID_ANY, _(
            "Delete\nEvent Page"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizer5.Add(self.buttonDeletePage, 1, wx.ALL, 5)

        self.buttonClearPage = wx.Button(staticSizerEnemies.GetStaticBox(), wx.ID_ANY, _(
            "Clear\nEvent Page"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizer5.Add(self.buttonClearPage, 1, wx.ALL, 5)

        sizer3.Add(sizer5, 0, wx.EXPAND, 5)

        self.notebookEventsTabControl = wx.Notebook(
            staticSizerEnemies.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.panelEventPageTemplate = wx.Panel(
            self.notebookEventsTabControl, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizerPage = wx.BoxSizer(wx.VERTICAL)

        sizerPageControls = wx.BoxSizer(wx.HORIZONTAL)

        self.labelCondition = wx.StaticText(self.panelEventPageTemplate, wx.ID_ANY, _(
            "Condition:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelCondition.Wrap(-1)
        sizerPageControls.Add(
            self.labelCondition, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        comboBoxConditionChoices = []
        self.comboBoxCondition = wx.ComboBox(self.panelEventPageTemplate, wx.ID_ANY, _(
            "Don't Run"), wx.DefaultPosition, wx.DefaultSize, comboBoxConditionChoices, 0)
        sizerPageControls.Add(
            self.comboBoxCondition, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.labelSpan = wx.StaticText(self.panelEventPageTemplate, wx.ID_ANY, _(
            "Span:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelSpan.Wrap(-1)
        sizerPageControls.Add(
            self.labelSpan, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        comboBoxSpanChoices = [_("Battle"), _("Turn"), _("Moment")]
        self.comboBoxSpan = wx.Choice(
            self.panelEventPageTemplate, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxSpanChoices, 0)
        self.comboBoxSpan.SetSelection(0)
        sizerPageControls.Add(
            self.comboBoxSpan, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sizerPage.Add(sizerPageControls, 0, wx.EXPAND, 5)

        listBoxEventsChoices = [_(">@")]
        self.listBoxEvents = wx.ListBox(
            self.panelEventPageTemplate, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxEventsChoices, 0)
        sizerPage.Add(self.listBoxEvents, 1, wx.ALL | wx.EXPAND, 5)

        self.panelEventPageTemplate.SetSizer(sizerPage)
        self.panelEventPageTemplate.Layout()
        sizerPage.Fit(self.panelEventPageTemplate)
        self.notebookEventsTabControl.AddPage(
            self.panelEventPageTemplate, _("1"), False)

        sizer3.Add(self.notebookEventsTabControl, 1, wx.ALL | wx.EXPAND, 5)

        staticSizerEnemies.Add(sizer3, 60, wx.EXPAND, 5)

        MainSizer.Add(staticSizerEnemies, 75, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        # Connect Events
        self.listBoxTroops.Bind(
            wx.EVT_LISTBOX, self.listBoxTroops_SelectionChanged)
        self.buttonMaximum.Bind(wx.EVT_BUTTON, self.buttonMaximum_Clicked)
        self.textCtrlName.Bind(wx.EVT_TEXT, self.textCtrlName_ValueChanged)
        self.buttonAutoname.Bind(wx.EVT_BUTTON, self.buttonAutoname_Clicked)
        self.buttonBattleback.Bind(wx.EVT_BUTTON, self.buttonBattleback_Click)
        self.buttonBattleTest.Bind(wx.EVT_BUTTON, self.buttonBattleTest_Click)
        self.buttonAddEnemy.Bind(wx.EVT_BUTTON, self.buttonAddEnemy_Click)
        self.buttonRemoveEnemy.Bind(
            wx.EVT_BUTTON, self.buttonRemoveEnemy_Click)
        self.buttonClearTroops.Bind(wx.EVT_BUTTON, self.buttonClearTroop_Click)
        self.buttonAlignTroops.Bind(wx.EVT_BUTTON, self.buttonAlignTroop_Click)
        self.listBoxEnemies.Bind(
            wx.EVT_LISTBOX, self.listBoxEnemies_SelectionChanged)
        self.buttonNewPage.Bind(wx.EVT_BUTTON, self.buttonNewEventPage_Click)
        self.buttonCopyPage.Bind(wx.EVT_BUTTON, self.buttonCopyEventPage_Click)
        self.buttonPastePage.Bind(
            wx.EVT_BUTTON, self.buttonPasteEventPage_Click)
        self.buttonDeletePage.Bind(
            wx.EVT_BUTTON, self.buttonDeleteEventPage_Click)
        self.buttonClearPage.Bind(
            wx.EVT_BUTTON, self.buttonClearEventPage_Click)
        self.comboBoxCondition.Bind(
            wx.EVT_LEFT_UP, self.comboBoxCondition_Clicked)
        self.comboBoxSpan.Bind(wx.EVT_CHOICE, self.comboBoxSpan_ValueChanged)
        self.listBoxEvents.Bind(
            wx.EVT_LEFT_DCLICK, self.listBoxEvents_DoubleClick)
        self.listBoxEvents.Bind(
            wx.EVT_LISTBOX_DCLICK, self.listBoxEvents_DoubleClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def listBoxTroops_SelectionChanged(self, event):
        event.Skip()

    def buttonMaximum_Clicked(self, event):
        event.Skip()

    def textCtrlName_ValueChanged(self, event):
        event.Skip()

    def buttonAutoname_Clicked(self, event):
        event.Skip()

    def buttonBattleback_Click(self, event):
        event.Skip()

    def buttonBattleTest_Click(self, event):
        event.Skip()

    def buttonAddEnemy_Click(self, event):
        event.Skip()

    def buttonRemoveEnemy_Click(self, event):
        event.Skip()

    def buttonClearTroop_Click(self, event):
        event.Skip()

    def buttonAlignTroop_Click(self, event):
        event.Skip()

    def listBoxEnemies_SelectionChanged(self, event):
        event.Skip()

    def buttonNewEventPage_Click(self, event):
        event.Skip()

    def buttonCopyEventPage_Click(self, event):
        event.Skip()

    def buttonPasteEventPage_Click(self, event):
        event.Skip()

    def buttonDeleteEventPage_Click(self, event):
        event.Skip()

    def buttonClearEventPage_Click(self, event):
        event.Skip()

    def comboBoxCondition_Clicked(self, event):
        event.Skip()

    def comboBoxSpan_ValueChanged(self, event):
        event.Skip()

    def listBoxEvents_DoubleClick(self, event):
        event.Skip()


###########################################################################
# Class States_Panel_Template
###########################################################################

class States_Panel_Template (wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(
            1034, 600), style=wx.TAB_TRAVERSAL)

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        StatesListSizer = wx.BoxSizer(wx.VERTICAL)

        self.bitmapStates = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(
            150, 26), wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)
        self.bitmapStates.SetMinSize(wx.Size(150, 26))
        self.bitmapStates.SetMaxSize(wx.Size(150, 26))

        StatesListSizer.Add(self.bitmapStates, 0, wx.ALL | wx.EXPAND, 5)

        listBoxStatesChoices = []
        self.listBoxStates = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(
            184, -1), listBoxStatesChoices, wx.LB_SINGLE | wx.CLIP_CHILDREN)
        StatesListSizer.Add(
            self.listBoxStates, 1, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        self.buttonMaximum = wx.Button(self, wx.ID_ANY, _(
            "Change Maximum..."), wx.DefaultPosition, wx.Size(150, -1), 0)
        StatesListSizer.Add(self.buttonMaximum, 0, wx.ALL | wx.EXPAND, 5)

        MainSizer.Add(StatesListSizer, 0, wx.EXPAND, 5)

        staticSizerStates = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.HORIZONTAL)

        sizer1 = wx.BoxSizer(wx.VERTICAL)

        sizer4 = wx.BoxSizer(wx.HORIZONTAL)

        sizer12 = wx.BoxSizer(wx.VERTICAL)

        self.labelName = wx.StaticText(staticSizerStates.GetStaticBox(), wx.ID_ANY, _(
            "Name:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelName.Wrap(-1)
        sizer12.Add(self.labelName, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlName = wx.TextCtrl(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlName.SetMaxLength(0)
        sizer12.Add(
            self.textCtrlName, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelAnimation = wx.StaticText(staticSizerStates.GetStaticBox(), wx.ID_ANY, _(
            "Animation:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelAnimation.Wrap(-1)
        sizer12.Add(self.labelAnimation, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxAnimationChoices = []
        self.comboBoxAnimation = wx.Choice(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxAnimationChoices, 0)
        self.comboBoxAnimation.SetSelection(0)
        sizer12.Add(
            self.comboBoxAnimation, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelRestriction = wx.StaticText(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, _("Restriction:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelRestriction.Wrap(-1)
        sizer12.Add(self.labelRestriction, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxRestrictionChoices = []
        self.comboBoxRestriction = wx.Choice(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxRestrictionChoices, 0)
        self.comboBoxRestriction.SetSelection(0)
        sizer12.Add(self.comboBoxRestriction, 0, wx.BOTTOM |
                    wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizer4.Add(sizer12, 1, wx.EXPAND, 5)

        sizerParameters = wx.StaticBoxSizer(wx.StaticBox(
            staticSizerStates.GetStaticBox(), wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.checkBoxNonresistance = wx.CheckBox(sizerParameters.GetStaticBox(
        ), wx.ID_ANY, _("Nonresistance"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerParameters.Add(
            self.checkBoxNonresistance, 0, wx.ALL | wx.EXPAND, 5)

        self.checkBoxRegardHP0 = wx.CheckBox(sizerParameters.GetStaticBox(), wx.ID_ANY, _(
            "Regard as HP 0"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerParameters.Add(self.checkBoxRegardHP0, 0, wx.ALL | wx.EXPAND, 5)

        self.checkBoxNoExp = wx.CheckBox(sizerParameters.GetStaticBox(), wx.ID_ANY, _(
            "Can't Get EXP"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerParameters.Add(self.checkBoxNoExp, 0, wx.ALL, 5)

        self.checkBoxNoEvade = wx.CheckBox(sizerParameters.GetStaticBox(), wx.ID_ANY, _(
            "Can't Evade"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerParameters.Add(self.checkBoxNoEvade, 0, wx.ALL, 5)

        self.checkBoxSlipDamage = wx.CheckBox(sizerParameters.GetStaticBox(), wx.ID_ANY, _(
            "Slip Damage"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerParameters.Add(self.checkBoxSlipDamage, 0, wx.ALL, 5)

        sizer4.Add(sizerParameters, 1, wx.ALL, 5)

        sizer1.Add(sizer4, 0, wx.EXPAND, 5)

        sizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelRating = wx.StaticText(staticSizerStates.GetStaticBox(), wx.ID_ANY, _(
            "Rating:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelRating.Wrap(-1)
        sizer5.Add(self.labelRating, 1, wx.ALL, 5)

        self.labelHitPercentage = wx.StaticText(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, _("Hit Rate %:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelHitPercentage.Wrap(-1)
        sizer5.Add(self.labelHitPercentage, 1, wx.ALL, 5)

        self.labelMaxHPPercentage = wx.StaticText(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, _("MaxHP %:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelMaxHPPercentage.Wrap(-1)
        sizer5.Add(self.labelMaxHPPercentage, 1, wx.ALL, 5)

        self.labelMaxSPPercentage = wx.StaticText(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, _("MaxSP %:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelMaxSPPercentage.Wrap(-1)
        sizer5.Add(self.labelMaxSPPercentage, 1, wx.ALL, 5)

        sizer1.Add(sizer5, 0, wx.EXPAND, 5)

        sizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.spinCtrlRating = wx.SpinCtrl(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizer6.Add(self.spinCtrlRating, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlHitRate = wx.SpinCtrl(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizer6.Add(self.spinCtrlHitRate, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlMaxHP = wx.SpinCtrl(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizer6.Add(self.spinCtrlMaxHP, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlMaxSP = wx.SpinCtrl(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizer6.Add(self.spinCtrlMaxSP, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizer1.Add(sizer6, 0, wx.EXPAND, 5)

        sizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelStrPercentage = wx.StaticText(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, _("STR %:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelStrPercentage.Wrap(-1)
        sizer7.Add(self.labelStrPercentage, 1, wx.ALL, 5)

        self.labelDexPercentage = wx.StaticText(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, _("DEX %:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelDexPercentage.Wrap(-1)
        sizer7.Add(self.labelDexPercentage, 1, wx.ALL, 5)

        self.labelAgiPercentage = wx.StaticText(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, _("AGI %:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelAgiPercentage.Wrap(-1)
        sizer7.Add(self.labelAgiPercentage, 1, wx.ALL, 5)

        self.labelIntPercentage = wx.StaticText(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, _("INT %:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelIntPercentage.Wrap(-1)
        sizer7.Add(self.labelIntPercentage, 1, wx.ALL, 5)

        sizer1.Add(sizer7, 0, wx.EXPAND, 5)

        sizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.spinCtrlStr = wx.SpinCtrl(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizer8.Add(self.spinCtrlStr, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlDex = wx.SpinCtrl(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizer8.Add(self.spinCtrlDex, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlAgi = wx.SpinCtrl(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizer8.Add(self.spinCtrlAgi, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlInt = wx.SpinCtrl(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizer8.Add(self.spinCtrlInt, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizer1.Add(sizer8, 0, wx.EXPAND, 5)

        sizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelAtkPercentage = wx.StaticText(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, _("ATK %:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelAtkPercentage.Wrap(-1)
        sizer9.Add(self.labelAtkPercentage, 1, wx.ALL, 5)

        self.labelPdefPercentage = wx.StaticText(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, _("PDEF %:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelPdefPercentage.Wrap(-1)
        sizer9.Add(self.labelPdefPercentage, 1, wx.ALL, 5)

        self.labelMdefPercentage = wx.StaticText(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, _("MDEF %:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelMdefPercentage.Wrap(-1)
        sizer9.Add(self.labelMdefPercentage, 1, wx.ALL, 5)

        self.lavelEvaPercentage = wx.StaticText(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, _("EVA %:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.lavelEvaPercentage.Wrap(-1)
        sizer9.Add(self.lavelEvaPercentage, 1, wx.ALL, 5)

        sizer1.Add(sizer9, 0, wx.EXPAND, 5)

        sizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.spinCtrlAtk = wx.SpinCtrl(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizer10.Add(self.spinCtrlAtk, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlPdef = wx.SpinCtrl(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizer10.Add(self.spinCtrlPdef, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlMdef = wx.SpinCtrl(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizer10.Add(self.spinCtrlMdef, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlEva = wx.SpinCtrl(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizer10.Add(self.spinCtrlEva, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizer1.Add(sizer10, 0, wx.EXPAND, 5)

        sizer11 = wx.StaticBoxSizer(wx.StaticBox(
            staticSizerStates.GetStaticBox(), wx.ID_ANY, _("Release Conditions")), wx.VERTICAL)

        self.lcheckBoxReleaseEnd = wx.CheckBox(sizer11.GetStaticBox(), wx.ID_ANY, _(
            "Release at the end of battle"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizer11.Add(self.lcheckBoxReleaseEnd, 0, wx.ALL, 5)

        sizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelAfter = wx.StaticText(sizer11.GetStaticBox(), wx.ID_ANY, _(
            "After"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelAfter.Wrap(-1)
        sizer13.Add(self.labelAfter, 0, wx.TOP | wx.BOTTOM |
                    wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)

        self.spinCtrlConditionTurns = wx.SpinCtrl(sizer11.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizer13.Add(self.spinCtrlConditionTurns, 1, wx.TOP | wx.BOTTOM, 5)

        self.labelTurns = wx.StaticText(sizer11.GetStaticBox(), wx.ID_ANY, _(
            "turns,"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelTurns.Wrap(-1)
        sizer13.Add(self.labelTurns, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.spinCtrlConditionTurnPercent = wx.SpinCtrl(sizer11.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizer13.Add(
            self.spinCtrlConditionTurnPercent, 1, wx.TOP | wx.BOTTOM, 5)

        self.labelChance1 = wx.StaticText(sizer11.GetStaticBox(), wx.ID_ANY, _(
            "% chance."), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelChance1.Wrap(-1)
        sizer13.Add(self.labelChance1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        sizer11.Add(sizer13, 0, wx.EXPAND, 5)

        sizer14 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelPhysical = wx.StaticText(sizer11.GetStaticBox(), wx.ID_ANY, _(
            "Each physical damage deal,"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelPhysical.Wrap(-1)
        sizer14.Add(
            self.labelPhysical, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.spinCtrlConditionPhysical = wx.SpinCtrl(sizer11.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizer14.Add(self.spinCtrlConditionPhysical, 1, wx.TOP | wx.BOTTOM, 5)

        self.labelChance2 = wx.StaticText(sizer11.GetStaticBox(), wx.ID_ANY, _(
            "% chance."), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelChance2.Wrap(-1)
        sizer14.Add(self.labelChance2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sizer11.Add(sizer14, 0, wx.EXPAND, 5)

        sizer1.Add(sizer11, 0, wx.EXPAND | wx.ALL, 5)

        staticSizerStates.Add(sizer1, 60, wx.EXPAND, 5)

        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelElements = wx.StaticText(staticSizerStates.GetStaticBox(), wx.ID_ANY, _(
            "Element Defense:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelElements.Wrap(-1)
        sizer2.Add(self.labelElements, 1, wx.ALL | wx.EXPAND, 5)

        self.labelStates = wx.StaticText(staticSizerStates.GetStaticBox(), wx.ID_ANY, _(
            "State Change:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelStates.Wrap(-1)
        sizer2.Add(self.labelStates, 1, wx.ALL | wx.EXPAND, 5)

        sizer.Add(sizer2, 0, wx.EXPAND, 5)

        sizer3 = wx.BoxSizer(wx.HORIZONTAL)

        from .Extras import ImageCheckList
        from .Extras import DatabaseManager as DM
        states = [False, True]
        images = DM.GetNormalCheckImageList()
        self.checkListElements = ImageCheckList(self, states, images)
        sizer3.Add(self.checkListElements, 0, wx.ALL |
                   wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        states = [0, 1, -1]
        images = DM.GetAddSubImageList()
        self.checkListStates = ImageCheckList(self, states, images)
        sizer3.Add(self.checkListStates, 0, wx.ALL | wx.BOTTOM |
                   wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        sizer.Add(sizer3, 1, wx.EXPAND, 5)

        self.labelNotes = wx.StaticText(staticSizerStates.GetStaticBox(), wx.ID_ANY, _(
            "Notes:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelNotes.Wrap(-1)
        sizer.Add(self.labelNotes, 0, wx.ALL, 5)

        self.textCtrlNotes = wx.TextCtrl(staticSizerStates.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.CLIP_CHILDREN)
        
        sizer.Add(self.textCtrlNotes, 1, wx.ALL | wx.EXPAND, 5)

        staticSizerStates.Add(sizer, 30, wx.EXPAND, 5)

        MainSizer.Add(staticSizerStates, 75, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        # Connect Events
        self.listBoxStates.Bind(
            wx.EVT_LISTBOX, self.listBoxStates_SelectionChanged)
        self.buttonMaximum.Bind(wx.EVT_BUTTON, self.buttonMaximum_Clicked)
        self.textCtrlName.Bind(wx.EVT_TEXT, self.textCtrlName_ValueChanged)
        self.comboBoxAnimation.Bind(
            wx.EVT_CHOICE, self.comboBoxAnimation_SelectionChanged)
        self.comboBoxRestriction.Bind(
            wx.EVT_CHOICE, self.comboBoxRestriction_SelectionChanged)
        self.checkBoxNonresistance.Bind(
            wx.EVT_CHECKBOX, self.checkBoxNonresistance_CheckChanged)
        self.checkBoxRegardHP0.Bind(
            wx.EVT_CHECKBOX, self.checkBoxHP0_CheckChanged)
        self.checkBoxNoExp.Bind(
            wx.EVT_CHECKBOX, self.checkBoxNoExp_CheckChanged)
        self.checkBoxNoEvade.Bind(
            wx.EVT_CHECKBOX, self.checkBoxNoEvade_CheckChanged)
        self.checkBoxSlipDamage.Bind(
            wx.EVT_CHECKBOX, self.checkBoxSlipDamage_CheckChanged)
        self.spinCtrlRating.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlRating_ValueChanged)
        self.spinCtrlHitRate.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlHitRate_ValueChanged)
        self.spinCtrlMaxHP.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlMaxHP_ValueChanged)
        self.spinCtrlMaxSP.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlMaxSP_ValueChanged)
        self.spinCtrlStr.Bind(wx.EVT_SPINCTRL, self.spinCtrlStr_ValueChanged)
        self.spinCtrlDex.Bind(wx.EVT_SPINCTRL, self.spinCtrlDex_ValueChanged)
        self.spinCtrlAgi.Bind(wx.EVT_SPINCTRL, self.spinCtrlAgi_ValueChanged)
        self.spinCtrlInt.Bind(wx.EVT_SPINCTRL, self.spinCtrlInt_ValueChanged)
        self.spinCtrlAtk.Bind(wx.EVT_SPINCTRL, self.spinCtrlAtk_ValueChanged)
        self.spinCtrlPdef.Bind(wx.EVT_SPINCTRL, self.spinCtrlPdef_ValueChanged)
        self.spinCtrlMdef.Bind(wx.EVT_SPINCTRL, self.spinCtrlMdef_ValueChanged)
        self.spinCtrlEva.Bind(wx.EVT_SPINCTRL, self.spinCtrlEva_ValueChanged)
        self.lcheckBoxReleaseEnd.Bind(
            wx.EVT_CHECKBOX, self.checkBoxBattleRelease_CheckChanged)
        self.spinCtrlConditionTurns.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlTurns_ValueChanged)
        self.spinCtrlConditionTurnPercent.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlTurnPercent_ValueChanged)
        self.spinCtrlConditionPhysical.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlPhysical_ValueChanged)
        self.checkListElements.Bind(
            wx.EVT_LEFT_DOWN, self.checkListElements_Clicked)
        self.checkListElements.Bind(
            wx.EVT_RIGHT_DOWN, self.checkListElements_Clicked)
        self.checkListStates.Bind(
            wx.EVT_LEFT_DOWN, self.checkListStates_Clicked)
        self.checkListStates.Bind(
            wx.EVT_RIGHT_DOWN, self.checkListStates_Clicked)
        self.textCtrlNotes.Bind(wx.EVT_TEXT, self.textCtrlNotes_TextChanged)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def listBoxStates_SelectionChanged(self, event):
        event.Skip()

    def buttonMaximum_Clicked(self, event):
        event.Skip()

    def textCtrlName_ValueChanged(self, event):
        event.Skip()

    def comboBoxAnimation_SelectionChanged(self, event):
        event.Skip()

    def comboBoxRestriction_SelectionChanged(self, event):
        event.Skip()

    def checkBoxNonresistance_CheckChanged(self, event):
        event.Skip()

    def checkBoxHP0_CheckChanged(self, event):
        event.Skip()

    def checkBoxNoExp_CheckChanged(self, event):
        event.Skip()

    def checkBoxNoEvade_CheckChanged(self, event):
        event.Skip()

    def checkBoxSlipDamage_CheckChanged(self, event):
        event.Skip()

    def spinCtrlRating_ValueChanged(self, event):
        event.Skip()

    def spinCtrlHitRate_ValueChanged(self, event):
        event.Skip()

    def spinCtrlMaxHP_ValueChanged(self, event):
        event.Skip()

    def spinCtrlMaxSP_ValueChanged(self, event):
        event.Skip()

    def spinCtrlStr_ValueChanged(self, event):
        event.Skip()

    def spinCtrlDex_ValueChanged(self, event):
        event.Skip()

    def spinCtrlAgi_ValueChanged(self, event):
        event.Skip()

    def spinCtrlInt_ValueChanged(self, event):
        event.Skip()

    def spinCtrlAtk_ValueChanged(self, event):
        event.Skip()

    def spinCtrlPdef_ValueChanged(self, event):
        event.Skip()

    def spinCtrlMdef_ValueChanged(self, event):
        event.Skip()

    def spinCtrlEva_ValueChanged(self, event):
        event.Skip()

    def checkBoxBattleRelease_CheckChanged(self, event):
        event.Skip()

    def spinCtrlTurns_ValueChanged(self, event):
        event.Skip()

    def spinCtrlTurnPercent_ValueChanged(self, event):
        event.Skip()

    def spinCtrlPhysical_ValueChanged(self, event):
        event.Skip()

    def checkListElements_Clicked(self, event):
        event.Skip()

    def checkListStates_Clicked(self, event):
        event.Skip()

    def textCtrlNotes_TextChanged(self, event):
        event.Skip()


###########################################################################
# Class Animations_Panel_Template
###########################################################################

class Animations_Panel_Template (wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(
            800, 600), style=wx.TAB_TRAVERSAL)

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        AnimationsListSizer = wx.BoxSizer(wx.VERTICAL)

        self.bitmapAnimations = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(
            150, 26), wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)
        self.bitmapAnimations.SetMinSize(wx.Size(150, 26))
        self.bitmapAnimations.SetMaxSize(wx.Size(150, 26))

        AnimationsListSizer.Add(
            self.bitmapAnimations, 0, wx.ALL | wx.EXPAND, 5)

        listBoxAnimationsChoices = []
        self.listBoxAnimations = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(
            184, -1), listBoxAnimationsChoices, wx.LB_SINGLE | wx.CLIP_CHILDREN)
        AnimationsListSizer.Add(
            self.listBoxAnimations, 1, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        self.buttonMaximum = wx.Button(self, wx.ID_ANY, _(
            "Change Maximum..."), wx.DefaultPosition, wx.Size(150, -1), 0)
        AnimationsListSizer.Add(self.buttonMaximum, 0, wx.ALL | wx.EXPAND, 5)

        MainSizer.Add(AnimationsListSizer, 0, wx.EXPAND, 5)

        staticSizerAnimations = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        sizer1 = wx.BoxSizer(wx.HORIZONTAL)

        sizer4 = wx.BoxSizer(wx.VERTICAL)

        self.labelName = wx.StaticText(staticSizerAnimations.GetStaticBox(), wx.ID_ANY, _(
            "Name:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelName.Wrap(-1)
        sizer4.Add(self.labelName, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlName = wx.TextCtrl(staticSizerAnimations.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlName.SetMaxLength(0)
        sizer4.Add(
            self.textCtrlName, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelGraphic = wx.StaticText(staticSizerAnimations.GetStaticBox(
        ), wx.ID_ANY, _("Animation Graphic:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelGraphic.Wrap(-1)
        sizer4.Add(self.labelGraphic, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxGraphicChoices = [_("(None)")]
        self.comboBoxGraphic = wx.ComboBox(staticSizerAnimations.GetStaticBox(), wx.ID_ANY, _(
            "(None)"), wx.DefaultPosition, wx.DefaultSize, comboBoxGraphicChoices, 0)
        sizer4.Add(self.comboBoxGraphic, 0, wx.EXPAND |
                   wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelPosition = wx.StaticText(staticSizerAnimations.GetStaticBox(
        ), wx.ID_ANY, _("Position:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelPosition.Wrap(-1)
        sizer7.Add(self.labelPosition, 1, wx.ALL | wx.EXPAND, 5)

        self.labelFrames = wx.StaticText(staticSizerAnimations.GetStaticBox(
        ), wx.ID_ANY, _("Frames:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelFrames.Wrap(-1)
        sizer7.Add(self.labelFrames, 1, wx.ALL | wx.EXPAND, 5)

        sizer4.Add(sizer7, 0, wx.EXPAND, 5)

        sizer8 = wx.BoxSizer(wx.HORIZONTAL)

        comboBoxPositionChoices = [
            _("Top"), _("Middle"), _("Bottom"), _("Screen")]
        self.comboBoxPosition = wx.Choice(staticSizerAnimations.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxPositionChoices, 0)
        self.comboBoxPosition.SetSelection(0)
        sizer8.Add(self.comboBoxPosition, 1, wx.EXPAND |
                   wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        comboBoxFramesChoices = []
        self.comboBoxFrames = wx.ComboBox(staticSizerAnimations.GetStaticBox(), wx.ID_ANY, _(
            "16"), wx.DefaultPosition, wx.DefaultSize, comboBoxFramesChoices, 0)
        sizer8.Add(
            self.comboBoxFrames, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizer4.Add(sizer8, 0, wx.EXPAND, 5)

        sizer1.Add(sizer4, 30, 0, 5)

        self.listCtrlTiming = wx.ListCtrl(staticSizerAnimations.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        sizer1.Add(
            self.listCtrlTiming, 70, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        staticSizerAnimations.Add(sizer1, 0, wx.EXPAND, 5)

        sizer2 = wx.BoxSizer(wx.HORIZONTAL)

        sizer5 = wx.BoxSizer(wx.VERTICAL)

        self.buttonBack = wx.Button(staticSizerAnimations.GetStaticBox(), wx.ID_ANY, _(
            "Back"), wx.DefaultPosition, wx.Size(56, -1), 0)
        sizer5.Add(self.buttonBack, 0, wx.ALL, 5)

        listBoxFrameChoices = []
        self.listBoxFrame = wx.ListBox(staticSizerAnimations.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(56, -1), listBoxFrameChoices, wx.LB_ALWAYS_SB)
        sizer5.Add(self.listBoxFrame, 1, wx.RIGHT | wx.LEFT, 5)

        self.buttonNext = wx.Button(staticSizerAnimations.GetStaticBox(), wx.ID_ANY, _(
            "Next"), wx.DefaultPosition, wx.Size(56, -1), 0)
        sizer5.Add(self.buttonNext, 0, wx.ALL, 5)

        sizer2.Add(sizer5, 0, wx.EXPAND, 5)

        self.bitmapPallette = wx.StaticBitmap(staticSizerAnimations.GetStaticBox(
        ), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER)
        sizer2.Add(self.bitmapPallette, 1, wx.ALL | wx.EXPAND, 5)

        sizer6 = wx.BoxSizer(wx.VERTICAL)

        sizer6.SetMinSize(wx.Size(100, -1))
        self.buttonBattler = wx.Button(staticSizerAnimations.GetStaticBox(), wx.ID_ANY, _(
            "[ED] Battler..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizer6.Add(self.buttonBattler, 0, wx.ALL | wx.EXPAND, 5)

        self.buttonPaste = wx.Button(staticSizerAnimations.GetStaticBox(), wx.ID_ANY, _(
            "Paste Last"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizer6.Add(
            self.buttonPaste, 0, wx.TOP | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonCopy = wx.Button(staticSizerAnimations.GetStaticBox(), wx.ID_ANY, _(
            "Copy Frames..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizer6.Add(self.buttonCopy, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonClear = wx.Button(staticSizerAnimations.GetStaticBox(), wx.ID_ANY, _(
            "Clear Frames..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizer6.Add(self.buttonClear, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonTweening = wx.Button(staticSizerAnimations.GetStaticBox(), wx.ID_ANY, _(
            "Tweening..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizer6.Add(self.buttonTweening, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonCellBatch = wx.Button(staticSizerAnimations.GetStaticBox(
        ), wx.ID_ANY, _("Cell Batch..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizer6.Add(self.buttonCellBatch, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonEntireSlide = wx.Button(staticSizerAnimations.GetStaticBox(
        ), wx.ID_ANY, _("Entire Slide..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizer6.Add(self.buttonEntireSlide, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonPlayHit = wx.Button(staticSizerAnimations.GetStaticBox(), wx.ID_ANY, _(
            "Play Hit"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizer6.Add(
            self.buttonPlayHit, 0, wx.TOP | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonPlayMiss = wx.Button(staticSizerAnimations.GetStaticBox(), wx.ID_ANY, _(
            "Play Miss"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizer6.Add(
            self.buttonPlayMiss, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizer2.Add(sizer6, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        staticSizerAnimations.Add(sizer2, 60, wx.EXPAND, 5)

        sizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_scrolledWindow3 = wx.ScrolledWindow(staticSizerAnimations.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.ALWAYS_SHOW_SB | wx.HSCROLL | wx.SUNKEN_BORDER | wx.VSCROLL)
        self.m_scrolledWindow3.SetScrollRate(5, 5)
        bSizer196 = wx.BoxSizer(wx.HORIZONTAL)

        self.bitmapAnimationFrames = wx.StaticBitmap(
            self.m_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer196.Add(self.bitmapAnimationFrames, 0, wx.ALL, 5)

        self.m_scrolledWindow3.SetSizer(bSizer196)
        self.m_scrolledWindow3.Layout()
        bSizer196.Fit(self.m_scrolledWindow3)
        sizer3.Add(self.m_scrolledWindow3, 1, wx.ALL | wx.EXPAND, 5)

        staticSizerAnimations.Add(sizer3, 35, wx.EXPAND, 5)

        MainSizer.Add(staticSizerAnimations, 75, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        # Connect Events
        self.listBoxAnimations.Bind(
            wx.EVT_LISTBOX, self.listBoxAnimations_SelectionChanged)
        self.buttonMaximum.Bind(wx.EVT_BUTTON, self.buttonMaximum_Clicked)
        self.textCtrlName.Bind(wx.EVT_TEXT, self.textCtrlName_ValueChanged)
        self.comboBoxGraphic.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxGraphic_Clicked)
        self.comboBoxPosition.Bind(
            wx.EVT_CHOICE, self.comboBoxPosition_SelectionChanged)
        self.comboBoxFrames.Bind(wx.EVT_LEFT_DOWN, self.comboBoxFrames_Clicked)
        self.listCtrlTiming.Bind(
            wx.EVT_LEFT_DCLICK, self.listControlTiming_DoubleClicked)
        self.buttonBack.Bind(wx.EVT_BUTTON, self.buttonBack_Clicked)
        self.listBoxFrame.Bind(
            wx.EVT_LISTBOX, self.listBoxFrames_SelectionChanged)
        self.buttonNext.Bind(wx.EVT_BUTTON, self.buttonNext_Clicked)
        self.buttonBattler.Bind(wx.EVT_BUTTON, self.buttonBattler_Clicked)
        self.buttonPaste.Bind(wx.EVT_BUTTON, self.buttonPaste_Clicked)
        self.buttonCopy.Bind(wx.EVT_BUTTON, self.buttonCopy_Clicked)
        self.buttonClear.Bind(wx.EVT_BUTTON, self.buttonClear_Clicked)
        self.buttonTweening.Bind(wx.EVT_BUTTON, self.buttonTweening_Clicked)
        self.buttonCellBatch.Bind(wx.EVT_BUTTON, self.buttonCellBatch_Clicked)
        self.buttonEntireSlide.Bind(
            wx.EVT_BUTTON, self.buttonEntireSlide_Clicked)
        self.buttonPlayHit.Bind(wx.EVT_BUTTON, self.buttonPlayHit_Clicked)
        self.buttonPlayMiss.Bind(wx.EVT_BUTTON, self.buttonPlayMiss_Clicked)
        self.bitmapAnimationFrames.Bind(
            wx.EVT_LEFT_DOWN, self.bitmapAnimationFrames_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def listBoxAnimations_SelectionChanged(self, event):
        event.Skip()

    def buttonMaximum_Clicked(self, event):
        event.Skip()

    def textCtrlName_ValueChanged(self, event):
        event.Skip()

    def comboBoxGraphic_Clicked(self, event):
        event.Skip()

    def comboBoxPosition_SelectionChanged(self, event):
        event.Skip()

    def comboBoxFrames_Clicked(self, event):
        event.Skip()

    def listControlTiming_DoubleClicked(self, event):
        event.Skip()

    def buttonBack_Clicked(self, event):
        event.Skip()

    def listBoxFrames_SelectionChanged(self, event):
        event.Skip()

    def buttonNext_Clicked(self, event):
        event.Skip()

    def buttonBattler_Clicked(self, event):
        event.Skip()

    def buttonPaste_Clicked(self, event):
        event.Skip()

    def buttonCopy_Clicked(self, event):
        event.Skip()

    def buttonClear_Clicked(self, event):
        event.Skip()

    def buttonTweening_Clicked(self, event):
        event.Skip()

    def buttonCellBatch_Clicked(self, event):
        event.Skip()

    def buttonEntireSlide_Clicked(self, event):
        event.Skip()

    def buttonPlayHit_Clicked(self, event):
        event.Skip()

    def buttonPlayMiss_Clicked(self, event):
        event.Skip()

    def bitmapAnimationFrames_Clicked(self, event):
        event.Skip()


###########################################################################
# Class Tilesets_Panel_Template
###########################################################################

class Tilesets_Panel_Template (wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(
            800, 600), style=wx.TAB_TRAVERSAL)

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        TilesetsListSizer = wx.BoxSizer(wx.VERTICAL)

        self.bitmapTilesets = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(
            150, 26), wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)
        self.bitmapTilesets.SetMinSize(wx.Size(150, 26))
        self.bitmapTilesets.SetMaxSize(wx.Size(150, 26))

        TilesetsListSizer.Add(self.bitmapTilesets, 0, wx.ALL | wx.EXPAND, 5)

        listBoxTilesetsChoices = []
        self.listBoxTilesets = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(
            184, -1), listBoxTilesetsChoices, wx.LB_SINGLE | wx.CLIP_CHILDREN)
        TilesetsListSizer.Add(
            self.listBoxTilesets, 1, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        self.buttonMaximum = wx.Button(self, wx.ID_ANY, _(
            "Change Maximum..."), wx.DefaultPosition, wx.Size(150, -1), 0)
        TilesetsListSizer.Add(self.buttonMaximum, 0, wx.ALL | wx.EXPAND, 5)

        MainSizer.Add(TilesetsListSizer, 0, wx.EXPAND, 5)

        staticSizerTilesets = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.HORIZONTAL)

        sizer1 = wx.BoxSizer(wx.VERTICAL)

        self.labelName = wx.StaticText(staticSizerTilesets.GetStaticBox(), wx.ID_ANY, _(
            "Name:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelName.Wrap(-1)
        sizer1.Add(self.labelName, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlName = wx.TextCtrl(staticSizerTilesets.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlName.SetMaxLength(0)
        sizer1.Add(
            self.textCtrlName, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelTileset = wx.StaticText(staticSizerTilesets.GetStaticBox(), wx.ID_ANY, _(
            "Tileset Graphic:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelTileset.Wrap(-1)
        sizer1.Add(self.labelTileset, 0, wx.ALL | wx.EXPAND, 5)

        self.comboBoxTileset = wx.adv.BitmapComboBox(staticSizerTilesets.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, "", 0)
        sizer1.Add(self.comboBoxTileset, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelAutotiles = wx.StaticText(staticSizerTilesets.GetStaticBox(
        ), wx.ID_ANY, _("Autotile Graphics:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelAutotiles.Wrap(-1)
        sizer1.Add(self.labelAutotiles, 0, wx.ALL | wx.EXPAND, 5)

        self.comboBoxAutotiles1 = wx.adv.BitmapComboBox(staticSizerTilesets.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, "", 0)
        sizer1.Add(self.comboBoxAutotiles1, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.comboBoxAutotiles2 = wx.adv.BitmapComboBox(staticSizerTilesets.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, "", 0)
        sizer1.Add(self.comboBoxAutotiles2, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.comboBoxAutotiles3 = wx.adv.BitmapComboBox(staticSizerTilesets.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, "", 0)
        sizer1.Add(self.comboBoxAutotiles3, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.comboBoxAutotiles4 = wx.adv.BitmapComboBox(staticSizerTilesets.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, "", 0)
        sizer1.Add(self.comboBoxAutotiles4, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.comboBoxAutotiles5 = wx.adv.BitmapComboBox(staticSizerTilesets.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, "", 0)
        sizer1.Add(self.comboBoxAutotiles5, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.comboBoxAutotiles6 = wx.adv.BitmapComboBox(staticSizerTilesets.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, "", 0)
        sizer1.Add(self.comboBoxAutotiles6, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.comboBoxAutotiles7 = wx.adv.BitmapComboBox(staticSizerTilesets.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, "", 0)
        sizer1.Add(self.comboBoxAutotiles7, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelPanorama = wx.StaticText(staticSizerTilesets.GetStaticBox(
        ), wx.ID_ANY, _("Panorama Graphic:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelPanorama.Wrap(-1)
        sizer1.Add(self.labelPanorama, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxPanoramaChoices = []
        self.comboBoxPanorama = wx.ComboBox(staticSizerTilesets.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxPanoramaChoices, 0)
        sizer1.Add(self.comboBoxPanorama, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelFog = wx.StaticText(staticSizerTilesets.GetStaticBox(), wx.ID_ANY, _(
            "Fog Graphic:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelFog.Wrap(-1)
        sizer1.Add(self.labelFog, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxFogChoices = []
        self.comboBoxFog = wx.ComboBox(staticSizerTilesets.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxFogChoices, 0)
        sizer1.Add(
            self.comboBoxFog, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelBattleback = wx.StaticText(staticSizerTilesets.GetStaticBox(
        ), wx.ID_ANY, _("Battleback Graphic:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelBattleback.Wrap(-1)
        sizer1.Add(self.labelBattleback, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxBattlebackChoices = []
        self.comboBoxBattleback = wx.ComboBox(staticSizerTilesets.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxBattlebackChoices, 0)
        sizer1.Add(self.comboBoxBattleback, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        staticSizerTilesets.Add(sizer1, 0, wx.EXPAND, 5)

        self.m_scrolledWindow4 = wx.ScrolledWindow(staticSizerTilesets.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL | wx.SUNKEN_BORDER | wx.VSCROLL)
        self.m_scrolledWindow4.SetScrollRate(5, 5)
        self.m_scrolledWindow4.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        sizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap36 = wx.StaticBitmap(
            self.m_scrolledWindow4, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(256, -1), 0)
        self.m_bitmap36.SetMinSize(wx.Size(256, -1))
        self.m_bitmap36.SetMaxSize(wx.Size(256, -1))

        sizer3.Add(self.m_bitmap36, 0, 0, 5)

        self.m_scrolledWindow4.SetSizer(sizer3)
        self.m_scrolledWindow4.Layout()
        sizer3.Fit(self.m_scrolledWindow4)
        staticSizerTilesets.Add(
            self.m_scrolledWindow4, 1, wx.EXPAND | wx.ALL, 5)

        sizer2 = wx.BoxSizer(wx.VERTICAL)

        self.buttonPassage = wx.Button(staticSizerTilesets.GetStaticBox(), wx.ID_ANY, _(
            "Passage"), wx.DefaultPosition, wx.Size(-1, 46), 0)
        sizer2.Add(self.buttonPassage, 0, wx.ALL, 5)

        self.buttonPassage4Dir = wx.Button(staticSizerTilesets.GetStaticBox(
        ), wx.ID_ANY, _("Passage\n(4 Dir)"), wx.DefaultPosition, wx.Size(-1, 46), 0)
        sizer2.Add(self.buttonPassage4Dir, 0, wx.ALL, 5)

        self.buttonPriority = wx.Button(staticSizerTilesets.GetStaticBox(), wx.ID_ANY, _(
            "Priority"), wx.DefaultPosition, wx.Size(-1, 46), 0)
        sizer2.Add(self.buttonPriority, 0, wx.ALL, 5)

        self.buttonBushFlag = wx.Button(staticSizerTilesets.GetStaticBox(), wx.ID_ANY, _(
            "Bush\nFlag"), wx.DefaultPosition, wx.Size(-1, 46), 0)
        sizer2.Add(self.buttonBushFlag, 0, wx.ALL, 5)

        self.buttonCounter = wx.Button(staticSizerTilesets.GetStaticBox(), wx.ID_ANY, _(
            "Counter\nFlag"), wx.DefaultPosition, wx.Size(-1, 46), 0)
        sizer2.Add(self.buttonCounter, 0, wx.ALL, 5)

        self.buttonTerrainTag = wx.Button(staticSizerTilesets.GetStaticBox(), wx.ID_ANY, _(
            "Terrain\nTag"), wx.DefaultPosition, wx.Size(-1, 46), 0)
        sizer2.Add(self.buttonTerrainTag, 0, wx.ALL, 5)

        staticSizerTilesets.Add(sizer2, 0, wx.EXPAND, 5)

        MainSizer.Add(staticSizerTilesets, 75, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        # Connect Events
        self.listBoxTilesets.Bind(
            wx.EVT_LISTBOX, self.listBoxTilesets_SelectionChanged)
        self.buttonMaximum.Bind(wx.EVT_BUTTON, self.buttonMaximum_Clicked)
        self.textCtrlName.Bind(wx.EVT_TEXT, self.textCtrlName_ValueChanged)
        self.comboBoxTileset.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxTileset_Clicked)
        self.comboBoxAutotiles1.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxAutotiles1_Clicked)
        self.comboBoxAutotiles2.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxAutotiles2_Clicked)
        self.comboBoxAutotiles3.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxAutotiles3_Clicked)
        self.comboBoxAutotiles4.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxAutotiles4_Clicked)
        self.comboBoxAutotiles5.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxAutotiles5_Clicked)
        self.comboBoxAutotiles6.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxAutotiles6_Clicked)
        self.comboBoxAutotiles7.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxAutotiles7_Clicked)
        self.comboBoxPanorama.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxPanorama_Clicked)
        self.comboBoxFog.Bind(wx.EVT_LEFT_DOWN, self.comboBoxFog_Clicked)
        self.comboBoxBattleback.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxBattleback_Clicked)
        self.m_bitmap36.Bind(wx.EVT_LEFT_DCLICK, self.bitmapTileset_LeftClick)
        self.m_bitmap36.Bind(wx.EVT_LEFT_DOWN, self.bitmapTileset_LMouseDown)
        self.m_bitmap36.Bind(wx.EVT_LEFT_UP, self.bitmapTileset_LeftMouseUp)
        self.m_bitmap36.Bind(
            wx.EVT_RIGHT_DCLICK, self.bitmapTileset_RightClick)
        self.m_bitmap36.Bind(
            wx.EVT_RIGHT_DOWN, self.bitmapTileset_RightMouseDown)
        self.m_bitmap36.Bind(wx.EVT_RIGHT_UP, self.bitmapTileset_RightMouseUP)
        self.buttonPassage.Bind(wx.EVT_BUTTON, self.buttonPassage_Clicked)
        self.buttonPassage4Dir.Bind(
            wx.EVT_BUTTON, self.buttonPassage4Dir_Clicked)
        self.buttonPriority.Bind(wx.EVT_BUTTON, self.buttonPriority_Clicked)
        self.buttonBushFlag.Bind(wx.EVT_BUTTON, self.buttonBushFlag_Clicked)
        self.buttonCounter.Bind(wx.EVT_BUTTON, self.buttonCounter_Clicked)
        self.buttonTerrainTag.Bind(
            wx.EVT_BUTTON, self.buttonTerrainTag_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def listBoxTilesets_SelectionChanged(self, event):
        event.Skip()

    def buttonMaximum_Clicked(self, event):
        event.Skip()

    def textCtrlName_ValueChanged(self, event):
        event.Skip()

    def comboBoxTileset_Clicked(self, event):
        event.Skip()

    def comboBoxAutotiles1_Clicked(self, event):
        event.Skip()

    def comboBoxAutotiles2_Clicked(self, event):
        event.Skip()

    def comboBoxAutotiles3_Clicked(self, event):
        event.Skip()

    def comboBoxAutotiles4_Clicked(self, event):
        event.Skip()

    def comboBoxAutotiles5_Clicked(self, event):
        event.Skip()

    def comboBoxAutotiles6_Clicked(self, event):
        event.Skip()

    def comboBoxAutotiles7_Clicked(self, event):
        event.Skip()

    def comboBoxPanorama_Clicked(self, event):
        event.Skip()

    def comboBoxFog_Clicked(self, event):
        event.Skip()

    def comboBoxBattleback_Clicked(self, event):
        event.Skip()

    def bitmapTileset_LeftClick(self, event):
        event.Skip()

    def bitmapTileset_LMouseDown(self, event):
        event.Skip()

    def bitmapTileset_LeftMouseUp(self, event):
        event.Skip()

    def bitmapTileset_RightClick(self, event):
        event.Skip()

    def bitmapTileset_RightMouseDown(self, event):
        event.Skip()

    def bitmapTileset_RightMouseUP(self, event):
        event.Skip()

    def buttonPassage_Clicked(self, event):
        event.Skip()

    def buttonPassage4Dir_Clicked(self, event):
        event.Skip()

    def buttonPriority_Clicked(self, event):
        event.Skip()

    def buttonBushFlag_Clicked(self, event):
        event.Skip()

    def buttonCounter_Clicked(self, event):
        event.Skip()

    def buttonTerrainTag_Clicked(self, event):
        event.Skip()


###########################################################################
# Class CommonEvents_Panel_Template
###########################################################################

class CommonEvents_Panel_Template (wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(
            800, 600), style=wx.TAB_TRAVERSAL)

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        CommonEventsListSizer = wx.BoxSizer(wx.VERTICAL)

        self.bitmapCommonEvents = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(
            150, 26), wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)
        self.bitmapCommonEvents.SetMinSize(wx.Size(150, 26))
        self.bitmapCommonEvents.SetMaxSize(wx.Size(150, 26))

        CommonEventsListSizer.Add(
            self.bitmapCommonEvents, 0, wx.ALL | wx.EXPAND, 5)

        listBoxCommonEventsChoices = []
        self.listBoxCommonEvents = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(
            184, -1), listBoxCommonEventsChoices, wx.LB_SINGLE | wx.CLIP_CHILDREN)
        CommonEventsListSizer.Add(
            self.listBoxCommonEvents, 1, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        self.buttonMaximum = wx.Button(self, wx.ID_ANY, _(
            "Change Maximum..."), wx.DefaultPosition, wx.Size(150, -1), 0)
        CommonEventsListSizer.Add(self.buttonMaximum, 0, wx.ALL | wx.EXPAND, 5)

        MainSizer.Add(CommonEventsListSizer, 0, wx.EXPAND, 5)

        staticSizerCommonEvents = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        sizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelName = wx.StaticText(staticSizerCommonEvents.GetStaticBox(
        ), wx.ID_ANY, _("Name:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelName.Wrap(-1)
        sizer1.Add(self.labelName, 35, wx.ALL, 5)

        self.labelTrigger = wx.StaticText(staticSizerCommonEvents.GetStaticBox(
        ), wx.ID_ANY, _("Trigger:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelTrigger.Wrap(-1)
        sizer1.Add(self.labelTrigger, 30, wx.ALL, 5)

        self.labelCondition = wx.StaticText(staticSizerCommonEvents.GetStaticBox(
        ), wx.ID_ANY, _("Condition Switch:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelCondition.Wrap(-1)
        sizer1.Add(self.labelCondition, 35, wx.ALL, 5)

        staticSizerCommonEvents.Add(sizer1, 0, wx.EXPAND, 5)

        sizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.textCtrlName = wx.TextCtrl(staticSizerCommonEvents.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlName.SetMaxLength(0)
        sizer2.Add(self.textCtrlName, 35, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        comboBoxTriggerChoices = [_("None"), _("Autorun"), _("Parallel")]
        self.comboBoxTrigger = wx.Choice(staticSizerCommonEvents.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxTriggerChoices, 0)
        self.comboBoxTrigger.SetSelection(0)
        sizer2.Add(self.comboBoxTrigger, 30, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        comboBoxConditionChoices = []
        self.comboBoxCondition = wx.ComboBox(staticSizerCommonEvents.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxConditionChoices, 0)
        sizer2.Add(
            self.comboBoxCondition, 35, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        staticSizerCommonEvents.Add(sizer2, 0, wx.EXPAND, 5)

        listBoxPageChoices = [_(">@")]
        self.listBoxPage = wx.ListBox(staticSizerCommonEvents.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxPageChoices, 0)
        staticSizerCommonEvents.Add(self.listBoxPage, 1, wx.ALL | wx.EXPAND, 5)

        MainSizer.Add(staticSizerCommonEvents, 75, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        # Connect Events
        self.listBoxCommonEvents.Bind(
            wx.EVT_LISTBOX, self.listBoxCommonEvents_SelectionChanged)
        self.buttonMaximum.Bind(wx.EVT_BUTTON, self.buttonMaximum_Clicked)
        self.textCtrlName.Bind(wx.EVT_TEXT, self.textCtrlName_ValueChanged)
        self.comboBoxTrigger.Bind(
            wx.EVT_CHOICE, self.comboBoxTrigger_SelectionChanged)
        self.comboBoxCondition.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxCondition_Clicked)
        self.listBoxPage.Bind(
            wx.EVT_LEFT_DCLICK, self.listBoxEvents_DoubleClicked)
        self.listBoxPage.Bind(
            wx.EVT_LISTBOX, self.listBoxPage_SelectionChanged)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def listBoxCommonEvents_SelectionChanged(self, event):
        event.Skip()

    def buttonMaximum_Clicked(self, event):
        event.Skip()

    def textCtrlName_ValueChanged(self, event):
        event.Skip()

    def comboBoxTrigger_SelectionChanged(self, event):
        event.Skip()

    def comboBoxCondition_Clicked(self, event):
        event.Skip()

    def listBoxEvents_DoubleClicked(self, event):
        event.Skip()

    def listBoxPage_SelectionChanged(self, event):
        event.Skip()


###########################################################################
# Class System_Panel_Template
###########################################################################

class System_Panel_Template (wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(
            800, 600), style=wx.TAB_TRAVERSAL)

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        sizer1 = wx.BoxSizer(wx.VERTICAL)

        self.labelInitialParty = wx.StaticText(
            self, wx.ID_ANY, _("Initial Party:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelInitialParty.Wrap(-1)
        sizer1.Add(self.labelInitialParty, 0, wx.ALL | wx.EXPAND, 5)

        self.listCtrlInitialParty = wx.ListCtrl(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        sizer1.Add(self.listCtrlInitialParty, 40, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelElements = wx.StaticText(
            self, wx.ID_ANY, _("Element Names:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelElements.Wrap(-1)
        sizer1.Add(self.labelElements, 0, wx.ALL | wx.EXPAND, 5)

        listBoxElementsChoices = []
        self.listBoxElements = wx.ListBox(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxElementsChoices, 0)
        sizer1.Add(self.listBoxElements, 60, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.textControlElementName = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textControlElementName.SetMaxLength(0)
        sizer1.Add(self.textControlElementName, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonMaximum = wx.Button(
            self, wx.ID_ANY, _("Change Maximum..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizer1.Add(self.buttonMaximum, 0, wx.ALL | wx.EXPAND, 5)

        MainSizer.Add(sizer1, 25, wx.EXPAND, 5)

        sizer2 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, _("System Graphics / BGM / SE / ME")), wx.HORIZONTAL)

        sizer4 = wx.BoxSizer(wx.VERTICAL)

        self.labelWindowskinGraphic = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Windowskin Graphic:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelWindowskinGraphic.Wrap(-1)
        sizer4.Add(self.labelWindowskinGraphic, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxWindowskinGraphicChoices = []
        self.comboBoxWindowskinGraphic = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxWindowskinGraphicChoices, 0)
        sizer4.Add(self.comboBoxWindowskinGraphic, 0,
                   wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelTitleGraphic = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Title Graphic:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelTitleGraphic.Wrap(-1)
        sizer4.Add(self.labelTitleGraphic, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxTitleGraphicChoices = []
        self.comboBoxTitleGraphic = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxTitleGraphicChoices, 0)
        sizer4.Add(self.comboBoxTitleGraphic, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelGameoverGraphic = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Gameover Graphic:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelGameoverGraphic.Wrap(-1)
        sizer4.Add(self.labelGameoverGraphic, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxGameoverGraphicChoices = []
        self.comboBoxGameoverGraphic = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxGameoverGraphicChoices, 0)
        sizer4.Add(self.comboBoxGameoverGraphic, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelBattleTransitionGraphic = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Battle Transition Graphic:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelBattleTransitionGraphic.Wrap(-1)
        sizer4.Add(self.labelBattleTransitionGraphic, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxBattleTransitionGraphicChoices = []
        self.comboBoxBattleTransitionGraphic = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxBattleTransitionGraphicChoices, 0)
        sizer4.Add(self.comboBoxBattleTransitionGraphic, 0,
                   wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelTitleBGM = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Title BGM:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelTitleBGM.Wrap(-1)
        sizer4.Add(self.labelTitleBGM, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxTitleBGMChoices = []
        self.comboBoxTitleBGM = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxTitleBGMChoices, 0)
        sizer4.Add(self.comboBoxTitleBGM, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelBattleBGM = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Battle BGM:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelBattleBGM.Wrap(-1)
        sizer4.Add(self.labelBattleBGM, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxBattleBGMChoices = []
        self.comboBoxBattleBGM = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxBattleBGMChoices, 0)
        sizer4.Add(self.comboBoxBattleBGM, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelBattleEndME = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Battle End ME:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelBattleEndME.Wrap(-1)
        sizer4.Add(self.labelBattleEndME, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxBattleEndMEChoices = []
        self.comboBoxBattleEndME = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxBattleEndMEChoices, 0)
        sizer4.Add(self.comboBoxBattleEndME, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelGameoverME = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Gameover ME:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelGameoverME.Wrap(-1)
        sizer4.Add(self.labelGameoverME, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxGameoverMEChoices = []
        self.comboBoxGameoverME = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxGameoverMEChoices, 0)
        sizer4.Add(self.comboBoxGameoverME, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelCursorSE = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Cursor SE:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelCursorSE.Wrap(-1)
        sizer4.Add(self.labelCursorSE, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxCursorSEChoices = []
        self.comboBoxCursorSE = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxCursorSEChoices, 0)
        sizer4.Add(self.comboBoxCursorSE, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelDecisionSE = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Decision SE:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelDecisionSE.Wrap(-1)
        sizer4.Add(self.labelDecisionSE, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxDecisionSEChoices = []
        self.comboBoxDecisionSE = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxDecisionSEChoices, 0)
        sizer4.Add(self.comboBoxDecisionSE, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizer2.Add(sizer4, 1, wx.EXPAND, 5)

        sizer5 = wx.BoxSizer(wx.VERTICAL)

        self.labelCancelSE = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Cancel SE:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelCancelSE.Wrap(-1)
        sizer5.Add(self.labelCancelSE, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxCancelSEChoices = []
        self.comboBoxCancelSE = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxCancelSEChoices, 0)
        sizer5.Add(self.comboBoxCancelSE, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelBuzzerSE = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Buzzer SE:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelBuzzerSE.Wrap(-1)
        sizer5.Add(self.labelBuzzerSE, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxBuzzerSEChoices = []
        self.comboBoxBuzzerSE = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxBuzzerSEChoices, 0)
        sizer5.Add(self.comboBoxBuzzerSE, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelEquipSE = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Equip SE:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelEquipSE.Wrap(-1)
        sizer5.Add(self.labelEquipSE, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxEquipSEChoices = []
        self.comboBoxEquipSE = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxEquipSEChoices, 0)
        sizer5.Add(self.comboBoxEquipSE, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelShopSE = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Shop SE:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelShopSE.Wrap(-1)
        sizer5.Add(self.labelShopSE, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxShopSEChoices = []
        self.comboBoxShopSE = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxShopSEChoices, 0)
        sizer5.Add(
            self.comboBoxShopSE, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelSaveSE = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Save SE:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelSaveSE.Wrap(-1)
        sizer5.Add(self.labelSaveSE, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxSaveSEChoices = []
        self.comboBoxSaveSE = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxSaveSEChoices, 0)
        sizer5.Add(
            self.comboBoxSaveSE, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelLoadSE = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Load SE:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelLoadSE.Wrap(-1)
        sizer5.Add(self.labelLoadSE, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxLoadSEChoices = []
        self.comboBoxLoadSE = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxLoadSEChoices, 0)
        sizer5.Add(
            self.comboBoxLoadSE, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelBattleStartSE = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Battle Start SE:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelBattleStartSE.Wrap(-1)
        sizer5.Add(self.labelBattleStartSE, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxBattleStartSEChoices = []
        self.comboBoxBattleStartSE = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxBattleStartSEChoices, 0)
        sizer5.Add(self.comboBoxBattleStartSE, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelEscapeSE = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Escape SE:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelEscapeSE.Wrap(-1)
        sizer5.Add(self.labelEscapeSE, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxEscapeSEChoices = []
        self.comboBoxEscapeSE = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxEscapeSEChoices, 0)
        sizer5.Add(self.comboBoxEscapeSE, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelActorCollapseSE = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Actor Collapse SE:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelActorCollapseSE.Wrap(-1)
        sizer5.Add(self.labelActorCollapseSE, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxActorCollapseSEChoices = []
        self.comboBoxActorCollapseSE = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxActorCollapseSEChoices, 0)
        sizer5.Add(self.comboBoxActorCollapseSE, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelEnemyCollapseSE = wx.StaticText(sizer2.GetStaticBox(), wx.ID_ANY, _(
            "Enemy Collapse SE:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelEnemyCollapseSE.Wrap(-1)
        sizer5.Add(self.labelEnemyCollapseSE, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxEnemyCollapseSEChoices = []
        self.comboBoxEnemyCollapseSE = wx.ComboBox(sizer2.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxEnemyCollapseSEChoices, 0)
        sizer5.Add(self.comboBoxEnemyCollapseSE, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizer2.Add(sizer5, 1, wx.EXPAND, 5)

        MainSizer.Add(sizer2, 45, wx.EXPAND | wx.ALL, 5)

        sizer3 = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Words")), wx.HORIZONTAL)

        sizer6 = wx.BoxSizer(wx.VERTICAL)

        self.labelGold = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "G (currency):"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelGold.Wrap(-1)
        sizer6.Add(self.labelGold, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlGold = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlGold.SetMaxLength(0)
        sizer6.Add(
            self.textCtrlGold, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelHP = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "HP:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelHP.Wrap(-1)
        sizer6.Add(self.labelHP, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlHP = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlHP.SetMaxLength(0)
        sizer6.Add(
            self.textCtrlHP, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelSP = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "SP:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelSP.Wrap(-1)
        sizer6.Add(self.labelSP, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlSP = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlSP.SetMaxLength(0)
        sizer6.Add(
            self.textCtrlSP, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelStr = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "STR:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelStr.Wrap(-1)
        sizer6.Add(self.labelStr, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlStr = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlStr.SetMaxLength(0)
        sizer6.Add(
            self.textCtrlStr, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelDex = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "DEX:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelDex.Wrap(-1)
        sizer6.Add(self.labelDex, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlDex = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlDex.SetMaxLength(0)
        sizer6.Add(
            self.textCtrlDex, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelAgi = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "AGI:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelAgi.Wrap(-1)
        sizer6.Add(self.labelAgi, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlAgi = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlAgi.SetMaxLength(0)
        sizer6.Add(
            self.textCtrlAgi, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelInt = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "INT:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelInt.Wrap(-1)
        sizer6.Add(self.labelInt, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlInt = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlInt.SetMaxLength(0)
        sizer6.Add(
            self.textCtrlInt, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelAtk = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "ATK:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelAtk.Wrap(-1)
        sizer6.Add(self.labelAtk, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlAtk = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlAtk.SetMaxLength(0)
        sizer6.Add(
            self.textCtrlAtk, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelPdef = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "PDEF:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelPdef.Wrap(-1)
        sizer6.Add(self.labelPdef, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlPdef = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlPdef.SetMaxLength(0)
        sizer6.Add(
            self.textCtrlPdef, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelMdef = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "MDEF:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelMdef.Wrap(-1)
        sizer6.Add(self.labelMdef, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlMdef = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlMdef.SetMaxLength(0)
        sizer6.Add(
            self.textCtrlMdef, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizer3.Add(sizer6, 1, wx.EXPAND, 5)

        sizer7 = wx.BoxSizer(wx.VERTICAL)

        self.labelWeapon = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "Weapon:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelWeapon.Wrap(-1)
        sizer7.Add(self.labelWeapon, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlWeapon = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlWeapon.SetMaxLength(0)
        sizer7.Add(
            self.textCtrlWeapon, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelShield = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "Shield:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelShield.Wrap(-1)
        sizer7.Add(self.labelShield, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlShield = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlShield.SetMaxLength(0)
        sizer7.Add(
            self.textCtrlShield, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelHelmet = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "Helmet:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelHelmet.Wrap(-1)
        sizer7.Add(self.labelHelmet, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlHelmet = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlHelmet.SetMaxLength(0)
        sizer7.Add(
            self.textCtrlHelmet, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelBodyArmor = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "Body Armor:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelBodyArmor.Wrap(-1)
        sizer7.Add(self.labelBodyArmor, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlBodyArmor = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlBodyArmor.SetMaxLength(0)
        sizer7.Add(self.textCtrlBodyArmor, 0, wx.EXPAND |
                   wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelAccessory = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "Accessory:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelAccessory.Wrap(-1)
        sizer7.Add(self.labelAccessory, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlAccessory = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlAccessory.SetMaxLength(0)
        sizer7.Add(self.textCtrlAccessory, 0, wx.EXPAND |
                   wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelAttack = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "Attack:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelAttack.Wrap(-1)
        sizer7.Add(self.labelAttack, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlAttack = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlAttack.SetMaxLength(0)
        sizer7.Add(
            self.textCtrlAttack, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelSkill = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "Skill:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelSkill.Wrap(-1)
        sizer7.Add(self.labelSkill, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlSkill = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlSkill.SetMaxLength(0)
        sizer7.Add(
            self.textCtrlSkill, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelDefend = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "Defend:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelDefend.Wrap(-1)
        sizer7.Add(self.labelDefend, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlDefend = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlDefend.SetMaxLength(0)
        sizer7.Add(
            self.textCtrlDefend, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelItem = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "Item:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelItem.Wrap(-1)
        sizer7.Add(self.labelItem, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlItem = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlItem.SetMaxLength(0)
        sizer7.Add(
            self.textCtrlItem, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelEquip = wx.StaticText(sizer3.GetStaticBox(), wx.ID_ANY, _(
            "Equip:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelEquip.Wrap(-1)
        sizer7.Add(self.labelEquip, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlEquip = wx.TextCtrl(sizer3.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlEquip.SetMaxLength(0)
        sizer7.Add(
            self.textCtrlEquip, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizer3.Add(sizer7, 1, wx.EXPAND, 5)

        MainSizer.Add(sizer3, 30, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        # Connect Events
        self.listCtrlInitialParty.Bind(
            wx.EVT_LEFT_DCLICK, self.listCtrlInitialParty_DoubleClicked)
        self.listCtrlInitialParty.Bind(
            wx.EVT_LIST_DELETE_ITEM, self.listCtrlInitialParty_ItemDeleted)
        self.listBoxElements.Bind(
            wx.EVT_LISTBOX, self.listBoxElements_SelectionChanged)
        self.textControlElementName.Bind(
            wx.EVT_TEXT, self.textCtrlElement_TextChanged)
        self.buttonMaximum.Bind(wx.EVT_BUTTON, self.buttonMaximum_Clicked)
        self.comboBoxWindowskinGraphic.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxWindowskinGraphic_Clicked)
        self.comboBoxTitleGraphic.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxTitleGraphic_Clicked)
        self.comboBoxGameoverGraphic.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxGameoverGraphic_Clciked)
        self.comboBoxBattleTransitionGraphic.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxBattleTransitionGraphic_Clicked)
        self.comboBoxTitleBGM.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxTitleBGM_Clicked)
        self.comboBoxBattleBGM.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxBattleBGM_Clicked)
        self.comboBoxBattleEndME.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxBattleEndME_Clicked)
        self.comboBoxGameoverME.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxGameoverME_Clicked)
        self.comboBoxCursorSE.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxCursorSE_Clicked)
        self.comboBoxDecisionSE.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxDecisionSE_Clicked)
        self.comboBoxCancelSE.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxCancelSE_Clicked)
        self.comboBoxBuzzerSE.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxBuzzerSE_Clicked)
        self.comboBoxEquipSE.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxEquipSE_Clicked)
        self.comboBoxShopSE.Bind(wx.EVT_LEFT_DOWN, self.comboBoxShopSE_Clicked)
        self.comboBoxSaveSE.Bind(wx.EVT_LEFT_DOWN, self.comboBoxSaveSE_Clicked)
        self.comboBoxLoadSE.Bind(wx.EVT_LEFT_DOWN, self.comboBoxLoadSE_Clicked)
        self.comboBoxBattleStartSE.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxBattleStartSE_Clicked)
        self.comboBoxEscapeSE.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxEscapeSE_Clicked)
        self.comboBoxActorCollapseSE.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxActorCollapseSE_Clicked)
        self.comboBoxEnemyCollapseSE.Bind(
            wx.EVT_LEFT_DOWN, self.comboBoxEnemyCollapseSE_Clicked)
        self.textCtrlGold.Bind(wx.EVT_TEXT, self.textCtrlGold_TextChanged)
        self.textCtrlHP.Bind(wx.EVT_TEXT, self.textCtrlHP_TextChanged)
        self.textCtrlSP.Bind(wx.EVT_TEXT, self.textCtrlSP_TextChanged)
        self.textCtrlStr.Bind(wx.EVT_TEXT, self.textCtrlStr_TextChanged)
        self.textCtrlDex.Bind(wx.EVT_TEXT, self.textCtrlDex_TextChanged)
        self.textCtrlAgi.Bind(wx.EVT_TEXT, self.textCtrlAgi_TextChanged)
        self.textCtrlInt.Bind(wx.EVT_TEXT, self.textCtrlInt_TextChanged)
        self.textCtrlAtk.Bind(wx.EVT_TEXT, self.textCtrlAtk_TextChanged)
        self.textCtrlPdef.Bind(wx.EVT_TEXT, self.textCtrlPdef_TextChanged)
        self.textCtrlMdef.Bind(wx.EVT_TEXT, self.textCtrlMdef_TextChanged)
        self.textCtrlWeapon.Bind(wx.EVT_TEXT, self.textCtrlWeapon_TextChanged)
        self.textCtrlShield.Bind(wx.EVT_TEXT, self.textCtrlShield_TextChanged)
        self.textCtrlHelmet.Bind(wx.EVT_TEXT, self.textCtrlHelmet_TextChanged)
        self.textCtrlBodyArmor.Bind(
            wx.EVT_TEXT, self.textCtrlBodyArmor_TextChanged)
        self.textCtrlAccessory.Bind(
            wx.EVT_TEXT, self.textCtrlAccessory_TextChanged)
        self.textCtrlAttack.Bind(wx.EVT_TEXT, self.textCtrlAttack_TextChanged)
        self.textCtrlSkill.Bind(wx.EVT_TEXT, self.textCtrlSkill_TextChanged)
        self.textCtrlDefend.Bind(wx.EVT_TEXT, self.textCtrlDefend_TextChanged)
        self.textCtrlItem.Bind(wx.EVT_TEXT, self.textCtrlItem_TextChanged)
        self.textCtrlEquip.Bind(wx.EVT_TEXT, self.textCtrlEquip_TextChanged)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def listCtrlInitialParty_DoubleClicked(self, event):
        event.Skip()

    def listCtrlInitialParty_ItemDeleted(self, event):
        event.Skip()

    def listBoxElements_SelectionChanged(self, event):
        event.Skip()

    def textCtrlElement_TextChanged(self, event):
        event.Skip()

    def buttonMaximum_Clicked(self, event):
        event.Skip()

    def comboBoxWindowskinGraphic_Clicked(self, event):
        event.Skip()

    def comboBoxTitleGraphic_Clicked(self, event):
        event.Skip()

    def comboBoxGameoverGraphic_Clciked(self, event):
        event.Skip()

    def comboBoxBattleTransitionGraphic_Clicked(self, event):
        event.Skip()

    def comboBoxTitleBGM_Clicked(self, event):
        event.Skip()

    def comboBoxBattleBGM_Clicked(self, event):
        event.Skip()

    def comboBoxBattleEndME_Clicked(self, event):
        event.Skip()

    def comboBoxGameoverME_Clicked(self, event):
        event.Skip()

    def comboBoxCursorSE_Clicked(self, event):
        event.Skip()

    def comboBoxDecisionSE_Clicked(self, event):
        event.Skip()

    def comboBoxCancelSE_Clicked(self, event):
        event.Skip()

    def comboBoxBuzzerSE_Clicked(self, event):
        event.Skip()

    def comboBoxEquipSE_Clicked(self, event):
        event.Skip()

    def comboBoxShopSE_Clicked(self, event):
        event.Skip()

    def comboBoxSaveSE_Clicked(self, event):
        event.Skip()

    def comboBoxLoadSE_Clicked(self, event):
        event.Skip()

    def comboBoxBattleStartSE_Clicked(self, event):
        event.Skip()

    def comboBoxEscapeSE_Clicked(self, event):
        event.Skip()

    def comboBoxActorCollapseSE_Clicked(self, event):
        event.Skip()

    def comboBoxEnemyCollapseSE_Clicked(self, event):
        event.Skip()

    def textCtrlGold_TextChanged(self, event):
        event.Skip()

    def textCtrlHP_TextChanged(self, event):
        event.Skip()

    def textCtrlSP_TextChanged(self, event):
        event.Skip()

    def textCtrlStr_TextChanged(self, event):
        event.Skip()

    def textCtrlDex_TextChanged(self, event):
        event.Skip()

    def textCtrlAgi_TextChanged(self, event):
        event.Skip()

    def textCtrlInt_TextChanged(self, event):
        event.Skip()

    def textCtrlAtk_TextChanged(self, event):
        event.Skip()

    def textCtrlPdef_TextChanged(self, event):
        event.Skip()

    def textCtrlMdef_TextChanged(self, event):
        event.Skip()

    def textCtrlWeapon_TextChanged(self, event):
        event.Skip()

    def textCtrlShield_TextChanged(self, event):
        event.Skip()

    def textCtrlHelmet_TextChanged(self, event):
        event.Skip()

    def textCtrlBodyArmor_TextChanged(self, event):
        event.Skip()

    def textCtrlAccessory_TextChanged(self, event):
        event.Skip()

    def textCtrlAttack_TextChanged(self, event):
        event.Skip()

    def textCtrlSkill_TextChanged(self, event):
        event.Skip()

    def textCtrlDefend_TextChanged(self, event):
        event.Skip()

    def textCtrlItem_TextChanged(self, event):
        event.Skip()

    def textCtrlEquip_TextChanged(self, event):
        event.Skip()


###########################################################################
# Class BattleTestActor_Panel_Template
###########################################################################

class BattleTestActor_Panel_Template (wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(
            464, 280), style=wx.TAB_TRAVERSAL)

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        sizerSettings = wx.BoxSizer(wx.VERTICAL)

        sizerSelection = wx.BoxSizer(wx.HORIZONTAL)

        sizerActor = wx.BoxSizer(wx.VERTICAL)

        self.labelActor = wx.StaticText(
            self, wx.ID_ANY, _("Actor:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelActor.Wrap(-1)
        sizerActor.Add(self.labelActor, 0, wx.ALL, 5)

        comboBoxActorChoices = []
        self.comboBoxActor = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(160, -1), comboBoxActorChoices, 0)
        self.comboBoxActor.SetSelection(0)
        sizerActor.Add(
            self.comboBoxActor, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerSelection.Add(sizerActor, 0, 0, 5)

        sizerLevel = wx.BoxSizer(wx.VERTICAL)

        self.labelLevel = wx.StaticText(
            self, wx.ID_ANY, _("Level:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelLevel.Wrap(-1)
        sizerLevel.Add(self.labelLevel, 0, wx.ALL, 5)

        self.spinCtrlLevel = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerLevel.Add(
            self.spinCtrlLevel, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizerSelection.Add(sizerLevel, 1, wx.EXPAND, 5)

        sizerSettings.Add(sizerSelection, 0, wx.EXPAND, 5)

        sizerEquipment = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Equipment")), wx.VERTICAL)

        sizerWeapon = wx.BoxSizer(wx.HORIZONTAL)

        self.labelWeapon = wx.StaticText(sizerEquipment.GetStaticBox(), wx.ID_ANY, _(
            "Weapon:"), wx.DefaultPosition, wx.Size(64, -1), 0)
        self.labelWeapon.Wrap(-1)
        sizerWeapon.Add(
            self.labelWeapon, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        comboBoxWeaponChoices = []
        self.comboBoxWeapon = wx.Choice(sizerEquipment.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxWeaponChoices, 0)
        self.comboBoxWeapon.SetSelection(0)
        sizerWeapon.Add(self.comboBoxWeapon, 1, wx.ALL, 5)

        sizerEquipment.Add(sizerWeapon, 0, wx.EXPAND, 5)

        sizerShield = wx.BoxSizer(wx.HORIZONTAL)

        self.labelShield = wx.StaticText(sizerEquipment.GetStaticBox(), wx.ID_ANY, _(
            "Shield:"), wx.DefaultPosition, wx.Size(64, -1), 0)
        self.labelShield.Wrap(-1)
        sizerShield.Add(
            self.labelShield, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        comboBoxShieldChoices = []
        self.comboBoxShield = wx.Choice(sizerEquipment.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxShieldChoices, 0)
        self.comboBoxShield.SetSelection(0)
        sizerShield.Add(self.comboBoxShield, 1, wx.ALL, 5)

        sizerEquipment.Add(sizerShield, 1, wx.EXPAND, 5)

        sizerHelmet = wx.BoxSizer(wx.HORIZONTAL)

        self.labelHelmet = wx.StaticText(sizerEquipment.GetStaticBox(), wx.ID_ANY, _(
            "Helmet:"), wx.DefaultPosition, wx.Size(64, -1), 0)
        self.labelHelmet.Wrap(-1)
        sizerHelmet.Add(
            self.labelHelmet, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        comboBoxHelmetChoices = []
        self.comboBoxHelmet = wx.Choice(sizerEquipment.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxHelmetChoices, 0)
        self.comboBoxHelmet.SetSelection(0)
        sizerHelmet.Add(self.comboBoxHelmet, 1, wx.ALL, 5)

        sizerEquipment.Add(sizerHelmet, 1, wx.EXPAND, 5)

        sizerArmor = wx.BoxSizer(wx.HORIZONTAL)

        self.labelBodyArmor = wx.StaticText(sizerEquipment.GetStaticBox(), wx.ID_ANY, _(
            "Body Armor:"), wx.DefaultPosition, wx.Size(64, -1), 0)
        self.labelBodyArmor.Wrap(-1)
        sizerArmor.Add(
            self.labelBodyArmor, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        comboBoxBodyArmorChoices = []
        self.comboBoxBodyArmor = wx.Choice(sizerEquipment.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxBodyArmorChoices, 0)
        self.comboBoxBodyArmor.SetSelection(0)
        sizerArmor.Add(self.comboBoxBodyArmor, 1, wx.ALL, 5)

        sizerEquipment.Add(sizerArmor, 1, wx.EXPAND, 5)

        sizerAccessory = wx.BoxSizer(wx.HORIZONTAL)

        self.labelAccessory = wx.StaticText(sizerEquipment.GetStaticBox(), wx.ID_ANY, _(
            "Accessory:"), wx.DefaultPosition, wx.Size(64, -1), 0)
        self.labelAccessory.Wrap(-1)
        sizerAccessory.Add(
            self.labelAccessory, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        comboBoxAccessoryChoices = []
        self.comboBoxAccessory = wx.Choice(sizerEquipment.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxAccessoryChoices, 0)
        self.comboBoxAccessory.SetSelection(0)
        sizerAccessory.Add(self.comboBoxAccessory, 1, wx.ALL, 5)

        sizerEquipment.Add(sizerAccessory, 1, wx.EXPAND, 5)

        sizerSettings.Add(sizerEquipment, 1, wx.EXPAND | wx.ALL, 5)

        MainSizer.Add(sizerSettings, 65, wx.EXPAND, 5)

        sizerStats = wx.BoxSizer(wx.VERTICAL)

        sizerStatus = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Status")), wx.HORIZONTAL)

        sizerStatName = wx.BoxSizer(wx.VERTICAL)

        self.labelNameMaxHP = wx.StaticText(sizerStatus.GetStaticBox(), wx.ID_ANY, _(
            "MaxHP:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelNameMaxHP.Wrap(-1)
        sizerStatName.Add(self.labelNameMaxHP, 0, wx.ALL, 5)

        self.labelNameMaxSP = wx.StaticText(sizerStatus.GetStaticBox(), wx.ID_ANY, _(
            "MaxSP:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelNameMaxSP.Wrap(-1)
        sizerStatName.Add(
            self.labelNameMaxSP, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelNameStr = wx.StaticText(sizerStatus.GetStaticBox(), wx.ID_ANY, _(
            "STR:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelNameStr.Wrap(-1)
        sizerStatName.Add(self.labelNameStr, 0, wx.ALL, 5)

        self.labelNameDex = wx.StaticText(sizerStatus.GetStaticBox(), wx.ID_ANY, _(
            "DEX:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelNameDex.Wrap(-1)
        sizerStatName.Add(
            self.labelNameDex, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelNameAgi = wx.StaticText(sizerStatus.GetStaticBox(), wx.ID_ANY, _(
            "AGI:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelNameAgi.Wrap(-1)
        sizerStatName.Add(
            self.labelNameAgi, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelNameInt = wx.StaticText(sizerStatus.GetStaticBox(), wx.ID_ANY, _(
            "INT:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelNameInt.Wrap(-1)
        sizerStatName.Add(
            self.labelNameInt, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelNameAtk = wx.StaticText(sizerStatus.GetStaticBox(), wx.ID_ANY, _(
            "ATK:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelNameAtk.Wrap(-1)
        sizerStatName.Add(self.labelNameAtk, 0, wx.ALL, 5)

        self.labelNamePdef = wx.StaticText(sizerStatus.GetStaticBox(), wx.ID_ANY, _(
            "PDEF:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelNamePdef.Wrap(-1)
        sizerStatName.Add(
            self.labelNamePdef, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelNameMdef = wx.StaticText(sizerStatus.GetStaticBox(), wx.ID_ANY, _(
            "MDEF:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelNameMdef.Wrap(-1)
        sizerStatName.Add(
            self.labelNameMdef, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerStatus.Add(sizerStatName, 1, wx.EXPAND, 5)

        sizerStatValue = wx.BoxSizer(wx.VERTICAL)

        self.labelValueMaxHP = wx.StaticText(sizerStatus.GetStaticBox(), wx.ID_ANY, _(
            "(Value)"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelValueMaxHP.Wrap(-1)
        sizerStatValue.Add(self.labelValueMaxHP, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.labelValueMaxSP = wx.StaticText(sizerStatus.GetStaticBox(), wx.ID_ANY, _(
            "(Value)"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelValueMaxSP.Wrap(-1)
        sizerStatValue.Add(
            self.labelValueMaxSP, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.ALIGN_RIGHT, 5)

        self.labelValueStr = wx.StaticText(sizerStatus.GetStaticBox(), wx.ID_ANY, _(
            "(Value)"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelValueStr.Wrap(-1)
        sizerStatValue.Add(self.labelValueStr, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.labelValueDex = wx.StaticText(sizerStatus.GetStaticBox(), wx.ID_ANY, _(
            "(Value)"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelValueDex.Wrap(-1)
        sizerStatValue.Add(
            self.labelValueDex, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.ALIGN_RIGHT, 5)

        self.labelValueAgi = wx.StaticText(sizerStatus.GetStaticBox(), wx.ID_ANY, _(
            "(Value)"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelValueAgi.Wrap(-1)
        sizerStatValue.Add(
            self.labelValueAgi, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.ALIGN_RIGHT, 5)

        self.labelValueInt = wx.StaticText(sizerStatus.GetStaticBox(), wx.ID_ANY, _(
            "(Value)"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelValueInt.Wrap(-1)
        sizerStatValue.Add(
            self.labelValueInt, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.ALIGN_RIGHT, 5)

        self.labelValueAtk = wx.StaticText(sizerStatus.GetStaticBox(), wx.ID_ANY, _(
            "(Value)"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelValueAtk.Wrap(-1)
        sizerStatValue.Add(self.labelValueAtk, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.labelValuePdef = wx.StaticText(sizerStatus.GetStaticBox(), wx.ID_ANY, _(
            "(Value)"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelValuePdef.Wrap(-1)
        sizerStatValue.Add(
            self.labelValuePdef, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.ALIGN_RIGHT, 5)

        self.labelValueMdef = wx.StaticText(sizerStatus.GetStaticBox(), wx.ID_ANY, _(
            "(Value)"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelValueMdef.Wrap(-1)
        sizerStatValue.Add(
            self.labelValueMdef, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.ALIGN_RIGHT, 5)

        sizerStatus.Add(sizerStatValue, 1, wx.EXPAND, 5)

        sizerStats.Add(sizerStatus, 1, wx.EXPAND | wx.ALL, 5)

        self.buttonIntialize = wx.Button(
            self, wx.ID_ANY, _("Initialize"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerStats.Add(
            self.buttonIntialize, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerStats, 35, wx.EXPAND, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        # Connect Events
        self.comboBoxActor.Bind(
            wx.EVT_CHOICE, self.comboBoxActor_SelectionChanged)
        self.spinCtrlLevel.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlLevel_ValueChanged)
        self.buttonIntialize.Bind(wx.EVT_BUTTON, self.buttonInitialize_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def comboBoxActor_SelectionChanged(self, event):
        event.Skip()

    def spinCtrlLevel_ValueChanged(self, event):
        event.Skip()

    def buttonInitialize_Clicked(self, event):
        event.Skip()


###########################################################################
# Class ChangeMaximum_Dialog_Template
###########################################################################

class ChangeMaximum_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(
            "Change Maximum..."), pos=wx.DefaultPosition, size=wx.Size(181, 115), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.Size(-1, -1))

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        self.labelMaximum = wx.StaticText(
            self, wx.ID_ANY, _("Maximum:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelMaximum.Wrap(-1)
        MainSizer.Add(self.labelMaximum, 0, wx.ALL, 5)

        self.spinCtrlMaximum = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), wx.SP_ARROW_KEYS | wx.SP_WRAP, 0, 65535, 0)
        MainSizer.Add(
            self.spinCtrlMaximum, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonCancel, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        MainSizer.Add(sizerOKCancel, 1, wx.ALIGN_BOTTOM |
                      wx.FIXED_MINSIZE | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class ExpCurve_Dialog_Template
###########################################################################

class ExpCurve_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_("Experience Curve"), pos=wx.DefaultPosition, size=wx.Size(
            449, 460), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        self.noteBookExpList = wx.Notebook(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.panelNextLevel = wx.Panel(
            self.noteBookExpList, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        panelSizerNextLevel = wx.BoxSizer(wx.VERTICAL)

        self.textCtrlExpList = wx.TextCtrl(self.panelNextLevel, wx.ID_ANY, wx.EmptyString,
                                           wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP | wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.textCtrlExpList.SetMaxLength(0)
        panelSizerNextLevel.Add(self.textCtrlExpList, 1, wx.EXPAND, 5)

        self.panelNextLevel.SetSizer(panelSizerNextLevel)
        self.panelNextLevel.Layout()
        panelSizerNextLevel.Fit(self.panelNextLevel)
        self.noteBookExpList.AddPage(
            self.panelNextLevel, _("To Next Level"), True)
        self.panelTotal = wx.Panel(
            self.noteBookExpList, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        panelSizerTotal = wx.BoxSizer(wx.VERTICAL)

        self.panelTotal.SetSizer(panelSizerTotal)
        self.panelTotal.Layout()
        panelSizerTotal.Fit(self.panelTotal)
        self.noteBookExpList.AddPage(self.panelTotal, _("Total"), False)

        MainSizer.Add(self.noteBookExpList, 1, wx.EXPAND | wx.ALL, 5)

        sizerControls = wx.BoxSizer(wx.HORIZONTAL)

        sizerBasis = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Basis")), wx.HORIZONTAL)

        self.sliderBasis = wx.Slider(sizerBasis.GetStaticBox(
        ), wx.ID_ANY, 35, 10, 50, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        sizerBasis.Add(self.sliderBasis, 1, wx.ALL, 5)

        self.spinCtrlBasis = wx.SpinCtrl(sizerBasis.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(60, -1), wx.SP_ARROW_KEYS, 10, 50, 35)
        sizerBasis.Add(self.spinCtrlBasis, 0, wx.ALL, 5)

        sizerControls.Add(sizerBasis, 1, wx.ALL, 5)

        sizerInflation = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Inflation")), wx.HORIZONTAL)

        self.sliderInflation = wx.Slider(sizerInflation.GetStaticBox(
        ), wx.ID_ANY, 35, 10, 50, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        sizerInflation.Add(self.sliderInflation, 1, wx.ALL, 5)

        self.spinCtrlInflation = wx.SpinCtrl(sizerInflation.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(60, -1), wx.SP_ARROW_KEYS, 10, 50, 35)
        sizerInflation.Add(self.spinCtrlInflation, 0, wx.ALL, 5)

        sizerControls.Add(sizerInflation, 1, wx.ALL, 5)

        MainSizer.Add(sizerControls, 0, wx.EXPAND, 5)

        sizerButtons = wx.BoxSizer(wx.HORIZONTAL)

        sizerGraphButton = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonViewGraph = wx.Button(
            self, wx.ID_ANY, _("View Graph..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerGraphButton.Add(self.buttonViewGraph, 0, wx.ALL, 5)

        sizerButtons.Add(sizerGraphButton, 1, 0, 5)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons.Add(self.buttonOK, 0, wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons.Add(self.buttonCancel, 0, wx.ALL, 5)

        MainSizer.Add(
            sizerButtons, 0, wx.ALIGN_RIGHT | wx.ALIGN_BOTTOM | wx.EXPAND, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.noteBookExpList.Bind(
            wx.EVT_NOTEBOOK_PAGE_CHANGED, self.noteBookExpCurve_PageChanged)
        self.sliderBasis.Bind(wx.EVT_SCROLL, self.sliderBasis_Scrolled)
        self.spinCtrlBasis.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlBasis__ValueChanged)
        self.sliderInflation.Bind(wx.EVT_SCROLL, self.sliderInflation_Scrolled)
        self.spinCtrlInflation.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlInflation_ValueChanged)
        self.buttonViewGraph.Bind(wx.EVT_BUTTON, self.buttonViewGraph_Clicked)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def noteBookExpCurve_PageChanged(self, event):
        event.Skip()

    def sliderBasis_Scrolled(self, event):
        event.Skip()

    def spinCtrlBasis__ValueChanged(self, event):
        event.Skip()

    def sliderInflation_Scrolled(self, event):
        event.Skip()

    def spinCtrlInflation_ValueChanged(self, event):
        event.Skip()

    def buttonViewGraph_Clicked(self, event):
        event.Skip()

    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class GenerateCurve_Dialog_Template
###########################################################################

class GenerateCurve_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(
            "Generate Curve"), pos=wx.DefaultPosition, size=wx.Size(275, 177), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        sizerLabels = wx.BoxSizer(wx.HORIZONTAL)

        self.labelLevel1 = wx.StaticText(
            self, wx.ID_ANY, _("Level 1:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelLevel1.Wrap(-1)
        sizerLabels.Add(self.labelLevel1, 1, wx.ALL, 5)

        self.labelMaxLevel = wx.StaticText(
            self, wx.ID_ANY, _("Max Level:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelMaxLevel.Wrap(-1)
        sizerLabels.Add(self.labelMaxLevel, 1, wx.ALL, 5)

        self.labelSpeed = wx.StaticText(
            self, wx.ID_ANY, _("Speed:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelSpeed.Wrap(-1)
        sizerLabels.Add(self.labelSpeed, 1, wx.ALL, 5)

        MainSizer.Add(sizerLabels, 0, wx.EXPAND, 5)

        sizerControls = wx.BoxSizer(wx.HORIZONTAL)

        self.spinCtrlInitial = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerControls.Add(
            self.spinCtrlInitial, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlFinal = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerControls.Add(
            self.spinCtrlFinal, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        from wx.lib.agw.floatspin import FloatSpin
        self.spinCtrlSpeed = FloatSpin(self)
        sizerControls.Add(
            self.spinCtrlSpeed, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerControls, 1, wx.EXPAND, 5)

        self.sliderSpeed = wx.Slider(self, wx.ID_ANY, 0, -10, 10, wx.DefaultPosition,
                                     wx.DefaultSize, wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS | wx.SL_TOP)
        MainSizer.Add(self.sliderSpeed, 0, wx.ALL | wx.EXPAND, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.buttonOK.SetDefault()
        sizerOKCancel.Add(self.buttonOK, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(
            self.buttonCancel, 0, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        MainSizer.Add(sizerOKCancel, 1, wx.ALIGN_RIGHT, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.sliderSpeed.Bind(wx.EVT_SCROLL, self.sliderSpeed_Scrolled)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def sliderSpeed_Scrolled(self, event):
        event.Skip()

    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class ChooseGraphic_Dialog_Template
###########################################################################

class ChooseGraphic_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_("Choose Graphic"), pos=wx.DefaultPosition, size=wx.Size(
            640, 480), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        sizerControls = wx.BoxSizer(wx.HORIZONTAL)

        listBoxGraphicsChoices = []
        self.listBoxGraphics = wx.ListBox(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(160, -1), listBoxGraphicsChoices, 0)
        sizerControls.Add(self.listBoxGraphics, 0, wx.ALL | wx.EXPAND, 5)

        sizerGraphic = wx.BoxSizer(wx.VERTICAL)

        self.panelGraphic = wx.ScrolledWindow(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL | wx.SUNKEN_BORDER | wx.VSCROLL)
        self.panelGraphic.SetScrollRate(5, 5)
        sizerGLGraphic = wx.BoxSizer(wx.VERTICAL)

        from .Extras import EditorGLPanel
        parent = self.panelGraphic
        self.glCanvasGraphic = EditorGLPanel(parent, -1, 1, 1, (0, 0,), 1)
        sizerGLGraphic.Add(self.glCanvasGraphic, 1, wx.ALL | wx.EXPAND, 0)

        self.panelGraphic.SetSizer(sizerGLGraphic)
        self.panelGraphic.Layout()
        sizerGLGraphic.Fit(self.panelGraphic)
        sizerGraphic.Add(self.panelGraphic, 1, wx.EXPAND | wx.ALL, 5)

        sizerHue = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Hue")), wx.VERTICAL)

        self.sliderHue = wx.Slider(sizerHue.GetStaticBox(
        ), wx.ID_ANY, 0, 0, 359, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        sizerHue.Add(self.sliderHue, 0, wx.ALL | wx.EXPAND, 5)

        sizerGraphic.Add(sizerHue, 0, wx.EXPAND | wx.ALL, 5)

        sizerControls.Add(sizerGraphic, 1, wx.EXPAND, 5)

        MainSizer.Add(sizerControls, 1, wx.EXPAND, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonCancel, 0, wx.ALL, 5)

        MainSizer.Add(sizerOKCancel, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.listBoxGraphics.Bind(
            wx.EVT_LISTBOX, self.listBoxGraphics_SelectionChanged)
        self.sliderHue.Bind(wx.EVT_SCROLL, self.sliderHue_Scrolled)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def listBoxGraphics_SelectionChanged(self, event):
        event.Skip()

    def sliderHue_Scrolled(self, event):
        event.Skip()

    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class Skill_Dialog_Template
###########################################################################

class Skill_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(
            "Skill"), pos=wx.DefaultPosition, size=wx.Size(244, 175), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.Size(-1, -1))

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        self.labelLevel = wx.StaticText(
            self, wx.ID_ANY, _("Level:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelLevel.Wrap(-1)
        MainSizer.Add(self.labelLevel, 0, wx.ALL, 5)

        self.spinCtrlLevel = wx.SpinCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(
            65, -1), wx.SP_ARROW_KEYS | wx.SP_WRAP, 0, 65535, 1)
        self.spinCtrlLevel.SetToolTipString(
            _("Level of the character when the skill is mastered"))

        MainSizer.Add(self.spinCtrlLevel, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelSkills = wx.StaticText(
            self, wx.ID_ANY, _("Skill to Learn:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelSkills.Wrap(-1)
        MainSizer.Add(self.labelSkills, 0, wx.ALL, 5)

        comboBoxSkillsChoices = []
        self.comboBoxSkills = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxSkillsChoices, 0)
        self.comboBoxSkills.SetSelection(0)
        self.comboBoxSkills.SetToolTipString(_("The skill to learn"))

        MainSizer.Add(
            self.comboBoxSkills, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        sizerOKCancel.SetMinSize(wx.Size(1, 1))
        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.buttonOK.SetToolTipString(_("Add skill to learn"))

        sizerOKCancel.Add(self.buttonOK, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.buttonCancel.SetToolTipString(_("Cancel changes and return"))

        sizerOKCancel.Add(self.buttonCancel, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        MainSizer.Add(sizerOKCancel, 1, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class EnemyAction_Dialog_Template
###########################################################################

class EnemyAction_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(
            "Action"), pos=wx.DefaultPosition, size=wx.Size(309, 406), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        sizerCondition = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Condition")), wx.VERTICAL)

        sizerTurm = wx.BoxSizer(wx.HORIZONTAL)

        self.checkBoxTurn = wx.CheckBox(sizerCondition.GetStaticBox(), wx.ID_ANY, _(
            "Turn"), wx.DefaultPosition, wx.Size(64, -1), 0)
        sizerTurm.Add(
            self.checkBoxTurn, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.spinCtrlTurn1 = wx.SpinCtrl(sizerCondition.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(75, -1), wx.SP_ARROW_KEYS, 0, 10, 1)
        sizerTurm.Add(self.spinCtrlTurn1, 0, wx.ALL, 5)

        self.labelPlus = wx.StaticText(sizerCondition.GetStaticBox(), wx.ID_ANY, _(
            "+"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelPlus.Wrap(-1)
        sizerTurm.Add(self.labelPlus, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.spinCtrlTurn2 = wx.SpinCtrl(sizerCondition.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(75, -1), wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerTurm.Add(self.spinCtrlTurn2, 0, wx.ALL, 5)

        self.labelX = wx.StaticText(sizerCondition.GetStaticBox(), wx.ID_ANY, _(
            "X"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelX.Wrap(-1)
        sizerTurm.Add(self.labelX, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sizerCondition.Add(sizerTurm, 0, wx.EXPAND, 5)

        sizerHP = wx.BoxSizer(wx.HORIZONTAL)

        self.checkBoxTurn = wx.CheckBox(sizerCondition.GetStaticBox(), wx.ID_ANY, _(
            "HP"), wx.DefaultPosition, wx.Size(64, -1), 0)
        sizerHP.Add(self.checkBoxTurn, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.spinCtrlHP = wx.SpinCtrl(sizerCondition.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(75, -1), wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerHP.Add(self.spinCtrlHP, 0, wx.ALL, 5)

        self.labelBelow = wx.StaticText(sizerCondition.GetStaticBox(), wx.ID_ANY, _(
            "% or below"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelBelow.Wrap(-1)
        sizerHP.Add(self.labelBelow, 0, wx.ALIGN_CENTER_VERTICAL |
                    wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        sizerCondition.Add(sizerHP, 0, wx.EXPAND, 5)

        sizerLevel = wx.BoxSizer(wx.HORIZONTAL)

        self.checkBoxLevel = wx.CheckBox(sizerCondition.GetStaticBox(), wx.ID_ANY, _(
            "Level"), wx.DefaultPosition, wx.Size(64, -1), 0)
        sizerLevel.Add(
            self.checkBoxLevel, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.spinCtrlLevel = wx.SpinCtrl(sizerCondition.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(75, -1), wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerLevel.Add(self.spinCtrlLevel, 0, wx.ALL, 5)

        self.labelAbove = wx.StaticText(sizerCondition.GetStaticBox(), wx.ID_ANY, _(
            "or above"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelAbove.Wrap(-1)
        sizerLevel.Add(
            self.labelAbove, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        sizerCondition.Add(sizerLevel, 0, wx.EXPAND, 5)

        sizerSwitch = wx.BoxSizer(wx.HORIZONTAL)

        self.checkBoxSwitch = wx.CheckBox(sizerCondition.GetStaticBox(), wx.ID_ANY, _(
            "Switch"), wx.DefaultPosition, wx.Size(64, -1), 0)
        sizerSwitch.Add(
            self.checkBoxSwitch, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        comboBoxSwitchChoices = []
        self.comboBoxSwitch = wx.Choice(sizerCondition.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxSwitchChoices, 0)
        self.comboBoxSwitch.SetSelection(0)
        sizerSwitch.Add(self.comboBoxSwitch, 1, wx.ALL, 5)

        self.labelON = wx.StaticText(sizerCondition.GetStaticBox(), wx.ID_ANY, _(
            "is ON"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelON.Wrap(-1)
        sizerSwitch.Add(
            self.labelON, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        sizerCondition.Add(sizerSwitch, 0, wx.EXPAND, 5)

        MainSizer.Add(sizerCondition, 0, wx.ALL | wx.EXPAND, 5)

        sizerAction = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Action")), wx.VERTICAL)

        sizerBasic = wx.BoxSizer(wx.HORIZONTAL)

        self.radioBtnBasic = wx.RadioButton(sizerAction.GetStaticBox(), wx.ID_ANY, _(
            "Basic"), wx.DefaultPosition, wx.Size(64, -1), 0)
        sizerBasic.Add(
            self.radioBtnBasic, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        comboBoxBasicChoices = []
        self.comboBoxBasic = wx.Choice(sizerAction.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxBasicChoices, 0)
        self.comboBoxBasic.SetSelection(0)
        sizerBasic.Add(
            self.comboBoxBasic, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sizerAction.Add(sizerBasic, 0, wx.EXPAND, 5)

        sizerSkill = wx.BoxSizer(wx.HORIZONTAL)

        self.radioBtnSkill = wx.RadioButton(sizerAction.GetStaticBox(), wx.ID_ANY, _(
            "Skill"), wx.DefaultPosition, wx.Size(64, -1), 0)
        sizerSkill.Add(
            self.radioBtnSkill, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        comboBoxSkillChoices = []
        self.comboBoxSkill = wx.Choice(sizerAction.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxSkillChoices, 0)
        self.comboBoxSkill.SetSelection(0)
        sizerSkill.Add(self.comboBoxSkill, 1, wx.ALL, 5)

        sizerAction.Add(sizerSkill, 0, wx.EXPAND, 5)

        MainSizer.Add(sizerAction, 0, wx.EXPAND | wx.ALL, 5)

        sizerRating = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Rating")), wx.HORIZONTAL)

        self.sliderRating = wx.Slider(sizerRating.GetStaticBox(
        ), wx.ID_ANY, 5, 0, 10, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS | wx.SL_HORIZONTAL)
        sizerRating.Add(self.sliderRating, 1, wx.ALL, 5)

        self.spinCtrlRating = wx.SpinCtrl(sizerRating.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(64, -1), wx.SP_ARROW_KEYS, 0, 10, 5)
        sizerRating.Add(self.spinCtrlRating, 0, wx.ALL, 5)

        MainSizer.Add(sizerRating, 0, wx.ALL | wx.EXPAND, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonCancel, 0, wx.ALL, 5)

        MainSizer.Add(sizerOKCancel, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.checkBoxTurn.Bind(wx.EVT_CHECKBOX, self.checkBoxTurn_CheckChanged)
        self.checkBoxTurn.Bind(wx.EVT_CHECKBOX, self.checkBoxHP_CheckChanged)
        self.checkBoxLevel.Bind(
            wx.EVT_CHECKBOX, self.checkBoxLevel_CheckChanged)
        self.checkBoxSwitch.Bind(
            wx.EVT_CHECKBOX, self.checkBoxSwitch_CheckChanged)
        self.radioBtnBasic.Bind(
            wx.EVT_RADIOBUTTON, self.radioBtnBasic_CheckChanged)
        self.radioBtnSkill.Bind(
            wx.EVT_RADIOBUTTON, self.radioBtnSkill_CheckChanged)
        self.sliderRating.Bind(wx.EVT_SCROLL, self.sliderRating_ValueChanged)
        self.spinCtrlRating.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlRating_ValueChanged)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def checkBoxTurn_CheckChanged(self, event):
        event.Skip()

    def checkBoxHP_CheckChanged(self, event):
        event.Skip()

    def checkBoxLevel_CheckChanged(self, event):
        event.Skip()

    def checkBoxSwitch_CheckChanged(self, event):
        event.Skip()

    def radioBtnBasic_CheckChanged(self, event):
        event.Skip()

    def radioBtnSkill_CheckChanged(self, event):
        event.Skip()

    def sliderRating_ValueChanged(self, event):
        event.Skip()

    def spinCtrlRating_ValueChanged(self, event):
        event.Skip()

    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class ChooseTreasure_Dialog_Template
###########################################################################

class ChooseTreasure_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_("Treasure"), pos=wx.DefaultPosition, size=wx.Size(
            395, 348), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        self.listCtrlTreasure = wx.ListCtrl(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
        MainSizer.Add(self.listCtrlTreasure, 1, wx.ALL | wx.EXPAND, 5)

        sizerTreasure = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Select Treasure")), wx.HORIZONTAL)

        bSizer618 = wx.BoxSizer(wx.VERTICAL)

        bSizer623 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelProbability = wx.StaticText(sizerTreasure.GetStaticBox(), wx.ID_ANY, _(
            "Probability:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelProbability.Wrap(-1)
        bSizer623.Add(self.labelProbability, 0,
                      wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.spinCtrlProbability = wx.SpinCtrl(sizerTreasure.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(56, -1), wx.SP_ARROW_KEYS | wx.SP_WRAP, 0, 100, 50)
        bSizer623.Add(
            self.spinCtrlProbability, 0, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        self.labelQuantity = wx.StaticText(sizerTreasure.GetStaticBox(), wx.ID_ANY, _(
            "Quantity:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelQuantity.Wrap(-1)
        bSizer623.Add(
            self.labelQuantity, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.spinCtrlQuantity = wx.SpinCtrl(sizerTreasure.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS | wx.SP_WRAP, 1, 10, 1)
        bSizer623.Add(
            self.spinCtrlQuantity, 1, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        bSizer618.Add(bSizer623, 1, wx.EXPAND, 5)

        sizerItem = wx.BoxSizer(wx.HORIZONTAL)

        self.radioBtnItem = wx.RadioButton(sizerTreasure.GetStaticBox(), wx.ID_ANY, _(
            "Item"), wx.DefaultPosition, wx.Size(80, -1), wx.RB_GROUP)
        self.radioBtnItem.SetValue(True)
        sizerItem.Add(self.radioBtnItem, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxItemChoices = []
        self.comboBoxItem = wx.Choice(sizerTreasure.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxItemChoices, 0)
        self.comboBoxItem.SetSelection(0)
        sizerItem.Add(self.comboBoxItem, 1, wx.ALL, 5)

        bSizer618.Add(sizerItem, 0, wx.EXPAND, 5)

        sizerWeapon = wx.BoxSizer(wx.HORIZONTAL)

        self.radioBtnWeapon = wx.RadioButton(sizerTreasure.GetStaticBox(), wx.ID_ANY, _(
            "Weapon"), wx.DefaultPosition, wx.Size(80, -1), 0)
        sizerWeapon.Add(
            self.radioBtnWeapon, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        comboBoxWeaponChoices = []
        self.comboBoxWeapon = wx.Choice(sizerTreasure.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxWeaponChoices, 0)
        self.comboBoxWeapon.SetSelection(0)
        self.comboBoxWeapon.Enable(False)

        sizerWeapon.Add(self.comboBoxWeapon, 1, wx.ALL, 5)

        bSizer618.Add(sizerWeapon, 0, wx.EXPAND, 5)

        sizerArmor = wx.BoxSizer(wx.HORIZONTAL)

        self.radioBtnArmor = wx.RadioButton(sizerTreasure.GetStaticBox(), wx.ID_ANY, _(
            "Armor"), wx.DefaultPosition, wx.Size(80, -1), 0)
        sizerArmor.Add(
            self.radioBtnArmor, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        comboBoxArmorChoices = []
        self.comboBoxArmor = wx.Choice(sizerTreasure.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxArmorChoices, 0)
        self.comboBoxArmor.SetSelection(0)
        self.comboBoxArmor.Enable(False)

        sizerArmor.Add(self.comboBoxArmor, 1, wx.ALL, 5)

        bSizer618.Add(sizerArmor, 0, wx.EXPAND, 5)

        sizerTreasure.Add(bSizer618, 1, wx.EXPAND, 5)

        bSizer619 = wx.BoxSizer(wx.VERTICAL)

        self.buttonAdd = wx.Button(sizerTreasure.GetStaticBox(), wx.ID_ANY, _(
            "Add"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer619.Add(self.buttonAdd, 0, wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.buttonRemove = wx.Button(sizerTreasure.GetStaticBox(), wx.ID_ANY, _(
            "Remove"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer619.Add(self.buttonRemove, 0, wx.ALL, 5)

        sizerTreasure.Add(bSizer619, 0, wx.EXPAND, 5)

        MainSizer.Add(sizerTreasure, 0, wx.ALL | wx.EXPAND, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(
            self.buttonCancel, 0, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        MainSizer.Add(sizerOKCancel, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.listCtrlTreasure.Bind(
            wx.EVT_KEY_DOWN, self.listCtrlTreasure_KeyPressed)
        self.radioBtnItem.Bind(
            wx.EVT_RADIOBUTTON, self.radioButtonItem_Clicked)
        self.radioBtnWeapon.Bind(
            wx.EVT_RADIOBUTTON, self.radioButtonWeapon_Clicked)
        self.radioBtnArmor.Bind(
            wx.EVT_RADIOBUTTON, self.radioButtonArmor_Clicked)
        self.buttonAdd.Bind(wx.EVT_BUTTON, self.buttonAdd_Clicked)
        self.buttonRemove.Bind(wx.EVT_BUTTON, self.buttonRemove_Clicked)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def listCtrlTreasure_KeyPressed(self, event):
        event.Skip()

    def radioButtonItem_Clicked(self, event):
        event.Skip()

    def radioButtonWeapon_Clicked(self, event):
        event.Skip()

    def radioButtonArmor_Clicked(self, event):
        event.Skip()

    def buttonAdd_Clicked(self, event):
        event.Skip()

    def buttonRemove_Clicked(self, event):
        event.Skip()

    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class EventCondition_Dialog_Template
###########################################################################

class EventCondition_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(
            "Condition"), pos=wx.DefaultPosition, size=wx.Size(310, 259), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        sizerConditions = wx.BoxSizer(wx.VERTICAL)

        sizerTurn = wx.BoxSizer(wx.HORIZONTAL)

        self.checkBoxTurn = wx.CheckBox(
            self, wx.ID_ANY, _("Turn"), wx.DefaultPosition, wx.Size(72, -1), 0)
        sizerTurn.Add(
            self.checkBoxTurn, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.spinCtrlTurn1 = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(75, -1), wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerTurn.Add(self.spinCtrlTurn1, 0, wx.ALL, 5)

        self.labelPlus = wx.StaticText(
            self, wx.ID_ANY, _("+"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelPlus.Wrap(-1)
        sizerTurn.Add(self.labelPlus, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.spinCtrlTurn2 = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(75, -1), wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerTurn.Add(self.spinCtrlTurn2, 0, wx.ALL, 5)

        self.labelX = wx.StaticText(
            self, wx.ID_ANY, _("X"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelX.Wrap(-1)
        sizerTurn.Add(self.labelX, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sizerConditions.Add(sizerTurn, 0, wx.EXPAND, 5)

        sizerEnemy1 = wx.BoxSizer(wx.HORIZONTAL)

        self.checkBoxEnemy = wx.CheckBox(
            self, wx.ID_ANY, _("Enemy"), wx.DefaultPosition, wx.Size(72, -1), 0)
        sizerEnemy1.Add(
            self.checkBoxEnemy, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        comboBoxEnemyChoices = []
        self.comboBoxEnemy = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(160, -1), comboBoxEnemyChoices, 0)
        self.comboBoxEnemy.SetSelection(0)
        sizerEnemy1.Add(self.comboBoxEnemy, 0, wx.ALL, 5)

        self.labelHP1 = wx.StaticText(
            self, wx.ID_ANY, _("'s HP is"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelHP1.Wrap(-1)
        sizerEnemy1.Add(
            self.labelHP1, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        sizerConditions.Add(sizerEnemy1, 0, wx.EXPAND, 5)

        sizerEnemy2 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelFiller1 = wx.StaticText(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(72, -1), 0)
        self.labelFiller1.Wrap(-1)
        sizerEnemy2.Add(self.labelFiller1, 0, wx.ALL, 5)

        self.spinCtrlEnemyHPPercent = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(75, -1), wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerEnemy2.Add(self.spinCtrlEnemyHPPercent, 0, wx.ALL, 5)

        self.labelBelow1 = wx.StaticText(
            self, wx.ID_ANY, _("% or below"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelBelow1.Wrap(-1)
        sizerEnemy2.Add(
            self.labelBelow1, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        sizerConditions.Add(sizerEnemy2, 0, wx.EXPAND, 5)

        sizerActor1 = wx.BoxSizer(wx.HORIZONTAL)

        self.checkBoxActor = wx.CheckBox(
            self, wx.ID_ANY, _("Actor"), wx.DefaultPosition, wx.Size(72, -1), 0)
        sizerActor1.Add(
            self.checkBoxActor, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        comboBoxActorChoices = []
        self.comboBoxActor = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(160, -1), comboBoxActorChoices, 0)
        self.comboBoxActor.SetSelection(0)
        sizerActor1.Add(self.comboBoxActor, 0, wx.ALL, 5)

        self.labelHP2 = wx.StaticText(
            self, wx.ID_ANY, _("'s HP is"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelHP2.Wrap(-1)
        sizerActor1.Add(
            self.labelHP2, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        sizerConditions.Add(sizerActor1, 0, wx.EXPAND, 5)

        sizerActor2 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelFiller2 = wx.StaticText(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(72, -1), 0)
        self.labelFiller2.Wrap(-1)
        sizerActor2.Add(self.labelFiller2, 0, wx.ALL, 5)

        self.spinCtrlActorHPPercent = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(75, -1), wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerActor2.Add(self.spinCtrlActorHPPercent, 0, wx.ALL, 5)

        self.labelBelow2 = wx.StaticText(
            self, wx.ID_ANY, _("% or below"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelBelow2.Wrap(-1)
        sizerActor2.Add(
            self.labelBelow2, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        sizerConditions.Add(sizerActor2, 0, wx.EXPAND, 5)

        sizerSwitch = wx.BoxSizer(wx.HORIZONTAL)

        self.checkBoxSwitch = wx.CheckBox(
            self, wx.ID_ANY, _("Switch"), wx.DefaultPosition, wx.Size(72, -1), 0)
        sizerSwitch.Add(
            self.checkBoxSwitch, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        comboBoxSwitchChoices = []
        self.comboBoxSwitch = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(160, -1), comboBoxSwitchChoices, 0)
        self.comboBoxSwitch.SetSelection(0)
        sizerSwitch.Add(self.comboBoxSwitch, 0, wx.ALL, 5)

        self.labelON = wx.StaticText(
            self, wx.ID_ANY, _("is ON"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelON.Wrap(-1)
        sizerSwitch.Add(
            self.labelON, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        sizerConditions.Add(sizerSwitch, 0, wx.EXPAND, 5)

        MainSizer.Add(sizerConditions, 1, wx.EXPAND, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonCancel, 0, wx.ALL, 5)

        MainSizer.Add(sizerOKCancel, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.checkBoxTurn.Bind(wx.EVT_CHECKBOX, self.checkBoxTurn_CheckChanged)
        self.checkBoxEnemy.Bind(
            wx.EVT_CHECKBOX, self.checkBoxEnemy_CheckChanged)
        self.checkBoxActor.Bind(
            wx.EVT_CHECKBOX, self.checkBoxActor_CheckChanged)
        self.checkBoxSwitch.Bind(
            wx.EVT_CHECKBOX, self.checkBoxSwitch_CheckChanged)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def checkBoxTurn_CheckChanged(self, event):
        event.Skip()

    def checkBoxEnemy_CheckChanged(self, event):
        event.Skip()

    def checkBoxActor_CheckChanged(self, event):
        event.Skip()

    def checkBoxSwitch_CheckChanged(self, event):
        event.Skip()

    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class AnimationTiming_Dialog_Template
###########################################################################

class AnimationTiming_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(
            "SE and Flash Timing"), pos=wx.DefaultPosition, size=wx.Size(418, 349), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        sizerFrame = wx.BoxSizer(wx.HORIZONTAL)

        sizer1 = wx.BoxSizer(wx.VERTICAL)

        self.labelFrame = wx.StaticText(
            self, wx.ID_ANY, _("Frame:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelFrame.Wrap(-1)
        sizer1.Add(self.labelFrame, 0, wx.ALL | wx.EXPAND, 5)

        self.spinCtrlFrames = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizer1.Add(
            self.spinCtrlFrames, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerFrame.Add(sizer1, 20, 0, 5)

        sizer2 = wx.BoxSizer(wx.VERTICAL)

        self.labelSE = wx.StaticText(
            self, wx.ID_ANY, _("SE:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelSE.Wrap(-1)
        sizer2.Add(self.labelSE, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxSEChoices = []
        self.comboBoxSE = wx.ComboBox(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxSEChoices, 0)
        sizer2.Add(
            self.comboBoxSE, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerFrame.Add(sizer2, 45, 0, 5)

        sizer3 = wx.BoxSizer(wx.VERTICAL)

        self.labelCondition = wx.StaticText(
            self, wx.ID_ANY, _("Condition:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelCondition.Wrap(-1)
        sizer3.Add(self.labelCondition, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxConditionChoices = []
        self.comboBoxCondition = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxConditionChoices, 0)
        self.comboBoxCondition.SetSelection(0)
        sizer3.Add(self.comboBoxCondition, 35, wx.EXPAND |
                   wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerFrame.Add(sizer3, 35, 0, 5)

        MainSizer.Add(sizerFrame, 0, wx.EXPAND, 5)

        sizerFlash = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Flash")), wx.VERTICAL)

        sizerFlashArea = wx.BoxSizer(wx.HORIZONTAL)

        self.radioButtonNone = wx.RadioButton(sizerFlash.GetStaticBox(), wx.ID_ANY, _(
            "None"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerFlashArea.Add(self.radioButtonNone, 0, wx.ALL, 5)

        self.radioButtonTarget = wx.RadioButton(sizerFlash.GetStaticBox(), wx.ID_ANY, _(
            "Target"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerFlashArea.Add(self.radioButtonTarget, 0, wx.ALL, 5)

        self.radioButtonScreen = wx.RadioButton(sizerFlash.GetStaticBox(), wx.ID_ANY, _(
            "Screen"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerFlashArea.Add(self.radioButtonScreen, 0, wx.ALL, 5)

        self.radioButtonHideTarget = wx.RadioButton(sizerFlash.GetStaticBox(
        ), wx.ID_ANY, _("Hide Target"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerFlashArea.Add(self.radioButtonHideTarget, 0, wx.ALL, 5)

        sizerFlash.Add(sizerFlashArea, 0, wx.EXPAND, 5)

        sizer4 = wx.BoxSizer(wx.HORIZONTAL)

        sizer6 = wx.BoxSizer(wx.HORIZONTAL)

        sizer7 = wx.BoxSizer(wx.VERTICAL)

        sizerRed = wx.BoxSizer(wx.HORIZONTAL)

        self.labelRed = wx.StaticText(sizerFlash.GetStaticBox(), wx.ID_ANY, _(
            "Red:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelRed.Wrap(-1)
        sizerRed.Add(
            self.labelRed, 20, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

        self.sliderRed = wx.Slider(sizerFlash.GetStaticBox(
        ), wx.ID_ANY, 255, 0, 255, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        sizerRed.Add(self.sliderRed, 55, wx.ALL, 5)

        self.spinCtrlRed = wx.SpinCtrl(sizerFlash.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 255, 255)
        sizerRed.Add(self.spinCtrlRed, 25, wx.ALL, 5)

        sizer7.Add(sizerRed, 0, wx.EXPAND, 5)

        sizerGreen = wx.BoxSizer(wx.HORIZONTAL)

        self.labelGreen = wx.StaticText(sizerFlash.GetStaticBox(), wx.ID_ANY, _(
            "Green:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelGreen.Wrap(-1)
        sizerGreen.Add(
            self.labelGreen, 20, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

        self.sliderGreen = wx.Slider(sizerFlash.GetStaticBox(
        ), wx.ID_ANY, 255, 0, 255, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        sizerGreen.Add(self.sliderGreen, 55, wx.ALL, 5)

        self.spinCtrlGreen = wx.SpinCtrl(sizerFlash.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 255, 255)
        sizerGreen.Add(self.spinCtrlGreen, 25, wx.ALL, 5)

        sizer7.Add(sizerGreen, 0, wx.EXPAND, 5)

        sizerBlue = wx.BoxSizer(wx.HORIZONTAL)

        self.labelBlue = wx.StaticText(sizerFlash.GetStaticBox(), wx.ID_ANY, _(
            "Blue:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelBlue.Wrap(-1)
        sizerBlue.Add(
            self.labelBlue, 20, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

        self.sliderBlue = wx.Slider(sizerFlash.GetStaticBox(
        ), wx.ID_ANY, 255, 0, 255, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        sizerBlue.Add(self.sliderBlue, 55, wx.ALL, 5)

        self.spinCtrlBlue = wx.SpinCtrl(sizerFlash.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 255, 255)
        sizerBlue.Add(self.spinCtrlBlue, 25, wx.ALL, 5)

        sizer7.Add(sizerBlue, 0, wx.EXPAND, 5)

        sizerStrength = wx.BoxSizer(wx.HORIZONTAL)

        self.labelStrength = wx.StaticText(sizerFlash.GetStaticBox(), wx.ID_ANY, _(
            "Strength:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelStrength.Wrap(-1)
        sizerStrength.Add(
            self.labelStrength, 20, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

        self.sliderStrength = wx.Slider(sizerFlash.GetStaticBox(
        ), wx.ID_ANY, 255, 0, 255, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        sizerStrength.Add(self.sliderStrength, 55, wx.ALL, 5)

        self.spinCtrlStrength = wx.SpinCtrl(sizerFlash.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 255, 255)
        sizerStrength.Add(self.spinCtrlStrength, 25, wx.ALL, 5)

        sizer7.Add(sizerStrength, 0, wx.EXPAND, 5)

        sizer6.Add(sizer7, 75, wx.EXPAND, 5)

        self.m_bitmap33 = wx.StaticBitmap(sizerFlash.GetStaticBox(
        ), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER)
        sizer6.Add(self.m_bitmap33, 25, wx.ALL | wx.EXPAND, 5)

        sizer4.Add(sizer6, 1, wx.EXPAND, 5)

        sizerFlash.Add(sizer4, 1, wx.EXPAND, 5)

        sizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelDuration = wx.StaticText(sizerFlash.GetStaticBox(), wx.ID_ANY, _(
            "Duration:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelDuration.Wrap(-1)
        sizer5.Add(self.labelDuration, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.spinCtrlDurationFrames = wx.SpinCtrl(sizerFlash.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(64, -1), wx.SP_ARROW_KEYS, 0, 10, 0)
        sizer5.Add(self.spinCtrlDurationFrames, 0, wx.ALL, 5)

        self.labelFrames = wx.StaticText(sizerFlash.GetStaticBox(), wx.ID_ANY, _(
            "Frames"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelFrames.Wrap(-1)
        sizer5.Add(self.labelFrames, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sizerFlash.Add(sizer5, 0, wx.EXPAND, 5)

        MainSizer.Add(sizerFlash, 1, wx.EXPAND | wx.ALL, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonCancel, 0, wx.ALL, 5)

        MainSizer.Add(sizerOKCancel, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.spinCtrlFrames.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlFrame_ValueChanged)
        self.comboBoxSE.Bind(wx.EVT_LEFT_DOWN, self.comboBoxSE_LeftClicked)
        self.comboBoxCondition.Bind(
            wx.EVT_CHOICE, self.comboBoxCondition_SelectionChanged)
        self.radioButtonNone.Bind(
            wx.EVT_RADIOBUTTON, self.radioButtonNone_Checked)
        self.radioButtonTarget.Bind(
            wx.EVT_RADIOBUTTON, self.radioButtonTarget_Checked)
        self.radioButtonScreen.Bind(
            wx.EVT_RADIOBUTTON, self.radioButtonScreen_Checked)
        self.radioButtonHideTarget.Bind(
            wx.EVT_RADIOBUTTON, self.radioButtonHideTarget_Checked)
        self.sliderRed.Bind(wx.EVT_SCROLL, self.slideCtrlRed_ValueChanged)
        self.spinCtrlRed.Bind(wx.EVT_SPINCTRL, self.spinCtrlRed_ValueChanged)
        self.sliderGreen.Bind(wx.EVT_SCROLL, self.slideCtrlGreen_ValueChanged)
        self.spinCtrlGreen.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlGreen_ValueChanged)
        self.sliderBlue.Bind(wx.EVT_SCROLL, self.slideCtrlBlue_ValueChanged)
        self.spinCtrlBlue.Bind(wx.EVT_SPINCTRL, self.spinCtrlBlue_ValueChanged)
        self.sliderStrength.Bind(
            wx.EVT_SCROLL, self.slideCtrlStrength_ValueChanged)
        self.spinCtrlStrength.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlStrength_ValueChanged)
        self.spinCtrlDurationFrames.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlDurationFrames_ValueChanged)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def spinCtrlFrame_ValueChanged(self, event):
        event.Skip()

    def comboBoxSE_LeftClicked(self, event):
        event.Skip()

    def comboBoxCondition_SelectionChanged(self, event):
        event.Skip()

    def radioButtonNone_Checked(self, event):
        event.Skip()

    def radioButtonTarget_Checked(self, event):
        event.Skip()

    def radioButtonScreen_Checked(self, event):
        event.Skip()

    def radioButtonHideTarget_Checked(self, event):
        event.Skip()

    def slideCtrlRed_ValueChanged(self, event):
        event.Skip()

    def spinCtrlRed_ValueChanged(self, event):
        event.Skip()

    def slideCtrlGreen_ValueChanged(self, event):
        event.Skip()

    def spinCtrlGreen_ValueChanged(self, event):
        event.Skip()

    def slideCtrlBlue_ValueChanged(self, event):
        event.Skip()

    def spinCtrlBlue_ValueChanged(self, event):
        event.Skip()

    def slideCtrlStrength_ValueChanged(self, event):
        event.Skip()

    def spinCtrlStrength_ValueChanged(self, event):
        event.Skip()

    def spinCtrlDurationFrames_ValueChanged(self, event):
        event.Skip()

    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class AnimationTweening_Dialog_Template
###########################################################################

class AnimationTweening_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(
            "Tweening"), pos=wx.DefaultPosition, size=wx.Size(179, 293), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        self.labelFrames = wx.StaticText(
            self, wx.ID_ANY, _("Frames:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelFrames.Wrap(-1)
        MainSizer.Add(self.labelFrames, 0, wx.ALL, 5)

        sizerFrames = wx.BoxSizer(wx.HORIZONTAL)

        self.spinCtrlFramesStart = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(64, -1), wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerFrames.Add(
            self.spinCtrlFramesStart, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelTilde1 = wx.StaticText(
            self, wx.ID_ANY, _("~"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelTilde1.Wrap(-1)
        sizerFrames.Add(
            self.labelTilde1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.spinCtrlFramesEnd = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(64, -1), wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerFrames.Add(
            self.spinCtrlFramesEnd, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerFrames, 0, wx.EXPAND, 5)

        self.labelCells = wx.StaticText(
            self, wx.ID_ANY, _("Cells:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelCells.Wrap(-1)
        MainSizer.Add(self.labelCells, 0, wx.ALL, 5)

        sizerCells = wx.BoxSizer(wx.HORIZONTAL)

        self.spinCtrlCellsStart = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(64, -1), wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerCells.Add(
            self.spinCtrlCellsStart, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelTilde2 = wx.StaticText(
            self, wx.ID_ANY, _("~"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelTilde2.Wrap(-1)
        sizerCells.Add(
            self.labelTilde2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.spinCtrlCellsEnd = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(64, -1), wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerCells.Add(
            self.spinCtrlCellsEnd, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerCells, 0, wx.EXPAND, 5)

        sizerTweeningItems = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Tweening Items")), wx.VERTICAL)

        self.checkBoxPattern = wx.CheckBox(sizerTweeningItems.GetStaticBox(), wx.ID_ANY, _(
            "Pattern"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerTweeningItems.Add(self.checkBoxPattern, 0, wx.ALL, 5)

        self.checkBoxPosition = wx.CheckBox(sizerTweeningItems.GetStaticBox(), wx.ID_ANY, _(
            "Position / Zoom / Angle"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerTweeningItems.Add(self.checkBoxPosition, 0, wx.ALL, 5)

        self.checkBoxOpacity = wx.CheckBox(sizerTweeningItems.GetStaticBox(), wx.ID_ANY, _(
            "Opacity / Blending"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerTweeningItems.Add(self.checkBoxOpacity, 0, wx.ALL, 5)

        MainSizer.Add(sizerTweeningItems, 0, wx.EXPAND | wx.ALL, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonCancel, 0, wx.ALL, 5)

        MainSizer.Add(sizerOKCancel, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.spinCtrlFramesStart.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlFramesStart_ValueChanged)
        self.spinCtrlFramesEnd.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlFramesEnd_ValueChanged)
        self.spinCtrlCellsStart.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlCellsStart_ValueChanged)
        self.spinCtrlCellsEnd.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlCellsEnd_ValueChanged)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def spinCtrlFramesStart_ValueChanged(self, event):
        event.Skip()

    def spinCtrlFramesEnd_ValueChanged(self, event):
        event.Skip()

    def spinCtrlCellsStart_ValueChanged(self, event):
        event.Skip()

    def spinCtrlCellsEnd_ValueChanged(self, event):
        event.Skip()

    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class AnimationEntireSlide_Dialog_Template
###########################################################################

class AnimationEntireSlide_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(
            "Entire Slide"), pos=wx.DefaultPosition, size=wx.Size(301, 215), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        self.labelFrames = wx.StaticText(
            self, wx.ID_ANY, _("Frames:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelFrames.Wrap(-1)
        MainSizer.Add(self.labelFrames, 0, wx.ALL, 5)

        sizerFrames = wx.BoxSizer(wx.HORIZONTAL)

        self.sinCtrlFramesStart = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerFrames.Add(
            self.sinCtrlFramesStart, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelTilde = wx.StaticText(
            self, wx.ID_ANY, _("~"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelTilde.Wrap(-1)
        sizerFrames.Add(self.labelTilde, 0, wx.ALL, 5)

        self.spinCtrlFramesEnd = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerFrames.Add(
            self.spinCtrlFramesEnd, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerFrames, 0, wx.EXPAND, 5)

        sizerMovement = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Movement Amount")), wx.HORIZONTAL)

        bSizer258 = wx.BoxSizer(wx.VERTICAL)

        self.labelMoveX = wx.StaticText(sizerMovement.GetStaticBox(), wx.ID_ANY, _(
            "X:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelMoveX.Wrap(-1)
        bSizer258.Add(self.labelMoveX, 0, wx.ALL | wx.EXPAND, 5)

        self.spinCtrlMoveX = wx.SpinCtrl(sizerMovement.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        bSizer258.Add(
            self.spinCtrlMoveX, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerMovement.Add(bSizer258, 1, wx.EXPAND, 5)

        bSizer259 = wx.BoxSizer(wx.VERTICAL)

        self.labelMoveY = wx.StaticText(sizerMovement.GetStaticBox(), wx.ID_ANY, _(
            "Y:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelMoveY.Wrap(-1)
        bSizer259.Add(self.labelMoveY, 0, wx.ALL | wx.EXPAND, 5)

        self.spinCtrlMoveY = wx.SpinCtrl(sizerMovement.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        bSizer259.Add(
            self.spinCtrlMoveY, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizerMovement.Add(bSizer259, 1, wx.EXPAND, 5)

        MainSizer.Add(sizerMovement, 0, wx.EXPAND | wx.ALL, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonCancel, 0, wx.ALL, 5)

        MainSizer.Add(sizerOKCancel, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.sinCtrlFramesStart.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlFramesStart_ValueChanged)
        self.spinCtrlFramesEnd.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlFramesEnd_ValueChanged)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Click)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Click)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def spinCtrlFramesStart_ValueChanged(self, event):
        event.Skip()

    def spinCtrlFramesEnd_ValueChanged(self, event):
        event.Skip()

    def buttonOK_Click(self, event):
        event.Skip()

    def buttonCancel_Click(self, event):
        event.Skip()


###########################################################################
# Class AnimationCellBatch_Dialog_Template
###########################################################################

class AnimationCellBatch_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(
            "Cell Batch"), pos=wx.DefaultPosition, size=wx.Size(335, 315), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        self.labelFrames = wx.StaticText(
            self, wx.ID_ANY, _("Frames:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelFrames.Wrap(-1)
        MainSizer.Add(self.labelFrames, 0, wx.ALL, 5)

        sizerFrames = wx.BoxSizer(wx.HORIZONTAL)

        self.spinCtrlFramesStart = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(64, -1), wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerFrames.Add(
            self.spinCtrlFramesStart, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelTilde1 = wx.StaticText(
            self, wx.ID_ANY, _("~"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelTilde1.Wrap(-1)
        sizerFrames.Add(self.labelTilde1, 0, wx.ALL, 5)

        self.spinCtrlFramesEnd = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(64, -1), wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerFrames.Add(
            self.spinCtrlFramesEnd, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerFrames, 0, wx.EXPAND, 5)

        self.labelCells = wx.StaticText(
            self, wx.ID_ANY, _("Cells:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelCells.Wrap(-1)
        MainSizer.Add(self.labelCells, 0, wx.ALL, 5)

        sizerCells = wx.BoxSizer(wx.HORIZONTAL)

        self.spinCtrlCellsStart = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(64, -1), wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerCells.Add(
            self.spinCtrlCellsStart, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelTilde2 = wx.StaticText(
            self, wx.ID_ANY, _("~"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelTilde2.Wrap(-1)
        sizerCells.Add(self.labelTilde2, 0, wx.ALL, 5)

        self.spinCtrlCellsEnd = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(64, -1), wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerCells.Add(
            self.spinCtrlCellsEnd, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerCells, 0, wx.EXPAND, 5)

        sizerSettings = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.HORIZONTAL)

        bSizer268 = wx.BoxSizer(wx.VERTICAL)

        self.checkBoxPattern = wx.CheckBox(sizerSettings.GetStaticBox(), wx.ID_ANY, _(
            "Pattern"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer268.Add(self.checkBoxPattern, 0, wx.ALL | wx.EXPAND, 5)

        self.spinCtrlPattern = wx.SpinCtrl(sizerSettings.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        bSizer268.Add(
            self.spinCtrlPattern, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.checkBoxAngle = wx.CheckBox(sizerSettings.GetStaticBox(), wx.ID_ANY, _(
            "Angle"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer268.Add(self.checkBoxAngle, 0, wx.ALL | wx.EXPAND, 5)

        self.spinCtrlAngle = wx.SpinCtrl(sizerSettings.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        bSizer268.Add(
            self.spinCtrlAngle, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerSettings.Add(bSizer268, 1, wx.EXPAND, 5)

        bSizer2681 = wx.BoxSizer(wx.VERTICAL)

        self.checkBoxX = wx.CheckBox(sizerSettings.GetStaticBox(), wx.ID_ANY, _(
            "X"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2681.Add(self.checkBoxX, 0, wx.ALL | wx.EXPAND, 5)

        self.spinCtrlX = wx.SpinCtrl(sizerSettings.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        bSizer2681.Add(
            self.spinCtrlX, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.checkBoxFlip = wx.CheckBox(sizerSettings.GetStaticBox(), wx.ID_ANY, _(
            "Flip"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2681.Add(self.checkBoxFlip, 0, wx.ALL | wx.EXPAND, 5)

        self.spinCtrlFlip = wx.SpinCtrl(sizerSettings.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        bSizer2681.Add(
            self.spinCtrlFlip, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerSettings.Add(bSizer2681, 1, wx.EXPAND, 5)

        bSizer2682 = wx.BoxSizer(wx.VERTICAL)

        self.checkBoxY = wx.CheckBox(sizerSettings.GetStaticBox(), wx.ID_ANY, _(
            "Y"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2682.Add(self.checkBoxY, 0, wx.ALL | wx.EXPAND, 5)

        self.spinCtrlY = wx.SpinCtrl(sizerSettings.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        bSizer2682.Add(
            self.spinCtrlY, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.checkBoxOpacity = wx.CheckBox(sizerSettings.GetStaticBox(), wx.ID_ANY, _(
            "Opacity"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2682.Add(self.checkBoxOpacity, 0, wx.ALL | wx.EXPAND, 5)

        self.spinCtrlOpacity = wx.SpinCtrl(sizerSettings.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        bSizer2682.Add(
            self.spinCtrlOpacity, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerSettings.Add(bSizer2682, 1, wx.EXPAND, 5)

        bSizer2683 = wx.BoxSizer(wx.VERTICAL)

        self.checkBoxZoom = wx.CheckBox(sizerSettings.GetStaticBox(), wx.ID_ANY, _(
            "Zoom"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2683.Add(self.checkBoxZoom, 0, wx.ALL | wx.EXPAND, 5)

        self.spinCtrlZoom = wx.SpinCtrl(sizerSettings.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        bSizer2683.Add(
            self.spinCtrlZoom, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.checkBoxBlending = wx.CheckBox(sizerSettings.GetStaticBox(), wx.ID_ANY, _(
            "Blending"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2683.Add(self.checkBoxBlending, 0, wx.ALL | wx.EXPAND, 5)

        self.spinCtrlBlending = wx.SpinCtrl(sizerSettings.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        bSizer2683.Add(
            self.spinCtrlBlending, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerSettings.Add(bSizer2683, 1, wx.EXPAND, 5)

        MainSizer.Add(sizerSettings, 0, wx.EXPAND | wx.ALL, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonCancel, 0, wx.ALL, 5)

        MainSizer.Add(sizerOKCancel, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.spinCtrlFramesStart.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlFramesStart_ValueChanged)
        self.spinCtrlFramesEnd.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlFramesEnd_ValueChanged)
        self.spinCtrlCellsStart.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlCellsStart_ValueChanged)
        self.spinCtrlCellsEnd.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlCellsEnd_ValueChanged)
        self.checkBoxPattern.Bind(
            wx.EVT_CHECKBOX, self.checkBoxPattern_CheckChanged)
        self.checkBoxAngle.Bind(
            wx.EVT_CHECKBOX, self.checkBoxAngle_CheckChanged)
        self.checkBoxX.Bind(wx.EVT_CHECKBOX, self.checkBoxX_CheckChanged)
        self.checkBoxFlip.Bind(wx.EVT_CHECKBOX, self.checkBoxFlip_CheckChanged)
        self.checkBoxY.Bind(wx.EVT_CHECKBOX, self.checkBoxY_CheckChanged)
        self.checkBoxOpacity.Bind(
            wx.EVT_CHECKBOX, self.checkBoxOpacity_CheckChanged)
        self.checkBoxZoom.Bind(wx.EVT_CHECKBOX, self.checkBoxZoom_CheckChanged)
        self.checkBoxBlending.Bind(
            wx.EVT_CHECKBOX, self.checkBoxBlending_CheckChanged)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def spinCtrlFramesStart_ValueChanged(self, event):
        event.Skip()

    def spinCtrlFramesEnd_ValueChanged(self, event):
        event.Skip()

    def spinCtrlCellsStart_ValueChanged(self, event):
        event.Skip()

    def spinCtrlCellsEnd_ValueChanged(self, event):
        event.Skip()

    def checkBoxPattern_CheckChanged(self, event):
        event.Skip()

    def checkBoxAngle_CheckChanged(self, event):
        event.Skip()

    def checkBoxX_CheckChanged(self, event):
        event.Skip()

    def checkBoxFlip_CheckChanged(self, event):
        event.Skip()

    def checkBoxY_CheckChanged(self, event):
        event.Skip()

    def checkBoxOpacity_CheckChanged(self, event):
        event.Skip()

    def checkBoxZoom_CheckChanged(self, event):
        event.Skip()

    def checkBoxBlending_CheckChanged(self, event):
        event.Skip()

    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class AnimationCellProperties_Dialog_Template
###########################################################################

class AnimationCellProperties_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(
            "Cell Properties"), pos=wx.DefaultPosition, size=wx.Size(571, 170), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        sizerLabels1 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelPattern = wx.StaticText(
            self, wx.ID_ANY, _("Pattern:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelPattern.Wrap(-1)
        sizerLabels1.Add(self.labelPattern, 1, wx.ALL, 5)

        self.labelX = wx.StaticText(
            self, wx.ID_ANY, _("X:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelX.Wrap(-1)
        sizerLabels1.Add(self.labelX, 1, wx.ALL, 5)

        self.labelY = wx.StaticText(
            self, wx.ID_ANY, _("Y:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelY.Wrap(-1)
        sizerLabels1.Add(self.labelY, 1, wx.ALL, 5)

        self.labelZoom = wx.StaticText(
            self, wx.ID_ANY, _("Zoom:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelZoom.Wrap(-1)
        sizerLabels1.Add(self.labelZoom, 1, wx.ALL, 5)

        MainSizer.Add(sizerLabels1, 0, wx.EXPAND, 5)

        sizerControls1 = wx.BoxSizer(wx.HORIZONTAL)

        self.spinCtrlPattern = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerControls1.Add(
            self.spinCtrlPattern, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlX = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerControls1.Add(
            self.spinCtrlX, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlY = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerControls1.Add(
            self.spinCtrlY, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlZoom = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerControls1.Add(
            self.spinCtrlZoom, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerControls1, 0, wx.EXPAND, 5)

        sizerLabels2 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelAngle = wx.StaticText(
            self, wx.ID_ANY, _("Angle:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelAngle.Wrap(-1)
        sizerLabels2.Add(self.labelAngle, 1, wx.ALL, 5)

        self.labelFlip = wx.StaticText(
            self, wx.ID_ANY, _("Flip:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelFlip.Wrap(-1)
        sizerLabels2.Add(self.labelFlip, 1, wx.ALL, 5)

        self.labelOpacity = wx.StaticText(
            self, wx.ID_ANY, _("Opacity:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelOpacity.Wrap(-1)
        sizerLabels2.Add(self.labelOpacity, 1, wx.ALL, 5)

        self.labelBlending = wx.StaticText(
            self, wx.ID_ANY, _("Blending:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelBlending.Wrap(-1)
        sizerLabels2.Add(self.labelBlending, 1, wx.ALL, 5)

        MainSizer.Add(sizerLabels2, 0, wx.EXPAND, 5)

        sizerControls2 = wx.BoxSizer(wx.HORIZONTAL)

        self.spinCtrlAngle = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerControls2.Add(
            self.spinCtrlAngle, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlFlip = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerControls2.Add(
            self.spinCtrlFlip, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlOpacity = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerControls2.Add(
            self.spinCtrlOpacity, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlBlending = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerControls2.Add(
            self.spinCtrlBlending, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerControls2, 0, wx.EXPAND, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonCancel, 0, wx.ALL, 5)

        MainSizer.Add(sizerOKCancel, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class ChooseFogGraphic_Dialog_Template
###########################################################################

class ChooseFogGraphic_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(
            "Fog Graphic"), pos=wx.DefaultPosition, size=wx.Size(714, 468), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        sizerControls = wx.BoxSizer(wx.HORIZONTAL)

        listBoxGraphicsChoices = []
        self.listBoxGraphics = wx.ListBox(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(160, -1), listBoxGraphicsChoices, 0)
        sizerControls.Add(self.listBoxGraphics, 0, wx.ALL | wx.EXPAND, 5)

        sizerPreview = wx.BoxSizer(wx.VERTICAL)

        sizerGraphic = wx.BoxSizer(wx.HORIZONTAL)

        self.panelGraphic = wx.ScrolledWindow(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL | wx.SUNKEN_BORDER | wx.VSCROLL)
        self.panelGraphic.SetScrollRate(5, 5)
        sizerGLGraphic = wx.BoxSizer(wx.VERTICAL)

        from .Extras import EditorGLPanel
        parent = self.panelGraphic
        self.glCanvasGraphic = EditorGLPanel(parent, -1, 1, 1, (0, 0,), 1)
        sizerGLGraphic.Add(self.glCanvasGraphic, 1, wx.ALL | wx.EXPAND, 0)

        self.panelGraphic.SetSizer(sizerGLGraphic)
        self.panelGraphic.Layout()
        sizerGLGraphic.Fit(self.panelGraphic)
        sizerGraphic.Add(self.panelGraphic, 1, wx.EXPAND | wx.ALL, 5)

        sizerOptions = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Options")), wx.VERTICAL)

        self.labelOpacity = wx.StaticText(sizerOptions.GetStaticBox(), wx.ID_ANY, _(
            "Opacity:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelOpacity.Wrap(-1)
        sizerOptions.Add(self.labelOpacity, 0, wx.ALL | wx.EXPAND, 5)

        self.spinCtrlOpacity = wx.SpinCtrl(sizerOptions.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(64, -1), wx.SP_ARROW_KEYS, 0, 255, 255)
        sizerOptions.Add(
            self.spinCtrlOpacity, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelBlending = wx.StaticText(sizerOptions.GetStaticBox(), wx.ID_ANY, _(
            "Blending:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelBlending.Wrap(-1)
        sizerOptions.Add(self.labelBlending, 0, wx.ALL | wx.EXPAND, 5)

        comboBoxBlendingChoices = [
            _("Normal"), _("Addition"), _("Subtraction")]
        self.comboBoxBlending = wx.Choice(sizerOptions.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(64, -1), comboBoxBlendingChoices, 0)
        self.comboBoxBlending.SetSelection(0)
        sizerOptions.Add(self.comboBoxBlending, 0, wx.ALL, 5)

        self.labelZoom = wx.StaticText(sizerOptions.GetStaticBox(), wx.ID_ANY, _(
            "Zoom:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelZoom.Wrap(-1)
        sizerOptions.Add(self.labelZoom, 0, wx.ALL | wx.EXPAND, 5)

        self.spinCtrlZoom = wx.SpinCtrl(sizerOptions.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(64, -1), wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerOptions.Add(
            self.spinCtrlZoom, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelSX = wx.StaticText(sizerOptions.GetStaticBox(), wx.ID_ANY, _(
            "SX:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelSX.Wrap(-1)
        sizerOptions.Add(self.labelSX, 0, wx.ALL | wx.EXPAND, 5)

        self.spinCtrlSX = wx.SpinCtrl(sizerOptions.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(64, -1), wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerOptions.Add(self.spinCtrlSX, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelSY = wx.StaticText(sizerOptions.GetStaticBox(), wx.ID_ANY, _(
            "SY:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelSY.Wrap(-1)
        sizerOptions.Add(self.labelSY, 0, wx.ALL | wx.EXPAND, 5)

        self.spinCtrlSY = wx.SpinCtrl(sizerOptions.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(64, -1), wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerOptions.Add(self.spinCtrlSY, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerGraphic.Add(sizerOptions, 0, wx.EXPAND | wx.ALL, 5)

        sizerPreview.Add(sizerGraphic, 1, wx.EXPAND, 5)

        sizerHue = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Hue")), wx.VERTICAL)

        self.sliderHue = wx.Slider(sizerHue.GetStaticBox(
        ), wx.ID_ANY, 0, 0, 359, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        sizerHue.Add(self.sliderHue, 0, wx.ALL | wx.EXPAND, 5)

        sizerPreview.Add(sizerHue, 0, wx.EXPAND | wx.ALL, 5)

        sizerControls.Add(sizerPreview, 1, wx.EXPAND, 5)

        MainSizer.Add(sizerControls, 1, wx.EXPAND, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonCancel, 0, wx.ALL, 5)

        MainSizer.Add(sizerOKCancel, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.listBoxGraphics.Bind(
            wx.EVT_LISTBOX, self.listBoxGraphics_SelectionChanged)
        self.spinCtrlOpacity.Bind(
            wx.EVT_SPINCTRL, self.spinCtrOpacityl_ValueChanged)
        self.comboBoxBlending.Bind(
            wx.EVT_CHOICE, self.comboBoxBlending_SelectionChanged)
        self.spinCtrlZoom.Bind(wx.EVT_SPINCTRL, self.spinCtrlZoom_ValueChanged)
        self.spinCtrlSX.Bind(wx.EVT_SPINCTRL, self.spinCtrlSX_ValueChanged)
        self.spinCtrlSY.Bind(wx.EVT_SPINCTRL, self.spinCtrlSY_ValueChanged)
        self.sliderHue.Bind(wx.EVT_SCROLL, self.sliderHue_Scrolled)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def listBoxGraphics_SelectionChanged(self, event):
        event.Skip()

    def spinCtrOpacityl_ValueChanged(self, event):
        event.Skip()

    def comboBoxBlending_SelectionChanged(self, event):
        event.Skip()

    def spinCtrlZoom_ValueChanged(self, event):
        event.Skip()

    def spinCtrlSX_ValueChanged(self, event):
        event.Skip()

    def spinCtrlSY_ValueChanged(self, event):
        event.Skip()

    def sliderHue_Scrolled(self, event):
        event.Skip()

    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class ChooseActor_Dialog_Template
###########################################################################

class ChooseActor_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(
            "Initial Party"), pos=wx.DefaultPosition, size=wx.Size(290, 99), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        sizerActor = wx.BoxSizer(wx.VERTICAL)

        self.labelActor = wx.StaticText(
            self, wx.ID_ANY, _("Actor:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelActor.Wrap(-1)
        sizerActor.Add(self.labelActor, 0, wx.ALL, 5)

        comboBoxActorsChoices = []
        self.comboBoxActors = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxActorsChoices, 0)
        self.comboBoxActors.SetSelection(0)
        sizerActor.Add(
            self.comboBoxActors, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerActor, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        sizerOKCancel = wx.BoxSizer(wx.VERTICAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(
            self.buttonCancel, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerOKCancel, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class ChooseSwitchVariable_Dialog_Template
###########################################################################

class ChooseSwitchVariable_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(
            "Switch"), pos=wx.DefaultPosition, size=wx.Size(317, 398), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        sizerControls = wx.BoxSizer(wx.HORIZONTAL)

        sizerGroup = wx.BoxSizer(wx.VERTICAL)

        self.bitmapHeader = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(
            "G:\\Projects\\arcreator\\editor\\Welder\\Database Panel Images\\Switch.png", wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerGroup.Add(self.bitmapHeader, 0, wx.ALL | wx.EXPAND, 5)

        listBoxGroupChoices = []
        self.listBoxGroup = wx.ListBox(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxGroupChoices, 0)
        sizerGroup.Add(
            self.listBoxGroup, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.buttonChangeMax = wx.Button(
            self, wx.ID_ANY, _("Change Max..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerGroup.Add(self.buttonChangeMax, 0, wx.ALL | wx.EXPAND, 5)

        sizerControls.Add(sizerGroup, 40, wx.EXPAND, 5)

        sizerItemList = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        listBoxItemsChoices = []
        self.listBoxItems = wx.ListBox(sizerItemList.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxItemsChoices, 0)
        sizerItemList.Add(self.listBoxItems, 1, wx.ALL | wx.EXPAND, 5)

        sizerName = wx.BoxSizer(wx.HORIZONTAL)

        self.labelName = wx.StaticText(sizerItemList.GetStaticBox(), wx.ID_ANY, _(
            "Name:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelName.Wrap(-1)
        sizerName.Add(self.labelName, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.textCtrlName = wx.TextCtrl(sizerItemList.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlName.SetMaxLength(0)
        sizerName.Add(self.textCtrlName, 1, wx.ALL, 5)

        sizerItemList.Add(sizerName, 0, wx.EXPAND, 5)

        sizerControls.Add(
            sizerItemList, 60, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerControls, 1, wx.EXPAND, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonCancel, 0, wx.ALL, 5)

        self.buttonApply = wx.Button(
            self, wx.ID_ANY, _("Apply"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonApply, 0, wx.ALL, 5)

        MainSizer.Add(sizerOKCancel, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.listBoxGroup.Bind(
            wx.EVT_LISTBOX, self.listBoxGroup_SelectionChanged)
        self.buttonChangeMax.Bind(wx.EVT_BUTTON, self.buttonMax_Clicked)
        self.listBoxItems.Bind(
            wx.EVT_LISTBOX, self.listBoxItems_SelectionChanged)
        self.textCtrlName.Bind(wx.EVT_TEXT, self.textCtrlName_TextChanged)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)
        self.buttonApply.Bind(wx.EVT_BUTTON, self.buttonApply_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def listBoxGroup_SelectionChanged(self, event):
        event.Skip()

    def buttonMax_Clicked(self, event):
        event.Skip()

    def listBoxItems_SelectionChanged(self, event):
        event.Skip()

    def textCtrlName_TextChanged(self, event):
        event.Skip()

    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()

    def buttonApply_Clicked(self, event):
        event.Skip()


###########################################################################
# Class TransferPlayerTilemap_Dialog_Template
###########################################################################

class TransferPlayerTilemap_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_("Transfer Player"), pos=wx.DefaultPosition, size=wx.Size(
            692, 467), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        MainSizer.SetMinSize(wx.Size(-1, 480))
        sizerControls = wx.BoxSizer(wx.HORIZONTAL)

        self.treeCtrlMap = wx.TreeCtrl(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(192, -1), wx.TR_DEFAULT_STYLE)
        sizerControls.Add(self.treeCtrlMap, 0, wx.ALL | wx.EXPAND, 5)

        sizerTilemap = wx.BoxSizer(wx.VERTICAL)

        sizerZoom = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonFull = wx.Button(
            self, wx.ID_ANY, _("1/1"), wx.DefaultPosition, wx.Size(64, 32), 0)
        sizerZoom.Add(self.buttonFull, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.buttonThreeQuarter = wx.Button(
            self, wx.ID_ANY, _("3/4"), wx.DefaultPosition, wx.Size(64, 32), 0)
        sizerZoom.Add(
            self.buttonThreeQuarter, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.buttonHalf = wx.Button(
            self, wx.ID_ANY, _("1/2"), wx.DefaultPosition, wx.Size(64, 32), 0)
        sizerZoom.Add(self.buttonHalf, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.buttonQuarter = wx.Button(
            self, wx.ID_ANY, _("1/4"), wx.DefaultPosition, wx.Size(64, 32), 0)
        sizerZoom.Add(self.buttonQuarter, 0, wx.ALL, 5)

        self.labelDummy = wx.StaticText(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelDummy.Wrap(-1)
        sizerZoom.Add(self.labelDummy, 1, wx.ALL, 5)

        self.panelCoordinates = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        sizerCoodinates = wx.BoxSizer(wx.VERTICAL)

        self.labelCoordinates = wx.StaticText(self.panelCoordinates, wx.ID_ANY, _(
            "(Coordinates)"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelCoordinates.Wrap(-1)
        sizerCoodinates.Add(
            self.labelCoordinates, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.panelCoordinates.SetSizer(sizerCoodinates)
        self.panelCoordinates.Layout()
        sizerCoodinates.Fit(self.panelCoordinates)
        sizerZoom.Add(self.panelCoordinates, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        sizerTilemap.Add(sizerZoom, 0, wx.EXPAND, 5)

        self.bitmapTilemap = wx.StaticBitmap(
            self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER)
        sizerTilemap.Add(self.bitmapTilemap, 1, wx.ALL | wx.EXPAND, 5)

        sizerControls.Add(sizerTilemap, 1, wx.EXPAND, 5)

        MainSizer.Add(sizerControls, 1, wx.EXPAND, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonCancel, 0, wx.ALL, 5)

        MainSizer.Add(sizerOKCancel, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.treeCtrlMap.Bind(
            wx.EVT_TREE_SEL_CHANGED, self.treeCtrlMaps_SelectionChanged)
        self.buttonFull.Bind(wx.EVT_BUTTON, self.buttonFull_Clicked)
        self.buttonThreeQuarter.Bind(
            wx.EVT_BUTTON, self.buttonThreeQuarter_Clicked)
        self.buttonHalf.Bind(wx.EVT_BUTTON, self.buttonHalf_Clicked)
        self.buttonQuarter.Bind(wx.EVT_BUTTON, self.buttonQuarter_Clicked)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def treeCtrlMaps_SelectionChanged(self, event):
        event.Skip()

    def buttonFull_Clicked(self, event):
        event.Skip()

    def buttonThreeQuarter_Clicked(self, event):
        event.Skip()

    def buttonHalf_Clicked(self, event):
        event.Skip()

    def buttonQuarter_Clicked(self, event):
        event.Skip()

    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class TransferEventTilemap_Dialog_Template
###########################################################################

class TransferEventTilemap_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                           pos=wx.DefaultPosition, size=wx.Size(604, 462), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        MainSizer.SetMinSize(wx.Size(-1, 480))
        sizerTilemap = wx.BoxSizer(wx.VERTICAL)

        sizerZoom = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonFull = wx.Button(
            self, wx.ID_ANY, _("1/1"), wx.DefaultPosition, wx.Size(64, 32), 0)
        sizerZoom.Add(self.buttonFull, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.buttonThreeQuarter = wx.Button(
            self, wx.ID_ANY, _("3/4"), wx.DefaultPosition, wx.Size(64, 32), 0)
        sizerZoom.Add(
            self.buttonThreeQuarter, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.buttonHalf = wx.Button(
            self, wx.ID_ANY, _("1/2"), wx.DefaultPosition, wx.Size(64, 32), 0)
        sizerZoom.Add(self.buttonHalf, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.buttonQuarter = wx.Button(
            self, wx.ID_ANY, _("1/4"), wx.DefaultPosition, wx.Size(64, 32), 0)
        sizerZoom.Add(self.buttonQuarter, 0, wx.ALL, 5)

        self.labelDummy = wx.StaticText(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelDummy.Wrap(-1)
        sizerZoom.Add(self.labelDummy, 1, wx.ALL, 5)

        self.panelCoordinates = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        sizerCoodinates = wx.BoxSizer(wx.VERTICAL)

        self.labelCoordinates = wx.StaticText(self.panelCoordinates, wx.ID_ANY, _(
            "(Coordinates)"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelCoordinates.Wrap(-1)
        sizerCoodinates.Add(
            self.labelCoordinates, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.panelCoordinates.SetSizer(sizerCoodinates)
        self.panelCoordinates.Layout()
        sizerCoodinates.Fit(self.panelCoordinates)
        sizerZoom.Add(self.panelCoordinates, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        sizerTilemap.Add(sizerZoom, 0, wx.EXPAND, 5)

        self.bitmapTilemap = wx.StaticBitmap(
            self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER)
        sizerTilemap.Add(self.bitmapTilemap, 1, wx.ALL | wx.EXPAND, 5)

        MainSizer.Add(sizerTilemap, 1, wx.EXPAND, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonCancel, 0, wx.ALL, 5)

        MainSizer.Add(sizerOKCancel, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.buttonFull.Bind(wx.EVT_BUTTON, self.buttonFull_Clicked)
        self.buttonThreeQuarter.Bind(
            wx.EVT_BUTTON, self.buttonThreeQuarter_Clicked)
        self.buttonHalf.Bind(wx.EVT_BUTTON, self.buttonHalf_Clicked)
        self.buttonQuarter.Bind(wx.EVT_BUTTON, self.buttonQuarter_Clicked)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def buttonFull_Clicked(self, event):
        event.Skip()

    def buttonThreeQuarter_Clicked(self, event):
        event.Skip()

    def buttonHalf_Clicked(self, event):
        event.Skip()

    def buttonQuarter_Clicked(self, event):
        event.Skip()

    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class MoveRoute_Dialog_Template
###########################################################################

class MoveRoute_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(
            "Move Route"), pos=wx.DefaultPosition, size=wx.Size(670, 418), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        sizerMoveRoute = wx.BoxSizer(wx.HORIZONTAL)

        sizerSettings = wx.BoxSizer(wx.VERTICAL)

        self.labelCharacter = wx.StaticText(
            self, wx.ID_ANY, _("Character:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelCharacter.Wrap(-1)
        sizerSettings.Add(self.labelCharacter, 0, wx.ALL, 5)

        comboBoxCharacterChoices = [_("This Event"), _("Player")]
        self.comboBoxCharacter = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxCharacterChoices, 0)
        self.comboBoxCharacter.SetSelection(0)
        sizerSettings.Add(
            self.comboBoxCharacter, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        listBoxMoveRouteChoices = []
        self.listBoxMoveRoute = wx.ListBox(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxMoveRouteChoices, 0)
        sizerSettings.Add(self.listBoxMoveRoute, 1, wx.ALL | wx.EXPAND, 5)

        sizerOptions = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Options")), wx.VERTICAL)

        self.checkBoxRepeatAction = wx.CheckBox(sizerOptions.GetStaticBox(), wx.ID_ANY, _(
            "Repeat Action"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOptions.Add(self.checkBoxRepeatAction, 0, wx.ALL, 5)

        self.checkBoxIgnore = wx.CheckBox(sizerOptions.GetStaticBox(), wx.ID_ANY, _(
            "Ignore If Can't Move "), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOptions.Add(self.checkBoxIgnore, 0, wx.ALL, 5)

        sizerSettings.Add(sizerOptions, 0, wx.ALL | wx.EXPAND, 5)

        sizerMoveRoute.Add(sizerSettings, 1, wx.EXPAND, 5)

        sizerButtons1 = wx.BoxSizer(wx.VERTICAL)

        self.buttonMoveDown = wx.Button(
            self, wx.ID_ANY, _("Move Down"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons1.Add(
            self.buttonMoveDown, 0, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        self.buttonMoveLeft = wx.Button(
            self, wx.ID_ANY, _("Move Left"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons1.Add(
            self.buttonMoveLeft, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonMoveRight = wx.Button(
            self, wx.ID_ANY, _("Move Right"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons1.Add(
            self.buttonMoveRight, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonMoveUp = wx.Button(
            self, wx.ID_ANY, _("Move Up"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons1.Add(
            self.buttonMoveUp, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonMoveLowerLeft = wx.Button(
            self, wx.ID_ANY, _("Move Lower Left"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons1.Add(
            self.buttonMoveLowerLeft, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonMoveLowerRight = wx.Button(
            self, wx.ID_ANY, _("Move Lower Right"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons1.Add(
            self.buttonMoveLowerRight, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonMoveUpperLeft = wx.Button(
            self, wx.ID_ANY, _("Move Upper Left"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons1.Add(
            self.buttonMoveUpperLeft, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonMoveUpperRight = wx.Button(
            self, wx.ID_ANY, _("Move Upper Right"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons1.Add(
            self.buttonMoveUpperRight, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonMoveRandom = wx.Button(
            self, wx.ID_ANY, _("Move at Random"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons1.Add(
            self.buttonMoveRandom, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonMoveTowardPlayer = wx.Button(
            self, wx.ID_ANY, _("Move Toward Player"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons1.Add(
            self.buttonMoveTowardPlayer, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonMoveAwayPlayer = wx.Button(self, wx.ID_ANY, _(
            "Move Away from Player"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons1.Add(
            self.buttonMoveAwayPlayer, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonStepForward = wx.Button(
            self, wx.ID_ANY, _("1 Step Forward"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons1.Add(
            self.buttonStepForward, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonStepBackward = wx.Button(
            self, wx.ID_ANY, _("1 Step Backward"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons1.Add(
            self.buttonStepBackward, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonJump = wx.Button(
            self, wx.ID_ANY, _("Jump..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons1.Add(
            self.buttonJump, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonWait = wx.Button(
            self, wx.ID_ANY, _("Wait..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons1.Add(
            self.buttonWait, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizerMoveRoute.Add(sizerButtons1, 1, 0, 5)

        sizerButtons2 = wx.BoxSizer(wx.VERTICAL)

        self.buttonTurnDown = wx.Button(
            self, wx.ID_ANY, _("Turn Down"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons2.Add(
            self.buttonTurnDown, 0, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        self.buttonTurnLeft = wx.Button(
            self, wx.ID_ANY, _("Turn Left"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons2.Add(
            self.buttonTurnLeft, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonTurnRight = wx.Button(
            self, wx.ID_ANY, _("Turn Right"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons2.Add(
            self.buttonTurnRight, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonTurnUp = wx.Button(
            self, wx.ID_ANY, _("Turn Up"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons2.Add(
            self.buttonTurnUp, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonTurn90Left = wx.Button(
            self, wx.ID_ANY, _("Turn 90º Left"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons2.Add(
            self.buttonTurn90Left, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonTurn90Right = wx.Button(
            self, wx.ID_ANY, _("Turn 90º Right"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons2.Add(
            self.buttonTurn90Right, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonTurn180 = wx.Button(
            self, wx.ID_ANY, _("Turn 180º"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons2.Add(
            self.buttonTurn180, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonTurn90 = wx.Button(self, wx.ID_ANY, _(
            "Turn 90º Right or Left"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons2.Add(
            self.buttonTurn90, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonTurnRandom = wx.Button(
            self, wx.ID_ANY, _("Turn at Random"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons2.Add(
            self.buttonTurnRandom, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonTurnTowardPlayer = wx.Button(
            self, wx.ID_ANY, _("Turn Toward Player"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons2.Add(
            self.buttonTurnTowardPlayer, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonTurnAwayPlayer = wx.Button(self, wx.ID_ANY, _(
            "Turn Away from Player"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons2.Add(
            self.buttonTurnAwayPlayer, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonSwitchOn = wx.Button(
            self, wx.ID_ANY, _("Switch ON..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons2.Add(
            self.buttonSwitchOn, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonSwitchOff = wx.Button(
            self, wx.ID_ANY, _("Switch OFF..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons2.Add(
            self.buttonSwitchOff, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonChangeSpeed = wx.Button(
            self, wx.ID_ANY, _("Change Speed..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons2.Add(
            self.buttonChangeSpeed, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonChangeFreq = wx.Button(self, wx.ID_ANY, _(
            "Change Frequency..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons2.Add(
            self.buttonChangeFreq, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizerMoveRoute.Add(sizerButtons2, 1, wx.EXPAND, 5)

        sizerButtons3 = wx.BoxSizer(wx.VERTICAL)

        self.buttonMoveAnimationOn = wx.Button(
            self, wx.ID_ANY, _("Move Animation ON"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons3.Add(
            self.buttonMoveAnimationOn, 0, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        self.buttonMoveAnimationOff = wx.Button(
            self, wx.ID_ANY, _("Move Animation OFF"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons3.Add(
            self.buttonMoveAnimationOff, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonStopAnimationOn = wx.Button(
            self, wx.ID_ANY, _("Stop Animation ON"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons3.Add(
            self.buttonStopAnimationOn, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonStopAnimationOff = wx.Button(
            self, wx.ID_ANY, _("Stop Animation OFF"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons3.Add(
            self.buttonStopAnimationOff, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonDirectionFixOn = wx.Button(
            self, wx.ID_ANY, _("Direction Fix ON"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons3.Add(
            self.buttonDirectionFixOn, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonDirectionFixOff = wx.Button(
            self, wx.ID_ANY, _("Direction Fix OFF"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons3.Add(
            self.buttonDirectionFixOff, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonThroughOn = wx.Button(
            self, wx.ID_ANY, _("Through ON"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons3.Add(
            self.buttonThroughOn, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonThroughOff = wx.Button(
            self, wx.ID_ANY, _("Through OFF"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons3.Add(
            self.buttonThroughOff, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonAlwaysTopOn = wx.Button(
            self, wx.ID_ANY, _("Always on Top ON"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons3.Add(
            self.buttonAlwaysTopOn, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonAlwaysTopOff = wx.Button(
            self, wx.ID_ANY, _("Always on Top OFF"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons3.Add(
            self.buttonAlwaysTopOff, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonChangeGraphic = wx.Button(
            self, wx.ID_ANY, _("Change Graphic..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons3.Add(
            self.buttonChangeGraphic, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonChangeOpacity = wx.Button(
            self, wx.ID_ANY, _("Change Opacity..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons3.Add(
            self.buttonChangeOpacity, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonChangeBlending = wx.Button(
            self, wx.ID_ANY, _("Change Blending..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons3.Add(
            self.buttonChangeBlending, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonPlaySE = wx.Button(
            self, wx.ID_ANY, _("Play SE..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons3.Add(
            self.buttonPlaySE, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonScript = wx.Button(
            self, wx.ID_ANY, _("Script..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons3.Add(
            self.buttonScript, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizerMoveRoute.Add(sizerButtons3, 1, wx.EXPAND, 5)

        MainSizer.Add(sizerMoveRoute, 1, wx.EXPAND, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonCancel, 0, wx.ALL, 5)

        MainSizer.Add(sizerOKCancel, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.listBoxMoveRoute.Bind(wx.EVT_CHAR, self.listBoxMoveRoute_OnChar)
        self.buttonMoveDown.Bind(wx.EVT_BUTTON, self.buttonMoveDown_Clicked)
        self.buttonMoveLeft.Bind(wx.EVT_BUTTON, self.buttonMoveLeft_Clicked)
        self.buttonMoveRight.Bind(wx.EVT_BUTTON, self.buttonMoveRight_Clicked)
        self.buttonMoveUp.Bind(wx.EVT_BUTTON, self.buttonMoveUp_Clicked)
        self.buttonMoveLowerLeft.Bind(
            wx.EVT_BUTTON, self.buttonMoveLowerLeft_Clicked)
        self.buttonMoveLowerRight.Bind(
            wx.EVT_BUTTON, self.buttonMoveLowerRight_Clicked)
        self.buttonMoveUpperLeft.Bind(
            wx.EVT_BUTTON, self.buttonMoveUpperLeft_Clicked)
        self.buttonMoveUpperRight.Bind(
            wx.EVT_BUTTON, self.buttonMoveUpperRight_Clicked)
        self.buttonMoveRandom.Bind(
            wx.EVT_BUTTON, self.buttonMoveRandom_Clicked)
        self.buttonMoveTowardPlayer.Bind(
            wx.EVT_BUTTON, self.buttonMoveTowardPlayer_Clicked)
        self.buttonMoveAwayPlayer.Bind(
            wx.EVT_BUTTON, self.buttonMoveAwayPlayer_Clicked)
        self.buttonStepForward.Bind(
            wx.EVT_BUTTON, self.buttonStepForward_Clicked)
        self.buttonStepBackward.Bind(
            wx.EVT_BUTTON, self.buttonStepBackward_Clicked)
        self.buttonJump.Bind(wx.EVT_BUTTON, self.buttonJump_Clicked)
        self.buttonWait.Bind(wx.EVT_BUTTON, self.buttonWait_Clicked)
        self.buttonTurnDown.Bind(wx.EVT_BUTTON, self.buttonTurnDown_Clicked)
        self.buttonTurnLeft.Bind(wx.EVT_BUTTON, self.buttonTurnLeft_Clicked)
        self.buttonTurnRight.Bind(wx.EVT_BUTTON, self.buttonTurnRight_Clicked)
        self.buttonTurnUp.Bind(wx.EVT_BUTTON, self.buttonTurnUp_Clicked)
        self.buttonTurn90Left.Bind(
            wx.EVT_BUTTON, self.buttonTurn90Left_Clicked)
        self.buttonTurn90Right.Bind(
            wx.EVT_BUTTON, self.buttonTurn90Right_Clicked)
        self.buttonTurn180.Bind(wx.EVT_BUTTON, self.buttonTurn180_Clicked)
        self.buttonTurn90.Bind(wx.EVT_BUTTON, self.buttonTurn90_Clicked)
        self.buttonTurnRandom.Bind(
            wx.EVT_BUTTON, self.buttonTurnRandom_Clicked)
        self.buttonTurnTowardPlayer.Bind(
            wx.EVT_BUTTON, self.buttonTurnTowardPlayer_Clicked)
        self.buttonTurnAwayPlayer.Bind(
            wx.EVT_BUTTON, self.buttonTurnAwayPlayer_Clicked)
        self.buttonSwitchOn.Bind(wx.EVT_BUTTON, self.buttonSwitchOn_Clicked)
        self.buttonSwitchOff.Bind(wx.EVT_BUTTON, self.buttonSwitchOff_Clicked)
        self.buttonChangeSpeed.Bind(
            wx.EVT_BUTTON, self.buttonChangeSpeed_Clicked)
        self.buttonChangeFreq.Bind(
            wx.EVT_BUTTON, self.buttonChangeFreq_Clicked)
        self.buttonMoveAnimationOn.Bind(
            wx.EVT_BUTTON, self.buttonMoveAnimationOn_Clicked)
        self.buttonMoveAnimationOff.Bind(
            wx.EVT_BUTTON, self.buttonMoveAnimationOff_Clicked)
        self.buttonStopAnimationOn.Bind(
            wx.EVT_BUTTON, self.buttonStopAnimationOn_Clicked)
        self.buttonStopAnimationOff.Bind(
            wx.EVT_BUTTON, self.buttonStopAnimationOff_Clicked)
        self.buttonDirectionFixOn.Bind(
            wx.EVT_BUTTON, self.buttonDirectionFixOn_Clicked)
        self.buttonDirectionFixOff.Bind(
            wx.EVT_BUTTON, self.buttonDirectionFixOff_Clicked)
        self.buttonThroughOn.Bind(wx.EVT_BUTTON, self.buttonThroughOn_Clicked)
        self.buttonThroughOff.Bind(
            wx.EVT_BUTTON, self.buttonThroughOff_Clicked)
        self.buttonAlwaysTopOn.Bind(
            wx.EVT_BUTTON, self.buttonAlwaysTopOn_Clicked)
        self.buttonAlwaysTopOff.Bind(
            wx.EVT_BUTTON, self.buttonAlwaysTopOff_Clicked)
        self.buttonChangeGraphic.Bind(
            wx.EVT_BUTTON, self.buttonChangeGraphic_Clicked)
        self.buttonChangeOpacity.Bind(
            wx.EVT_BUTTON, self.buttonChangeOpacity_Clicked)
        self.buttonChangeBlending.Bind(
            wx.EVT_BUTTON, self.buttonChangeBlending_Clicked)
        self.buttonPlaySE.Bind(wx.EVT_BUTTON, self.buttonPlaySE_Clicked)
        self.buttonScript.Bind(wx.EVT_BUTTON, self.buttonScript_Clicked)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def listBoxMoveRoute_OnChar(self, event):
        event.Skip()

    def buttonMoveDown_Clicked(self, event):
        event.Skip()

    def buttonMoveLeft_Clicked(self, event):
        event.Skip()

    def buttonMoveRight_Clicked(self, event):
        event.Skip()

    def buttonMoveUp_Clicked(self, event):
        event.Skip()

    def buttonMoveLowerLeft_Clicked(self, event):
        event.Skip()

    def buttonMoveLowerRight_Clicked(self, event):
        event.Skip()

    def buttonMoveUpperLeft_Clicked(self, event):
        event.Skip()

    def buttonMoveUpperRight_Clicked(self, event):
        event.Skip()

    def buttonMoveRandom_Clicked(self, event):
        event.Skip()

    def buttonMoveTowardPlayer_Clicked(self, event):
        event.Skip()

    def buttonMoveAwayPlayer_Clicked(self, event):
        event.Skip()

    def buttonStepForward_Clicked(self, event):
        event.Skip()

    def buttonStepBackward_Clicked(self, event):
        event.Skip()

    def buttonJump_Clicked(self, event):
        event.Skip()

    def buttonWait_Clicked(self, event):
        event.Skip()

    def buttonTurnDown_Clicked(self, event):
        event.Skip()

    def buttonTurnLeft_Clicked(self, event):
        event.Skip()

    def buttonTurnRight_Clicked(self, event):
        event.Skip()

    def buttonTurnUp_Clicked(self, event):
        event.Skip()

    def buttonTurn90Left_Clicked(self, event):
        event.Skip()

    def buttonTurn90Right_Clicked(self, event):
        event.Skip()

    def buttonTurn180_Clicked(self, event):
        event.Skip()

    def buttonTurn90_Clicked(self, event):
        event.Skip()

    def buttonTurnRandom_Clicked(self, event):
        event.Skip()

    def buttonTurnTowardPlayer_Clicked(self, event):
        event.Skip()

    def buttonTurnAwayPlayer_Clicked(self, event):
        event.Skip()

    def buttonSwitchOn_Clicked(self, event):
        event.Skip()

    def buttonSwitchOff_Clicked(self, event):
        event.Skip()

    def buttonChangeSpeed_Clicked(self, event):
        event.Skip()

    def buttonChangeFreq_Clicked(self, event):
        event.Skip()

    def buttonMoveAnimationOn_Clicked(self, event):
        event.Skip()

    def buttonMoveAnimationOff_Clicked(self, event):
        event.Skip()

    def buttonStopAnimationOn_Clicked(self, event):
        event.Skip()

    def buttonStopAnimationOff_Clicked(self, event):
        event.Skip()

    def buttonDirectionFixOn_Clicked(self, event):
        event.Skip()

    def buttonDirectionFixOff_Clicked(self, event):
        event.Skip()

    def buttonThroughOn_Clicked(self, event):
        event.Skip()

    def buttonThroughOff_Clicked(self, event):
        event.Skip()

    def buttonAlwaysTopOn_Clicked(self, event):
        event.Skip()

    def buttonAlwaysTopOff_Clicked(self, event):
        event.Skip()

    def buttonChangeGraphic_Clicked(self, event):
        event.Skip()

    def buttonChangeOpacity_Clicked(self, event):
        event.Skip()

    def buttonChangeBlending_Clicked(self, event):
        event.Skip()

    def buttonPlaySE_Clicked(self, event):
        event.Skip()

    def buttonScript_Clicked(self, event):
        event.Skip()

    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class ChangeBlending_Dialog_Template
###########################################################################

class ChangeBlending_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(
            "Change Blending"), pos=wx.DefaultPosition, size=wx.Size(255, 93), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        sizerBlending = wx.BoxSizer(wx.VERTICAL)

        self.labelBlending = wx.StaticText(
            self, wx.ID_ANY, _("Blending:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelBlending.Wrap(-1)
        sizerBlending.Add(self.labelBlending, 0, wx.ALL, 5)

        comboBoxBlendingChoices = [_("Normal"), _("Add"), _("Subtract")]
        self.comboBoxBlending = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxBlendingChoices, 0)
        self.comboBoxBlending.SetSelection(0)
        sizerBlending.Add(
            self.comboBoxBlending, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerBlending, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        sizerOKCancel = wx.BoxSizer(wx.VERTICAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(
            self.buttonCancel, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerOKCancel, 0, 0, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class Jump_Dialog_Template
###########################################################################

class Jump_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(
            "Jump"), pos=wx.DefaultPosition, size=wx.Size(185, 131), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        sizerJump = wx.BoxSizer(wx.VERTICAL)

        self.labelJumpX = wx.StaticText(
            self, wx.ID_ANY, _("X+:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelJumpX.Wrap(-1)
        sizerJump.Add(self.labelJumpX, 0, wx.ALL, 5)

        self.spinCtrlJumpX = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerJump.Add(
            self.spinCtrlJumpX, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelJumpY = wx.StaticText(
            self, wx.ID_ANY, _("Y+:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelJumpY.Wrap(-1)
        sizerJump.Add(self.labelJumpY, 0, wx.ALL, 5)

        self.spinCtrlJumpY = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        sizerJump.Add(
            self.spinCtrlJumpY, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerJump, 1, wx.EXPAND, 5)

        sizerOKCancel = wx.BoxSizer(wx.VERTICAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(
            self.buttonCancel, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerOKCancel, 0, 0, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class ChangeSpeed_Dialog_Template
###########################################################################

class ChangeSpeed_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(
            "Change Speed"), pos=wx.DefaultPosition, size=wx.Size(256, 89), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        sizerSpeed = wx.BoxSizer(wx.VERTICAL)

        self.labelMoveSpeed = wx.StaticText(
            self, wx.ID_ANY, _("Move Speed:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelMoveSpeed.Wrap(-1)
        sizerSpeed.Add(self.labelMoveSpeed, 0, wx.ALL, 5)

        comboBoxMoveSpeedChoices = [_("1: Slowest"), _("2: Slower"), _(
            "3: Slow"), _("4: Fast"), _("5: Faster"), _("6: Fastest")]
        self.comboBoxMoveSpeed = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxMoveSpeedChoices, 0)
        self.comboBoxMoveSpeed.SetSelection(0)
        sizerSpeed.Add(
            self.comboBoxMoveSpeed, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerSpeed, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        sizerOKCancel = wx.BoxSizer(wx.VERTICAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(
            self.buttonCancel, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerOKCancel, 0, 0, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class ChangeFrequency_Dialog_Template
###########################################################################

class ChangeFrequency_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(
            "Change Frequency"), pos=wx.DefaultPosition, size=wx.Size(256, 89), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        sizerFrequency = wx.BoxSizer(wx.VERTICAL)

        self.labelMoveFrequency = wx.StaticText(
            self, wx.ID_ANY, _("Move Frequency:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelMoveFrequency.Wrap(-1)
        sizerFrequency.Add(self.labelMoveFrequency, 0, wx.ALL, 5)

        comboBoxMoveFrequencyChoices = [_("1: Lowest"), _("2: Lower"), _(
            "3: Low"), _("4: High"), _("5: Higher"), _("6: Highest")]
        self.comboBoxMoveFrequency = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxMoveFrequencyChoices, 0)
        self.comboBoxMoveFrequency.SetSelection(0)
        sizerFrequency.Add(
            self.comboBoxMoveFrequency, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerFrequency, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        sizerOKCancel = wx.BoxSizer(wx.VERTICAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.ALL, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(
            self.buttonCancel, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(sizerOKCancel, 0, 0, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class ParameterGraph_Panel_Template
###########################################################################

class ParameterGraph_Panel_Template (wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(
            577, 447), style=wx.FULL_REPAINT_ON_RESIZE | wx.TAB_TRAVERSAL)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        sizerNoteBook = wx.BoxSizer(wx.VERTICAL)

        self.noteBookParameters = wx.Notebook(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.panelMaxHP = wx.Panel(
            self.noteBookParameters, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizerGraph = wx.BoxSizer(wx.VERTICAL)

        from .Extras import ParameterGraph
        self.interactiveGraph = ParameterGraph(self.panelMaxHP)
        sizerGraph.Add(self.interactiveGraph, 1, wx.EXPAND, 0)

        self.panelMaxHP.SetSizer(sizerGraph)
        self.panelMaxHP.Layout()
        sizerGraph.Fit(self.panelMaxHP)
        self.noteBookParameters.AddPage(self.panelMaxHP, _("MaxHP"), False)
        self.panelMaxSP = wx.Panel(
            self.noteBookParameters, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.noteBookParameters.AddPage(self.panelMaxSP, _("MaxSP"), False)

        sizerNoteBook.Add(self.noteBookParameters, 1, wx.EXPAND | wx.ALL, 5)

        MainSizer.Add(sizerNoteBook, 1, wx.EXPAND, 5)

        sizerButtons = wx.BoxSizer(wx.HORIZONTAL)

        sizerGenerate = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonGenerate = wx.Button(
            self, wx.ID_ANY, _("Generate"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerGenerate.Add(self.buttonGenerate, 0, wx.ALL, 5)

        self.checkBoxScaled = wx.CheckBox(
            self, wx.ID_ANY, _("Scaled"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerGenerate.Add(
            self.checkBoxScaled, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer639 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelX = wx.StaticText(
            self, wx.ID_ANY, _("Level:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelX.Wrap(-1)
        bSizer639.Add(self.labelX, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.labelValueX = wx.StaticText(
            self, wx.ID_ANY, _("VALUE_X"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelValueX.Wrap(-1)
        bSizer639.Add(
            self.labelValueX, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sizerGenerate.Add(bSizer639, 1, wx.EXPAND, 5)

        bSizer640 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelY = wx.StaticText(
            self, wx.ID_ANY, _("Value:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelY.Wrap(-1)
        bSizer640.Add(self.labelY, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.labelValueY = wx.StaticText(
            self, wx.ID_ANY, _("VALUE_Y"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelValueY.Wrap(-1)
        bSizer640.Add(
            self.labelValueY, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sizerGenerate.Add(bSizer640, 1, wx.EXPAND, 5)

        sizerButtons.Add(sizerGenerate, 1, wx.EXPAND, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonApply = wx.Button(
            self, wx.ID_ANY, _("Apply"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonApply, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.buttonClose = wx.Button(
            self, wx.ID_ANY, _("Close"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(
            self.buttonClose, 0, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        sizerButtons.Add(sizerOKCancel, 0, wx.EXPAND, 5)

        MainSizer.Add(sizerButtons, 0, wx.EXPAND, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        # Connect Events
        self.noteBookParameters.Bind(
            wx.EVT_NOTEBOOK_PAGE_CHANGED, self.noteBookParameters_PageChanged)
        self.buttonGenerate.Bind(wx.EVT_BUTTON, self.buttonGenerate_Clicked)
        self.checkBoxScaled.Bind(
            wx.EVT_CHECKBOX, self.checkBoxScaled_CheckChanged)
        self.buttonApply.Bind(wx.EVT_BUTTON, self.buttonApply_Clicked)
        self.buttonClose.Bind(wx.EVT_BUTTON, self.buttonClose_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def noteBookParameters_PageChanged(self, event):
        event.Skip()

    def buttonGenerate_Clicked(self, event):
        event.Skip()

    def checkBoxScaled_CheckChanged(self, event):
        event.Skip()

    def buttonApply_Clicked(self, event):
        event.Skip()

    def buttonClose_Clicked(self, event):
        event.Skip()


###########################################################################
# Class EnemyExpGold_Dialog_Template
###########################################################################

class EnemyExpGold_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(
            "Enemy (Exp/Gold)"), pos=wx.DefaultPosition, size=wx.Size(280, 112), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        bSizer637 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelType = wx.StaticText(self, wx.ID_ANY, _(
            "(Gold/Experience):"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelType.Wrap(-1)
        bSizer637.Add(self.labelType, 70, wx.ALL, 5)

        self.labelVariance = wx.StaticText(
            self, wx.ID_ANY, _("Variance:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelVariance.Wrap(-1)
        bSizer637.Add(self.labelVariance, 30, wx.ALL, 5)

        MainSizer.Add(bSizer637, 0, wx.EXPAND, 5)

        bSizer638 = wx.BoxSizer(wx.HORIZONTAL)

        self.spinCtrlValue = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS | wx.SP_WRAP, 0, 10, 0)
        bSizer638.Add(
            self.spinCtrlValue, 70, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlVariance = wx.SpinCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS | wx.SP_WRAP, 0, 100, 0)
        bSizer638.Add(
            self.spinCtrlVariance, 30, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        MainSizer.Add(bSizer638, 0, wx.EXPAND, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonCancel, 0, wx.ALL, 5)

        MainSizer.Add(sizerOKCancel, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class AudioPlayer_Panel_Template
###########################################################################

class AudioPlayer_Panel_Template (wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(
            417, 476), style=wx.TAB_TRAVERSAL)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        sizerControls = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        sizerSelection = wx.BoxSizer(wx.HORIZONTAL)

        self.notebookAudio = wx.Notebook(
            sizerControls.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.panelBGM = wx.Panel(
            self.notebookAudio, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer6311 = wx.BoxSizer(wx.VERTICAL)

        listBoxAudioChoices = []
        self.listBoxAudio = wx.ListBox(
            self.panelBGM, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxAudioChoices, wx.LB_SINGLE | wx.CLIP_CHILDREN)
        self.listBoxAudio.SetHelpText(_("Select the file to play"))

        bSizer6311.Add(self.listBoxAudio, 1, wx.EXPAND, 5)

        self.panelBGM.SetSizer(bSizer6311)
        self.panelBGM.Layout()
        bSizer6311.Fit(self.panelBGM)
        self.notebookAudio.AddPage(self.panelBGM, _("BGM"), False)

        sizerSelection.Add(
            self.notebookAudio, 1, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        sizerVolume = wx.StaticBoxSizer(
            wx.StaticBox(sizerControls.GetStaticBox(), wx.ID_ANY, _("Volume")), wx.VERTICAL)

        self.sliderVolume = wx.Slider(sizerVolume.GetStaticBox(
        ), wx.ID_ANY, 80, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_INVERSE | wx.SL_LABELS | wx.SL_VERTICAL)
        self.sliderVolume.SetHelpText(
            _("Adjust the volume to play the sound at"))

        sizerVolume.Add(self.sliderVolume, 1, wx.ALL, 5)

        self.spinCtrlVolume = wx.SpinCtrl(sizerVolume.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(54, -1), wx.SP_ARROW_KEYS, 0, 100, 80)
        self.spinCtrlVolume.SetHelpText(
            _("Adjust the volume to play the sound at"))

        sizerVolume.Add(self.spinCtrlVolume, 0, wx.ALL, 5)

        sizerSelection.Add(sizerVolume, 0, wx.ALL | wx.EXPAND, 5)

        sizerPitch = wx.StaticBoxSizer(
            wx.StaticBox(sizerControls.GetStaticBox(), wx.ID_ANY, _("Pitch")), wx.VERTICAL)

        self.sliderPitch = wx.Slider(sizerPitch.GetStaticBox(
        ), wx.ID_ANY, 100, 25, 300, wx.DefaultPosition, wx.DefaultSize, wx.SL_INVERSE | wx.SL_LABELS | wx.SL_VERTICAL)
        self.sliderPitch.SetHelpText(
            _("Adjust the pitch shift to apply to the sound"))

        sizerPitch.Add(self.sliderPitch, 1, wx.ALL, 5)

        self.spinCtrlPitch = wx.SpinCtrl(sizerPitch.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(48, -1), wx.SP_ARROW_KEYS, 25, 300, 100)
        self.spinCtrlPitch.SetHelpText(
            _("Adjust the pitch shift to apply to the sound"))

        sizerPitch.Add(self.spinCtrlPitch, 0, wx.ALL, 5)

        sizerSelection.Add(sizerPitch, 0, wx.ALL | wx.EXPAND, 5)

        sizerControls.Add(sizerSelection, 1, wx.EXPAND, 5)

        sizerPlayback = wx.BoxSizer(wx.VERTICAL)

        bSizer632 = wx.BoxSizer(wx.VERTICAL)

        from .Extras import WaveFormPanel
        color = wx.Colour(100, 100, 220, 255)
        self.waveFormPanelLeft = WaveFormPanel(self, color=color)
        self.waveFormPanelLeft.SetHelpText(
            _("Visual representation of the left audio channel"))
        self.waveFormPanelLeft.SetMinSize(wx.Size(-1, 56))

        bSizer632.Add(
            self.waveFormPanelLeft, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        from .Extras import WaveFormPanel
        color = wx.Colour(220, 100, 100, 255)
        self.waveFormPanelRight = WaveFormPanel(self, color=color)
        self.waveFormPanelRight.SetHelpText(
            _("Visual representation of the right audio channel"))
        self.waveFormPanelRight.SetMinSize(wx.Size(-1, 56))

        bSizer632.Add(
            self.waveFormPanelRight, 0, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        bSizer6301 = wx.BoxSizer(wx.VERTICAL)

        self.sliderPosition = wx.Slider(sizerControls.GetStaticBox(
        ), wx.ID_ANY, 0, 0, 10, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        self.sliderPosition.Enable(False)
        self.sliderPosition.SetHelpText(
            _("Adjust the offset that playback will begin from"))

        bSizer6301.Add(self.sliderPosition, 0, wx.ALL | wx.EXPAND, 5)

        bSizer631 = wx.BoxSizer(wx.HORIZONTAL)

        self.checkBoxRepeat = wx.CheckBox(sizerControls.GetStaticBox(), wx.ID_ANY, _(
            "Repeat"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.checkBoxRepeat.SetHelpText(
            _("Check to loop playback when the end of the stream is reached"))

        bSizer631.Add(self.checkBoxRepeat, 0, wx.ALL | wx.EXPAND, 5)

        sizerLabel = wx.BoxSizer(wx.VERTICAL)

        self.labelFileName = wx.StaticText(sizerControls.GetStaticBox(), wx.ID_ANY, _(
            "FILENAME"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelFileName.Wrap(-1)
        self.labelFileName.SetHelpText(
            _("The currently loaded file and duration of playback"))

        sizerLabel.Add(
            self.labelFileName, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.ALL, 5)

        self.labelFileDuration = wx.StaticText(sizerControls.GetStaticBox(), wx.ID_ANY, _(
            "[0.00.00]"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT)
        self.labelFileDuration.Wrap(-1)
        self.labelFileDuration.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), 76, 90, 90, False, wx.EmptyString))

        sizerLabel.Add(self.labelFileDuration, 0,
                       wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        bSizer631.Add(sizerLabel, 1, 0, 5)

        self.buttonPlay = wx.BitmapButton(sizerControls.GetStaticBox(
        ), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        self.buttonPlay.SetHelpText(
            _("Play the sound on the current channel"))

        bSizer631.Add(self.buttonPlay, 0, wx.ALL, 5)

        self.buttonPause = wx.BitmapButton(sizerControls.GetStaticBox(
        ), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        self.buttonPause.SetHelpText(
            _("Pause playback on the current channel"))

        bSizer631.Add(self.buttonPause, 0, wx.TOP | wx.BOTTOM, 5)

        self.buttonStop = wx.BitmapButton(sizerControls.GetStaticBox(
        ), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        self.buttonStop.SetHelpText(_("Stop playback on the current channel"))

        bSizer631.Add(self.buttonStop, 0, wx.ALL, 5)

        bSizer6301.Add(bSizer631, 0, wx.ALIGN_RIGHT | wx.EXPAND, 5)

        bSizer632.Add(bSizer6301, 0, wx.EXPAND, 5)

        sizerPlayback.Add(bSizer632, 0, wx.EXPAND, 5)

        sizerControls.Add(sizerPlayback, 0, wx.EXPAND, 5)

        MainSizer.Add(sizerControls, 1, wx.EXPAND | wx.ALL, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        sizerStop = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonStopAll = wx.Button(
            self, wx.ID_ANY, _("Stop All"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.buttonStopAll.SetHelpText(_("Stop playback on all channels"))

        sizerStop.Add(self.buttonStopAll, 0, wx.ALL, 5)

        self.checkBoxMicroseconds = wx.CheckBox(self, wx.ID_ANY, _(
            "Display Microseconds"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.checkBoxMicroseconds.SetHelpText(
            _("Check to have microseconds displayed in the duration label"))

        sizerStop.Add(
            self.checkBoxMicroseconds, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sizerOKCancel.Add(sizerStop, 1, wx.EXPAND, 5)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.buttonOK.SetHelpText(_("Apply settings and close window"))

        sizerOKCancel.Add(self.buttonOK, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.buttonCancel.SetHelpText(_("Cancel settings and close window"))

        sizerOKCancel.Add(
            self.buttonCancel, 0, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        MainSizer.Add(sizerOKCancel, 0, wx.ALIGN_RIGHT | wx.EXPAND, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        # Connect Events
        self.notebookAudio.Bind(
            wx.EVT_NOTEBOOK_PAGE_CHANGED, self.notebookAudio_PageChanged)
        self.listBoxAudio.Bind(
            wx.EVT_LISTBOX_DCLICK, self.listBoxAudio_DoubleClick)
        self.sliderVolume.Bind(
            wx.EVT_ERASE_BACKGROUND, self.ControlOnEraseBackground)
        self.sliderVolume.Bind(wx.EVT_SCROLL, self.sliderVolume_Scrolled)
        self.spinCtrlVolume.Bind(
            wx.EVT_ERASE_BACKGROUND, self.ControlOnEraseBackground)
        self.spinCtrlVolume.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlVolume_ValueChanged)
        self.sliderPitch.Bind(
            wx.EVT_ERASE_BACKGROUND, self.ControlOnEraseBackground)
        self.sliderPitch.Bind(wx.EVT_SCROLL, self.sliderPitch_Scrolled)
        self.spinCtrlPitch.Bind(
            wx.EVT_ERASE_BACKGROUND, self.ControlOnEraseBackground)
        self.spinCtrlPitch.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlPitch_ValueChanged)
        self.sliderPosition.Bind(
            wx.EVT_ERASE_BACKGROUND, self.ControlOnEraseBackground)
        self.sliderPosition.Bind(wx.EVT_SCROLL, self.sliderPosition_Scrolled)
        self.checkBoxRepeat.Bind(
            wx.EVT_CHECKBOX, self.checkBoxRepeat_CheckChanged)
        self.checkBoxRepeat.Bind(
            wx.EVT_ERASE_BACKGROUND, self.ControlOnEraseBackground)
        self.labelFileName.Bind(
            wx.EVT_ERASE_BACKGROUND, self.ControlOnEraseBackground)
        self.buttonPlay.Bind(wx.EVT_BUTTON, self.buttonPlay_Clicked)
        self.buttonPlay.Bind(
            wx.EVT_ERASE_BACKGROUND, self.ControlOnEraseBackground)
        self.buttonPause.Bind(wx.EVT_BUTTON, self.buttonPause_Clicked)
        self.buttonPause.Bind(
            wx.EVT_ERASE_BACKGROUND, self.ControlOnEraseBackground)
        self.buttonStop.Bind(wx.EVT_BUTTON, self.buttonStop_Clicked)
        self.buttonStop.Bind(
            wx.EVT_ERASE_BACKGROUND, self.ControlOnEraseBackground)
        self.buttonStopAll.Bind(wx.EVT_BUTTON, self.buttonStopAll_Clicked)
        self.checkBoxMicroseconds.Bind(
            wx.EVT_CHECKBOX, self.checkBoxMicroseconds_CheckChanged)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def notebookAudio_PageChanged(self, event):
        event.Skip()

    def listBoxAudio_DoubleClick(self, event):
        event.Skip()

    def ControlOnEraseBackground(self, event):
        event.Skip()

    def sliderVolume_Scrolled(self, event):
        event.Skip()

    def spinCtrlVolume_ValueChanged(self, event):
        event.Skip()

    def sliderPitch_Scrolled(self, event):
        event.Skip()

    def spinCtrlPitch_ValueChanged(self, event):
        event.Skip()

    def sliderPosition_Scrolled(self, event):
        event.Skip()

    def checkBoxRepeat_CheckChanged(self, event):
        event.Skip()

    def buttonPlay_Clicked(self, event):
        event.Skip()

    def buttonPause_Clicked(self, event):
        event.Skip()

    def buttonStop_Clicked(self, event):
        event.Skip()

    def buttonStopAll_Clicked(self, event):
        event.Skip()

    def checkBoxMicroseconds_CheckChanged(self, event):
        event.Skip()

    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class ExpGraph_Dialog_Template
###########################################################################

class ExpGraph_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_("Experience Graph"), pos=wx.DefaultPosition, size=wx.Size(
            405, 311), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        from .Extras import ParameterGraph
        self.graphPanel = ParameterGraph(self)
        MainSizer.Add(self.graphPanel, 1, wx.ALL | wx.EXPAND, 5)

        sizerClose = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.buttonOK.SetDefault()
        sizerClose.Add(self.buttonOK, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerClose.Add(self.buttonCancel, 0, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        MainSizer.Add(sizerClose, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class ExpGrid_Dialog_Template
###########################################################################

class ExpGrid_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_("Experience Curve"), pos=wx.DefaultPosition, size=wx.Size(
            540, 496), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        self.noteBookExpList = wx.Notebook(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.panelNextLevel = wx.Panel(
            self.noteBookExpList, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        panelSizerNextLevel = wx.BoxSizer(wx.VERTICAL)

        self.expGrid = wx.grid.Grid(
            self.panelNextLevel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL | wx.VSCROLL)

        # Grid
        self.expGrid.CreateGrid(0, 10)
        self.expGrid.EnableEditing(False)
        self.expGrid.EnableGridLines(False)
        self.expGrid.EnableDragGridSize(False)
        self.expGrid.SetMargins(0, 0)

        # Columns
        self.expGrid.EnableDragColMove(False)
        self.expGrid.EnableDragColSize(False)
        self.expGrid.SetColLabelSize(0)
        self.expGrid.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.expGrid.EnableDragRowSize(False)
        self.expGrid.SetRowLabelSize(0)
        self.expGrid.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.expGrid.SetLabelFont(
            wx.Font(8, 76, 90, 90, False, wx.EmptyString))

        # Cell Defaults
        self.expGrid.SetDefaultCellFont(
            wx.Font(8, 76, 90, 90, False, wx.EmptyString))
        self.expGrid.SetDefaultCellAlignment(wx.ALIGN_RIGHT, wx.ALIGN_TOP)
        panelSizerNextLevel.Add(self.expGrid, 1, wx.ALL | wx.EXPAND, 5)

        self.panelNextLevel.SetSizer(panelSizerNextLevel)
        self.panelNextLevel.Layout()
        panelSizerNextLevel.Fit(self.panelNextLevel)
        self.noteBookExpList.AddPage(
            self.panelNextLevel, _("To Next Level"), True)
        self.panelTotal = wx.Panel(
            self.noteBookExpList, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        panelSizerTotal = wx.BoxSizer(wx.VERTICAL)

        self.panelTotal.SetSizer(panelSizerTotal)
        self.panelTotal.Layout()
        panelSizerTotal.Fit(self.panelTotal)
        self.noteBookExpList.AddPage(self.panelTotal, _("Total"), False)

        MainSizer.Add(self.noteBookExpList, 1, wx.EXPAND | wx.ALL, 5)

        bSizer638 = wx.BoxSizer(wx.HORIZONTAL)

        sizerControls = wx.BoxSizer(wx.VERTICAL)

        sizerBasis = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Basis")), wx.HORIZONTAL)

        self.sliderBasis = wx.Slider(sizerBasis.GetStaticBox(
        ), wx.ID_ANY, 35, 5, 50, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        sizerBasis.Add(self.sliderBasis, 1, wx.ALL, 5)

        self.spinCtrlBasis = wx.SpinCtrl(sizerBasis.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(60, -1), wx.SP_ARROW_KEYS, 5, 50, 35)
        sizerBasis.Add(self.spinCtrlBasis, 0, wx.ALL, 5)

        sizerControls.Add(sizerBasis, 1, wx.ALL | wx.EXPAND, 5)

        sizerInflation = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Inflation")), wx.HORIZONTAL)

        self.sliderInflation = wx.Slider(sizerInflation.GetStaticBox(
        ), wx.ID_ANY, 35, 5, 50, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        sizerInflation.Add(self.sliderInflation, 1, wx.ALL, 5)

        self.spinCtrlInflation = wx.SpinCtrl(sizerInflation.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(60, -1), wx.SP_ARROW_KEYS, 5, 50, 35)
        sizerInflation.Add(self.spinCtrlInflation, 0, wx.ALL, 5)

        sizerControls.Add(sizerInflation, 1, wx.ALL | wx.EXPAND, 5)

        bSizer638.Add(sizerControls, 50, wx.EXPAND, 5)

        sizerCurveGeneration = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Curve Generation")), wx.VERTICAL)

        sizerLabels = wx.BoxSizer(wx.HORIZONTAL)

        self.labelMinValue = wx.StaticText(sizerCurveGeneration.GetStaticBox(
        ), wx.ID_ANY, _("First Level:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelMinValue.Wrap(-1)
        sizerLabels.Add(self.labelMinValue, 30, wx.ALL, 5)

        self.labelMaxLevel = wx.StaticText(sizerCurveGeneration.GetStaticBox(
        ), wx.ID_ANY, _("Final Level:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelMaxLevel.Wrap(-1)
        sizerLabels.Add(self.labelMaxLevel, 45, wx.ALL, 5)

        self.labelSpeed = wx.StaticText(sizerCurveGeneration.GetStaticBox(), wx.ID_ANY, _(
            "Speed:"), wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.labelSpeed.Wrap(-1)
        sizerLabels.Add(self.labelSpeed, 25, wx.ALL, 5)

        sizerCurveGeneration.Add(sizerLabels, 0, wx.EXPAND, 5)

        sizerControls1 = wx.BoxSizer(wx.HORIZONTAL)

        self.spinCtrlMinValue = wx.SpinCtrl(sizerCurveGeneration.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS | wx.SP_WRAP, 0, 2147483647, 0)
        self.spinCtrlMinValue.Enable(False)

        sizerControls1.Add(
            self.spinCtrlMinValue, 30, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlMaxValue = wx.SpinCtrl(sizerCurveGeneration.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS | wx.SP_WRAP, 0, 2147483647, 0)
        self.spinCtrlMaxValue.Enable(False)

        sizerControls1.Add(
            self.spinCtrlMaxValue, 45, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        from wx.lib.agw.floatspin import FloatSpin
        self.spinCtrlSpeed = FloatSpin(self)
        self.spinCtrlSpeed.Enable(False)

        sizerControls1.Add(
            self.spinCtrlSpeed, 25, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerCurveGeneration.Add(sizerControls1, 1, wx.EXPAND, 5)

        self.sliderSpeed = wx.Slider(sizerCurveGeneration.GetStaticBox(
        ), wx.ID_ANY, 0, -10, 10, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_TOP)
        self.sliderSpeed.Enable(False)

        sizerCurveGeneration.Add(
            self.sliderSpeed, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.buttonGraphEditor = wx.Button(sizerCurveGeneration.GetStaticBox(
        ), wx.ID_ANY, _("Graph Editor..."), wx.DefaultPosition, wx.DefaultSize, 0)
        self.buttonGraphEditor.Enable(False)

        sizerCurveGeneration.Add(
            self.buttonGraphEditor, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        bSizer638.Add(sizerCurveGeneration, 50, wx.EXPAND | wx.ALL, 5)

        MainSizer.Add(bSizer638, 0, wx.EXPAND, 5)

        sizerButtons = wx.BoxSizer(wx.HORIZONTAL)

        sizerGraphButton = wx.BoxSizer(wx.HORIZONTAL)

        self.checkBoxCurveGeneration = wx.CheckBox(self, wx.ID_ANY, _(
            "Use Curve Generation"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerGraphButton.Add(
            self.checkBoxCurveGeneration, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sizerButtons.Add(sizerGraphButton, 1, wx.EXPAND, 5)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons.Add(self.buttonOK, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerButtons.Add(
            self.buttonCancel, 0, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        MainSizer.Add(
            sizerButtons, 0, wx.ALIGN_RIGHT | wx.ALIGN_BOTTOM | wx.EXPAND, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.noteBookExpList.Bind(
            wx.EVT_NOTEBOOK_PAGE_CHANGED, self.noteBookExpCurve_PageChanged)
        self.sliderBasis.Bind(wx.EVT_SCROLL, self.sliderBasis_Scrolled)
        self.spinCtrlBasis.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlBasis__ValueChanged)
        self.sliderInflation.Bind(wx.EVT_SCROLL, self.sliderInflation_Scrolled)
        self.spinCtrlInflation.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlInflation_ValueChanged)
        self.spinCtrlMinValue.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlMinValue_ValueChanged)
        self.spinCtrlMaxValue.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlMaxValue_ValueChanged)
        self.sliderSpeed.Bind(wx.EVT_SCROLL, self.sliderSpeed_Scrolled)
        self.buttonGraphEditor.Bind(
            wx.EVT_BUTTON, self.buttonGraphEditor_Clicked)
        self.checkBoxCurveGeneration.Bind(
            wx.EVT_CHECKBOX, self.checkBoxCurveGeneration_CheckChanged)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def noteBookExpCurve_PageChanged(self, event):
        event.Skip()

    def sliderBasis_Scrolled(self, event):
        event.Skip()

    def spinCtrlBasis__ValueChanged(self, event):
        event.Skip()

    def sliderInflation_Scrolled(self, event):
        event.Skip()

    def spinCtrlInflation_ValueChanged(self, event):
        event.Skip()

    def spinCtrlMinValue_ValueChanged(self, event):
        event.Skip()

    def spinCtrlMaxValue_ValueChanged(self, event):
        event.Skip()

    def sliderSpeed_Scrolled(self, event):
        event.Skip()

    def buttonGraphEditor_Clicked(self, event):
        event.Skip()

    def checkBoxCurveGeneration_CheckChanged(self, event):
        event.Skip()

    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class ScriptEditor_Panel_Template
###########################################################################

class ScriptEditor_Panel_Template (wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(
            540, 485), style=wx.TAB_TRAVERSAL)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        bSizer643 = wx.BoxSizer(wx.HORIZONTAL)

        sizerScriptControl = wx.BoxSizer(wx.VERTICAL)

        self.scriptPanel = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizerScript = wx.BoxSizer(wx.VERTICAL)

        self.toolBar = wx.ToolBar(self.scriptPanel, wx.ID_ANY, wx.DefaultPosition,
                                  wx.DefaultSize, wx.TB_FLAT | wx.TB_HORIZONTAL | wx.CLIP_CHILDREN)
        self.toolBar.Realize()

        sizerScript.Add(self.toolBar, 0, wx.EXPAND | wx.TOP, 5)

        from .Extras import ScriptTextCtrl
        self.scriptCtrl = ScriptTextCtrl(self.scriptPanel)

        sizerScript.Add(self.scriptCtrl, 1, wx.EXPAND, 5)

        self.scriptPanel.SetSizer(sizerScript)
        self.scriptPanel.Layout()
        sizerScript.Fit(self.scriptPanel)
        sizerScriptControl.Add(self.scriptPanel, 1, wx.EXPAND | wx.ALL, 5)

        bSizer643.Add(sizerScriptControl, 1, wx.EXPAND, 5)

        MainSizer.Add(bSizer643, 1, wx.EXPAND, 5)

        self.SetSizer(MainSizer)
        self.Layout()

    def __del__(self):
        pass


###########################################################################
# Class FindReplace_Dialog_Template
###########################################################################

class FindReplace_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_("Find & Replace"), pos=wx.DefaultPosition, size=wx.Size(
            295, 365), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        sizerNotebook = wx.BoxSizer(wx.VERTICAL)

        self.noteBookFindReplace = wx.Notebook(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.panelFind = wx.Panel(
            self.noteBookFindReplace, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizerFind = wx.BoxSizer(wx.VERTICAL)

        self.labelFind = wx.StaticText(self.panelFind, wx.ID_ANY, _(
            "Find what:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelFind.Wrap(-1)
        sizerFind.Add(self.labelFind, 0, wx.ALL, 5)

        self.textCtrlFindSearch = wx.TextCtrl(
            self.panelFind, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlFindSearch.SetMaxLength(0)
        sizerFind.Add(
            self.textCtrlFindSearch, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelLookFind = wx.StaticText(
            self.panelFind, wx.ID_ANY, _("Look in:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelLookFind.Wrap(-1)
        sizerFind.Add(self.labelLookFind, 0, wx.ALL, 5)

        comboBoxLookChoices = [_("Current Script"), _("All Scripts")]
        self.comboBoxLook = wx.Choice(
            self.panelFind, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxLookChoices, 0)
        self.comboBoxLook.SetSelection(0)
        sizerFind.Add(
            self.comboBoxLook, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizerFindOptions = wx.StaticBoxSizer(
            wx.StaticBox(self.panelFind, wx.ID_ANY, _("Options")), wx.VERTICAL)

        self.checkBoxFindMatchCase = wx.CheckBox(sizerFindOptions.GetStaticBox(
        ), wx.ID_ANY, _("Match case"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerFindOptions.Add(self.checkBoxFindMatchCase, 0, wx.ALL, 5)

        self.checkBoxFindWholeWord = wx.CheckBox(sizerFindOptions.GetStaticBox(
        ), wx.ID_ANY, _("Match whole word"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerFindOptions.Add(
            self.checkBoxFindWholeWord, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.checkBoxFindSearchUp = wx.CheckBox(sizerFindOptions.GetStaticBox(
        ), wx.ID_ANY, _("Search up"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerFindOptions.Add(
            self.checkBoxFindSearchUp, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.checkBoxFindFlags = wx.CheckBox(sizerFindOptions.GetStaticBox(
        ), wx.ID_ANY, _("Use:"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerFindOptions.Add(
            self.checkBoxFindFlags, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        comboBoxFindFlagsChoices = [
            _("Regular Expressions"), _("Wild Cards")]
        self.comboBoxFindFlags = wx.Choice(sizerFindOptions.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxFindFlagsChoices, 0)
        self.comboBoxFindFlags.SetSelection(0)
        self.comboBoxFindFlags.Enable(False)

        sizerFindOptions.Add(
            self.comboBoxFindFlags, 0, wx.EXPAND | wx.RIGHT | wx.LEFT, 20)

        sizerFind.Add(sizerFindOptions, 0, wx.EXPAND | wx.ALL, 5)

        self.buttonFind = wx.Button(self.panelFind, wx.ID_ANY, _(
            "Find Next"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerFind.Add(self.buttonFind, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.panelFind.SetSizer(sizerFind)
        self.panelFind.Layout()
        sizerFind.Fit(self.panelFind)
        self.noteBookFindReplace.AddPage(self.panelFind, _("Find"), False)
        self.panelReplace = wx.Panel(
            self.noteBookFindReplace, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizerReplace = wx.BoxSizer(wx.VERTICAL)

        self.labelReplace = wx.StaticText(self.panelReplace, wx.ID_ANY, _(
            "Find what:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelReplace.Wrap(-1)
        sizerReplace.Add(self.labelReplace, 0, wx.ALL, 5)

        self.textCtrlReplaceSearch = wx.TextCtrl(
            self.panelReplace, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlReplaceSearch.SetMaxLength(0)
        sizerReplace.Add(
            self.textCtrlReplaceSearch, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelReplaceWith = wx.StaticText(self.panelReplace, wx.ID_ANY, _(
            "Replace with:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelReplaceWith.Wrap(-1)
        sizerReplace.Add(self.labelReplaceWith, 0, wx.ALL, 5)

        self.textCtrlReplace = wx.TextCtrl(
            self.panelReplace, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlReplace.SetMaxLength(0)
        sizerReplace.Add(
            self.textCtrlReplace, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.labelLookReplace = wx.StaticText(self.panelReplace, wx.ID_ANY, _(
            "Look in:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelLookReplace.Wrap(-1)
        sizerReplace.Add(self.labelLookReplace, 0, wx.ALL, 5)

        comboBoxLookReplaceChoices = [_("Current Script"), _("All Scripts")]
        self.comboBoxLookReplace = wx.Choice(
            self.panelReplace, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxLookReplaceChoices, 0)
        self.comboBoxLookReplace.SetSelection(0)
        sizerReplace.Add(
            self.comboBoxLookReplace, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizerReplaceOptions = wx.StaticBoxSizer(
            wx.StaticBox(self.panelReplace, wx.ID_ANY, _("Options")), wx.VERTICAL)

        self.checkBoxReplaceMatchCase = wx.CheckBox(sizerReplaceOptions.GetStaticBox(
        ), wx.ID_ANY, _("Match case"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerReplaceOptions.Add(self.checkBoxReplaceMatchCase, 0, wx.ALL, 5)

        self.checkBoxReplaceWholeWord = wx.CheckBox(sizerReplaceOptions.GetStaticBox(
        ), wx.ID_ANY, _("Match whole word"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerReplaceOptions.Add(
            self.checkBoxReplaceWholeWord, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.checkBoxReplaceSearchUp = wx.CheckBox(sizerReplaceOptions.GetStaticBox(
        ), wx.ID_ANY, _("Search up"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerReplaceOptions.Add(
            self.checkBoxReplaceSearchUp, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.checkBoxReplaceFlags = wx.CheckBox(sizerReplaceOptions.GetStaticBox(
        ), wx.ID_ANY, _("Use:"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerReplaceOptions.Add(
            self.checkBoxReplaceFlags, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        comboBoxReplaceFlagsChoices = [
            _("Regular Expressions"), _("Wild Cards")]
        self.comboBoxReplaceFlags = wx.Choice(sizerReplaceOptions.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxReplaceFlagsChoices, 0)
        self.comboBoxReplaceFlags.SetSelection(0)
        self.comboBoxReplaceFlags.Enable(False)

        sizerReplaceOptions.Add(
            self.comboBoxReplaceFlags, 0, wx.EXPAND | wx.RIGHT | wx.LEFT, 20)

        sizerReplace.Add(sizerReplaceOptions, 0, wx.EXPAND | wx.ALL, 5)

        bSizer653 = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonFindNext = wx.Button(self.panelReplace, wx.ID_ANY, _(
            "Find Next"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer653.Add(
            self.buttonFindNext, 0, wx.ALIGN_RIGHT | wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.buttonReplace = wx.Button(self.panelReplace, wx.ID_ANY, _(
            "Replace"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer653.Add(self.buttonReplace, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.buttonReplaceAll = wx.Button(self.panelReplace, wx.ID_ANY, _(
            "Replace All"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer653.Add(
            self.buttonReplaceAll, 0, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        sizerReplace.Add(bSizer653, 1, wx.ALIGN_RIGHT, 5)

        self.panelReplace.SetSizer(sizerReplace)
        self.panelReplace.Layout()
        sizerReplace.Fit(self.panelReplace)
        self.noteBookFindReplace.AddPage(
            self.panelReplace, _("Replace"), True)

        sizerNotebook.Add(self.noteBookFindReplace, 1, wx.EXPAND, 5)

        MainSizer.Add(sizerNotebook, 1, wx.EXPAND, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.noteBookFindReplace.Bind(
            wx.EVT_NOTEBOOK_PAGE_CHANGED, self.noteBookFindReplace_PageChanged)
        self.labelFind.Bind(wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.textCtrlFindSearch.Bind(wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.labelLookFind.Bind(wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.comboBoxLook.Bind(
            wx.EVT_CHOICE, self.comboBoxLook_SelectionChanged)
        self.comboBoxLook.Bind(wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.checkBoxFindMatchCase.Bind(
            wx.EVT_CHECKBOX, self.checkBoxMatchCase_CheckChanged)
        self.checkBoxFindMatchCase.Bind(
            wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.checkBoxFindWholeWord.Bind(
            wx.EVT_CHECKBOX, self.checkBoxWholeWord_CheckChanged)
        self.checkBoxFindWholeWord.Bind(
            wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.checkBoxFindSearchUp.Bind(
            wx.EVT_CHECKBOX, self.checkBoxSearchUP_CheckChanged)
        self.checkBoxFindSearchUp.Bind(wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.checkBoxFindFlags.Bind(
            wx.EVT_CHECKBOX, self.checkBoxFlags_CheckChanged)
        self.checkBoxFindFlags.Bind(wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.comboBoxFindFlags.Bind(
            wx.EVT_CHOICE, self.comboBoxFlags_SelectionChanged)
        self.comboBoxFindFlags.Bind(wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.buttonFind.Bind(wx.EVT_BUTTON, self.buttonFindNext_Clicked)
        self.buttonFind.Bind(wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.labelReplace.Bind(wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.textCtrlReplaceSearch.Bind(
            wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.labelReplaceWith.Bind(wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.textCtrlReplace.Bind(wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.comboBoxLookReplace.Bind(
            wx.EVT_CHOICE, self.comboBoxLook_SelectionChanged)
        self.comboBoxLookReplace.Bind(wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.checkBoxReplaceMatchCase.Bind(
            wx.EVT_CHECKBOX, self.checkBoxMatchCase_CheckChanged)
        self.checkBoxReplaceMatchCase.Bind(
            wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.checkBoxReplaceWholeWord.Bind(
            wx.EVT_CHECKBOX, self.checkBoxWholeWord_CheckChanged)
        self.checkBoxReplaceWholeWord.Bind(
            wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.checkBoxReplaceSearchUp.Bind(
            wx.EVT_CHECKBOX, self.checkBoxSearchUP_CheckChanged)
        self.checkBoxReplaceSearchUp.Bind(
            wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.checkBoxReplaceFlags.Bind(
            wx.EVT_CHECKBOX, self.checkBoxFlags_CheckChanged)
        self.checkBoxReplaceFlags.Bind(wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.comboBoxReplaceFlags.Bind(
            wx.EVT_CHOICE, self.comboBoxFlags_SelectionChanged)
        self.comboBoxReplaceFlags.Bind(wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.buttonFindNext.Bind(wx.EVT_BUTTON, self.buttonFindNext_Clicked)
        self.buttonFindNext.Bind(wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.buttonReplace.Bind(wx.EVT_BUTTON, self.buttonReplace_Clicked)
        self.buttonReplace.Bind(wx.EVT_ERASE_BACKGROUND, self.DoNothing)
        self.buttonReplaceAll.Bind(
            wx.EVT_BUTTON, self.buttonReplaceAll_Clicked)
        self.buttonReplaceAll.Bind(wx.EVT_ERASE_BACKGROUND, self.DoNothing)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def noteBookFindReplace_PageChanged(self, event):
        event.Skip()

    def DoNothing(self, event):
        event.Skip()

    def comboBoxLook_SelectionChanged(self, event):
        event.Skip()

    def checkBoxMatchCase_CheckChanged(self, event):
        event.Skip()

    def checkBoxWholeWord_CheckChanged(self, event):
        event.Skip()

    def checkBoxSearchUP_CheckChanged(self, event):
        event.Skip()

    def checkBoxFlags_CheckChanged(self, event):
        event.Skip()

    def comboBoxFlags_SelectionChanged(self, event):
        event.Skip()

    def buttonFindNext_Clicked(self, event):
        event.Skip()

    def buttonReplace_Clicked(self, event):
        event.Skip()

    def buttonReplaceAll_Clicked(self, event):
        event.Skip()


###########################################################################
# Class ScriptSettings_Dialog_Template
###########################################################################

class ScriptSettings_Dialog_Template (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_("Script Editor Settings"), pos=wx.DefaultPosition, size=wx.Size(
            423, 309), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        self.noteBookSettings = wx.Notebook(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.panelFont = wx.Panel(
            self.noteBookSettings, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizerFontMain = wx.BoxSizer(wx.VERTICAL)

        sizerFontLabels = wx.BoxSizer(wx.HORIZONTAL)

        self.labelFont = wx.StaticText(
            self.panelFont, wx.ID_ANY, _("Font:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelFont.Wrap(-1)
        sizerFontLabels.Add(self.labelFont, 75, wx.ALL | wx.EXPAND, 5)

        self.labelSize = wx.StaticText(
            self.panelFont, wx.ID_ANY, _("Size:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelSize.Wrap(-1)
        sizerFontLabels.Add(self.labelSize, 25, wx.ALL | wx.EXPAND, 5)

        sizerFontMain.Add(sizerFontLabels, 0, wx.EXPAND, 5)

        sizerFontSelection = wx.BoxSizer(wx.HORIZONTAL)

        comboBoxFontChoices = []
        self.comboBoxFont = wx.Choice(
            self.panelFont, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxFontChoices, 0)
        self.comboBoxFont.SetSelection(0)
        sizerFontSelection.Add(
            self.comboBoxFont, 75, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        comboBoxSizeChoices = [_("6"), _("7"), _("8"), _("9"), _("10"), _("11"), _("12"), _("13"), _(
            "14"), _("15"), _("16"), _("17"), _("18"), _("19"), _("20"), _("21"), _("22"), _("23"), _("24")]
        self.comboBoxSize = wx.Choice(
            self.panelFont, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxSizeChoices, 0)
        self.comboBoxSize.SetSelection(4)
        sizerFontSelection.Add(
            self.comboBoxSize, 25, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        sizerFontMain.Add(sizerFontSelection, 0, wx.EXPAND, 5)

        sizerSettings = wx.BoxSizer(wx.HORIZONTAL)

        sizerDisplayItem = wx.BoxSizer(wx.VERTICAL)

        self.labelDisplayItem = wx.StaticText(self.panelFont, wx.ID_ANY, _(
            "Display Item:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelDisplayItem.Wrap(-1)
        sizerDisplayItem.Add(self.labelDisplayItem, 0, wx.ALL | wx.EXPAND, 5)

        listBoxDisplayItemsChoices = [_("Global Default"), _("Line Number"), _("Control Character"), _("Brace Light"), _("Brace Bad"), _("Comment Block"), _("Comment Line"), _("Number"), _("Double Quote String"), _("Single Quote String"), _("Keyword"), _(
            "Class Name"), _("Module Name"), _("Method Name"), _("Operator"), _("Normal Text"), _("Global Variable"), _("Instance Variable"), _("Class Variable"), _("Regular Expression"), _("Symbol"), _("Back Tick"), _("Data Section"), _("Error")]
        self.listBoxDisplayItems = wx.ListBox(
            self.panelFont, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxDisplayItemsChoices, wx.LB_SINGLE)
        sizerDisplayItem.Add(
            self.listBoxDisplayItems, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerSettings.Add(sizerDisplayItem, 45, wx.EXPAND, 5)

        sizerFontStyle = wx.BoxSizer(wx.VERTICAL)

        self.labelItemForeground = wx.StaticText(self.panelFont, wx.ID_ANY, _(
            "Item Foreground:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelItemForeground.Wrap(-1)
        sizerFontStyle.Add(self.labelItemForeground, 0, wx.ALL, 5)

        sizerForeground = wx.BoxSizer(wx.HORIZONTAL)

        self.panelForeColor = wx.Panel(
            self.panelFont, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        sizerForeground.Add(self.panelForeColor, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlForeColor = wx.TextCtrl(
            self.panelFont, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlForeColor.SetMaxLength(0)
        sizerForeground.Add(
            self.textCtrlForeColor, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.buttonForeColor = wx.Button(self.panelFont, wx.ID_ANY, _(
            "Choose..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerForeground.Add(
            self.buttonForeColor, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sizerFontStyle.Add(sizerForeground, 0, wx.EXPAND, 5)

        self.labelItemBackground = wx.StaticText(self.panelFont, wx.ID_ANY, _(
            "Item Background:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelItemBackground.Wrap(-1)
        sizerFontStyle.Add(self.labelItemBackground, 0, wx.ALL, 5)

        sizerBackground = wx.BoxSizer(wx.HORIZONTAL)

        self.panelBackColor = wx.Panel(
            self.panelFont, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        sizerBackground.Add(self.panelBackColor, 0, wx.EXPAND | wx.ALL, 5)

        self.textCtrlBackColor = wx.TextCtrl(
            self.panelFont, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlBackColor.SetMaxLength(0)
        sizerBackground.Add(
            self.textCtrlBackColor, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.buttonBackColor = wx.Button(self.panelFont, wx.ID_ANY, _(
            "Choose..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerBackground.Add(
            self.buttonBackColor, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sizerFontStyle.Add(sizerBackground, 0, wx.EXPAND, 5)

        sizerBoldItalic = wx.BoxSizer(wx.VERTICAL)

        self.labelItemStyle = wx.StaticText(self.panelFont, wx.ID_ANY, _(
            "Item Style:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelItemStyle.Wrap(-1)
        sizerBoldItalic.Add(self.labelItemStyle, 0, wx.ALL, 5)

        sizerStyleChecks = wx.BoxSizer(wx.HORIZONTAL)

        self.checkBoxBold = wx.CheckBox(
            self.panelFont, wx.ID_ANY, _("Bold"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerStyleChecks.Add(self.checkBoxBold, 1, wx.ALL, 5)

        self.checkBoxItalic = wx.CheckBox(
            self.panelFont, wx.ID_ANY, _("Italic"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerStyleChecks.Add(self.checkBoxItalic, 1, wx.ALL, 5)

        sizerBoldItalic.Add(sizerStyleChecks, 1, wx.EXPAND, 5)

        sizerFontStyle.Add(sizerBoldItalic, 0, wx.EXPAND, 5)

        sizerSettings.Add(sizerFontStyle, 55, wx.EXPAND, 5)

        sizerFontMain.Add(sizerSettings, 1, wx.EXPAND, 5)

        self.panelFont.SetSizer(sizerFontMain)
        self.panelFont.Layout()
        sizerFontMain.Fit(self.panelFont)
        self.noteBookSettings.AddPage(
            self.panelFont, _("Font Settings"), False)
        self.panelEditor = wx.Panel(
            self.noteBookSettings, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        panelEditorMainSizer = wx.BoxSizer(wx.HORIZONTAL)

        sizerEditor = wx.BoxSizer(wx.VERTICAL)

        self.labelTabWidth = wx.StaticText(self.panelEditor, wx.ID_ANY, _(
            "Tab Width:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelTabWidth.Wrap(-1)
        sizerEditor.Add(self.labelTabWidth, 0, wx.ALL, 5)

        self.spinCtrlTabWidth = wx.SpinCtrl(
            self.panelEditor, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS | wx.SP_WRAP, 1, 20, 2)
        sizerEditor.Add(
            self.spinCtrlTabWidth, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.labelEdgeColumn = wx.StaticText(self.panelEditor, wx.ID_ANY, _(
            "Edge Column:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelEdgeColumn.Wrap(-1)
        sizerEditor.Add(self.labelEdgeColumn, 0, wx.ALL, 5)

        self.spinCtrlEdgeColumn = wx.SpinCtrl(
            self.panelEditor, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 240, 80)
        sizerEditor.Add(
            self.spinCtrlEdgeColumn, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.checkBoxIndentGuides = wx.CheckBox(self.panelEditor, wx.ID_ANY, _(
            "Indent Guides"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.checkBoxIndentGuides.SetValue(True)
        sizerEditor.Add(self.checkBoxIndentGuides, 0, wx.ALL, 5)

        self.checkBoxCaret = wx.CheckBox(
            self.panelEditor, wx.ID_ANY, _("Caret"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.checkBoxCaret.SetValue(True)
        sizerEditor.Add(self.checkBoxCaret, 0, wx.ALL, 5)

        panelEditorMainSizer.Add(sizerEditor, 1, wx.EXPAND, 5)

        sizerCaret = wx.StaticBoxSizer(
            wx.StaticBox(self.panelEditor, wx.ID_ANY, _("Caret Settings")), wx.VERTICAL)

        self.labelCaretFore = wx.StaticText(sizerCaret.GetStaticBox(), wx.ID_ANY, _(
            "Forecolor:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelCaretFore.Wrap(-1)
        sizerCaret.Add(self.labelCaretFore, 0, wx.ALL, 5)

        sizerCaret1 = wx.BoxSizer(wx.HORIZONTAL)

        self.panelCaretFore = wx.Panel(sizerCaret.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        sizerCaret1.Add(
            self.panelCaretFore, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.textCtrlCaretFore = wx.TextCtrl(sizerCaret.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlCaretFore.SetMaxLength(0)
        sizerCaret1.Add(
            self.textCtrlCaretFore, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerCaret.Add(sizerCaret1, 0, wx.EXPAND, 5)

        sizerCaret2 = wx.BoxSizer(wx.VERTICAL)

        self.buttonCaretFore = wx.Button(sizerCaret.GetStaticBox(), wx.ID_ANY, _(
            "Choose..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerCaret2.Add(
            self.buttonCaretFore, 0, wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerCaret.Add(sizerCaret2, 0, wx.EXPAND, 5)

        self.labelCaretBack = wx.StaticText(sizerCaret.GetStaticBox(), wx.ID_ANY, _(
            "Background:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelCaretBack.Wrap(-1)
        sizerCaret.Add(self.labelCaretBack, 0, wx.ALL, 5)

        sizerCaret11 = wx.BoxSizer(wx.HORIZONTAL)

        self.panelCaretBack = wx.Panel(sizerCaret.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        sizerCaret11.Add(
            self.panelCaretBack, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.textCtrlCaretBack = wx.TextCtrl(sizerCaret.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.textCtrlCaretBack.SetMaxLength(0)
        sizerCaret11.Add(
            self.textCtrlCaretBack, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerCaret.Add(sizerCaret11, 1, wx.EXPAND, 5)

        sizerCaret21 = wx.BoxSizer(wx.VERTICAL)

        self.buttonCaretBack = wx.Button(sizerCaret.GetStaticBox(), wx.ID_ANY, _(
            "Choose..."), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerCaret21.Add(
            self.buttonCaretBack, 0, wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerCaret.Add(sizerCaret21, 0, wx.EXPAND, 5)

        sizerCaret3 = wx.BoxSizer(wx.HORIZONTAL)

        self.labelCaretAlpha = wx.StaticText(sizerCaret.GetStaticBox(), wx.ID_ANY, _(
            "Caret Alpha:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelCaretAlpha.Wrap(-1)
        sizerCaret3.Add(
            self.labelCaretAlpha, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.spinCtrlCaretAlpha = wx.SpinCtrl(sizerCaret.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 255, 40)
        sizerCaret3.Add(
            self.spinCtrlCaretAlpha, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        sizerCaret.Add(sizerCaret3, 0, wx.EXPAND, 5)

        panelEditorMainSizer.Add(sizerCaret, 1, wx.ALL, 5)

        self.panelEditor.SetSizer(panelEditorMainSizer)
        self.panelEditor.Layout()
        panelEditorMainSizer.Fit(self.panelEditor)
        self.noteBookSettings.AddPage(
            self.panelEditor, _("Editor Settings"), True)

        MainSizer.Add(self.noteBookSettings, 1, wx.EXPAND | wx.ALL, 5)

        bSizer673 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer674 = wx.BoxSizer(wx.VERTICAL)

        self.buttonDefault = wx.Button(
            self, wx.ID_ANY, _("Apply Default"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer674.Add(self.buttonDefault, 0, wx.ALL, 5)

        bSizer673.Add(bSizer674, 1, 0, 5)

        sizerOKCancel = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOK = wx.Button(
            self, wx.ID_ANY, _("OK"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonOK, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.buttonCancel = wx.Button(
            self, wx.ID_ANY, _("Cancel"), wx.DefaultPosition, wx.DefaultSize, 0)
        sizerOKCancel.Add(self.buttonCancel, 0, wx.ALL, 5)

        bSizer673.Add(sizerOKCancel, 0, wx.ALIGN_RIGHT | wx.ALIGN_BOTTOM, 5)

        MainSizer.Add(bSizer673, 0, wx.EXPAND, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.noteBookSettings.Bind(
            wx.EVT_NOTEBOOK_PAGE_CHANGED, self.noteBookSettings_PageChanged)
        self.comboBoxFont.Bind(
            wx.EVT_CHOICE, self.comboBoxFont_SelectionChanged)
        self.comboBoxSize.Bind(
            wx.EVT_CHOICE, self.comboBoxSize_SelectionChanged)
        self.listBoxDisplayItems.Bind(
            wx.EVT_LISTBOX, self.listBoxDisplayItems_SelectionChanged)
        self.textCtrlForeColor.Bind(
            wx.EVT_TEXT, self.textCtrlForeColor_TextChanged)
        self.buttonForeColor.Bind(wx.EVT_BUTTON, self.buttonForeColor_Clicked)
        self.textCtrlBackColor.Bind(
            wx.EVT_TEXT, self.textCtrlBackColor_TextChanged)
        self.buttonBackColor.Bind(wx.EVT_BUTTON, self.buttonBackColor_Clicked)
        self.checkBoxBold.Bind(wx.EVT_CHECKBOX, self.checkBoxBold_CheckChanged)
        self.checkBoxItalic.Bind(
            wx.EVT_CHECKBOX, self.checkBoxItalic_CheckChanged)
        self.spinCtrlTabWidth.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlTabWidth_ValueChanged)
        self.spinCtrlEdgeColumn.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlEdgeColumn_ValueChanged)
        self.checkBoxIndentGuides.Bind(
            wx.EVT_CHECKBOX, self.checkBoxIndentGuide_CheckChanged)
        self.checkBoxCaret.Bind(
            wx.EVT_CHECKBOX, self.checkBoxCaret_CheckChanged)
        self.textCtrlCaretFore.Bind(
            wx.EVT_TEXT, self.textCtrlCaretFore_TextChanged)
        self.buttonCaretFore.Bind(wx.EVT_BUTTON, self.buttonCaretFore_Clicked)
        self.textCtrlCaretBack.Bind(
            wx.EVT_TEXT, self.textCtrlCaretBack_TextChanged)
        self.buttonCaretBack.Bind(wx.EVT_BUTTON, self.buttonCaretBack_Clicked)
        self.spinCtrlCaretAlpha.Bind(
            wx.EVT_SPINCTRL, self.spinCtrlCaretAlpha_ValueChanged)
        self.buttonDefault.Bind(wx.EVT_BUTTON, self.buttonDefault_Clicked)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.buttonOK_Clicked)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.buttonCancel_Clicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def noteBookSettings_PageChanged(self, event):
        event.Skip()

    def comboBoxFont_SelectionChanged(self, event):
        event.Skip()

    def comboBoxSize_SelectionChanged(self, event):
        event.Skip()

    def listBoxDisplayItems_SelectionChanged(self, event):
        event.Skip()

    def textCtrlForeColor_TextChanged(self, event):
        event.Skip()

    def buttonForeColor_Clicked(self, event):
        event.Skip()

    def textCtrlBackColor_TextChanged(self, event):
        event.Skip()

    def buttonBackColor_Clicked(self, event):
        event.Skip()

    def checkBoxBold_CheckChanged(self, event):
        event.Skip()

    def checkBoxItalic_CheckChanged(self, event):
        event.Skip()

    def spinCtrlTabWidth_ValueChanged(self, event):
        event.Skip()

    def spinCtrlEdgeColumn_ValueChanged(self, event):
        event.Skip()

    def checkBoxIndentGuide_CheckChanged(self, event):
        event.Skip()

    def checkBoxCaret_CheckChanged(self, event):
        event.Skip()

    def textCtrlCaretFore_TextChanged(self, event):
        event.Skip()

    def buttonCaretFore_Clicked(self, event):
        event.Skip()

    def textCtrlCaretBack_TextChanged(self, event):
        event.Skip()

    def buttonCaretBack_Clicked(self, event):
        event.Skip()

    def spinCtrlCaretAlpha_ValueChanged(self, event):
        event.Skip()

    def buttonDefault_Clicked(self, event):
        event.Skip()

    def buttonOK_Clicked(self, event):
        event.Skip()

    def buttonCancel_Clicked(self, event):
        event.Skip()


###########################################################################
# Class MapManager_Panel_Template
###########################################################################

class MapManager_Panel_Template (wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                          size=wx.Size(-1, -1), style=wx.TAB_TRAVERSAL)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        addMapSizer = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("New Map")), wx.HORIZONTAL)

        self.addNameLabel = wx.StaticText(addMapSizer.GetStaticBox(), wx.ID_ANY, _(
            "Name"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.addNameLabel.Wrap(-1)
        addMapSizer.Add(self.addNameLabel, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.addMapNameCtrl = wx.TextCtrl(addMapSizer.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        addMapSizer.Add(self.addMapNameCtrl, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        self.addMapButton = wx.BitmapButton(addMapSizer.GetStaticBox(), wx.ID_ANY, wx.ArtProvider.GetBitmap(
            wx.ART_NEW,), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        addMapSizer.Add(self.addMapButton, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        MainSizer.Add(addMapSizer, 0, wx.EXPAND, 5)

        self.mapDataViewTree = wx.dataview.DataViewTreeCtrl(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        MainSizer.Add(self.mapDataViewTree, 1, wx.ALL | wx.EXPAND, 5)

        navSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.moveUpLevelButton = wx.BitmapButton(self, wx.ID_ANY, wx.ArtProvider.GetBitmap(
            wx.ART_GO_BACK,), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        navSizer.Add(self.moveUpLevelButton, 1, wx.ALL, 5)

        self.moveDownLevelButton = wx.BitmapButton(self, wx.ID_ANY, wx.ArtProvider.GetBitmap(
            wx.ART_GO_FORWARD,), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        navSizer.Add(self.moveDownLevelButton, 1, wx.ALL, 5)

        self.moveUpButton = wx.BitmapButton(self, wx.ID_ANY, wx.ArtProvider.GetBitmap(
            wx.ART_GO_UP,), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        navSizer.Add(self.moveUpButton, 1, wx.ALL, 5)

        self.moveDownButton = wx.BitmapButton(self, wx.ID_ANY, wx.ArtProvider.GetBitmap(
            wx.ART_GO_DOWN,), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        navSizer.Add(self.moveDownButton, 1, wx.ALL, 5)

        self.mapDeleteButton = wx.BitmapButton(self, wx.ID_ANY, wx.ArtProvider.GetBitmap(
            wx.ART_DELETE,), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        navSizer.Add(self.mapDeleteButton, 1, wx.ALL, 5)

        MainSizer.Add(navSizer, 0, wx.EXPAND, 5)

        mapPropertiesSizer = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, _("Properties")), wx.VERTICAL)

        mapNameSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.mapNameSizer = wx.StaticText(mapPropertiesSizer.GetStaticBox(), wx.ID_ANY, _(
            "Name"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.mapNameSizer.Wrap(-1)
        mapNameSizer1.Add(self.mapNameSizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.mapNameCtrl = wx.TextCtrl(mapPropertiesSizer.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        mapNameSizer1.Add(self.mapNameCtrl, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        mapPropertiesSizer.Add(mapNameSizer1, 0, wx.EXPAND, 5)

        mapTilesetSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.tilesetLabel = wx.StaticText(mapPropertiesSizer.GetStaticBox(), wx.ID_ANY, _(
            "Tileset"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.tilesetLabel.Wrap(-1)
        mapTilesetSizer.Add(self.tilesetLabel, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        tilesetChoiceBoxChoices = []
        self.tilesetChoiceBox = wx.Choice(mapPropertiesSizer.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, tilesetChoiceBoxChoices, 0)
        self.tilesetChoiceBox.SetSelection(0)
        mapTilesetSizer.Add(
            self.tilesetChoiceBox, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        mapPropertiesSizer.Add(mapTilesetSizer, 0, wx.EXPAND, 5)

        soundSizer = wx.StaticBoxSizer(wx.StaticBox(
            mapPropertiesSizer.GetStaticBox(), wx.ID_ANY, _("Auto Change Sound")), wx.VERTICAL)

        BGMSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.BGMCheckBox = wx.CheckBox(soundSizer.GetStaticBox(), wx.ID_ANY, _(
            "BGM"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.BGMCheckBox.SetMinSize(wx.Size(45, -1))

        BGMSizer.Add(self.BGMCheckBox, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        BGMChoiceBoxChoices = []
        self.BGMChoiceBox = wx.Choice(soundSizer.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, BGMChoiceBoxChoices, 0)
        self.BGMChoiceBox.SetSelection(0)
        self.BGMChoiceBox.Enable(False)

        BGMSizer.Add(self.BGMChoiceBox, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        self.playBGMButton = wx.BitmapButton(soundSizer.GetStaticBox(
        ), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        BGMSizer.Add(self.playBGMButton, 0, wx.ALIGN_CENTER | wx.LEFT, 5)

        soundSizer.Add(BGMSizer, 0, wx.EXPAND, 5)

        BGSSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.BGSCheckBox = wx.CheckBox(soundSizer.GetStaticBox(), wx.ID_ANY, _(
            "BGS"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.BGSCheckBox.SetMinSize(wx.Size(45, -1))

        BGSSizer.Add(self.BGSCheckBox, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        BGSChoiceBoxChoices = []
        self.BGSChoiceBox = wx.Choice(soundSizer.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, BGSChoiceBoxChoices, 0)
        self.BGSChoiceBox.SetSelection(0)
        self.BGSChoiceBox.Enable(False)

        BGSSizer.Add(self.BGSChoiceBox, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        self.playBGSButton = wx.BitmapButton(soundSizer.GetStaticBox(
        ), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        BGSSizer.Add(self.playBGSButton, 0, wx.ALIGN_CENTER | wx.LEFT, 5)

        soundSizer.Add(BGSSizer, 1, wx.EXPAND, 5)

        mapPropertiesSizer.Add(soundSizer, 0, wx.EXPAND, 5)

        encounterSizer = wx.StaticBoxSizer(wx.StaticBox(
            mapPropertiesSizer.GetStaticBox(), wx.ID_ANY, _("Encounters")), wx.VERTICAL)

        troopControllSizer = wx.BoxSizer(wx.HORIZONTAL)

        troopListBoxChoices = []
        self.troopListBox = wx.ListBox(encounterSizer.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, troopListBoxChoices, wx.LB_EXTENDED | wx.LB_MULTIPLE)
        troopControllSizer.Add(self.troopListBox, 1, wx.ALL | wx.EXPAND, 5)

        troopAddRemoveSizer = wx.BoxSizer(wx.VERTICAL)

        self.troopAddButton = wx.Button(encounterSizer.GetStaticBox(), wx.ID_ANY, _(
            "+"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.troopAddButton.SetMinSize(wx.Size(25, -1))

        troopAddRemoveSizer.Add(
            self.troopAddButton, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.troopRemoveButton = wx.Button(encounterSizer.GetStaticBox(), wx.ID_ANY, _(
            "-"), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
        self.troopRemoveButton.SetMinSize(wx.Size(25, -1))

        troopAddRemoveSizer.Add(
            self.troopRemoveButton, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.troopUpButton = wx.Button(encounterSizer.GetStaticBox(), wx.ID_ANY, _(
            "▲"), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
        self.troopUpButton.SetMinSize(wx.Size(25, -1))

        troopAddRemoveSizer.Add(
            self.troopUpButton, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.troopDownButton = wx.Button(encounterSizer.GetStaticBox(), wx.ID_ANY, _(
            "▼"), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
        self.troopDownButton.SetMinSize(wx.Size(25, -1))

        troopAddRemoveSizer.Add(
            self.troopDownButton, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        troopControllSizer.Add(troopAddRemoveSizer, 0, wx.EXPAND, 5)

        encounterSizer.Add(troopControllSizer, 1, wx.EXPAND, 5)

        encounterRateSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.troopStepsLabel = wx.StaticText(encounterSizer.GetStaticBox(), wx.ID_ANY, _(
            "Steps Average:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.troopStepsLabel.Wrap(-1)
        encounterRateSizer.Add(
            self.troopStepsLabel, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.troopStepsSpinner = wx.SpinCtrl(encounterSizer.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
        encounterRateSizer.Add(
            self.troopStepsSpinner, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        encounterSizer.Add(encounterRateSizer, 0, wx.EXPAND, 5)

        mapPropertiesSizer.Add(encounterSizer, 1, wx.EXPAND, 5)

        MainSizer.Add(mapPropertiesSizer, 1, wx.EXPAND, 5)

        self.SetSizer(MainSizer)
        self.Layout()
        MainSizer.Fit(self)

        # Connect Events
        self.addMapNameCtrl.Bind(wx.EVT_TEXT_ENTER, self.onNewMapCreate)
        self.addMapButton.Bind(wx.EVT_BUTTON, self.onNewMapCreate)
        self.moveUpLevelButton.Bind(wx.EVT_BUTTON, self.onUpLevelButtonClicked)
        self.moveDownLevelButton.Bind(
            wx.EVT_BUTTON, self.onDownLevelButtonClicked)
        self.moveUpButton.Bind(wx.EVT_BUTTON, self.onUpButtonClicked)
        self.moveDownButton.Bind(wx.EVT_BUTTON, self.onDownButtonClicked)
        self.mapDeleteButton.Bind(wx.EVT_BUTTON, self.onDeleteButtonClicked)
        self.mapNameCtrl.Bind(wx.EVT_TEXT, self.onMapNameChangeText)
        self.mapNameCtrl.Bind(wx.EVT_TEXT_ENTER, self.onMapNameChangeEnter)
        self.tilesetChoiceBox.Bind(
            wx.EVT_CHOICE, self.onMapTilesetSelectionChanged)
        self.BGMCheckBox.Bind(wx.EVT_CHECKBOX, self.onMapBGMCheckBox)
        self.BGMChoiceBox.Bind(wx.EVT_CHOICE, self.onMapBGMChoice)
        self.BGMChoiceBox.Bind(
            wx.EVT_LEFT_DCLICK, self.onMapBGMChoiceLeftDClick)
        self.playBGMButton.Bind(wx.EVT_BUTTON, self.onMapBGMPlayButtonClick)
        self.BGSCheckBox.Bind(wx.EVT_CHECKBOX, self.onMapBGSCheckBox)
        self.BGSChoiceBox.Bind(wx.EVT_CHOICE, self.onMapBGSChoice)
        self.BGSChoiceBox.Bind(
            wx.EVT_LEFT_DCLICK, self.onMapBGSChoiceLeftDClick)
        self.playBGSButton.Bind(wx.EVT_BUTTON, self.onMapBGSPlayButtonClick)
        self.troopListBox.Bind(wx.EVT_LISTBOX, self.onTroopSelectionChanged)
        self.troopListBox.Bind(wx.EVT_LISTBOX_DCLICK, self.onTroopDClick)
        self.troopAddButton.Bind(wx.EVT_BUTTON, self.onTroopAddButtonClick)
        self.troopRemoveButton.Bind(
            wx.EVT_BUTTON, self.onTroopRemoveButtonClick)
        self.troopUpButton.Bind(wx.EVT_BUTTON, self.onTroopUpButtonClick)
        self.troopDownButton.Bind(wx.EVT_BUTTON, self.onTroopDownButtonClick)
        self.troopStepsSpinner.Bind(
            wx.EVT_SPINCTRL, self.onEncounterStepsChanged)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onNewMapCreate(self, event):
        event.Skip()

    def onUpLevelButtonClicked(self, event):
        event.Skip()

    def onDownLevelButtonClicked(self, event):
        event.Skip()

    def onUpButtonClicked(self, event):
        event.Skip()

    def onDownButtonClicked(self, event):
        event.Skip()

    def onDeleteButtonClicked(self, event):
        event.Skip()

    def onMapNameChangeText(self, event):
        event.Skip()

    def onMapNameChangeEnter(self, event):
        event.Skip()

    def onMapTilesetSelectionChanged(self, event):
        event.Skip()

    def onMapBGMCheckBox(self, event):
        event.Skip()

    def onMapBGMChoice(self, event):
        event.Skip()

    def onMapBGMChoiceLeftDClick(self, event):
        event.Skip()

    def onMapBGMPlayButtonClick(self, event):
        event.Skip()

    def onMapBGSCheckBox(self, event):
        event.Skip()

    def onMapBGSChoice(self, event):
        event.Skip()

    def onMapBGSChoiceLeftDClick(self, event):
        event.Skip()

    def onMapBGSPlayButtonClick(self, event):
        event.Skip()

    def onTroopSelectionChanged(self, event):
        event.Skip()

    def onTroopDClick(self, event):
        event.Skip()

    def onTroopAddButtonClick(self, event):
        event.Skip()

    def onTroopRemoveButtonClick(self, event):
        event.Skip()

    def onTroopUpButtonClick(self, event):
        event.Skip()

    def onTroopDownButtonClick(self, event):
        event.Skip()

    def onEncounterStepsChanged(self, event):
        event.Skip()
