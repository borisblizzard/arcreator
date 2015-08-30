import wx

import welder_kernel as kernel
from PyitectConsumes import PanelBase, Armors_Panel_Template
from PyitectConsumes import DatabaseManager as DM
from PyitectConsumes import RPG_RGSS1 as RPG

# --------------------------------------------------------------------------------------
# Armors_Panel
# --------------------------------------------------------------------------------------


class Armors_Panel(Armors_Panel_Template, PanelBase):

    _arc_panel_info = {
        "Name": "ArmorsPanel",
        "Caption": "Armors",
        "CaptionV": True,
        "Center": None,
        "CloseB": True,
        "DestroyOC": True,
        "Floatable": True,
        "IconARCM": 'armors',
        "MaximizeB": True,
        "MinimizeB": True,
        "MinimizeM": ["POS_SMART", "CAPT_SMART"],
        "Movable": True,
        "NotebookD": True,
        "Resizable": True,
        "Snappable": True
    }

    def __init__(self, parent, armor_index=0):
        """Basic constructor for the Armors panel"""
        Armors_Panel_Template.__init__(self, parent)

        global Config, DataArmors, DataStates, DataElements
        
        try:
            proj = kernel.GlobalObjects['PROJECT']
            DataArmors = proj.getData('Armors')
            DataStates = proj.getData('States')
            DataElements = proj.getData('System').elements
        except NameError:
            kernel.Log(
                'Database opened before Project has been initialized', '[Database:ARMORS]', True)
            self.Destroy()
        if DM.ARC_FORMAT:
            self.checkListStates.SetStates([0, 1, -1], DM.GetAddSubImageList())
        else:
            self.checkListStates.SetStates(
                [False, True], DM.GetNormalCheckImageList())
        font = wx.Font(
            8, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        font.SetFaceName(kernel.Config.getUnified()['Misc']['NoteFont'])
        self.textCtrlNotes.SetFont(font)

        default = ['Price:', 'PDEF:', 'MDEF:', 'EVA:']
        self.ParameterControls = DM.CreateParameterControls(self.panelParameters,
                                                            self.spinCtrlParameter_ValueChanged, '+:', 4, default)
        self.setRanges()
        self.SelectedArmor = DataArmors[DM.FixedIndex(armor_index)]
        self.refreshAll()
        self.listBoxArmors.SetSelection(armor_index)
        DM.DrawHeaderBitmap(self.bitmapArmors, 'Armors')

        # Bind the panel tot he Panel Manager
        self.bindPanelManager()

    def setRanges(self):
        """Applies the range of values allowed fir the controls on the panel"""
        self.ParameterControls[0].SetRange(0, int(kernel.Config.getUnified()['DatabaseLimits']['Gold']))
        max = int(kernel.Config.getUnified()['DatabaseLimits']['ActorParameter'])
        for i in range(1, len(self.ParameterControls)):
            self.ParameterControls[i].SetRange(-max, max)

    def refreshAll(self):
        """Refreshes all the controls on the panel"""
        self.refreshArmorList()
        self.refreshElements()
        self.refreshStates()
        self.refreshKinds()
        self.refreshValues()

    def refreshArmorList(self):
        """Refreshes the list of armors"""
        digits = len(kernel.Config.getUnified()['GameObjects']['Armors'])
        DM.FillControl(self.listBoxArmors, DataArmors, digits, [])

    def refreshElements(self):
        """Refreshes the list of elements in the wxCheckListBox"""
        self.checkListElements.Clear()
        self.checkListElements.AppendItems(DataElements[DM.FixedIndex(0):])

    def refreshStates(self):
        """Refreshes the list of states in the wxCheckListBox"""
        digits = len(kernel.Config.getUnified()['GameObjects']['States'])
        DM.FillWithoutNumber(self.checkListStates, DataStates, [])
        DM.FillControl(self.comboBoxAutoState, DataStates, digits, ['(None)'])

    def refreshKinds(self):
        """updates the armor kinds"""
        if DM.ARC_FORMAT:
            kinds = list(kernel.Config.getUnified()['GameSetup']['ArmorSlots'])
        else:
            kinds = ['Shield', 'Helmet', 'Body Armor', 'Accessory']
        DM.FillWithoutNumber(self.comboBoxKind, [], kinds)

    def refreshValues(self):
        """Refreshes the panel to display the values for the selected armor"""
        armor = self.SelectedArmor
        self.textCtrlName.ChangeValue(armor.name)
        self.labelIconName.SetLabel(armor.icon_name)
        self.labelIconName.Wrap(-1)
        DM.DrawButtonIcon(self.bitmapButtonIcon, armor.icon_name, False)
        self.textCtrlDescription.ChangeValue(armor.description)
        self.comboBoxKind.SetSelection(armor.kind)
        self.comboBoxAutoState.SetSelection(armor.auto_state_id)
        if DM.ARC_FORMAT:
            # TODO: Implement
            self.checkListElements.SetChecked(
                [i for i in armor.guard_element_set])
            self.checkListStates.SetChecked([i for i in armor.guard_state_set])
        else:
            self.checkListElements.SetChecked(
                [i - 1 for i in armor.guard_element_set])
            self.checkListStates.SetChecked(
                [i - 1 for i in armor.guard_state_set])
            self.ParameterControls[0].SetValue(armor.price)
            self.ParameterControls[1].SetValue(armor.pdef)
            self.ParameterControls[2].SetValue(armor.mdef)
            self.ParameterControls[3].SetValue(armor.eva)
            self.ParameterControls[4].SetValue(armor.str_plus)
            self.ParameterControls[5].SetValue(armor.dex_plus)
            self.ParameterControls[6].SetValue(armor.agi_plus)
            self.ParameterControls[7].SetValue(armor.int_plus)
        if not hasattr(armor, 'note'):
            setattr(armor, 'note', '')
        self.textCtrlNotes.ChangeValue(armor.note)

    def spinCtrlParameter_ValueChanged(self, event):
        """updates the selected armor's parameter"""
        index = self.ParameterControls.index(event.GetEventObject())
        if DM.ARC_FORMAT:
            # TODO: Implement
            pass
        else:
            value = event.GetInt()
            if index == 0:
                self.SelectedArmor.price = value
            elif index == 1:
                self.SelectedArmor.pdef = value
            elif index == 2:
                self.SelectedArmor.mdef = value
            elif index == 3:
                self.SelectedArmor.eva = value
            elif index == 4:
                self.SelectedArmor.str_plus = value
            elif index == 5:
                self.SelectedArmor.dex_plus = value
            elif index == 6:
                self.SelectedArmor.agi_plus = value
            elif index == 7:
                self.SelectedArmor.int_plus = value

    def listBoxArmors_SelectionChanged(self, event):
        """Changes the selected armor and update the values on the panel"""
        index = DM.FixedIndex(event.GetSelection())
        if DataArmors[index] is None:
            DataArmors[index] = RPG.Armor()
        self.SelectedArmor = DataArmors[index]
        self.refreshValues()

    def buttonMaximum_Clicked(self, event):
        """Starts the Change Maximum dialog"""
        max = int(kernel.Config.getUnified()['GameObjects']['Armors'])
        DM.ChangeDataCapacity(self, self.listBoxArmors, DataArmors, max)

    def textCtrlName_TextChanged(self, event):
        """updates the selected armor's name"""
        DM.updateObjectName(self.SelectedArmor, event.GetString(),
                            self.listBoxArmors, len(kernel.Config.getUnified()['GameObjects']['Armors']))

    def bitmapButtonIcon_Clicked(self, event):
        """Opens dialog to select an icon for the selected skill"""
        DM.ChooseGraphic(
            'Graphics/Icon/', self.SelectedArmor.icon_name, 0, False)

    def textCtrlDescription_TextChange(self, event):
        """Set the selected armor's description"""
        self.SelectedArmor.description = event.GetString()

    def comboBoxKind_SelectionChanged(self, event):
        """Set the selected armor's kind"""
        self.SelectedArmor.kind = event.GetInt()

    def comboBoxAutoState_SelectionChanged(self, event):
        """Set the selected armor's auto-state"""
        self.SelectedArmor.auto_state_id = event.GetInt()

    def checkListElements_CheckChanged(self, event):
        """Sets the IDs that are in the selected armor's element set"""
        ids = [DM.FixedIndex(id) for id in self.checkListElements.GetChecked()]
        self.SelectedArmor.guard_element_set = ids

    def textCtrlNotes_TextChanged(self, event):
        """Set the selected armor's magical defense"""
        self.SelectedArmor.note = event.GetString()

    def checkListElements_Clicked(self, event):
        """updates the guard elements for the selected armor"""
        self.checkListElements.ChangeState(event, 1)
        if DM.ARC_FORMAT:
            # TODO: Implement
            pass
        else:
            ids = [DM.FixedIndex(id)
                   for id in self.checkListElements.GetChecked()]
            self.SelectedArmor.guard_element_set = ids

    def checkListStates_Clicked(self, event):
        """updates the guard states for the selected armor"""
        data = self.checkListStates.ChangeState(event, 1)
        if DM.ARC_FORMAT:
            # TODO: Implement
            pass
        else:
            ids = [DM.FixedIndex(id)
                   for id in self.checkListStates.GetChecked()]
            self.SelectedArmor.guard_state_set = ids
