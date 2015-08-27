import wx

import Kernel

from PyitectConsumes import AddParameter_Dialog_Template

# -------------------------------------------------------------------------
# AddParameter_Dialog
# -------------------------------------------------------------------------

# Implementing AddParameter_Dialog


class AddParameter_Dialog(AddParameter_Dialog_Template):

    def __init__(self, parent):
        AddParameter_Dialog_Template.__init__(self, parent)

    def buttonOK_Clicked(self, event):
        """End the dialog and return wx.ID_OK"""
        self.EndModal(wx.ID_OK)

    def buttonCancel_Clicked(self, event):
        """End the dialog and return wx.ID_CANCEL"""
        self.EndModal(wx.ID_CANCEL)
