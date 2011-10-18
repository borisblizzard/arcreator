from Kernel import GlobalObjects
import DatabaseActions#, DatabasePackage
import wx
import ARCed_Templates
import ARCedChangeMaximum_Dialog, ARCedSkill_Dialog
import maxvalues
from RMXPProject import Project
import RGSS1_RPG as RPG

# Implementing Classes_Panel
class ARCedClasses_Panel( ARCed_Templates.Classes_Panel ):
	def __init__( self, parent ):
		ARCed_Templates.Classes_Panel.__init__( self, parent )
		if not GlobalObjects.has_key('DatabaseConfiguration'):
			config = maxvalues.DatabaseLimits('ini/DatabaseLimits.ini')
			GlobalObjects.request_new_key('DatabaseConfiguration', 'CORE', config)
		global Limits, DigitMax
		Limits = GlobalObjects.get_value('DatabaseConfiguration').Classes
		DigitMax = len(str(Limits['maxclasses']))

		for i in range(20):
			Project.Data_classes.append(RPG.Class())
			Project.Data_skills.append(RPG.Skill())

		self.refreshClassList()
		self.listBoxClasses.Select(0)
		
	
	def refreshClassList( self ):
		i = 0
		for klass in Project.Data_classes:
			i += 1
			self.listBoxClasses.Append(str(i).zfill(DigitMax) + ': ' + klass.name)
	
	# Handlers for Classes_Panel events.
	def listBoxClasses_SelectionChanged( self, event ):
		i = self.listBoxClasses.GetSelection() + 1
		if Project.Data_classes[i] == None:
			Project.Data_classes[i] = RPG.Class()
		self.textCtrlName.SetValue(Project.Data_classes[i].name)


	def buttonMaximum_Clicked( self, event ):
		""" Shows dialog for changing the list capacity """
		items = self.listBoxClasses.GetItems()
		currentMax = len(items)
		maxsClasses = Limits['maxclasses']
		dlg = ARCedChangeMaximum_Dialog.ARCedChangeMaximum_Dialog(self, currentMax, 1, maxClasses)
		if dlg.ShowModal() == wx.ID_OK:
			newMax = dlg.spinCtrlMaximum.GetValue()
			if newMax != currentMax: 
				if newMax > currentMax:
					newClasses = [None for i in xrange(newMax - currentMax)]
					newLabels = [str(1 + currentMax + i).zfill(DigitMax) + ': ' for i in xrange(newMax - currentMax)]
					Project.Data_classes.extend(newClasses)
					self.listBoxClasses.InsertItems(newLabels, currentMax)
				else:
					if self.listBoxClasses.GetSelection() >= newMax:
						self.listBoxClasses.Select(newMax - 1)
					del Project.Data_classes[newMax:currentMax]
					for i in reversed(range(currentMax)):
						if i >= newMax:
							self.listBoxClasses.Delete(i)
						else:
							break;
		dlg.Destroy()		

	def textCtrlName_TextChanged( self, event ):
		# TODO: Implement textCtrlName_TextChanged
		pass

	def checkListWeapons_CheckChanged( self, event ):
		# TODO: Implement checkListWeapons_CheckChanged
		pass

	def buttonWeaponAll_Clicked( self, event ):
		# TODO: Implement buttonWeaponAll_Clicked
		pass

	def buttonWeaponNone_Clicked( self, event ):
		# TODO: Implement buttonWeaponNone_Clicked
		pass

	def comboBoxPosition_SelectionChanged( self, event ):
		# TODO: Implement comboBoxPosition_SelectionChanged
		pass

	def checkListArmors_CheckChanged( self, event ):
		# TODO: Implement checkListArmors_CheckChanged
		pass

	def buttonArmorAll_Clicked( self, event ):
		# TODO: Implement buttonArmorAll_Clicked
		pass

	def buttonArmorNone_Clicked( self, event ):
		# TODO: Implement buttonArmorNone_Clicked
		pass

	def checkListElements_CheckChanged( self, event ):
		# TODO: Implement checkListElements_CheckChanged
		pass

	def checkListStates_ChceckChanged( self, event ):
		# TODO: Implement checkListStates_ChceckChanged
		pass

	def listBoxSkills_DoubleClick( self, event ):
		# TODO: Implement listBoxSkills_DoubleClick
		pass


