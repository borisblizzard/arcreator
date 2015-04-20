import wx
import Kernel

from PyitectConsumes import DatabaseManager as DM
from PyitectConsumes import RGSS1_RPG as RPG

from PyitectConsumes import ChooseGraphic_Dialog
from PyitectConsumes import EnemyAction_Dialog
from PyitectConsumes import EnemyExpGold_Dialog
from PyitectConsumes import ChooseTreasure_Dialog

from PyitectConsumes import PanelBase, Enemies_Panel_Template

# --------------------------------------------------------------------------------------
# Enemies_Panel
# --------------------------------------------------------------------------------------


class Enemies_Panel(Enemies_Panel_Template, PanelBase):

    _arc_panel_info_string = "Name Caption Center CloseB CaptionV DestroyOC Floatable Float IconARCM MaximizeB MinimizeM MinimizeB Movable NotebookD Resizable Snappable"
    _arc_panel_info_data = {"Name": "Enemies Panel", "Caption": "Enemies Panel", "CaptionV": True, "MinimizeM": ["POS_SMART", "CAPT_SMART", ],
                            "MinimizeB": True, "CloseB": True, 'IconARCM': 'enemiesicon'}

    def __init__(self, parent, enemy_index=0):
        """Basic constructor for the Enemies panel"""
        Enemies_Panel_Template.__init__(self, parent)
        global Config, DataEnemies, DataStates, DataAnimations, DataElements
        
        try:
            proj = Kernel.GlobalObjects['PROJECT']
            DataEnemies = proj.getData('Enemies')
            DataAnimations = proj.getData('Animations')
            DataStates = proj.getData('States')
            DataElements = proj.getData('System').elements
        except NameError:
            Kernel.Log(
                'Database opened before Project has been initialized', '[Database:ENEMIES]', True)
            self.Destroy()
        font = wx.Font(
            8, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        font.SetFaceName(Kernel.Config.getUnified()['Misc']['NoteFont'])
        self.textCtrlNotes.SetFont(font)
        default = ['MaxHP:', 'MaxSP:', 'EVA:', 'ATK:', 'PDEF:', 'MDEF:']
        self.ParameterControls = DM.CreateParameterControls(self.panelParameters,
                                                            self.spinCtrlParameter_ValueChanged, ':', 3, default)
        self.SelectedEnemy = DataEnemies[DM.FixedIndex(enemy_index)]
        self.setRanges()
        self.refreshAll()
        self.listBoxEnemies.SetSelection(enemy_index)
        DM.DrawHeaderBitmap(self.bitmapEnemies, 'Enemies')

        # Bind the panel to the Panel Manager
        self.bindPanelManager()

    def setRanges(self):
        """Sets the ranges of allowed values for the controls"""
        self.ParameterControls[0].SetRange(
            1, int(Kernel.Config.getUnified()['DatabaseLimits']['EnemyHP']))
        self.ParameterControls[1].SetRange(
            1, int(Kernel.Config.getUnified()['DatabaseLimits']['EnemySP']))
        for i in range(2, len(self.ParameterControls)):
            self.ParameterControls[i].SetRange(0,
                                               int(Kernel.Config.getUnified()['DatabaseLimits']['EnemyParameter']))

    def refreshAll(self):
        """Refreshes all the controls on the panel"""
        self.refreshEnemyList()
        self.refreshGraphic()
        self.refreshAnimations()
        self.refreshStates()
        self.refreshElements()
        self.refreshValues()

    def refreshEnemyList(self):
        """Refreshes the list of enemies"""
        digits = len(Kernel.Config.getUnified()['GameObjects']['Enemies'])
        DM.FillControl(self.listBoxEnemies, DataEnemies, digits, [])

    def refreshGraphic(self):
        """Refreshes the battler graphic"""
        DM.RenderImage(self.glCanvasEnemyGraphic, self.SelectedEnemy.battler_name,
                       self.SelectedEnemy.battler_hue, 'battler')

    def refreshAnimations(self):
        """Refreshes the choices in the user and target animation controls"""
        digits = len(Kernel.Config.getUnified()['GameObjects']['Animations'])
        DM.FillControl(
            self.comboBoxTargetAnimation, DataAnimations, digits, ['(None)'])
        DM.FillControl(
            self.comboBoxAttackAnimation, DataAnimations, digits, ['(None)'])

    def refreshStates(self):
        """Clears and refreshes the list of states in the checklist"""
        self.checkListStates.DeleteAllItems()
        names = [DataStates[i].name for i in range(
            DM.FixedIndex(0), len(DataStates))]
        self.checkListStates.AppendItems(names)

    def refreshElements(self):
        """Clears and refreshes the list of elements in the checklist"""
        self.checkListElements.Clear()
        self.checkListElements.AppendItems(DataElements[DM.FixedIndex(0):])

    def refreshActions(self):
        # TODO: Implement
        pass

    def refreshValues(self):
        """Refreshes the values of all the controls to reflect the selected enemy"""
        enemy = self.SelectedEnemy
        self.textCtrlName.ChangeValue(enemy.name)
        if not hasattr(enemy, 'description'):
            setattr(enemy, 'description', '')
        self.textCtrlDescription.ChangeValue(enemy.description)
        self.comboBoxAttackAnimation.SetSelection(enemy.animation1_id)
        self.comboBoxTargetAnimation.SetSelection(enemy.animation2_id)
        if DM.ARC_FORMAT:
            # TODO: Implement showing treasure, parameters, and variance with
            # gold/exp
            pass
        else:
            self.comboBoxExp.SetValue(str(enemy.exp))
            self.comboBoxGold.SetValue(str(enemy.gold))
            trsr = None
            proj = Kernel.GlobalObjects['PROJECT']
            if enemy.item_id != 0:
                trsr = (proj.getData('Items'), enemy.item_id)
            elif enemy.weapon_id != 0:
                trsr = (proj.getData('Weapons'), enemy.weapon_id)
            elif enemy.armor_id != 0:
                trsr = (proj.getData('Armors'), enemy.armor_id)
            if trsr is not None:
                text = ''.join(
                    [trsr[0][trsr[1]].name, ' (', str(enemy.treasure_prob), '%)'])
                self.comboBoxTreasure.SetValue(text)
            else:
                self.comboBoxTreasure.SetValue('(None)')
            self.ParameterControls[0].SetValue(enemy.maxhp)
            self.ParameterControls[1].SetValue(enemy.maxsp)
            self.ParameterControls[2].SetValue(enemy.eva)
            self.ParameterControls[3].SetValue(enemy.atk)
            self.ParameterControls[4].SetValue(enemy.pdef)
            self.ParameterControls[5].SetValue(enemy.mdef)
            self.ParameterControls[6].SetValue(enemy.str)
            self.ParameterControls[7].SetValue(enemy.dex)
            self.ParameterControls[8].SetValue(enemy.agi)
            self.ParameterControls[9].SetValue(enemy.int)
            if not hasattr(enemy, 'note'):
                setattr(enemy, 'note', '')
            self.textCtrlNotes.ChangeValue(enemy.note)
            self.refreshGraphic()
            self.refreshActions()

    def listBoxEnemies_SelectionChanged(self, event):
        """Changes the selected armor and update the values on the panel"""
        index = DM.FixedIndex(event.GetSelection())
        if DataEnemies[index] is None:
            DataEnemies[index] = RPG.Enemy()
        self.SelectedEnemy = DataEnemies[index]
        self.refreshValues()

    def buttonMaximum_Clicked(self, event):
        """Starts the Change Maximum dialog"""
        max = int(Kernel.Config.getUnified()['GameObjects']['Enemies'])
        DM.ChangeDataCapacity(self, self.listBoxEnemies, DataEnemies, max)

    def textCtrlName_ValueChanged(self, event):
        """updates the selected enemy's name"""
        self.SelectedEnemy.name = event.GetString()

    def textCtrlDescription_TextChanged(self, event):
        """updates the selected enemy's description"""
        self.SelectedEnemy.description = event.GetString()

    def bitmapGraphic_DoubleClick(self, event):
        # TODO: Implement bitmapGraphic_DoubleClick
        pass

    def comboBoxAttackAnimation_SelectionChanged(self, event):
        """updates the selected enemy's user animation"""
        self.SelectedEnemy.animation1_id = event.GetInt()

    def comboBoxTargetAnimation_ValueChanged(self, event):
        """updates the selected enemy's target animation"""
        self.SelectedEnemy.animation2_id = event.GetInt()

    def spinCtrlParameter_ValueChanged(self, event):
        """updates the selected enemy's parameter"""
        index = self.ParameterControls.index(event.GetEventObject())
        if DM.ARC_FORMAT:
            # TODO: Implement
            pass
        else:
            value = event.GetInt()
            # TODO refactor away form elif branch
            if index == 0:
                self.SelectedEnemy.maxhp = value
            elif index == 1:
                self.SelectedEnemy.maxsp = value
            elif index == 2:
                self.SelectedEnemy.eva = value
            elif index == 3:
                self.SelectedEnemy.atk = value
            elif index == 4:
                self.SelectedEnemy.pdef = value
            elif index == 5:
                self.SelectedEnemy.mdef = value
            elif index == 6:
                self.SelectedEnemy.str = value
            elif index == 7:
                self.SelectedEnemy.dex = value
            elif index == 8:
                self.SelectedEnemy.agi = value
            elif index == 9:
                self.SelectedEnemy.int = value

    def comboBoxExp_Clicked(self, event):
        """Starts the dialog to set the selected enemy's experience"""

        if DM.ARC_FORMAT:
            # TODO: Implement getting variance
            pass
        else:
            variance = None
        dialog = EnemyExpGold_Dialog(self, 'Experience:',
                                     int(Kernel.Config.getUnified()['DatabaseLimits']['EnemyExperience']), self.SelectedEnemy.exp, variance)
        dialog.SetLabel('Enemy Experience')
        if dialog.ShowModal() == wx.ID_OK:
            data = dialog.GetValues()
            self.SelectedEnemy.exp = data[0]
            self.comboBoxExp.SetValue(str(data[0]))
            if DM.ARC_FORMAT:
                # TODO: Implement setting variance
                pass
        dialog.Destroy()

    def comboBoxGold_Clicked(self, event):
        """Starts the dialog to set the selected enemy's gold"""
        if DM.ARC_FORMAT:
            # TODO: Implement getting variance
            pass
        else:
            variance = None
        dialog = EnemyExpGold_Dialog(self, 'Gold:',
                                     int(Kernel.Config.getUnified()['DatabaseLimits']['Gold']), self.SelectedEnemy.gold, variance)
        dialog.SetLabel('Enemy Gold')
        if dialog.ShowModal() == wx.ID_OK:
            data = dialog.GetValues()
            self.SelectedEnemy.gold = data[0]
            self.comboBoxGold.SetValue(str(data[0]))
            if DM.ARC_FORMAT:
                # TODO: Implement setting variance
                pass
        dialog.Destroy()

    def comboBoxTreasure_Clicked(self, event):

        if DM.ARC_FORMAT:
            # TODO: Implement
            pass
        else:
            enemy = self.SelectedEnemy
            items, weapons, armors = [], [], []
            if enemy.item_id != 0:
                items = [(enemy.item_id, enemy.treasure_prob, 1)]
            elif enemy.weapon_id != 0:
                weapons = [(enemy.weapon_id, enemy.treasure_prob, 1)]
            elif enemy.armor_id != 0:
                armors = [(enemy.armor_id, enemy.treasure_prob, 1)]

            items = [(1, 33, 6), (2, 33, 2)]
            weapons = [(5, 25, 1), (32, 1, 1), (1, 10, 2), (1, 75, 1)]
            armors = [(2, 12, 1), (32, 8, 1)]

            treasure = [items, weapons, armors]

        dialog = ChooseTreasure_Dialog(self, treasure)
        if dialog.ShowModal() == wx.ID_OK:

            pass
        dialog.Destroy()

    def checkListElements_ValueChanged(self, event):
        # TODO: Implement checkListElements_ValueChanged
        pass

    def checkListStates_ValueChanged(self, event):
        # TODO: Implement checkListStates_ValueChanged
        pass

    def listCtrlAction_DoubleClick(self, event):
        # TODO: Implement listCtrlAction_DoubleClick
        pass

    def textCtrlNotes_TextChanged(self, event):
        """updates the selected enemy's note"""
        self.SelectedEnemy.note = event.GetString()
