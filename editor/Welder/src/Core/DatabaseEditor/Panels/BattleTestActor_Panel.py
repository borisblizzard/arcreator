import Kernel

from PyitectConsumes import PanelBase, BattleTestActor_Panel_Template
from PyitectConsumes import DatabaseManager as DM
from PyitectConsumes import RGSS1_RPG as RPG
# -------------------------------------------------------------------------
# BattleTestActor_Panel
# -------------------------------------------------------------------------

# Implementing BattleTestActor_Panel


class BattleTestActor_Panel(BattleTestActor_Panel_Template, PanelBase):

    def __init__(self, parent):
        BattleTestActor_Panel_Template.__init__(self, parent)

        # Bind the panel tot he Panel Manager
        self.BindPanelManager()

    # Handlers for BattleTestActor_Panel events.
    def comboBoxActor_SelectionChanged(self, event):
        # TODO: Implement comboBoxActor_SelectionChanged
        pass

    def spinCtrlLevel_ValueChanged(self, event):
        # TODO: Implement spinCtrlLevel_ValueChanged
        pass

    def buttonInitialize_Clicked(self, event):
        # TODO: Implement buttonInitialize_Clicked
        pass
