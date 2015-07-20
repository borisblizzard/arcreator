import wx

import Kernel

from PyitectConsumes import DatabaseManager as DM
from PyitectConsumes import RGSS1_RPG as RPG

from PyitectConsumes import ChooseGraphic_Dialog

from PyitectConsumes import PanelBase, Skills_Panel_Template

# --------------------------------------------------------------------------------------
# Skills_Panel
# --------------------------------------------------------------------------------------


class Skills_Panel(Skills_Panel_Template, PanelBase):

    _arc_panel_info = {
        "Name": "Skills Panel",
        "Caption": "Skills Panel",
        "CaptionV": True,
        "Center": None,
        "CloseB": True,
        "DestroyOC": True,
        "Floatable": True,
        "Float": None,
        "IconARCM": 'skillsicon',
        "MaximizeB": True,
        "MinimizeB": True,
        "MinimizeM": ["POS_SMART", "CAPT_SMART"],
        "Movable": True,
        "NotebookD": True,
        "Resizable": True,
        "Snappable": True
    }
    def __init__(self, parent, skill_index=0):
        Skills_Panel_Template.__init__(self, parent)
        global Config, DataSkills, DataAnimations, DataElements
        global DataStates, DataCommonEvents
        
        try:
            proj = Kernel.GlobalObjects['PROJECT']
            DataSkills = proj.getData('Skills')
            DataAnimations = proj.getData('Animations')
            DataStates = proj.getData('States')
            DataElements = proj.getData('System').elements
            DataCommonEvents = proj.getData('CommonEvents')
        except NameError:
            Kernel.Log(
                'Database opened before Project has been initialized', '[Database:SKILLS]', True)
            self.Destroy()

        try:
            note_font = str(Kernel.Config.getUnified()['Misc']['NoteFont'])
        except KeyError as e:
            Kernel.Log("Bad Config Value", error=True)
            note_font = "Arial"

        font = wx.Font(
            8, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        font.SetFaceName(note_font)

        self.textCtrlNotes.SetFont(font)
        DM.DrawButtonIcon(self.bitmapButtonAudioTest, 'play_button', True)
        self.comboBoxMenuSE.SetCursor(wx.STANDARD_CURSOR)

        default = ['SP Cost:', 'Power:', 'Variance:', 'Hit Rate:',
                   'ATK-F:', 'PDEF-F:', 'MDEF-F:', 'EVA-F:']
        self.ParameterControls = DM.CreateParameterControls(self.panelParameters,
                                                            self.spinCtrlParameter_ValueChanged, '-F:', 4, default)

        self.setRanges()
        self.SelectedSkill = DataSkills[DM.FixedIndex(skill_index)]
        self.refreshAll()
        self.listBoxSkills.SetSelection(skill_index)
        DM.DrawHeaderBitmap(self.bitmapSkills, 'Skills')

        # Bind the panel to the Panel Manager
        self.bindPanelManager()

    def refreshSkillList(self):
        """Refreshes the values in the skill wxListBox control"""
        try:
            digits = int(Kernel.Config.getUnified()['GameObjects']['Skills'])
        except Exception as e:
            Kernel.Log("Bad Config Value", error=True)
            digits = 9999

        DM.FillControl(self.listBoxSkills, DataSkills, digits, [])

    def refreshAnimations(self):
        """Refreshes the choices in the user and target animation controls"""
        try:
            digits = int(Kernel.Config.getUnified()['GameObjects']['Animations'])
        except Exception as e:
            Kernel.Log("Bad Config Value", error=True)
            digits = 9999

        
        DM.FillControl(
            self.comboBoxTargetAnimation, DataAnimations, digits, ['(None)'])
        DM.FillControl(
            self.comboBoxUserAnimation, DataAnimations, digits, ['(None)'])

    def refreshElements(self):
        """Clears and refreshes the list of elements in the checklist"""
        self.checkListElements.Clear()
        self.checkListElements.AppendItems(DataElements[DM.FixedIndex(0):])

    def refreshStates(self):
        """Clears and refreshes the list of states in the checklist"""
        self.checkListStates.DeleteAllItems()
        names = [DataStates[i].name for i in range(
            DM.FixedIndex(0), len(DataStates))]
        self.checkListStates.AppendItems(names)

    def refreshCommonEvents(self):
        """Refreshes the common events in the combo box"""
        try:
            digits = int(Kernel.Config.getUnified()['GameObjects']['CommonEvents'])
        except Exception as e:
            Kernel.Log("Bad Config Value", error=True)
            digits = 999

        
        DM.FillControl(
            self.comboBoxCommonEvent, DataCommonEvents, digits, ['(None)'])

    def refreshValues(self):
        """Resets the values of all the controls to reflect the selected skill"""
        skill = self.SelectedSkill
        self.textCtrlName.ChangeValue(skill.name)
        self.textCtrlDescription.ChangeValue(skill.description)
        self.labelIconName.SetLabel(skill.icon_name)
        DM.DrawButtonIcon(self.bitmapButtonIcon, skill.icon_name, False)
        self.comboBoxScope.SetSelection(skill.scope)
        self.comboBoxOccasion.SetSelection(skill.occasion)
        self.comboBoxUserAnimation.SetSelection(skill.animation1_id)
        self.comboBoxTargetAnimation.SetSelection(skill.animation2_id)
        self.comboBoxCommonEvent.SetSelection(skill.common_event_id)
        self.comboBoxMenuSE.SetValue(skill.menu_se.name)

        # TODO: Remove this. Something got screwed up with the conversion
        if skill.power > 2147483647:
            skill.power = 0

        if DM.ARC_FORMAT:
            # TODO: Implement
            pass
        else:
            self.ParameterControls[0].SetValue(skill.sp_cost)
            self.ParameterControls[1].SetValue(skill.power)
            self.ParameterControls[2].SetValue(skill.hit)
            self.ParameterControls[3].SetValue(skill.variance)
            self.ParameterControls[4].SetValue(skill.atk_f)
            self.ParameterControls[5].SetValue(skill.pdef_f)
            self.ParameterControls[6].SetValue(skill.mdef_f)
            self.ParameterControls[7].SetValue(skill.eva_f)
            self.ParameterControls[8].SetValue(skill.str_f)
            self.ParameterControls[9].SetValue(skill.dex_f)
            self.ParameterControls[10].SetValue(skill.agi_f)
            self.ParameterControls[11].SetValue(skill.int_f)
        # update elements
        for i in range(self.checkListElements.GetItemCount()):
            checked = skill.element_set
            if not DM.ARC_FORMAT:
                checked = [i - 1 for i in checked]
            self.checkListElements.SetChecked(checked)
        # update plus/minus states
        if DM.ARC_FORMAT:
            addstates = skill.plus_state_set
            minusstates = skill.minus_state_set
        else:
            addstates = [id - 1 for id in skill.plus_state_set]
            minusstates = [id - 1 for id in skill.minus_state_set]
        for i in range(self.checkListStates.GetItemCount()):
            if i in addstates:
                self.checkListStates.SetItemImage(i, 1)
            elif i in minusstates:
                self.checkListStates.SetItemImage(i, 2)
            else:
                self.checkListStates.SetItemImage(i, 0)
        # RMXP Compatibility
        if not hasattr(skill, 'note'):
            setattr(skill, 'note', '')
        self.textCtrlNotes.ChangeValue(skill.note)

    def refreshAll(self):
        """Refreshes all child controls of the panel"""
        self.refreshSkillList()
        self.refreshAnimations()
        self.refreshStates()
        self.refreshElements()
        self.refreshCommonEvents()
        self.refreshValues()

    def setRanges(self):
        try:
            actor_sp_max = int(Kernel.Config.getUnified()['DatabaseLimits']['ActorSP'])
        except Exception as e:
            Kernel.Log("Bad Config Value", error=True)
            actor_sp_max = 999

        try:
            actor_peram_max = int(Kernel.Config.getUnified()['DatabaseLimits']['ActorParameter'])
        except Exception as e:
            Kernel.Log("Bad Config Value", error=True)
            actor_peram_max = 9999

        self.ParameterControls[0].SetRange(0, actor_sp_max)
        
        self.ParameterControls[1].SetRange(-actor_peram_max, actor_peram_max)

        for i in range(2, len(self.ParameterControls)):
            self.ParameterControls[i].SetRange(0, actor_peram_max)

    def listBoxSkills_SelectionChanged(self, event):
        """Changes the selected skill and update the values on the panel"""
        index = DM.FixedIndex(event.GetSelection())
        if DataSkills[index] is None:
            DataSkills[index] = RPG.Skill()
        self.SelectedSkill = DataSkills[index]
        self.refreshValues()

    def buttonMaximum_Clicked(self, event):
        """Starts the Change Maximum dialog"""
        try:
            skills_max = int(Kernel.Config.getUnified()['GameObjects']['Skills'])
        except Exception as e:
            Kernel.Log("Bad Config Value", error=True)
            skills_max = 9999   
        
        DM.ChangeDataCapacity(self, self.listBoxSkills, DataSkills, skills_max)

    def textCtrlName_TextChanged(self, event):
        """updates the selected skill's name"""
        try:
            skills_max = int(Kernel.Config.getUnified()['GameObjects']['Skills'])
        except Exception as e:
            Kernel.Log("Bad Config Value", error=True)
            skills_max = 9999   
        
        DM.updateObjectName(self.SelectedSkill, event.GetString(),
                            self.listBoxSkills, skills_max)

    def bitmapButtonIcon_Clicked(self, event):
        """Opens dialog to select an icon for the selected skill"""
        filename = DM.ChooseGraphic(
            self, 'Icons', self.SelectedSkill.icon_name)
        if filename:
            self.SelectedSkill.icon_name = filename
        self.refreshValues()

    def bitmapButtonAudioTest_Clicked(self, event):
        """Plays the sound effect as a quick test without opening the dialog"""
        DM.QuickPlay(self.SelectedSkill.menu_se, 'SE')

    def textCtrlDescription_TextChange(self, event):
        """Set the selected skill's description"""
        self.SelectedSkill.description = event.GetString()

    def comboBoxScope_SelectionChanged(self, event):
        """Set the selected skill's scope"""
        self.SelectedSkill.scope = event.GetInt()

    def comboBoxUserAnimation_SelectionChanged(self, event):
        """Set the selected skill's user animation ID"""
        self.SelectedSkill.animation1_id = event.GetInt()

    def comboBoxMenuSE_Clicked(self, event):
        """Opens the dialog for selecting the audio file to use"""
        audio = DM.ChooseAudio(self, self.SelectedSkill.menu_se, 'SE')
        if audio:
            self.SelectedSkill.menu_se = audio
            self.comboBoxMenuSE.SetValue(audio.name)

    def comboBoxOccasion_SelectionChanged(self, event):
        """Set the selected skill's occasion"""
        self.SelectedSkill.occasion = event.GetInt()

    def comboBoxTargetAnimation_SelectionChanged(self, event):
        """Set the selected skill's target animation ID"""
        self.SelectedSkill.animation2_id = event.GetInt()

    def comboBoxCommonEvent_SelectionChanged(self, event):
        """Set the selected skill's SP cost"""
        self.SelectedSkill.common_event_id = event.GetInt()

    def spinCtrlParameter_ValueChanged(self, event):
        index = self.ParameterControls.index(event.GetEventObject())
        skill = self.SelectedSkill
        if DM.ARC_FORMAT:
            # TODO: Implement
            pass
        else:
            # TODO: refactor away form elif branch
            value = event.GetInt()
            if index == 0:
                skill.sp_cost = value
            elif index == 1:
                skill.power = value
            elif index == 2:
                skill.variance = value
            elif index == 3:
                skill.hit_rate = value
            elif index == 4:
                skill.atk_f = value
            elif index == 5:
                skill.pdef_f = value
            elif index == 6:
                skill.mdef_f = value
            elif index == 7:
                skill.eva_f = value
            elif index == 8:
                skill.str_f = value
            elif index == 9:
                skill.dex_f = value
            elif index == 10:
                skill.agi_f = value
            elif index == 11:
                skill.int_f = value

    def textCtrlNotes_TextChanged(self, event):
        """Sets the note for the selected skill"""
        self.SelectedSkill.note = event.GetString()

    def checkListElements_Clicked(self, event):
        """updates the element set for the selected skill"""
        self.checkListElements.ChangeState(event, 1)
        if DM.ARC_FORMAT:
            # TODO: Implement
            pass
        else:
            ids = [DM.FixedIndex(id)
                   for id in self.checkListElements.GetChecked()]
            self.SelectedSkill.element_set = ids

    def checkListStates_LeftClicked(self, event):
        """updates the plus/minus state set for the selected skill"""
        data = self.checkListStates.ChangeState(event, 1)
        DM.ChangeSkillStates(self.SelectedSkill, data[0], data[1])

    def checkListStates_RigthClicked(self, event):
        """updates the plus/minus state set for the selected skill"""
        data = self.checkListStates.ChangeState(event, -1)
        DM.ChangeSkillStates(self.SelectedSkill, data[0], data[1])
