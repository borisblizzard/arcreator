import wx
import numpy as np

import Kernel

from PyitectConsumes import PanelBase, Actors_Panel_Template, ExpGrid_Dialog, GenerateCurve_Dialog, AddParameter_Dialog
from PyitectConsumes import DatabaseManager as DM
from PyitectConsumes import RGSS1_RPG as RPG

from .GraphColors import GRAPH_COLORS

# --------------------------------------------------------------------------------------
# Actors_Panel
# --------------------------------------------------------------------------------------


class Actors_Panel(Actors_Panel_Template, PanelBase):

    _arc_panel_info_string = "Name Caption Center CloseB CaptionV DestroyOC Floatable Float IconARCM MaximizeB MinimizeM MinimizeB Movable NotebookD  Resizable Snappable"
    _arc_panel_info_data = {"Name": "Actors Panel", "Caption": "Actors Panel", "CaptionV": True, "MinimizeM": ["POS_SMART", "CAPT_SMART", ],
                            "MinimizeB": True, "CloseB": True, 'IconARCM': 'actorsicon'}

    def __init__(self, parent, actorIndex=0):
        """Basic constructor for the Actors panel"""
        Actors_Panel_Template.__init__(self, parent)

        config = Kernel.Config.getUnified()

        # Set font for the note control
        font = wx.Font(8, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        if "Misc" in config and "NoteFont" in config["Misc"]:
            font.SetFaceName(str(config['Misc']['NoteFont']))
        self.textCtrlNotes.SetFont(font)
        self.ParamTab = 0

        # Set the ranges for initial and final level spin controls
        ma = 999
        if "DatabaseLimits" in config and "ActorLevel" in config["DatabaseLimits"]:
            ma = int(config['DatabaseLimits']['ActorLevel'])

        self.spinCtrlInitialLevel.SetRange(1, ma)
        self.spinCtrlFinalLevel.SetRange(1, ma)
        self.spinCtrlLevel.SetRange(1, ma)
        self.glCanvasCharacter.canvas.Bind(wx.EVT_LEFT_DCLICK, Kernel.Protect(self.glCanvasCharacter_DoubleClick))
        self.glCanvasBattler.canvas.Bind(wx.EVT_LEFT_DCLICK, Kernel.Protect(self.glCanvasBattler_DoubleClick))
        self.parameterGraph.canvas.Bind(wx.EVT_LEFT_DCLICK, Kernel.Protect(self.parameterGraph_DoubleClicked))

        actors = Kernel.GlobalObjects['PROJECT'].getData('Actors')
        # Initialize the selected actor attribute
        if actorIndex >= len(actors):
            actorIndex = 0
        self.SelectedActor = actors[DM.FixedIndex(actorIndex)]

        # Create the controls for the equipment and set the values for all the
        # controls
        self.CreateEquipmentControls()
        params = []
        if "GameSetup" in config and "Parameters" in config["GameSetup"]:
            params = list(config['GameSetup']['Parameters'])
        for param in params:
            self.AddParameterPage(param)

        self.noteBookActorParameters.ChangeSelection(0)
        self.comboBoxExpCurve.SetCursor(wx.STANDARD_CURSOR)

        DM.DrawHeaderBitmap(self.bitmapActors, 'Actors')
        self.refreshAll()

        # Set the initial selection of the list control
        self.listBoxActors.SetSelection(actorIndex)
        # Bind the panel to the Panel Manager
        self.bindPanelManager()

    def AddParameterPage(self, title, activate=False):
        """Creates a page and adds it to the notebook control"""
        page = wx.Panel(self.noteBookActorParameters)
        self.noteBookActorParameters.AddPage(page, title)
        index = self.noteBookActorParameters.GetPageCount() - 1
        maxlevel = int(Kernel.Config.getUnified()['DatabaseLimits']['ActorLevel'])
        actors = Kernel.GlobalObjects['PROJECT'].getData('Actors')
        for actor in actors:
            if actor is None:
                actor = RPG.Actor()
            actor.parameters.resize(index + 1, maxlevel + 1)
            for j in range(1, maxlevel):
                actor.parameters[index, j] = 50 + 5 * j
        if activate:
            self.noteBookActorParameters.SetSelection(index)

    def CreateEquipmentControls(self):
        """Creates the controls for each equipment type defined in the configuration"""
        if DM.ARC_FORMAT:
            equipment = list(Kernel.Config.getUnified()['GameSetup']['WeaponSlots'])
            equipment.extend(list(Kernel.Config.getUnified()['GameSetup']['ArmorSlots']))
        else:
            equipment = [
                'Weapon', 'Shield', 'Helmet', 'Body Armor', 'Accessory']
        sizerEquipment = wx.BoxSizer(wx.VERTICAL)
        self.EquipmentBoxes = []
        self.FixedCheckBoxes = []
        for i in range(len(equipment)):
            sizer = wx.BoxSizer(wx.HORIZONTAL)
            label = wx.StaticText(self.scrolledWindowEquipment, wx.ID_ANY,
                                  equipment[i], wx.DefaultPosition, wx.Size(80, -1), wx.ALIGN_LEFT)
            label.Wrap(-1)
            sizer.Add(label, 0, wx.TOP | wx.LEFT | wx.RIGHT, 5)
            comboBox = wx.Choice(self.scrolledWindowEquipment, wx.ID_ANY,
                                 wx.DefaultPosition, wx.DefaultSize, [], 0)
            comboBox.SetDoubleBuffered(True)
            comboBox.Bind(wx.EVT_CHOICE,
                          Kernel.Protect(self.comboBoxEquipment_SelectionChanged))
            comboBox.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
            self.EquipmentBoxes.append(comboBox)
            sizer.Add(comboBox, 1, wx.RIGHT | wx.LEFT, 5)
            checkBox = wx.CheckBox(self.scrolledWindowEquipment, wx.ID_ANY, "Fixed",
                                   wx.DefaultPosition, wx.DefaultSize, 0)
            checkBox.Bind(wx.EVT_CHECKBOX,
                          Kernel.Protect(self.checkBoxFixedEquipment_CheckChanged))
            checkBox.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
            self.FixedCheckBoxes.append(checkBox)
            sizer.Add(checkBox, 0, wx.ALL, 5)
            sizerEquipment.Add(sizer, 1, wx.EXPAND, 5)
        self.scrolledWindowEquipment.SetSizer(sizerEquipment)
        self.scrolledWindowEquipment.Layout()
        sizerEquipment.Fit(self.scrolledWindowEquipment)
        self.scrolledWindowEquipment.SetDoubleBuffered(True)

    def refreshActorList(self):
        """Refreshes the values in the actor wxListBox control"""
        config = Kernel.Config.getUnified()
        digits = 4
        if "GameObjects" in config and "Actors" in config["GameObjects"]:
            digits = len(str(int(config['GameObjects']['Actors'])))
        actors = Kernel.GlobalObjects['PROJECT'].getData('Actors')
        DM.FillControl(self.listBoxActors, actors, digits, [])

    def refreshClasses(self):
        """Refreshes the values in the class wxChoice control"""
        config = Kernel.Config.getUnified()
        digits = 4
        if "GameObjects" in config and "Classes" in config["GameObjects"]:
            digits = len(str(int(config['GameObjects']['Classes'])))
        classes = Kernel.GlobalObjects['PROJECT'].getData('Classes')
        DM.FillControl(self.comboBoxClass, classes, digits, [])

    def refreshWeapons(self):
        """Sets the weapon combobox(s) data determined by the actor's class"""
        digits = 4
        weaponSlots = 1

        config = Kernel.Config.getUnified()
        if "GameSetup" in config and 'WeaponSlots' in config["GameSetup"]:
            weaponSlots = len(list(config['GameSetup']['WeaponSlots']))
        if "GameObjects" in config and "Weapons" in config["GameObjects"]:
            digits = len(str(int(config['GameObjects']['Weapons'])))

        weapons = Kernel.GlobalObjects['PROJECT'].getDataCopy('Weapons')

        for i in range(weaponSlots):
            items = ['(None)']
            ids = self.GetWeaponIDs()
            for id in ids:
                if weapons[id] is None:
                    weapons[id] = RPG.Weapon()
            items.extend(
                [''.join([str(weapons[id].id).zfill(digits), ': ',
                          weapons[id].name]) for id in ids])
            self.EquipmentBoxes[i].Clear()
            self.EquipmentBoxes[i].AppendItems(items)
            if DM.ARC_FORMAT:
                # TODO: Implement multiple weapon equip
                pass
            else:
                id, index = self.SelectedActor.weapon_id, 0
                if id != 0:
                    try:
                        index = self.GetWeaponIDs().index(id) + 1
                    except ValueError:
                        self.SelectedActor.weapon_id = 0
                self.EquipmentBoxes[0].SetSelection(index)

    def refreshArmors(self):
        """Sets the armor combo box data determined by the actor's class"""
        digits = 4
        weaponSlots = 1
        cypher = [0, 1, 2, 3, 3, 3]
        kinds = {}

        config = Kernel.Config.getUnified()
        if "GameSetup" in config and "WeaponSlots" in config["GameSetup"]:
            weaponSlots = len(list(config['GameSetup']['WeaponSlots']))
        if "GameObjects" in config and "Armors" in config["GameObjects"]:
            digits = len(str(int(config['GameObjects']['Armors'])))
        if "GameSetup" in config and "ArmorSlotKinds" in config["GameSetup"]:
            cypher = [int(k) for k in list(config['GameSetup']['ArmorSlotKinds'])]

        armors = Kernel.GlobalObjects['PROJECT'].getDataCopy('Armors')

        for k in list(Kernel.Config.getUnified()['GameSetup']['ArmorSlotKinds']):
            key = int(k)
            if key not in kinds:
                values = ['(None)']
                ids = self.GetArmorIDs(key)
                for id in ids:
                    if armors[id] is None:
                        armors[id] = RPG.Weapon()
                values.extend(
                    [''.join([str(id).zfill(digits), ': ',
                              armors[id].name]) for id in ids])
                kinds[key] = values

        for i in range(weaponSlots, len(self.EquipmentBoxes)):
            kind = cypher[i - weaponSlots]
            items = kinds[kind]
            self.EquipmentBoxes[i].Clear()
            self.EquipmentBoxes[i].AppendItems(items)
            index = 0
            exec(
                ''.join(['id = self.SelectedActor.armor', str(i + 1 - weaponSlots), '_id']))
            if id != 0:
                try:
                    index = self.GetArmorIDs(kind).index(id) + 1
                except ValueError:
                    # If the class changes, the index() method no longer works
                    index = 0
                    exec(
                        ''.join(['self.SelectedActor.armor', str(i + 1 - weaponSlots), '_id = 0']))
            self.EquipmentBoxes[i].SetSelection(index)

    def refreshParameters(self):
        """Refreshes the data values on the control"""
        actor = self.SelectedActor
        self.textCtrlName.ChangeValue(actor.name)
        self.comboBoxClass.Select(actor.class_id - 1)
        basis = str(actor.exp_basis)
        inflation = str(actor.exp_inflation)
        text = 'Basis: ' + basis + ', Inflation: ' + inflation
        self.comboBoxExpCurve.SetValue(text)
        self.spinCtrlLevel.SetRange(1, actor.final_level)
        self.refreshValues()
        self.spinCtrlLevel.SetValue(actor.initial_level)
        self.spinCtrlFinalLevel.SetValue(actor.final_level)
        self.spinCtrlInitialLevel.SetRange(1, actor.final_level)

    def refreshFixedEquipment(self):
        if DM.ARC_FORMAT:
            # TODO: Implement
            pass
        else:
            actor = self.SelectedActor
            self.FixedCheckBoxes[0].SetValue(actor.weapon_fix)
            self.FixedCheckBoxes[1].SetValue(actor.armor1_fix)
            self.FixedCheckBoxes[2].SetValue(actor.armor2_fix)
            self.FixedCheckBoxes[3].SetValue(actor.armor3_fix)
            self.FixedCheckBoxes[4].SetValue(actor.armor4_fix)

    def refreshGraphics(self):
        """Refreshes the character and battler graphic for the actor"""
        DM.RenderImage(self.glCanvasCharacter, self.SelectedActor.character_name,
                       self.SelectedActor.character_hue, 'character')
        DM.RenderImage(self.glCanvasBattler, self.SelectedActor.battler_name,
                       self.SelectedActor.battler_hue, 'battler')

    def refreshValues(self, level=None):
        """Applies the limits defined for the selected parameter, and updates the value"""
        if level is None:
            level = self.spinCtrlLevel.GetValue()
        self.spinCtrlValue.SetValue(
            self.GetParameterValue(self.ParamTab, level))
        self.spinCtrlValue.SetRange(1, self.GetValueMax(self.ParamTab))
        if not hasattr(self.SelectedActor, 'note'):
            setattr(self.SelectedActor, 'note', '')
        self.textCtrlNotes.ChangeValue(self.SelectedActor.note)

    def refreshGraph(self):
        """Refreshes the graph to reflect the selected actor' values"""
        name = self.noteBookActorParameters.GetPageText(self.ParamTab)
        color = GRAPH_COLORS[self.ParamTab % len(GRAPH_COLORS)]
        maxValue = None
        if not self.checkBoxScaled.GetValue():
            maxValue = self.GetValueMax(self.ParamTab)
        self.parameterGraph.SetData(self.GetParameterData(), name, color,
                                    maxvalue=maxValue, maxlevel=self.SelectedActor.final_level,
                                    minlevel=self.SelectedActor.initial_level)

    def refreshAll(self):
        """Refreshes all the controls that contain game object values"""
        self.refreshActorList()
        self.refreshClasses()
        self.refreshWeapons()
        self.refreshArmors()
        self.refreshFixedEquipment()
        self.refreshParameters()
        self.refreshGraphics()
        self.refreshGraph()

    def listBoxActors_SelectionChanged(self, event):
        """Changes the data on the panel to reflect the values of the selected actor"""
        index = DM.FixedIndex(event.GetSelection())
        actors = Kernel.GlobalObjects['PROJECT'].getData('Actors')
        if actors[index] is None:
            actors[index] = RPG.Actor()
        self.SelectedActor = actors[index]
        self.refreshWeapons()
        self.refreshArmors()
        self.refreshFixedEquipment()
        self.refreshParameters()
        self.refreshGraphics()

    def SetParameterValue(self, param, level, value):
        """Sets the newly defined value for the selected actor's parameter"""
        self.SelectedActor.parameters[param, level] = value

    def GetParameterValue(self, index, level):
        """Retrieves the value of the current actor's selected parameter for the defined level"""
        if self.SelectedActor.parameters.xsize <= index or self.SelectedActor.parameters.ysize < level:
            maxlevel = 999
            config = Kernel.Config.getUnified()
            if "DatabaseLimits" in config and "ActorLevel" in config["DatabaseLimits"]:
                maxlevel = int(config['DatabaseLimits']['ActorLevel'])
            actors = Kernel.GlobalObjects['PROJECT'].getData('Actors')
            for actor in actors:
                if actor is None:
                    actor = RPG.Actor()
                actor.parameters.resize(index + 1, maxlevel + 1)
                for j in range(1, maxlevel):
                    actor.parameters[index, j] = 50 + 5 * j
        return self.SelectedActor.parameters[index, level]

    def buttonMaximum_Clicked(self, event):
        """Starts the Change Maximum dialog"""
        config = Kernel.Config.getUnified()
        ma = 9999
        if "GameObjects" in config and "Actors" in config["GameObjects"]:
            ma = int(Kernel.Config.getUnified()['GameObjects']['Actors'])
        actors = Kernel.GlobalObjects['PROJECT'].getData('Actors')
        DM.ChangeDataCapacity(self, self.listBoxActors, actors, ma)

    def textBoxName_TextChanged(self, event):
        """updates the selected actor's name"""
        DM.updateObjectName(self.SelectedActor, event.GetString(),
                            self.listBoxActors, len(Kernel.Config.getUnified()['GameObjects']['Actors']))

    def comboBoxClass_SelectionChanged(self, event):
        """updates the actor's class ID and refreshes the equipment allowed by the class"""
        self.SelectedActor.class_id = DM.FixedIndex(
            self.comboBoxClass.GetSelection())
        self.refreshWeapons()
        self.refreshArmors()

    def spinCtrlInitialLevel_ValueChanged(self, event):
        """Sets the selected actor's initial level to the value of the wxSpinCtrl"""
        self.spinCtrlInitialLevel.SetRange(
            1, self.spinCtrlFinalLevel.GetValue())
        self.SelectedActor.initial_level = self.spinCtrlInitialLevel.GetValue()
        self.refreshGraph()

    def spinCtrlFinalLevel_ValueChanged(self, event):
        """Sets the selected actor's final level to the value of the wxSpinCtrl"""
        final = event.GetInt()
        self.spinCtrlInitialLevel.SetRange(1, final)
        self.spinCtrlLevel.SetRange(1, final)
        self.SelectedActor.final_level = final
        self.refreshGraph()

    def comboBoxExperience_Click(self, event):
        """Opens window to generate experience tables"""

        actor = self.SelectedActor
        dlg = ExpGrid_Dialog(self, actor)
        if dlg.ShowModal() == wx.ID_OK:
            # TODO: Fix 'actor' which errors out. Pass the instance to window
            actor.exp_basis = dlg.spinCtrlBasis.GetValue()
            actor.exp_inflation = dlg.spinCtrlInflation.GetValue()
        dlg.Destroy()
        self.refreshParameters()

    def glCanvasCharacter_DoubleClick(self, event):
        """Opens dialog to change the character graphic"""
        result = DM.ChooseGraphic(
            self, 'Characters', self.SelectedActor.character_name, self.SelectedActor.character_hue)
        if result:
            filename, hue = result
            if filename is not None and hue is not None:
                self.SelectedActor.character_name = filename
                self.SelectedActor.character_hue = hue
                self.refreshGraphics()

    def glCanvasBattler_DoubleClick(self, event):
        """Opens dialog to change the battler graphic"""
        result = DM.ChooseGraphic(
            self, 'Battlers', self.SelectedActor.battler_name, self.SelectedActor.battler_hue)
        if result:
            filename, hue = result
            if filename is not None and hue is not None:
                self.SelectedActor.battler_name = filename
                self.SelectedActor.battler_hue = hue
                self.refreshGraphics()

    def comboBoxEquipment_SelectionChanged(self, event):
        """updates the weapon/armor id for the selected type for the actor"""
        ctrlIndex = self.EquipmentBoxes.index(event.GetEventObject())
        if DM.ARC_FORMAT:
            weaponSlots = len(list(Kernel.Config.getUnified()['GameSetup']['WeaponSlots']))
        else:
            weaponSlots = 1
        selection = event.GetInt()
        if ctrlIndex == 0:
            # Weapon Changed
            if DM.ARC_FORMAT:
                # TODO: Implement multiple weapon slots
                pass
            else:
                if selection == 0:
                    self.SelectedActor.weapon_id = 0
                else:
                    self.SelectedActor.weapon_id = self.GetWeaponIDs()[
                        selection - 1]
        else:
            # Armor Changed
            if selection == 0:
                exec(
                    ''.join(['self.SelectedActor.armor', str(ctrlIndex), '_id = 0']))
            else:
                kinds = list(Kernel.Config.getUnified()['GameSetup']['ArmorSlotKinds'])
                kind = int(kinds[ctrlIndex - weaponSlots])
                exec(''.join(['self.SelectedActor.armor', str(ctrlIndex), '_id = ',
                              str(self.GetArmorIDs(kind)[selection - 1])]))

    def checkBoxFixedEquipment_CheckChanged(self, event):
        """updates the "fixed" states for the selected actor's equipment"""
        ctrlIndex = self.FixedCheckBoxes.index(event.GetEventObject())
        if DM.ARC_FORMAT:
            # TODO: Implement
            weaponSlots = len(list(Kernel.Config.getUnified()['GameSetup']['WeaponSlots']))
            if ctrlIndex < weaponSlots:
                pass
            else:
                pass
        else:  # RMXP
            if ctrlIndex == 0:
                self.SelectedActor.weapon_fix = event.Checked()
            else:
                exec(''.join(['self.SelectedActor.armor', str(ctrlIndex),
                              '_fix = event.Checked()']))

    def spinCtrlParamLevel_ValueChanged(self, event):
        """update the controls on each page when the level is changed"""
        self.refreshValues(self.spinCtrlLevel.GetValue())

    def GetValueMax(self, param_index):
        """Returns the max value for the parameter type"""
        if param_index == 0:
            return int(Kernel.Config.getUnified()['DatabaseLimits']['ActorHP'])
        elif param_index == 1:
            return int(Kernel.Config.getUnified()['DatabaseLimits']['ActorSP'])
        else:
            return int(Kernel.Config.getUnified()['DatabaseLimits']['ActorParameter'])

    def spinCtrlValue_ValueChanged(self, event):
        """updates the actors parameter table with the value"""
        self.SetParameterValue(
            self.ParamTab, self.spinCtrlLevel.GetValue(), self.spinCtrlValue.GetValue())
        self.refreshGraph()

    def buttonGenerateCurve_Clicked(self, event):
        """Create the parameter curve dialog, using the passed index to determine the parameter"""

        actor, i = self.SelectedActor, self.ParamTab
        vRange = (
            actor.parameters[i, 1], actor.parameters[i, actor.final_level])
        lRange = (actor.initial_level, actor.final_level)
        max = self.GetValueMax(i)
        dlg = GenerateCurve_Dialog(self, vRange, lRange, max)
        if dlg.ShowModal() == wx.ID_OK:
            curve = dlg.GenerateCurve()
            for j in range(len(curve)):
                lvl = j + actor.initial_level
                actor.parameters[i, j] = curve[j]
            self.refreshGraph()
        dlg.Destroy()

    def noteBookParameters_PageChanged(self, event):
        """Sets the index of the page when the tab is traversed"""
        self.ParamTab = event.GetSelection()
        if not DM.ARC_FORMAT:
            self.buttonRemoveParameter.Enabled = (self.ParamTab > 5)
        else:
            self.buttonRemoveParameter.Enabled = self.noteBookActorParameters.GetPageCount >= 1
        self.refreshGraph()
        self.refreshValues()

    def GetParameterData(self):
        """Returns the parameter data in a format fit to graph"""
        params = self.SelectedActor.parameters
        x = np.arange(1, self.SelectedActor.final_level + 1, dtype=int)
        y = [params[self.ParamTab, i] for i in x]
        return np.column_stack((x, y))

    def checkBoxScaled_CheckChanged(self, event):
        """Refreshes the graph after changing state"""
        self.refreshGraph()

    def buttonQuickA_Clicked(self, event):
        """Generates a quick curve setting within a range"""
        self.GenerateQuickCurve(0.75)

    def buttonQuickB_Clicked(self, event):
        """Generates a quick curve setting within a range"""
        self.GenerateQuickCurve(0.65)

    def buttonQuickC_Clicked(self, event):
        """Generates a quick curve setting within a range"""
        self.GenerateQuickCurve(0.55)

    def buttonQuickD_Clicked(self, event):
        """Generates a quick curve setting within a range"""
        self.GenerateQuickCurve(0.45)

    def buttonQuickE_Clicked(self, event):
        """Generates a quick curve setting within a range"""
        self.GenerateQuickCurve(0.35)

    def GenerateQuickCurve(self, percent):
        """Generates a quick random curve, ensuring it falls within a range"""
        from random import randint
        actor, index = self.SelectedActor, self.ParamTab
        limit = self.GetValueMax(index)
        max, mod = int(limit * percent), int(limit * 0.05)
        upper, min = randint(max - mod, max + mod), max / 10
        mod /= 10
        lower = randint(min - mod, min + mod)
        init, final = actor.initial_level, actor.final_level
        for i in np.arange(init, final + 1, dtype=int):
            actor.parameters[index, i] = int(DM.CalculateParameter(lower,
                                                                   upper, 0, i, init, final))
        self.refreshGraph()

    def parameterGraph_DoubleClicked(self, event):
        """Opens the larger graph panel for interactive editing"""
        from .ParameterGraph_Panel import ParameterGraph_Panel
        tabs, data = [], self.SelectedActor.parameters
        for i in range(2, self.noteBookActorParameters.GetPageCount()):
            tabs.append(self.noteBookActorParameters.GetPageText(i))
        dlg = wx.Dialog(self, title='Parameter Growth', size=(640, 480),
                        style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        dlgSizer = wx.BoxSizer(wx.VERTICAL)
        panel = ParameterGraph_Panel(dlg, self.SelectedActor, tabs,
                                     self.ParamTab, self.checkBoxScaled.GetValue())
        dlgSizer.Add(panel, 1, wx.EXPAND, 5)
        dlg.SetSizer(dlgSizer)
        dlg.Layout()
        dlg.Centre(wx.BOTH)
        if dlg.ShowModal() == wx.ID_OK:
            self.refreshGraph()

    def buttonAddParameter_Clicked(self, event):
        """Opens dialog for the user to create a custom parameter"""

        dialog = AddParameter_Dialog(self)
        if (dialog.ShowModal() == wx.ID_OK):
            paramName = dialog.textCtrlParameterName.GetLineText(0)
            self.AddParameterPage(paramName)

    def buttonRemoveParameter_Clicked(self, event):
        """Removes the selected page from the tab control and resizes the actors' parameter tables"""
        params = self.SelectedActor.parameters
        for i in range(self.ParamTab, params.xsize - 1):
            params[i, :] = params[i + 1, :]
        params.resize(
            params.xsize - 1, int(Kernel.Config.getUnified()['DatabaseLimits']['ActorLevel']) + 1)
        try:
            self.noteBookActorParameters.RemovePage(self.ParamTab)
        except wx.PyAssertionError:
            # There is a strange bug with wx on Windows that raises this exception when
            # a page is deleted. Removing the page works fine, but it throws the
            # exception regardless, so this little empty catch is required...
            # :P
            pass
        if self.ParamTab >= self.noteBookActorParameters.GetPageCount():
            self.ParamTab -= 1
        self.noteBookActorParameters.SetSelection(self.ParamTab)

    def textCtrlNotes_TextChanged(self, event):
        """updates the notes for the selected actor"""
        self.SelectedActor.note = event.GetString()

    def GetWeaponIDs(self):
        """Returns the ID of the weapon found at index in the actor's weapon set"""
        classes = Kernel.GlobalObjects['PROJECT'].getData('Classes')
        return classes[self.SelectedActor.class_id].weapon_set

    def GetArmorIDs(self, kind):
        """Returns all actor armor IDs that are of type 'kind'"""
        classes = Kernel.GlobalObjects['PROJECT'].getData('Classes')
        armors = Kernel.GlobalObjects['PROJECT'].getData('Armors')
        ids = classes[self.SelectedActor.class_id].armor_set
        filtered = []
        for id in ids:
            if armors[id].kind == kind:
                filtered.append(id)
        return filtered
