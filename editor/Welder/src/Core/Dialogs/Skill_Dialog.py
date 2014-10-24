import wx


import Kernel


from PyitectConsumes import RGSS1_RPG as RPG
from PyitectConsumes import DatabaseManager as DM

ARC_FORMAT = False  # TEST


from PyitectConsumes import Skill_Dialog_Template


class Skill_Dialog(Skill_Dialog_Template):

    def __init__(self, parent, skills, maxlevel, level=1, skill_id=1):
        """.Basic constructor for the skills dialog."""
        Skill_Dialog_Template.__init__(self, parent)
        self.spinCtrlLevel.SetRange(1, maxlevel)
        self.spinCtrlLevel.SetValue(level)

        config = Kernel.Config
        digits = len(config.get('GameObjects', 'Skills'))

        if ARC_FORMAT:
            start = 0
        else:
            start = 1
            skill_id -= 1
        items = ["".join([str(i).zfill(digits), ': ',
                          skills[i].name]) for i in range(start, len(skills))]
        self.comboBoxSkills.AppendItems(items)
        self.comboBoxSkills.SetSelection(skill_id)

    def GetLearning(self):
        """Creates a RPG.Class.Learning instance from the data and returns it"""
        learning = RPG.Class.Learning()
        learning.level = self.spinCtrlLevel.GetValue()
        learning.skill_id = self.comboBoxSkills.GetSelection()
        if not ARC_FORMAT:
            learning.skill_id += 1
        return learning

    def buttonOK_Clicked(self, event):
        """Closes the dialog with a result of wx.ID_OK"""
        self.EndModal(wx.ID_OK)

    def buttonCancel_Clicked(self, event):
        """Closes the dialog with a result of wx.ID_CANCEL"""
        self.EndModal(wx.ID_CANCEL)
