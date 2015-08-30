import welder_kernel as kernel

from PyitectConsumes import PanelBase, CommonEvents_Panel_Template
from PyitectConsumes import DatabaseManager as DM

from PyitectConsumes import ChooseSwitchVariable_Dialog

# -------------------------------------------------------------------------
# CommonEvents_Panel
# -------------------------------------------------------------------------

# Implementing CommonEvents_Panel


class CommonEvents_Panel(CommonEvents_Panel_Template, PanelBase):

    _arc_panel_info = {
        "Name": "CommonEventsPanel",
        "Caption": "Common Events",
        "CaptionV": True,
        "Center": None,
        "CloseB": True,
        "DestroyOC": True,
        "Floatable": True,
        "Float": None,
        "IconARCM": 'commoneventsicon',
        "MaximizeB": True,
        "MinimizeB": True,
        "MinimizeM": ["POS_SMART", "CAPT_SMART"],
        "Movable": True,
        "NotebookD": True,
        "Resizable": True,
        "Snappable": True
    }

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
