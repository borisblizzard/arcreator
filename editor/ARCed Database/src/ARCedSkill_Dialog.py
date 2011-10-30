import wx
import ARCed_Templates

import Kernel
from Kernel import Manager as KM

class ARCedSkill_Dialog( ARCed_Templates.Skill_Dialog ):
	def __init__( self, parent, skills, maxlevel, level=1, skill_id=1 ):
		''' Basic constructor for the skills dialog '''
		ARCed_Templates.Skill_Dialog.__init__( self, parent )
		self.spinCtrlLevel.SetRange(1, maxlevel)
		self.spinCtrlLevel.SetValue(level)
		limits = Kernel.GlobalObjects.get_value('DatabaseConfiguration').GameObjects
		digits = len(str(limits['skills']))
		
	
	def GetLevel( self ):
		''' Returns the value of the level spin control '''
		return self.spinCtrlLevel.GetValue()

	def GetSkill( self ):
		''' Returns the index of the skill combo box '''
		return self.comboBoxSkills.GetSelection()
	
	def buttonOK_Clicked( self, event ):
		''' Closes the dialog with a result of wx.ID_OK '''
		self.EndModal(wx.ID_OK)
	
	def buttonCancel_Clicked( self, event ):
		''' Closes the dialog with a result of wx.ID_CANCEL '''
		self.EndModal(wx.ID_CANCEL)
	
