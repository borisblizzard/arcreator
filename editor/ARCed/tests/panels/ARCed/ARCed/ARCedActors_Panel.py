import TEST
import RGSS1_RPG as RPG
from RGSS1_RPG import Actor
from RMXPProject import Project
import wx
import ARCed_Templates
import ARCedChangeMaximum_Dialog
import ARCedExpCurve_Dialog
import ARCedChooseGraphic_Dialog
import ARCedActorParameters_Dialog

# Implementing Actors_Panel
class ARCedActors_Panel( ARCed_Templates.Actors_Panel ):
	def __init__( self, parent ):
		ARCed_Templates.Actors_Panel.__init__( self, parent )
		for i in range(20):
			Project.Data_weapons.append(RPG.Weapon())
			Project.Data_armors.append(RPG.Armor())
			Project.Data_actors.append(RPG.Actor())
			Project.Data_classes.append(RPG.Class())

		self.comboBoxClass.Clear()
		self.listBoxActors.Clear()
		for klass in Project.Data_classes:
			self.comboBoxClass.Append(klass.name)
		i = 0
		for actor in Project.Data_actors:
			text = format(1 + i, '04d') + ': ' + actor.name
			self.listBoxActors.Append(text)


	# Handlers for Actors_Panel events.
	def listBoxActors_SelectionChanged( self, event ):
		self.textCtrlName.SetValue(self.SelectedActor().name)

	def buttonMaximum_Clicked( self, event ):
		# Shows dialog for changing the list capacity
		items = self.listBoxActors.GetItems()
		currentMax = len(items)
		dlg = ARCedChangeMaximum_Dialog.ARCedChangeMaximum_Dialog(self, currentMax)
		if dlg.ShowModal() == wx.ID_OK:
			newMax = dlg.spinCtrlMaximum.GetValue()
			if newMax != currentMax: 
				if newMax > currentMax:
					# Insert new items to the end of the list
					for i in range(newMax - currentMax):
						self.listBoxActors.Append(format(1 + currentMax + i, '04d') + ': ')
						Project.Data_actors.append(Actor())
				else:
					for i in reversed(range(currentMax)):
						# Remove all items whose index is greater than or equal to the new max
						if i >= newMax:
							self.listBoxActors.Delete(i)
							Project.Data_actors.pop()
						else:
							break;
		dlg.Destroy()


	def textBoxName_TextChanged( self, event ):
		index = self.listBoxActors.GetSelection()
		if index >= 0:
			name = self.textCtrlName.GetLineText(0)
			self.SelectedActor().name = name
			self.listBoxActors.SetString(index, format(1 + index, '04d') + ': ' + name)

	def comboBoxClass_SelectionChanged( self, event ):
		# TODO: Implement comboBoxClass_SelectionChanged
		pass

	def spinCtrlInitialLevel_ValueChanged( self, event ):
		# TODO: Implement spinCtrlInitialLevel_ValueChanged
		pass

	def spinCtrlFinalLevel_ValueChanged( self, event ):
		# TODO: Implement spinCtrlFinalLevel_ValueChanged
		pass

	def comboBoxExperience_Click( self, event ):
		dlg = ARCedExpCurve_Dialog.ARCedExpCurve_Dialog(self)
		if dlg.ShowModal() == wx.ID_OK:
			# TODO: Implement
			print 'Actor experience curve changed'
		dlg.Destroy()

	def bitmapCharacterGraphic_Click( self, event ):
		# TODO: Implement bitmapCharacterGraphic_Click
		pass

	def bitmapBattlerGraphic_Click( self, event ):
		# TODO: Implement bitmapBattlerGraphic_Click
		pass

	def bitmapMaxHP_Click( self, event ):
		self.showActorParametersDialog(0)

	def bitmapStr_Click( self, event ):
		self.showActorParametersDialog(2)

	def bitmapAgi_Click( self, event ):
		self.showActorParametersDialog(4)

	def bitmapMaxSP_Click( self, event ):
		self.showActorParametersDialog(1)

	def bitmapDex_Click( self, event ):
		self.showActorParametersDialog(3)

	def bitmapInt_Click( self, event ):
		self.showActorParametersDialog(5)

	def showActorParametersDialog(self, index):
		dlg = ARCedActorParameters_Dialog.ARCedActorParameters_Dialog(self) # ACTOR argument
		dlg.noteBookExperienceCurve.ChangeSelection(index)
		if dlg.ShowModal() == wx.ID_OK:
			# TODO: IMPLEMENT
			print 'Change Values'
		dlg.Destroy()

	def comboBoxWeapon_SelectionChanged( self, event ):
		# TODO: Implement comboBoxWeapon_SelectionChanged
		pass

	def comboBoxShield_SelectionChanged( self, event ):
		# TODO: Implement comboBoxShield_SelectionChanged
		pass

	def comboBoxHelmet_SelectionChanged( self, event ):
		# TODO: Implement comboBoxHelmet_SelectionChanged
		pass

	def comboBoxBodyArmor_SelectionChanged( self, event ):
		# TODO: Implement comboBoxBodyArmor_SelectionChanged
		pass

	def comboBoxAccessory_SelectionChanged( self, event ):
		# TODO: Implement comboBoxAccessory_SelectionChanged
		pass

	def checkBoxWeapon_CheckChanged( self, event ):
		# TODO: Implement checkBoxWeapon_CheckChanged
		pass

	def checkBoxShield_CheckChanged( self, event ):
		# TODO: Implement checkBoxShield_CheckChanged
		pass

	def checkBoxHelmet_CheckChanged( self, event ):
		# TODO: Implement checkBoxHelmet_CheckChanged
		pass

	def checkBoxBodyArmor_CheckChanged( self, event ):
		# TODO: Implement checkBoxBodyArmor_CheckChanged
		pass

	def checkBoxAccessory_CheckChanged( self, event ):
		# TODO: Implement checkBoxAccessory_CheckChanged
		pass

	def SelectedActor(self):
		return Project.Data_actors[self.listBoxActors.GetSelection()]