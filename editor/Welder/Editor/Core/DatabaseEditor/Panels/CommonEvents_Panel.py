import Kernel

from PyitectConsumes import PanelBase, CommonEvents_Panel_Template
from PyitectConsumes import DatabaseManager as DM

from PyitectConsumes import ChooseSwitchVariable_Dialog

# -------------------------------------------------------------------------
# CommonEvents_Panel
# -------------------------------------------------------------------------

# Implementing CommonEvents_Panel


class CommonEvents_Panel(CommonEvents_Panel_Template, PanelBase):

    _arc_panel_info_string = "Name Caption Center CloseB CaptionV DestroyOC Floatable Float IconARCM MaximizeB MinimizeM MinimizeB Movable NotebookD Resizable Snappable"
    _arc_panel_info_data = {"Name": "Common Events Panel", "Caption": "Common Events Panel", "CaptionV": True,  "MinimizeM": ["POS_SMART", "CAPT_SMART", ],
                            "MinimizeB": True, "CloseB": True, 'IconARCM': 'commoneventsicon'}

    def __init__(self, parent):
        CommonEvents_Panel_Template.__init__(self, parent)

        DM.DrawHeaderBitmap(self.bitmapCommonEvents, 'Common Events')

        # Bind the panel tot he Panel Manager
        self.bindPanelManager()

    # Handlers for CommonEvents_Panel events.
    def listBoxCommonEvents_SelectionChanged(self, event):
        # TODO: Implement listBoxCommonEvents_SelectionChanged
        pass

    def buttonMaximum_Clicked(self, event):
        # TODO: Implement buttonMaximum_Clicked
        pass

    def textCtrlName_ValueChanged(self, event):
        # TODO: Implement textCtrlName_ValueChanged
        pass

    def comboBoxTrigger_SelectionChanged(self, event):
        # TODO: Implement comboBoxTrigger_SelectionChanged
        pass

    def comboBoxCondition_Clicked(self, event):
        # TODO: Implement comboBoxCondition_Clicked
        pass

    def listBoxEvents_DoubleClicked(self, event):
        # TODO: Implement listBoxEvents_DoubleClicked
        pass

    def listBoxPage_SelectionChanged(self, event):
        # TODO: Implement listBoxPage_SelectionChanged
        pass
