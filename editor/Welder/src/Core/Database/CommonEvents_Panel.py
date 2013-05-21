import wx
import EventCommands1_Panel
import EventCommands2_Panel
import EventCommands3_Panel

from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates
PanelBase = Core.Panels.PanelBase
DM = Core.Database.Manager

ChooseSwitchVariable_Dialog = Core.Database.Dialogs.ChooseSwitchVariable_Dialog

#--------------------------------------------------------------------------------------
# CommonEvents_Panel
#--------------------------------------------------------------------------------------

# Implementing CommonEvents_Panel
class CommonEvents_Panel( Templates.CommonEvents_Panel, PanelBase  ):

    _arc_panel_info_string = "Name Caption Center CloseB CaptionV DestroyOC Floatable Float IconARCM MaximizeB MinimizeM MinimizeB Movable NotebookD Resizable Snappable"
    _arc_panel_info_data = {"Name": "Common Events Panel", "Caption": "Common Events Panel", "CaptionV": True,  "MinimizeM": ["POS_SMART", "CAPT_SMART",], 
                            "MinimizeB": True, "CloseB": True, 'IconARCM': 'commoneventsicon'}

    def __init__( self, parent ):
        Templates.CommonEvents_Panel.__init__( self, parent )

        DM.DrawHeaderBitmap(self.bitmapCommonEvents, 'Common Events')

        # Bind the panel tot he Panel Manager
        self.BindPanelManager()



    # Handlers for CommonEvents_Panel events.
    def listBoxCommonEvents_SelectionChanged( self, event ):
        # TODO: Implement listBoxCommonEvents_SelectionChanged
        pass

    def buttonMaximum_Clicked( self, event ):
        # TODO: Implement buttonMaximum_Clicked
        pass

    def textCtrlName_ValueChanged( self, event ):
        # TODO: Implement textCtrlName_ValueChanged
        pass

    def comboBoxTrigger_SelectionChanged( self, event ):
        # TODO: Implement comboBoxTrigger_SelectionChanged
        pass

    def comboBoxCondition_Clicked( self, event ):
        # TODO: Implement comboBoxCondition_Clicked
        pass

    def listBoxEvents_DoubleClicked( self, event ):
        # TODO: Implement listBoxEvents_DoubleClicked
        pass

    def listBoxPage_SelectionChanged( self, event ):
        # TODO: Implement listBoxPage_SelectionChanged
        pass


