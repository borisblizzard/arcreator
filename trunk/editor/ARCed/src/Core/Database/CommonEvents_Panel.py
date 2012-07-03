import wx
from Core.Database import ARCed_Templates as Templates
import EventCommands1_Panel
import EventCommands2_Panel
import EventCommands3_Panel
from Core.Database.Dialogs import ChooseSwitchVariable_Dialog
from Core.Panels import PanelBase
from Core.Database import Manager as DM
#--------------------------------------------------------------------------------------
# CommonEvents_Panel
#--------------------------------------------------------------------------------------

# Implementing CommonEvents_Panel
class CommonEvents_Panel( Templates.CommonEvents_Panel, PanelBase  ):
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


