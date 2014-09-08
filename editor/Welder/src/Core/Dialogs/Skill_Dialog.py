import wx

from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')
Templates = Core.Database.Welder_Templates

RPG	= Core.RMXP.RGSS1_RPG.RPG
DM = Core.Database.Manager	

ARC_FORMAT = False # TEST

class Skill_Dialog( Templates.Skill_Dialog ):
	def __init__( self, parent, skills, maxlevel, level=1, skill_id=1 ):
		""".Basic constructor for the skills dialog."""
		Templates.Skill_Dialog.__init__( self, parent )
		self.spinCtrlLevel.SetRange(1, maxlevel)
		self.spinCtrlLevel.SetValue(level)

		config = Kernel.GlobalObjects.get_value('Welder_config')
		digits = len(config.get('GameObjects', 'Skills'))

		if ARC_FORMAT: start = 0 
		else: 
			start = 1
			skill_id -= 1
		items = ["".join([str(i).zfill(digits), ': ', 
			skills[i].name]) for i in range(start, len(skills))]
		self.comboBoxSkills.AppendItems(items)
		self.comboBoxSkills.SetSelection(skill_id)
	
	def GetLearning( self ):
		"""Creates a RPG.Class.Learning instance from the data and returns it"""
		learning = RPG.Class.Learning()
		learning.level = self.spinCtrlLevel.GetValue()
		learning.skill_id = self.comboBoxSkills.GetSelection()
		if not ARC_FORMAT:
			learning.skill_id += 1
		return learning
	
	def buttonOK_Clicked( self, event ):
		"""Closes the dialog with a result of wx.ID_OK"""
		self.EndModal(wx.ID_OK)
	
	def buttonCancel_Clicked( self, event ):
		"""Closes the dialog with a result of wx.ID_CANCEL"""
		self.EndModal(wx.ID_CANCEL)
	
