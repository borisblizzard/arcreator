import wx

import welder_kernel as kernel

from PyitectConsumes import AnimationTweening_Dialog_Template

#-------------------------------------------------------------------------
# AnimationTweening_Dialog
#-------------------------------------------------------------------------

# Implementing AnimationTweening_Dialog
class AnimationTweening_Dialog(AnimationTweening_Dialog_Template):

    def __init__(self, parent):
        AnimationTweening_Dialog_Template.__init__(self, parent)

    # Handlers for AnimationTweening_Dialog events.
    def spinCtrlFramesStart_ValueChanged(self, event):
        # TODO: Implement spinCtrlFramesStart_ValueChanged
        pass

    def spinCtrlFramesEnd_ValueChanged(self, event):
        # TODO: Implement spinCtrlFramesEnd_ValueChanged
        pass

    def spinCtrlCellsStart_ValueChanged(self, event):
        # TODO: Implement spinCtrlCellsStart_ValueChanged
        pass

    def spinCtrlCellsEnd_ValueChanged(self, event):
        # TODO: Implement spinCtrlCellsEnd_ValueChanged
        pass

    def buttonOK_Clicked(self, event):
        # TODO: Implement buttonOK_Clicked
        pass

    def buttonCancel_Clicked(self, event):
        # TODO: Implement buttonCancel_Clicked
        pass
