import wx

import welder_kernel as kernel
from PyitectConsumes import PanelBase, System_Panel_Template
from PyitectConsumes import DatabaseManager as DM

from PyitectConsumes import ChooseGraphic_Dialog

# --------------------------------------------------------------------------------------
# System_Panel
# --------------------------------------------------------------------------------------

# Implementing System_Panel


class System_Panel(System_Panel_Template, PanelBase):

    _arc_panel_info = {
        "Name": "SystemPanel",
        "Caption": "System",
        "CaptionV": True,
        "Center": None,
        "CloseB": True,
        "DestroyOC": True,
        "Floatable": True,
        "IconARCM": 'system',
        "MaximizeB": True,
        "MinimizeB": True,
        "MinimizeM": ["POS_SMART", "CAPT_SMART"],
        "Movable": True,
        "NotebookD": True,
        "Resizable": True,
        "Snappable": True
    }

    def __init__(self, parent):
        System_Panel_Template.__init__(self, parent)

        # Bind the panel tot he Panel Manager
        self.bindPanelManager()

    # Handlers for System_Panel events.
    def listCtrlInitialParty_DoubleClicked(self, event):
        # TODO: Implement listCtrlInitialParty_DoubleClicked
        pass

    def listCtrlInitialParty_ItemDeleted(self, event):
        # TODO: Implement listCtrlInitialParty_ItemDeleted
        pass

    def listBoxElements_SelectionChanged(self, event):
        # TODO: Implement listBoxElements_SelectionChanged
        pass

    def textCtrlElement_TextChanged(self, event):
        # TODO: Implement textCtrlElement_TextChanged
        pass

    def buttonMaximum_Clicked(self, event):
        # TODO: Implement buttonMaximum_Clicked
        pass

    def comboBoxWindowskinGraphic_Clicked(self, event):
        # TODO: Implement comboBoxWindowskinGraphic_Clicked
        pass

    def comboBoxTitleGraphic_Clicked(self, event):
        # TODO: Implement comboBoxTitleGraphic_Clicked
        pass

    def comboBoxGameoverGraphic_Clciked(self, event):
        # TODO: Implement comboBoxGameoverGraphic_Clciked
        pass

    def comboBoxBattleTransitionGraphic_Clicked(self, event):
        # TODO: Implement comboBoxBattleTransitionGraphic_Clicked
        pass

    def comboBoxTitleBGM_Clicked(self, event):
        # TODO: Implement comboBoxTitleBGM_Clicked
        pass

    def comboBoxBattleBGM_Clicked(self, event):
        # TODO: Implement comboBoxBattleBGM_Clicked
        pass

    def comboBoxBattleEndME_Clicked(self, event):
        # TODO: Implement comboBoxBattleEndME_Clicked
        pass

    def comboBoxGameoverME_Clicked(self, event):
        # TODO: Implement comboBoxGameoverME_Clicked
        pass

    def comboBoxCursorSE_Clicked(self, event):
        # TODO: Implement comboBoxCursorSE_Clicked
        pass

    def comboBoxDecisionSE_Clicked(self, event):
        # TODO: Implement comboBoxDecisionSE_Clicked
        pass

    def comboBoxCancelSE_Clicked(self, event):
        # TODO: Implement comboBoxCancelSE_Clicked
        pass

    def comboBoxBuzzerSE_Clicked(self, event):
        # TODO: Implement comboBoxBuzzerSE_Clicked
        pass

    def comboBoxEquipSE_Clicked(self, event):
        # TODO: Implement comboBoxEquipSE_Clicked
        pass

    def comboBoxShopSE_Clicked(self, event):
        # TODO: Implement comboBoxShopSE_Clicked
        pass

    def comboBoxSaveSE_Clicked(self, event):
        # TODO: Implement comboBoxSaveSE_Clicked
        pass

    def comboBoxLoadSE_Clicked(self, event):
        # TODO: Implement comboBoxLoadSE_Clicked
        pass

    def comboBoxBattleStartSE_Clicked(self, event):
        # TODO: Implement comboBoxBattleStartSE_Clicked
        pass

    def comboBoxEscapeSE_Clicked(self, event):
        # TODO: Implement comboBoxEscapeSE_Clicked
        pass

    def comboBoxActorCollapseSE_Clicked(self, event):
        # TODO: Implement comboBoxActorCollapseSE_Clicked
        pass

    def comboBoxEnemyCollapseSE_Clicked(self, event):
        # TODO: Implement comboBoxEnemyCollapseSE_Clicked
        pass

    def textCtrlGold_TextChanged(self, event):
        # TODO: Implement textCtrlGold_TextChanged
        pass

    def textCtrlHP_TextChanged(self, event):
        # TODO: Implement textCtrlHP_TextChanged
        pass

    def textCtrlSP_TextChanged(self, event):
        # TODO: Implement textCtrlSP_TextChanged
        pass

    def textCtrlStr_TextChanged(self, event):
        # TODO: Implement textCtrlStr_TextChanged
        pass

    def textCtrlDex_TextChanged(self, event):
        # TODO: Implement textCtrlDex_TextChanged
        pass

    def textCtrlAgi_TextChanged(self, event):
        # TODO: Implement textCtrlAgi_TextChanged
        pass

    def textCtrlInt_TextChanged(self, event):
        # TODO: Implement textCtrlInt_TextChanged
        pass

    def textCtrlAtk_TextChanged(self, event):
        # TODO: Implement textCtrlAtk_TextChanged
        pass

    def textCtrlPdef_TextChanged(self, event):
        # TODO: Implement textCtrlPdef_TextChanged
        pass

    def textCtrlMdef_TextChanged(self, event):
        # TODO: Implement textCtrlMdef_TextChanged
        pass

    def textCtrlWeapon_TextChanged(self, event):
        # TODO: Implement textCtrlWeapon_TextChanged
        pass

    def textCtrlShield_TextChanged(self, event):
        # TODO: Implement textCtrlShield_TextChanged
        pass

    def textCtrlHelmet_TextChanged(self, event):
        # TODO: Implement textCtrlHelmet_TextChanged
        pass

    def textCtrlBodyArmor_TextChanged(self, event):
        # TODO: Implement textCtrlBodyArmor_TextChanged
        pass

    def textCtrlAccessory_TextChanged(self, event):
        # TODO: Implement textCtrlAccessory_TextChanged
        pass

    def textCtrlAttack_TextChanged(self, event):
        # TODO: Implement textCtrlAttack_TextChanged
        pass

    def textCtrlSkill_TextChanged(self, event):
        # TODO: Implement textCtrlSkill_TextChanged
        pass

    def textCtrlDefend_TextChanged(self, event):
        # TODO: Implement textCtrlDefend_TextChanged
        pass

    def textCtrlItem_TextChanged(self, event):
        # TODO: Implement textCtrlItem_TextChanged
        pass

    def textCtrlEquip_TextChanged(self, event):
        # TODO: Implement textCtrlEquip_TextChanged
        pass
