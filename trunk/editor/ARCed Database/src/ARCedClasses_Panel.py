'''
Contains the functionality of all the events raised on the Classes Database panel

'''
import wx
import ARCed_Templates
import ARCedChangeMaximum_Dialog
import ARCedSkill_Dialog

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
			print DataStates
			DataElements = proj.getData('System').elements
			DataSkills = proj.getData('Skills')
		except NameError:
			Kernel.Log('Database opened before Project has been initialized', '[Database:CLASSES]', True)
			self.Destroy()
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

	def refreshClassList(self):
		''' Refreshes the values in the class wxListBox control '''
		self.listBoxClasses.Clear()
		for i, klass in enumerate(DataClasses):
			if not ARC_FORMAT and i == 0:
				continue
			text = "".join([str(i).zfill(len(str(Limits['actors']))), ': ', klass.name])
			self.listBoxClasses.Append(text)

	def refreshWeapons(self):
		self.checkListWeapons.Clear()
		start = self.FixedIndex(0)
		names = [DataWeapons[i].name for i in xrange(start, len(DataWeapons))]
		self.checkListWeapons.InsertItems(names, 0)


	def refreshArmors(self):
		self.checkListArmors.Clear()
		start = self.FixedIndex(0)
		names = [DataArmors[i].name for i in xrange(start, len(DataArmors))]
		self.checkListArmors.InsertItems(names, 0)

	def refreshStates(self):
		self.listBoxStates.Clear()
		start = self.FixedIndex(0)
		names = [DataStates[i].name for i in xrange(start, len(DataStates))]
		self.listBoxStates.InsertItems(names, 0)

	def refreshElements(self):
		self.listBoxElements.Clear()
		start = self.FixedIndex(0)
		names = [DataElements[i].name for i in xrange(start, len(DataElements))]
		self.listBoxElements.InsertItems(0, names)

	def refreshSkills(self):
		pass

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
		maxsClasses = Limits['classes']
		dlg = ARCedChangeMaximum_Dialog.ARCedChangeMaximum_Dialog(self, currentMax, 1, maxClasses)
		if dlg.ShowModal() == wx.ID_OK:
			newMax = dlg.spinCtrlMaximum.GetValue()
			if newMax != currentMax: 
				if newMax > currentMax:
					newClasses = [None for i in xrange(newMax - currentMax)]
					newLabels = [
						"".join([str(1 + currentMax + i).zfill(DigitMax), ': ']) for i in xrange(newMax - currentMax)]
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
		# TODO: Implement checkListElements_CheckChanged
		pass

	def listBoxStates_SelectionChanged( self, event ):
		# TODO: Implement checkListStates_ChceckChanged
		pass

	def spinCtrlElements_ValueChanged( self, event ):
		pass

	def spinCtrlStates_ValueChanged( self, event ):
		pass

	def listBoxSkills_DoubleClick( self, event ):
		# TODO: Implement listBoxSkills_DoubleClick
		pass

	def textCtrlNotes_TextChanged( self, event ):
		pass


	@staticmethod
	def FixedIndex(index):
		''' Returns the correct starting index for game data structure depending on the current format '''
		if ARC_FORMAT:
			return index
		else:
			return index + 1