import RGSS1_RPG as RPG					# Remove after testing
from RGSS1_RPG import Actor
from RMXPProject import Project
import maxvalues						# TEST for now, will be stored in the core later
import wx
import ARCed_Templates
import ARCedChangeMaximum_Dialog
import ARCedExpCurve_Dialog
import ARCedChooseGraphic_Dialog
import ARCedActorParameters_Dialog

# Implementing Actors_Panel
class ARCedActors_Panel( ARCed_Templates.Actors_Panel ):
	def __init__( self, parent, actorIndex=0 ):
		""" Initializes the Actors panel """
		ARCed_Templates.Actors_Panel.__init__( self, parent )
		self.Limits = maxvalues.DatabaseLimits('ini/DatabaseLimits.ini')
		self.spinCtrlFinalLevel.SetRange(1, self.Limits.Actors['finallevel'])
		global DigitMax
		DigitMax = len(str(self.Limits.Actors['maxactors']))

		# TODO: Remove this
		for i in range(20):
			Project.Data_weapons.append(RPG.Weapon())
			Project.Data_armors.append(RPG.Armor())
			Project.Data_actors.append(RPG.Actor())
			Project.Data_classes.append(RPG.Class())

		self.refreshAll()
		self.listBoxActors.Select(actorIndex)

	def SelectedActor(self):
		""" Returns the actor object associated with the selected item in the list """
		index = self.listBoxActors.GetSelection()
		if Project.Data_actors[index] == None:
			# This is probably not needed, but just in case...
			Project.Data_actors[index] = Actor()
		return Project.Data_actors[index]

	def refreshActorList(self):
		""" Refreshes the values in the actor wxListBox control """
		i = 0
		self.listBoxActors.Clear()
		for actor in Project.Data_actors:
			i += 1
			self.listBoxActors.Append(str(i).zfill(DigitMax) + ': ' + actor.name)

	def refreshClasses(self):
		""" Refreshes the values in the class wxChoice control """
		i = 0
		self.comboBoxClass.Clear()
		for klass in Project.Data_classes:
			i += 1
			self.comboBoxClass.Append(str(i).zfill(DigitMax) + ': ' + klass.name)

	def refreshWeapons(self):
		""" Refreshes the values in the weapon wxChoice control """
		i = 0
		self.comboBoxWeapon.Clear()
		self.comboBoxWeapon.Append('(None)')
		weapon_set = Project.Data_classes[self.SelectedActor().class_id].weapon_set
		for weapon in Project.Data_weapons:
			i += 1
			if i not in weapon_set:
				continue
			self.comboBoxWeapon.Append(str(i).zfill(DigitMax) + ': ' + weapon.name)

	def refreshArmors(self):
		""" Refreshes the values in the wxChoice controls for shield, helmet,  armor, and accessory """ 
		i = 0
		self.comboBoxShield.Clear()
		self.comboBoxHelmet.Clear()
		self.comboBoxBodyArmor.Clear()
		self.comboBoxAccessory.Clear()
		self.comboBoxShield.Append('(None)')
		self.comboBoxHelmet.Append('(None)')
		self.comboBoxBodyArmor.Append('(None)')
		self.comboBoxAccessory.Append('(None)')
		armor_set = Project.Data_classes[self.SelectedActor().class_id].armor_set
		for armor in Project.Data_armors:
			i += 1
			if i not in armor_set:
				continue
			text = str(i).zfill(DigitMax) + ': ' + armor.name
			if armor.kind == 0:
				self.comboBoxShield.Append(text)
			if armor.kind == 1:
				self.comboBoxHelemt.Append(text)
			if armor.kind == 2:
				self.comboBoxBodyArmor.Append(text)
			if armor.kind == 3:
				self.comboBoxAccessory.Append(text)

	def refreshAll(self):
		""" Refreshes all the controls that contain game object values """
		self.refreshActorList()
		self.refreshClasses()
		self.refreshWeapons()
		self.refreshArmors()

	def listBoxActors_SelectionChanged( self, event ):
		""" Changes the data on the panel to reflect the values of the selected actor """
		if Project.Data_actors[self.listBoxActors.GetSelection()] == None:
			Project.Data_actors[self.listBoxActors.GetSelection()] = Actor()
		self.textCtrlName.SetValue(self.SelectedActor().name)

	def buttonMaximum_Clicked( self, event ):
		""" Shows dialog for changing the list capacity """
		items = self.listBoxActors.GetItems()
		currentMax = len(items)
		maxActors = self.Limits.Actors['maxactors']
		dlg = ARCedChangeMaximum_Dialog.ARCedChangeMaximum_Dialog(self, currentMax, 1, maxActors)
		if dlg.ShowModal() == wx.ID_OK:
			newMax = dlg.spinCtrlMaximum.GetValue()
			if newMax != currentMax: 
				if newMax > currentMax:
					newActors = [None for i in range(newMax - currentMax)]
					newLabels = [str(1 + currentMax + i).zfill(DigitMax) + ': ' for i in range(newMax - currentMax)]
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
			self.SelectedActor().name = name
			self.listBoxActors.SetString(index, str(1 + index).zfill(DigitMax) + ': ' + name)

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
			self.SelectedActor().weapon_id = 0
		for armor_index in armor_indices:
			if armor_index not in Project.Data_classes[class_index].armor_set:
				if Project.Data_armors[armor_index].kind == 0: # Shield
					self.comboBoxShield.SetSelection(0)
					self.SelectedActor().armor1_id = 0
				elif Project.Data_armors[armor_index].kind == 1: # Helmet
					self.comboBoxHelmet.SetSelection(0)
					self.SelectedActor().armor2_id = 0
				elif Project.Data_armors[armor_index].kind == 2: # Body Armor
					self.comboBoxBodyArmor.SetSelection(0)
					self.SelectedActor().armor3_id = 0
				elif Project.Data_armors[armor_index].kind == 3: # Accessory
					self.comboBoxAccessory.SetSelection(0)
					self.SelectedActor().armor4_id = 0
		self.refreshWeapons()
		self.refreshArmors()

	def spinCtrlInitialLevel_ValueChanged( self, event ):
		""" Sets the selected actor's initial level to the value of the wxSpinCtrl """
		SelectedActor().initial_level = self.spinCtrlInitialLevel.GetValue()

	def spinCtrlFinalLevel_ValueChanged( self, event ):
		""" Sets the selected actor's final level to the value of the wxSpinCtrl """
		self.SelectedActor().final_level = self.spinCtrlFinalLevel.GetValue()

	def comboBoxExperience_Click( self, event ):
		""" Opens window to generate experience tables """
		actor = self.SelectedActor()
		dlg = ARCedExpCurve_Dialog.ARCedExpCurve_Dialog(self, actor, self.Limits.Actors)
		if dlg.ShowModal() == wx.ID_OK:
			actor.exp_basis = dlg.Basis
			actor.exp_inflation = dlg.Inflation
		dlg.Destroy()

	def bitmapCharacterGraphic_Click( self, event ):
		""" Opens dialog to change the character graphic """
		# TODO: Have 'path' set to projects character graphics folder
		path = 'images'
		name = self.SelectedActor().character_name
		hue = self.SelectedActor().character_hue
		dlg = ARCedChooseGraphic_Dialog.ARCedChooseGraphic_Dialog(self, path, name, hue)
		if dlg.ShowModal() == wx.ID_OK:
			index = dlg.listBoxGraphics.GetSelection()
			self.SelectedActor().character_name = dlg.listBoxGraphics.GetString(index)
			self.SelectedActor().character_hue = dlg.sliderHue.GetValue()
			# TODO: Implement splitting to show only single frame of character graphic
			self.bitmapCharacterGraphic.SetBitmap(wx.Bitmap(dlg.Images[index]))
		dlg.Destroy()

	def bitmapBattlerGraphic_Click( self, event ):
		""" Opens dialog to change the battler graphic """
		# TODO: Have 'path' set to projects battler graphics folder
		path = 'images'
		name = self.SelectedActor().battler_name
		hue = self.SelectedActor().battler_hue
		dlg = ARCedChooseGraphic_Dialog.ARCedChooseGraphic_Dialog(self, path, name, hue)
		if dlg.ShowModal() == wx.ID_OK:
			index = dlg.listBoxGraphics.GetSelection()
			self.SelectedActor().battler_name = dlg.listBoxGraphics.GetString(index)
			self.SelectedActor().battler_hue = dlg.sliderHue.GetValue()
			self.bitmapBattlerGraphic.SetBitmap(wx.Bitmap(dlg.Images[index]))
		dlg.Destroy()

	def bitmapMaxHP_Click( self, event ):
		""" Opens the actor parameters dialog with the MaxHP tab focused """
		self.showActorParametersDialog(0)

	def bitmapStr_Click( self, event ):
		""" Opens the actor parameters dialog with the Str tab focused """
		self.showActorParametersDialog(2)

	def bitmapAgi_Click( self, event ):
		""" Opens the actor parameters dialog with the Agi tab focused """
		self.showActorParametersDialog(4)

	def bitmapMaxSP_Click( self, event ):
		""" Opens the actor parameters dialog with the MaxSP tab focused """
		self.showActorParametersDialog(1)

	def bitmapDex_Click( self, event ):
		""" Opens the actor parameters dialog with the Dex tab focused """
		self.showActorParametersDialog(3)

	def bitmapInt_Click( self, event ):
		""" Opens the actor parameters dialog with the Int tab focused """
		self.showActorParametersDialog(5)

	def showActorParametersDialog(self, index):
		""" Initializes the dialog to set actor parameters, using the selected actor """
		limits = self.Limits.Actors
		dlg = ARCedActorParameters_Dialog.ARCedActorParameters_Dialog(self, self.SelectedActor(), limits)
		dlg.noteBookActorParameters.ChangeSelection(index)
		if dlg.ShowModal() == wx.ID_OK:
			# TODO: Need to change this to work differently since this won't be a dialog
			Project.Data_actors[self.listBoxActors.GetSelection()].parameters = dlg.ParameterTable
		dlg.Destroy()

	def comboBoxWeapon_SelectionChanged( self, event ):
		""" Changes the value for the selected actor's initial weapon_id """
		self.SelectedActor().weapon_id = self.comboBoxWeapon.GetSelection()

	def comboBoxShield_SelectionChanged( self, event ):
		""" Changes the value for the selected actor's initial armor1_id """
		self.SelectedActor().armor1_id = self.comboBoxShield.GetSelection()

	def comboBoxHelmet_SelectionChanged( self, event ):
		""" Changes the value for the selected actor's initial armor2_id """
		self.SelectedActor().armor2_id = self.comboBoxHelmet.GetSelection()

	def comboBoxBodyArmor_SelectionChanged( self, event ):
		""" Changes the value for the selected actor's initial armor3_id """
		self.SelectedActor().armor3_id = self.comboBoxBodyArmor.GetSelection()

	def comboBoxAccessory_SelectionChanged( self, event ):
		""" Changes the value for the selected actor's initial armor4_id """
		self.SelectedActor().armor4_id = self.comboBoxAccessory.GetSelection()

	def checkBoxWeapon_CheckChanged( self, event ):
		""" Toggles the "fixed" state of the actor's weapon """
		self.SelectedActor().weapon_fix = self.checkBoxWeapon.GetValue()

	def checkBoxShield_CheckChanged( self, event ):
		""" Toggles the "fixed" state of the actor's shield """
		self.SelectedActor().armor1_fix = self.checkBoxShield.GetValue()

	def checkBoxHelmet_CheckChanged( self, event ):
		""" Toggles the "fixed" state of the actor's helmet """
		self.SelectedActor().armor2_fix = self.checkBoxHelmet.GetValue()

	def checkBoxBodyArmor_CheckChanged( self, event ):
		""" Toggles the "fixed" state of the actor's body armor """
		self.SelectedActor().armor3_fix = self.checkBoxBodyArmor.GetValue()

	def checkBoxAccessory_CheckChanged( self, event ):
		""" Toggles the "fixed" state of the actor's accessory """
		self.SelectedActor().armor4_fix = self.checkBoxAccessory.GetValue()