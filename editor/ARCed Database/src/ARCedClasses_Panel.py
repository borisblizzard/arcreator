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
			self.listBoxClasses.Append(str(i).zfill(len(str(Limits['actors']))) + ': ' + klass.name)

	def refreshWeapons(self):
		pass

	def refreshArmors(self):
		pass

	def refreshStates(self):
		pass

	def refreshElements(self):
		pass

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


	@staticmethod
	def FixedIndex(index):
		''' Returns the correct starting index for game data structure depending on the current format '''
		if ARC_FORMAT:
			return index
		else:
			return index + 1