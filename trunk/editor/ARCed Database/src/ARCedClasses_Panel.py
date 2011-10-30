'''
Contains the functionality of all the events raised on the Classes Database panel

'''
import wx
import ARCed_Templates
from ARCedChangeMaximum_Dialog import ARCedChangeMaximum_Dialog
from ARCedSkill_Dialog import ARCedSkill_Dialog

import RGSS1_RPG as RPG
import maxvalues
import DatabaseActions
import Kernel 
from Kernel import Manager as KM

# TEST STUFF
ARC_FORMAT = False

class ARCedClasses_Panel( ARCed_Templates.Classes_Panel ):
	def __init__( self, parent ):
		''' Constructor for the Classes panel '''
		ARCed_Templates.Classes_Panel.__init__( self, parent )
		proj = Kernel.GlobalObjects.get_value('PROJECT')
		global DataClasses, DataWeapons, DataArmors, DataStates, DataElements, DataSkills, Limits
		try:
			DataClasses = proj.getData('Classes')
			DataWeapons = proj.getData('Weapons')
			DataArmors = proj.getData('Armors')
			DataStates = proj.getData('States')
			DataElements = proj.getData('System').elements
			DataSkills = proj.getData('Skills')
		except NameError:
			Kernel.Log('Database opened before Project has been initialized', '[Database:CLASSES]', True)
			self.Destroy()
		
		self.listCtrlSkills.InsertColumn(0, "Level", width=64)
		self.listCtrlSkills.InsertColumn(1, "Skill", width=148)		
		if ARC_FORMAT:
			# TODO: Implement loading these values from config
			self.spinCtrlElements.SetRange(-1000, 1000)
			self.spinCtrlStates.SetRange(-1000, 1000)
		else:
			self.spinCtrlElements.SetRange(0, 5)
			self.spinCtrlStates.SetRange(0, 5)

		Limits = Kernel.GlobalObjects.get_value('DatabaseConfiguration').GameObjects
		self.SelectedClass = DataClasses[self.FixedIndex(0)]
		self.refreshAll()

	def refreshAll(self):
		self.refreshClassList()
		self.refreshWeapons()
		self.refreshArmors()
		self.refreshStates()
		self.refreshElements()
		self.refreshSkills()
		self.refreshValues()

	def refreshClassList(self):
		''' Refreshes the values in the class wxListBox control '''
		self.listBoxClasses.Clear()
		for i, klass in enumerate(DataClasses):
			if not ARC_FORMAT and i == 0:
				continue
			text = "".join([str(i).zfill(len(str(Limits['classes']))), ': ', klass.name])
			self.listBoxClasses.Append(text)
		self.listBoxClasses.SetSelection(0)

	def refreshWeapons(self):
		''' Clears and refreshes the list of weapons in the checklist '''
		self.checkListWeapons.Clear()
		start = self.FixedIndex(0)
		names = [DataWeapons[i].name for i in xrange(start, len(DataWeapons))]
		self.checkListWeapons.InsertItems(names, 0)

	def refreshArmors(self):
		''' Clears and refreshes the list of armors in the checklist '''
		self.checkListArmors.Clear()
		start = self.FixedIndex(0)
		names = [DataArmors[i].name for i in xrange(start, len(DataArmors))]
		self.checkListArmors.InsertItems(names, 0)

	def refreshStates(self):
		''' Clears and refreshes the list of states in the checklist '''
		self.listBoxStates.Clear()
		start = self.FixedIndex(0)
		names = [DataStates[i].name for i in xrange(start, len(DataStates))]
		self.listBoxStates.InsertItems(names, 0)
		self.listBoxStates.SetSelection(0)

	def refreshElements(self):
		''' Clears and refreshes the list of elements in the checklist '''
		self.listBoxElements.Clear()
		start = self.FixedIndex(0)
		names = DataElements[start:]
		self.listBoxElements.InsertItems(names, 0)
		self.listBoxElements.SetSelection(0)

	def refreshSkills(self):
		''' Clears and refreshes the list of skills in the list control '''
		self.listCtrlSkills.DeleteAllItems()
		for i, skill in enumerate(self.SelectedClass.learnings):
			if not ARC_FORMAT and i == 0:
				pass
			self.listCtrlSkills.InsertStringItem(i, "".join(['Lv. ', str(skill.level)]))
			name = "".join([str(skill.skill_id).zfill(len(str(Limits['skills']))), ': ', 
				   DataSkills[skill.skill_id].name])
			self.listCtrlSkills.SetStringItem(i, 1, name)

	def refreshValues( self ):
		''' Updates the values of all the controls to reflect the selected Class '''
		self.textCtrlName.ChangeValue(self.SelectedClass.name)
		self.checkListWeapons.SetChecked([id - 1 for id in self.SelectedClass.weapon_set])
		self.checkListArmors.SetChecked([id - 1 for id in self.SelectedClass.armor_set])
		element = self.FixedIndex(self.listBoxElements.GetSelection())
		state = self.FixedIndex(self.listBoxStates.GetSelection())

		element = self.SelectedClass.element_ranks[[element]]
		state = self.SelectedClass.state_ranks[[state]]

		self.spinCtrlElements.SetValue(element)
		self.spinCtrlStates.SetValue(state)

	def listBoxClasses_SelectionChanged( self, event ):
		''' Ensures the class is not None, then refreshes the controls '''
		index = self.FixedIndex(event.GetInt())
		if DataClasses[index] == None:
			DataClasses[index] = RPG.Class()
		self.SelectedClass = DataClasses[index]
		self.refreshValues()

	def buttonMaximum_Clicked( self, event ):
		""" Shows dialog for changing the list capacity """
		items = self.listBoxClasses.GetItems()
		currentMax = len(items)
		maxClasses = Limits['classes']
		dlg = ARCedChangeMaximum_Dialog(self, currentMax, 1, maxClasses)
		if dlg.ShowModal() == wx.ID_OK:
			newMax = dlg.spinCtrlMaximum.GetValue()
			if newMax != currentMax: 
				if newMax > currentMax:
					newClasses = [None for i in xrange(newMax - currentMax)]
					digits = len(str(Limits['classes']))
					newLabels = [
						"".join([str(1 + currentMax + i).zfill(digits), 
						': ']) for i in xrange(newMax - currentMax)]
					DataClasses.extend(newClasses)
					self.listBoxClasses.InsertItems(newLabels, currentMax)
				else:
					if self.listBoxClasses.GetSelection() >= newMax:
						self.listBoxClasses.Select(newMax - 1)
					del DataClasses[newMax:currentMax]
					for i in reversed(range(currentMax)):
						if i >= newMax:
							self.listBoxClasses.Delete(i)
						else:
							break;
		dlg.Destroy()		

	def textCtrlName_TextChanged( self, event ):
		''' Changes the name of the class '''
		index = self.listBoxClasses.GetSelection()
		name = self.textCtrlName.GetLineText(0)
		self.SelectedClass.name = name
		self.listBoxClasses.SetString(index, 
			"".join([str(self.FixedIndex(index)).zfill(len(str(Limits['classes']))), ': ', name]))

	def checkListWeapons_CheckChanged( self, event ):
		''' Adds/Removes the weapon from the class weapon set as needed '''
		index = event.GetInt()
		if self.checkListWeapons.IsChecked(index):
			self.SelectedClass.weapon_set.append(self.FixedIndex(index))
		else:
			self.SelectedClass.weapon_set.remove(self.FixedIndex(index))

	def buttonWeaponAll_Clicked( self, event ):
		''' Checks all weapons and adds each weapon's ID to the class weapon set '''
		for i in xrange(self.checkListWeapons.GetCount()):
			self.checkListWeapons.Check(i, True)
		ids = [i for i in xrange(self.FixedIndex(0), len(DataWeapons))]
		self.SelectedClass.weapon_set = ids

	def buttonWeaponNone_Clicked( self, event ):
		''' Unchecks all weapons and clears the class weapon set '''
		for i in xrange(self.checkListWeapons.GetCount()):
			self.checkListWeapons.Check(i, False)
		self.SelectedClass.weapon_set = []

	def comboBoxPosition_SelectionChanged( self, event ):
		''' Sets the position of the selected class to the index of the combo box '''
		self.SelectedClass.position = event.GetInt()

	def checkListArmors_CheckChanged( self, event ):
		''' Adds/Removes the armor from the class armor set as needed '''
		index = event.GetInt()
		if self.checkListArmors.IsChecked(index):
			self.SelectedClass.armor_set.append(self.FixedIndex(index))
		else:
			self.SelectedClass.armor_set.remove(self.FixedIndex(index))

	def buttonArmorAll_Clicked( self, event ):
		''' Checks all armors and adds each armor's ID to the class armor set '''
		for i in xrange(self.checkListArmors.GetCount()):
			self.checkListArmors.Check(i, True)
		ids = [i for i in xrange(self.FixedIndex(0), len(DataArmors))]
		self.SelectedClass.armor_set = ids

	def buttonArmorNone_Clicked( self, event ):
		''' Unchecks all armors and clears the class armor set '''
		for i in xrange(self.checkListArmors.GetCount()):
			self.checkListArmors.Check(i, False)
		self.SelectedClass.armor_set = []

	def listBoxElements_SelectionChanged( self, event ):
		''' Sets the value of the spin control to reflect the value of the element rank '''
		index = self.FixedIndex(event.GetInt())
		value = self.SelectedClass.element_ranks[[index]]
		self.spinCtrlElements.SetValue(value)

	def listBoxStates_SelectionChanged( self, event ):
		''' Sets the value of the spin control to reflect the value of the state rank '''
		index = self.FixedIndex(event.GetInt())
		value = self.SelectedClass.state_ranks[[index]]
		self.spinCtrlStates.SetValue(value)

	def spinCtrlElements_ValueChanged( self, event ):
		''' Sets the selected element rank for the class '''
		index = self.FixedIndex(self.listBoxElements.GetSelection())
		self.SelectedClass.element_ranks[[index]] = event.GetInt()
		print self.SelectedClass.element_ranks[[index]]

	def spinCtrlStates_ValueChanged( self, event ):
		''' Sets the selected state rank for the class '''
		index = self.FixedIndex(self.listBoxStates.GetSelection())
		self.SelectedClass.state_ranks[[index]] = event.GetInt()

	def listBoxSkills_DoubleClick( self, event ):
		''' Opens the skill selection dialog '''
		# TODO: Remove TEST
		level = 4
		skill_id = 4
		maxlevel = 999

		dialog = ARCedSkill_Dialog(self, DataSkills, maxlevel, level, skill_id)
		dialog.ShowModal()

	def textCtrlNotes_TextChanged( self, event ):
		pass


	@staticmethod
	def FixedIndex(index):
		''' Returns the correct starting index for game data structure depending on the current format '''
		if ARC_FORMAT:
			return index
		else:
			return index + 1