pimport wx


import Kernel


#-------------------------------------------------------------------------
# BattleAnimation_Dialog
#-------------------------------------------------------------------------

# Implementing BattleAnimation_Dialog
from PyitectConsumes import BattleAnimation_Dialog_Template


class BattleAnimation_Dialog(BattleAnimation_Dialog_Template):

    def __init__(self, parent):
        BattleAnimation_Dialog_Template.__init__(self, parent)

    # Handlers for BattleAnimation_Dialog events.
    def radioButtonEnemy_CheckChanged(self, event):
        # TODO: Implement radioButtonEnemy_CheckChanged
        pass

    def radioButtonActor_CheckChanged(self, event):
        # TODO: Implement radioButtonActor_CheckChanged
        pass

    def buttonOK_Clicked(self, event):
        # TODO: Implement buttonOK_Clicked
        pass

    def buttonCancel_Clicked(self, event):
        # TODO: Implement buttonCancel_Clicked
        pass
