import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates
PanelBase = Core.Panels.PanelBase
DM = Core.Database.Manager

ChangeMaximum_Dialog = Core.Database.Dialogs.ChangeMaximum_Dialog
ChooseGraphic_Dialog = Core.Database.Dialogs.ChooseGraphic_Dialog
BattleTest_Dialog = Core.Database.Dialogs.BattleTest_Dialog
EventCondition_Dialog = Core.Database.Dialogs.EventCondition_Dialog

#--------------------------------------------------------------------------------------
# Troops_Panel
#--------------------------------------------------------------------------------------

# Implementing Troops_Panel
class Troops_Panel( Templates.Troops_Panel, PanelBase ):

    _arc_panel_info_string = "Name Caption Center CloseB CaptionV DestroyOC Floatable Float IconARCM MaximizeB MinimizeM MinimizeB Movable NotebookD Resizable Snappable"
    _arc_panel_info_data = {"Name": "Troops Panel", "Caption": "Troops Panel", "CaptionV": True,  "MinimizeM": ["POS_SMART", "CAPT_SMART",], 
                            "MinimizeB": True, "CloseB": True, 'IconARCM': 'troopsicon'}

    def __init__( self, parent ):
        Templates.Troops_Panel.__init__( self, parent )


        DM.DrawHeaderBitmap(self.bitmapTroops, 'Troops')

        # Bind the panel tot he Panel Manager
        self.BindPanelManager()

    # Handlers for Troops_Panel events.
    def listBoxTroops_SelectionChanged( self, event ):
        # TODO: Implement listBoxTroops_SelectionChanged
        pass

    def buttonMaximum_Clicked( self, event ):
        # TODO: Implement buttonMaximum_Clicked
        pass

    def textCtrlName_ValueChanged( self, event ):
        # TODO: Implement textCtrlName_ValueChanged
        pass

    def buttonAutoname_Clicked( self, event ):
        # TODO: Implement buttonAutoname_Clicked
        pass

    def buttonBattleback_Click( self, event ):
        # TODO: Implement buttonBattleback_Click
        pass

    def buttonBattleTest_Click( self, event ):
        # TODO: Implement buttonBattleTest_Click
        pass

    def buttonAddEnemy_Click( self, event ):
        # TODO: Implement buttonAddEnemy_Click
        pass

    def buttonRemoveEnemy_Click( self, event ):
        # TODO: Implement buttonRemoveEnemy_Click
        pass

    def buttonClearTroop_Click( self, event ):
        # TODO: Implement buttonClearTroop_Click
        pass

    def buttonAlignTroop_Click( self, event ):
        # TODO: Implement buttonAlignTroop_Click
        pass

    def listBoxEnemies_SelectionChanged( self, event ):
        # TODO: Implement listBoxEnemies_SelectionChanged
        pass

    def buttonNewEventPage_Click( self, event ):
        # TODO: Implement buttonNewEventPage_Click
        pass

    def buttonCopyEventPage_Click( self, event ):
        # TODO: Implement buttonCopyEventPage_Click
        pass

    def buttonPasteEventPage_Click( self, event ):
        # TODO: Implement buttonPasteEventPage_Click
        pass

    def buttonDeleteEventPage_Click( self, event ):
        # TODO: Implement buttonDeleteEventPage_Click
        pass

    def buttonClearEventPage_Click( self, event ):
        # TODO: Implement buttonClearEventPage_Click
        pass

    def comboBoxCondition_Clicked( self, event ):
        # TODO: Implement comboBoxCondition_Clicked
        pass

    def comboBoxSpan_ValueChanged( self, event ):
        # TODO: Implement comboBoxSpan_ValueChanged
        pass

    def listBoxEvents_DoubleClick( self, event ):
        # TODO: Implement listBoxEvents_DoubleClick
        pass


