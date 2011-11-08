import wx
import ARCed_Templates
from ARCedChangeMaximum_Dialog import ARCedChangeMaximum_Dialog
from ARCedSkill_Dialog import ARCedSkill_Dialog

from DatabaseManager import DatabaseManager as DM
from Core.RMXP import RGSS1_RPG as RPG	
from Core import RPGutil
import DatabaseActions
import Kernel 


class ARCedClasses_Panel( ARCed_Templates.Classes_Panel ):
	def __init__( self, parent, class_index=0 ):
		''' Basic constructor for the Classes panel '''
		ARCed_Templates.Classes_Panel.__init__( self, parent )
		global Config
		Config = Kernel.GlobalObjects.get_value('ARCed_config')
		global DataClasses, DataWeapons, DataArmors, DataStates, DataElements, DataSkills
		try:
			proj = Kernel.GlobalObjects.get_value('PROJECT')
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
		self.listCtrlSkills.InsertColumn(1, "Skill", width=160)		
		if DM.ARC_FORMAT:
			self.spinCtrlElements.SetRange(Config.getint('Classes', 'MinElemEfficiency'), 
				Config.getint('Classes', 'MaxElemEfficiency'))
			self.spinCtrlStates.SetRange(Config.getint('Classes', 'MinStateEfficiency'), 
				Config.getint('Classes', 'MaxStateEfficiency'))
		else:
			self.spinCtrlElements.SetRange(0, 5)
			self.spinCtrlStates.SetRange(0, 5)
		positions = Config.getlist('Classes', 'Positions')
		self.comboBoxPosition.AppendItems(positions)
		font = wx.Font(8, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		font.SetFaceName(Config.get('Misc', 'NoteFont')) 
		self.textCtrlNotes.SetFont(font)
		self.SelectedClass = DataClasses[DM.FixedIndex(class_index)]
		self.refreshAll()
		self.listBoxClasses.SetSelection(class_index)
		DM.DrawHeaderBitmap(self.bitmapClasses, 'Classes')

	def refreshAll( self ):
		''' Refreshes all child controls of the panel '''
		self.refreshClassList()
		self.refreshWeapons()
		self.refreshArmors()
		self.refreshStates()
		self.refreshElements()
		self.refreshSkills()
		self.refreshValues()

	def refreshClassList( self ):
		''' Refreshes the values in the class wxListBox control '''
		self.listBoxClasses.Clear()
		start = DM.FixedIndex(0)
		digits = len(Config.get('GameObjects', 'Classes'))
		klasses = [
		   ''.join([str(i).zfill(digits), ': ', 
			  DataClasses[i].name]) for i in xrange(start, len(DataClasses))]
		self.listBoxClasses.AppendItems(klasses)

	def refreshWeapons( self ):
		''' Clears and refreshes the list of weapons in the checklist '''
		self.checkListWeapons.Clear()
		start = DM.FixedIndex(0)
		names = [DataWeapons[i].name for i in xrange(start, len(DataWeapons))]
		self.checkListWeapons.InsertItems(names, 0)

	def refreshArmors( self ):
		''' Clears and refreshes the list of armors in the checklist '''
		self.checkListArmors.Clear()
		start = DM.FixedIndex(0)
		names = [DataArmors[i].name for i in xrange(start, len(DataArmors))]
		self.checkListArmors.InsertItems(names, 0)

	def refreshStates( self ):
		''' Clears and refreshes the list of states in the checklist '''
		self.listBoxStates.Clear()
		start = DM.FixedIndex(0)
		names = [DataStates[i].name for i in xrange(start, len(DataStates))]
		self.listBoxStates.InsertItems(names, 0)
		self.listBoxStates.SetSelection(0)

	def refreshElements( self ):
		''' Clears and refreshes the list of elements in the checklist '''
		self.listBoxElements.Clear()
		start = DM.FixedIndex(0)
		names = DataElements[start:]
		self.listBoxElements.InsertItems(names, 0)
		self.listBoxElements.SetSelection(0)

	def refreshSkills( self ):
		''' Clears and refreshes the list of skills in the list control '''
		self.listCtrlSkills.DeleteAllItems()
		self.SelectedClass.learnings = sorted(self.SelectedClass.learnings, cmp=self.LearningsSort)
		for i, skill in enumerate(self.SelectedClass.learnings):
			if not DM.ARC_FORMAT and i == 0:
				pass
			self.listCtrlSkills.InsertStringItem(i, "".join(['Lv. ', str(skill.level)]))
			digits = len(Config.get('GameObjects', 'Skills'))
			name = "".join([str(skill.skill_id).zfill(digits), ': ',  DataSkills[skill.skill_id].name])
			self.listCtrlSkills.SetStringItem(i, 1, name)

	def LearningsSort( self, learning1, learning2 ):
		''' Sorting method to sort class learnings by level '''
		if learning1.level > learning2.level: return 1
		elif learning1.level < learning2.level: return -1
		else: return 0

	def refreshValues( self ):
		''' Updates the values of all the controls to reflect the selected Class '''
		klass = self.SelectedClass
		self.textCtrlName.ChangeValue(klass.name)
		if klass.position >= self.comboBoxPosition.GetCount():
			klass.position = 0
		self.comboBoxPosition.SetSelection(klass.position)
		self.checkListWeapons.SetChecked([id - 1 for id in klass.weapon_set])
		self.checkListArmors.SetChecked([id - 1 for id in klass.armor_set])
		element = DM.FixedIndex(self.listBoxElements.GetSelection())
		state = DM.FixedIndex(self.listBoxStates.GetSelection())
		element = klass.element_ranks[element]
		state = klass.state_ranks[state]
		self.spinCtrlElements.SetValue(element)
		self.spinCtrlStates.SetValue(state)
		self.refreshSkills()
		if not hasattr(klass, 'note'):
			setattr(klass, 'note', '')
		self.textCtrlNotes.ChangeValue(klass.note)

	def listBoxClasses_SelectionChanged( self, event ):
		''' Ensures the class is not None, then refreshes the controls '''
		index = DM.FixedIndex(event.GetInt())
		if DataClasses[index] == None:
			klass = RPG.Class()
			start = DM.FixedIndex(0)
			default = 3
			if DM.ARC_FORMAT: data = 100
			klass.element_ranks = RPGutil.Table(len(DataElements))
			klass.state_ranks = RPGutil.Table(len(DataStates))
			for i in xrange(start, len(DataElements)):
				klass.element_ranks[i] = default
			for i in xrange(start, len(DataStates)):
				klass.state_ranks[i] = default
			DataClasses[index] = klass
		self.SelectedClass = DataClasses[index]
		self.refreshValues()

	def buttonMaximum_Clicked( self, event ):
		""" Shows dialog for changing the list capacity """
		items = self.listBoxClasses.GetItems()
		currentMax = len(items)
		maxClasses = Config.getint('GameObjects', 'Classes')
		dlg = ARCedChangeMaximum_Dialog(self, currentMax, 1, maxClasses)
		if dlg.ShowModal() == wx.ID_OK:
			newMax = dlg.spinCtrlMaximum.GetValue()
			if newMax != currentMax: 
				if newMax > currentMax:
					newClasses = [None for i in xrange(newMax - currentMax)]
					digits = len(Config.get('GameObjects', 'Classes'))
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
		digits = len(Config.get('GameObjects', 'Classes'))
		self.listBoxClasses.SetString(index, 
			"".join([str(DM.FixedIndex(index)).zfill(digits), ': ', name]))

	def checkListWeapons_CheckChanged( self, event ):
		''' Adds/Removes the weapon from the class weapon set as needed '''
		index = event.GetInt()
		if self.checkListWeapons.IsChecked(index):
			self.SelectedClass.weapon_set.append(DM.FixedIndex(index))
		else:
			self.SelectedClass.weapon_set.remove(DM.FixedIndex(index))

	def buttonWeaponAll_Clicked( self, event ):
		''' Checks all weapons and adds each weapon's ID to the class weapon set '''
		for i in xrange(self.checkListWeapons.GetCount()):
			self.checkListWeapons.Check(i, True)
		ids = [i for i in xrange(DM.FixedIndex(0), len(DataWeapons))]
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
			self.SelectedClass.armor_set.append(DM.FixedIndex(index))
		else:
			self.SelectedClass.armor_set.remove(DM.FixedIndex(index))

	def buttonArmorAll_Clicked( self, event ):
		''' Checks all armors and adds each armor's ID to the class armor set '''
		for i in xrange(self.checkListArmors.GetCount()):
			self.checkListArmors.Check(i, True)
		ids = [i for i in xrange(DM.FixedIndex(0), len(DataArmors))]
		self.SelectedClass.armor_set = ids

	def buttonArmorNone_Clicked( self, event ):
		''' Unchecks all armors and clears the class armor set '''
		for i in xrange(self.checkListArmors.GetCount()):
			self.checkListArmors.Check(i, False)
		self.SelectedClass.armor_set = []

	def listBoxElements_SelectionChanged( self, event ):
		''' Sets the value of the spin control to reflect the value of the element rank '''
		index = DM.FixedIndex(event.GetInt())
		value = self.SelectedClass.element_ranks[index]
		self.spinCtrlElements.SetValue(value)

	def listBoxStates_SelectionChanged( self, event ):
		''' Sets the value of the spin control to reflect the value of the state rank '''
		index = DM.FixedIndex(event.GetInt())
		value = self.SelectedClass.state_ranks[index]
		self.spinCtrlStates.SetValue(value)

	def spinCtrlElements_ValueChanged( self, event ):
		''' Sets the selected element rank for the class '''
		index = DM.FixedIndex(self.listBoxElements.GetSelection())
		self.SelectedClass.element_ranks[index] = event.GetInt()
		print self.SelectedClass.element_ranks[index]

	def spinCtrlStates_ValueChanged( self, event ):
		''' Sets the selected state rank for the class '''
		index = DM.FixedIndex(self.listBoxStates.GetSelection())
		self.SelectedClass.state_ranks[index] = event.GetInt()

	def GetSkillIndex( self ):
		''' Finds the selected index of the skill list control '''
		index = -1
		index = self.listCtrlSkills.GetNextItem(index, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
		return index

	def StartSkillDialog( self, index=-1 ):
		''' Opens the skill selection dialog '''
		edit = (index != -1 and index < len(self.SelectedClass.learnings))
		lvl = skill_id = 1
		if edit:
			lvl = self.SelectedClass.learnings[index].level
			skill_id = self.SelectedClass.learnings[index].skill_id
		maxlvl = Config.getint('Actors', 'MaxLevel')
		dialog = ARCedSkill_Dialog(self, DataSkills, maxlvl, lvl, skill_id)
		if dialog.ShowModal() == wx.ID_OK:
			if edit: del (self.SelectedClass.learnings[index])
			self.SelectedClass.learnings.append(dialog.GetLearning())
			self.refreshSkills()
		dialog.Destroy()

	def listCtrlSkills_DoubleClick( self, event ):
		''' Opens the skill dialog, using "edit mode" if a current item was clicked '''
		self.StartSkillDialog(self.GetSkillIndex())

	def buttonSkillRemove_Clicked( self, event ):
		''' Removes the selected item and refreshes the list. Does nothing if there is no selection '''
		index = self.GetSkillIndex()
		if index != -1 and index < len(self.SelectedClass.learnings):
			del (self.SelectedClass.learnings[index])
			self.refreshSkills()

	def buttonSkillAdd_Clicked( self, event ):
		''' Starts the skill dialog set to the default '''
		self.StartSkillDialog(-1)

	def listCtrlSkills_KeyDown( self, event ):
		''' Shortcut to use INSERT and DELETE to add/remove skills '''
		code = event.GetKeyCode()
		if code == wx.WXK_DELETE:
			self.buttonSkillRemove_Clicked(event)
		if code == wx.WXK_INSERT:
			self.StartSkillDialog(-1)

	def textCtrlNotes_TextChanged( self, event ):
		''' Updates the the value of the selected class's note '''
		self.SelectedClass.note = event.GetString()
