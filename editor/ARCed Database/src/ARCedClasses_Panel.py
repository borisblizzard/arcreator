import Kernel 
from Kernel import Manager as KM

import DatabaseActions#, DatabasePackage
import wx
import ARCed_Templates
import ARCedChangeMaximum_Dialog, ARCedSkill_Dialog
import maxvalues
import RGSS1_RPG as RPG
#from RMXPProject import Project
import time

# Implementing Classes_Panel
class ARCedClasses_Panel( ARCed_Templates.Classes_Panel ):
	def __init__( self, parent ):
		ARCed_Templates.Classes_Panel.__init__( self, parent )
		global Limits, DigitMax, Project
		Project = Kernel.GlobalObjects.get_value('PROJECT')
		Limits = Kernel.GlobalObjects.get_value('DatabaseConfiguration').GameObjects
		DigitMax = len(str(Limits['classes']))
		self.refreshClassList()
		self.listBoxClasses.Select(0)
	
	def benchMark(self, iterations, method, *args):
		total = 0
		for i in xrange(iterations):
			start = time.time()
			method(*args)
			total += (time.time() - start)
		print total / iterations

	def refreshClassList( self ):
		self.listBoxClasses.Clear()
		for i, klass in enumerate(Project.Data_classes): 
			self.listBoxClasses.Append(str(i + 1).zfill(DigitMax) + ': ' + klass.name)

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


