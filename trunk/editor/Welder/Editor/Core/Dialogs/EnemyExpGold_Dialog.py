import wx


import Kernel


from PyitectConsumes import EnemyExpGold_Dialog_Template


class EnemyExpGold_Dialog(EnemyExpGold_Dialog_Template):

    def __init__(self, parent, label, max, current=0, variance=None):
        """Basic constructor for the dialog"""
        EnemyExpGold_Dialog_Template.__init__(self, parent)
        self.labelType.SetLabel(label)
        self.spinCtrlValue.SetRange(0, max)
        self.spinCtrlVariance.SetRange(0, max)
        self.spinCtrlValue.SetValue(current)
        if variance is None:
            self.spinCtrlVariance.Disable()
        else:
            self.spinCtrlVariance.SetValue(variance)

    def GetValues(self):
        """Returns the value defined and the variance in a two element tuple"""
        return (self.spinCtrlValue.GetValue(), self.spinCtrlVariance.GetValue())

    def buttonOK_Clicked(self, event):
        """Closes the dialog and returns wx.ID_OK"""
        self.EndModal(wx.ID_OK)

    def buttonCancel_Clicked(self, event):
        """Closes the dialog and returns wx.ID_CANCEL"""
        self.EndModal(wx.ID_CANCEL)
