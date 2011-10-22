from Kernel import GlobalObjects
import DatabaseActions#, DatabasePackage # Import once Kernel registration actually works
import wx
import ARCed_Templates
import ARCedChangeMaximum_Dialog, ARCedExpCurve_Dialog, ARCedGenerateCurve_Dialog
import ARCedChooseGraphic_Dialog, ARCedActorParameters_Dialog, ARCedAddParameter_Dialog

import RGSS1_RPG as RPG					# Remove after testing
import maxvalues						# Change Later
from RPGutil import Table
from RMXPProject import Project

RGSS_COMPATIBLE = False#True

class ARCedActors_Panel( ARCed_Templates.Actors_Panel ):
	def __init__( self, parent, actorIndex=0 ):
		""" Initializes the Actors panel """
		ARCed_Templates.Actors_Panel.__init__( self, parent )
		if not GlobalObjects.has_key('DatabaseConfiguration'):
			config = maxvalues.DatabaseLimits('ini/DatabaseLimits.ini')
			GlobalObjects.request_new_key('DatabaseConfiguration', 'CORE', config)
		global Limits, ActorLimits, SelectedActor
		self.buttonRemoveParameter.Enabled = False
		Limits = GlobalObjects.get_value('DatabaseConfiguration').GameObjects
		ActorLimits = GlobalObjects.get_value('DatabaseConfiguration').Actors
		self.ParamTab = 0
		self.spinCtrlFinalLevel.SetRange(1, ActorLimits['finallevel'])
		SelectedActor = Project.Data_actors[0]
		self.refreshAll()

	def SetParameterValue(self, param, level, value):
		""" Sets the newly defined value for the selected actor's parameter """
		SelectedActor.parameters[param, level] = value

	def GetParameterValue( self, index, level ):
		""" Retrieves the value of the current actor's selected parameter for the defined level """
		if SelectedActor.parameters.xsize <= index:
			for actor in Project.Data_actors:
				actor.parameters.resize(index + 1, ActorLimits['finallevel'])
				for i in xrange(1, ActorLimits['finallevel']):
					actor.parameters[index, i] = 50 + 5 * i
		return SelectedActor.parameters[index, level]

	def refreshActorList(self):
		""" Refreshes the values in the actor wxListBox control """
		self.listBoxActors.Clear()
		index = self.listBoxActors.GetSelection()
		for i, actor in enumerate(Project.Data_actors):
			self.listBoxActors.Append(str(i + 1).zfill(len(str(Limits['actors']))) + ': ' + actor.name)

	def refreshClasses(self):
		""" Refreshes the values in the class wxChoice control """
		self.comboBoxClass.Clear()
		for i, klass in enumerate(Project.Data_classes):
			self.comboBoxClass.Append(str(i + 1).zfill(len(str(Limits['classes']))) + ': ' + klass.name)
		self.comboBoxClass.Select(SelectedActor.class_id - 1)

	def refreshWeapons(self):
		""" Refreshes the values in the weapon wxChoice control """
		self.comboBoxWeapon.Clear()
		self.comboBoxWeapon.Append('(None)')
		weapon_set = Project.Data_classes[SelectedActor.class_id].weapon_set
		wpnIndex = 0
		for weapon, i in enumerate(Project.Data_weapons):
			if i not in weapon_set:
				continue
			self.comboBoxWeapon.Append(str(i).zfill(len(str(Limits['weapons']))) + ': ' + weapon.name)
			if SelectedActor.weapon_id == i:
				wpnIndex = self.comboBoxWeapon.GetCount()
		self.comboBoxWeapon.Select(wpnIndex)

	def refreshArmors(self):
		""" Refreshes the values in the wxChoice controls for shield, helmet,  armor, and accessory """
		# This needs massively improved, and needs to be modular, but works for now  

		# Create this dynamically instead of like this
		armorBoxes = [self.comboBoxShield, self.comboBoxHelmet, 
				self.comboBoxBodyArmor, self.comboBoxAccessory]
		armorFixChecks = [self.checkBoxShield, self.checkBoxHelmet,
				self.checkBoxBodyArmor, self.checkBoxAccessory]
		armorFixes = [SelectedActor.armor1_fix, SelectedActor.armor2_fix,
				SelectedActor.armor3_fix, SelectedActor.armor4_fix]
		currentArmor = [SelectedActor.armor1_id, SelectedActor.armor2_id,
				SelectedActor.armor3_id, SelectedActor.armor4_id]
		armorIndices = []
		armor_set = Project.Data_classes[SelectedActor.class_id].armor_set

		for i in xrange(len(armorBoxes)):
			armorBoxes[i].Clear()
			armorBoxes[i].Append('(None)')
			armorIndices.append(0)
			armorFixChecks[i].SetValue(armorFixes[i])
			
		for armor, i in enumerate(Project.Data_armors):
			if i not in armor_set:
				continue
			text = str(i).zfill(len(str(Limits['armors']))) + ': ' + armor.name
			armorBoxes[armor.kind].Append(text)
			if currentArmor[armor.kind] == i:
				armorIndices[armor.kind] = armorBoxes[armor.kind].GetCount() - 1

		for i in xrange(len(armorBoxes)):
			armorFixChecks[i].SetValue(armorFixes[i])
			armorBoxes[i].Select(armorIndices[i])


	def refreshAll(self):
		""" Refreshes all the controls that contain game object values """
		self.textCtrlName.SetValue(SelectedActor.name)
		self.refreshActorList()
		self.refreshClasses()
		self.refreshWeapons()
		self.refreshArmors()

	def listBoxActors_SelectionChanged( self, event ):
		""" Changes the data on the panel to reflect the values of the selected actor """
		index = self.listBoxActors.GetSelection()
		if Project.Data_actors[index] == None:
			Project.Data_actors[index] = RPG.Actor()
		SelectedActor = Project.Data_actors[index]
		self.refreshWeapons()
		self.refreshArmors()

	def buttonMaximum_Clicked( self, event ):
		""" Shows dialog for changing the list capacity """
		items = self.listBoxActors.GetItems()
		currentMax = len(items)
		dlg = ARCedChangeMaximum_Dialog.ARCedChangeMaximum_Dialog(self, currentMax, 1, Limits['actors'])
		if dlg.ShowModal() == wx.ID_OK:
			newMax = dlg.spinCtrlMaximum.GetValue()
			if newMax != currentMax: 
				if newMax > currentMax:
					newActors = [None for i in xrange(newMax - currentMax)]
					newLabels = [str(1 + currentMax + i).zfill(len(str(Limits['actors']))) + 
						': ' for i in xrange(newMax - currentMax)]
					Project.Data_actors.extend(newActors)
					self.listBoxActors.InsertItems(newLabels, currentMax)
				else:
					if self.listBoxActors.GetSelection() >= newMax:
						self.listBoxActors.Select(newMax - 1)
					del Project.Data_actors[newMax:currentMax]
					for i in reversed(range(currentMax)):
						if i >= newMax:
							self.listBoxActors.Delete(i)
						else:
							break;
		dlg.Destroy()

	def textBoxName_TextChanged( self, event ):
		""" Renames the selected actor and syncs text with the ListBox control """
		index = self.listBoxActors.GetSelection()
		if index >= 0:
			name = self.textCtrlName.GetLineText(0)
			SelectedActor.name = name
			self.listBoxActors.SetString(index, str(1 + index).zfill(len(str(Limits['actors']))) + 
				': ' + name)

	def comboBoxClass_SelectionChanged( self, event ):
		""" Removes any initial equipment that may be equipped if the chosen class does not permit """
		class_index = self.comboBoxClass.GetSelection()
		wpn_index = self.comboBoxWeapon.GetSelection()
		armor_indices = [
				   self.comboBoxShield.GetSelection(),
				   self.comboBoxHelmet.GetSelection(),
				   self.comboBoxBodyArmor.GetSelection(),
				   self.comboBoxAccessory.GetSelection()
				]
		if wpn_index not in Project.Data_classes[class_index].weapon_set:
			self.comboBoxWeapon.SetSelection(0)
			SelectedActor.weapon_id = 0
		for armor_index in armor_indices:
			if armor_index not in Project.Data_classes[class_index].armor_set:
				if Project.Data_armors[armor_index].kind == 0: # Shield
					self.comboBoxShield.SetSelection(0)
					SelectedActor.armor1_id = 0
				elif Project.Data_armors[armor_index].kind == 1: # Helmet
					self.comboBoxHelmet.SetSelection(0)
					SelectedActor.armor2_id = 0
				elif Project.Data_armors[armor_index].kind == 2: # Body Armor
					self.comboBoxBodyArmor.SetSelection(0)
					SelectedActor.armor3_id = 0
				elif Project.Data_armors[armor_index].kind == 3: # Accessory
					self.comboBoxAccessory.SetSelection(0)
					SelectedActor.armor4_id = 0
		self.refreshWeapons()
		self.refreshArmors()

	def spinCtrlInitialLevel_ValueChanged( self, event ):
		""" Sets the selected actor's initial level to the value of the wxSpinCtrl """
		SelectedActor.initial_level = self.spinCtrlInitialLevel.GetValue()

	def spinCtrlFinalLevel_ValueChanged( self, event ):
		""" Sets the selected actor's final level to the value of the wxSpinCtrl """
		SelectedActor.final_level = self.spinCtrlFinalLevel.GetValue()

	def comboBoxExperience_Click( self, event ):
		""" Opens window to generate experience tables """
		actor = SelectedActor
		dlg = ARCedExpCurve_Dialog.ARCedExpCurve_Dialog(self, actor, ActorLimits)
		if dlg.ShowModal() == wx.ID_OK:
			actor.exp_basis = dlg.Basis
			actor.exp_inflation = dlg.Inflation
		dlg.Destroy()

	def bitmapCharacterGraphic_Click( self, event ):
		""" Opens dialog to change the character graphic """
		# TODO: Have 'path' set to projects character graphics folder
		path = 'images'
		name = SelectedActor.character_name
		hue = SelectedActor.character_hue
		dlg = ARCedChooseGraphic_Dialog.ARCedChooseGraphic_Dialog(self, path, name, hue)
		if dlg.ShowModal() == wx.ID_OK:
			index = dlg.listBoxGraphics.GetSelection()
			SelectedActor.character_name = dlg.listBoxGraphics.GetString(index)
			SelectedActor.character_hue = dlg.sliderHue.GetValue()
			# TODO: Implement splitting to show only single frame of character graphic
			self.bitmapCharacterGraphic.SetBitmap(wx.Bitmap(dlg.Images[index]))
		dlg.Destroy()

	def bitmapBattlerGraphic_Click( self, event ):
		""" Opens dialog to change the battler graphic """
		# TODO: Have 'path' set to projects battler graphics folder
		path = 'images'
		name = SelectedActor.battler_name
		hue = SelectedActor.battler_hue
		dlg = ARCedChooseGraphic_Dialog.ARCedChooseGraphic_Dialog(self, path, name, hue)
		if dlg.ShowModal() == wx.ID_OK:
			index = dlg.listBoxGraphics.GetSelection()
			SelectedActor.battler_name = dlg.listBoxGraphics.GetString(index)
			SelectedActor.battler_hue = dlg.sliderHue.GetValue()
			self.bitmapBattlerGraphic.SetBitmap(wx.Bitmap(dlg.Images[index]))
		dlg.Destroy()

	def comboBoxWeapon_SelectionChanged( self, event ):
		""" Changes the value for the selected actor's initial weapon_id """
		SelectedActor.weapon_id = self.comboBoxWeapon.GetSelection()

	def comboBoxShield_SelectionChanged( self, event ):
		""" Changes the value for the selected actor's initial armor1_id """
		SelectedActor.armor1_id = self.comboBoxShield.GetSelection()

	def comboBoxHelmet_SelectionChanged( self, event ):
		""" Changes the value for the selected actor's initial armor2_id """
		SelectedActor.armor2_id = self.comboBoxHelmet.GetSelection()

	def comboBoxBodyArmor_SelectionChanged( self, event ):
		""" Changes the value for the selected actor's initial armor3_id """
		SelectedActor.armor3_id = self.comboBoxBodyArmor.GetSelection()

	def comboBoxAccessory_SelectionChanged( self, event ):
		""" Changes the value for the selected actor's initial armor4_id """
		SelectedActor.armor4_id = self.comboBoxAccessory.GetSelection()

	def checkBoxWeapon_CheckChanged( self, event ):
		""" Toggles the "fixed" state of the actor's weapon """
		SelectedActor.weapon_fix = self.checkBoxWeapon.GetValue()

	def checkBoxShield_CheckChanged( self, event ):
		""" Toggles the "fixed" state of the actor's shield """
		SelectedActor.armor1_fix = self.checkBoxShield.GetValue()

	def checkBoxHelmet_CheckChanged( self, event ):
		""" Toggles the "fixed" state of the actor's helmet """
		SelectedActor.armor2_fix = self.checkBoxHelmet.GetValue()

	def checkBoxBodyArmor_CheckChanged( self, event ):
		""" Toggles the "fixed" state of the actor's body armor """
		SelectedActor.armor3_fix = self.checkBoxBodyArmor.GetValue()

	def checkBoxAccessory_CheckChanged( self, event ):
		""" Toggles the "fixed" state of the actor's accessory """
		SelectedActor.armor4_fix = self.checkBoxAccessory.GetValue()

	def changeLevel( self, event ):
		""" Update the controls on each page when the level is changed """
		self.refreshValues(self.spinCtrlLevel.GetValue())

	def refreshValues( self, level=None ):
		""" Applies the limits defined for the selected parameter, and updates the value """
		if level == None:
			level = self.spinCtrlLevel.GetValue()
		self.spinCtrlValue.SetValue(self.GetParameterValue(self.ParamTab, level))
		self.setValueRange()
		
	def setValueRange( self ):
		if self.ParamTab == 0:
			self.spinCtrlValue.SetRange(0, ActorLimits['maxhp'])
		elif self.ParamTab == 1:
			self.spinCtrlValue.SetRange(0, ActorLimits['maxsp'])
		elif self.ParamTab == 2:
			self.spinCtrlValue.SetRange(0, ActorLimits['maxstr'])
		elif self.ParamTab == 3:
			self.spinCtrlValue.SetRange(0, ActorLimits['maxdex'])
		elif self.ParamTab == 4:
			self.spinCtrlValue.SetRange(0, ActorLimits['maxagi'])
		elif self.ParamTab == 5:
			self.spinCtrlValue.SetRange(0, ActorLimits['maxint'])
		else:
		    self.spinCtrlValue.SetRange(0, ActorLimits['maxextra'])

	def drawCurve( self, parameterList, text ):

		pass

	def bitmapGraph_LeftClick( self, event ):
		print 'CLICKED'
	
	def bitmapGraph_LeftDown( self, event ):
		print 'DOWN'
	
	def bitmapGraph_LeftUp( self, event ):
		print 'UP'
	
	def spinCtrlValue_ValueChanged( self, event ):
		self.SetParameterValue(self.ParamTab, self.spinCtrlLevel.GetValue(), self.spinCtrlValue.GetValue())

	def buttonGenerateCurve_Clicked( self, event):
		""" Create the parameter curve dialog, using the passed index to determine the parameter """
		dlg = ARCedGenerateCurve_Dialog.ARCedGenerateCurve_Dialog(self, self.ParamTab)
		if dlg.ShowModal() == wx.ID_OK:
			# TODO: Implement curve modification
			pass
		dlg.Destroy()

	def noteBookParameters_PageChanged( self, event ):
		""" Sets the index of the page when the tab is traversed """
		# Fix for Windows. Using wxNotebook#GetSelection() can return inconsistent results, while reading
		# it from the wxNoteBookEvent#GetSelection() is accurate
		self.ParamTab = event.GetSelection()
		self.buttonRemoveParameter.Enabled = (self.ParamTab > 5)
		self.refreshValues()

	def buttonQuickA_Clicked( self, event ):
		print 'A'

	def buttonQuickB_Clicked( self, event ):
		print 'B'

	def buttonQuickC_Clicked( self, event ):
		print 'C'

	def buttonQuickD_Clicked( self, event ):
		print 'D'

	def buttonQuickE_Clicked( self, event ):
		print 'E'

	def buttonAddParameter_Clicked( self, event ):
		""" Opens dialog for the user to create a custom parameter """
		dialog = ARCedAddParameter_Dialog.ARCedAddParameter_Dialog(self)
		if (dialog.ShowModal() == wx.ID_OK):
			paramName = dialog.textCtrlParameterName.GetLineText(0)
			tab = wx.Panel(self.noteBookActorParameters)
			self.noteBookActorParameters.AddPage(tab, paramName)

	def buttonRemoveParameter_Clicked( self, event ):
		""" Removes the selected page from the tab control and resizes the actors' parameter tables """
		if self.ParamTab > 5:
			# TODO: Implement
			print 'Delete page, resize parameters table...'
			pass

	@staticmethod
	def FixedIndex(index):
		""" Returns the correct starting index for game data structure depending on the current format """
		if ARC_FORMAT:
			return index
		else:
			return index + 1