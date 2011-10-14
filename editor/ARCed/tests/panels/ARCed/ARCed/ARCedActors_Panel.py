import wx
import ARCed_Templates
import ARCedChangeMaximum_Dialog
import ARCedExpCurve_Dialog
import ARCedChooseGraphic_Dialog
import ARCedActorParameters_Dialog

# Dummy class for now
class Actor():
	def __init__(self, name, index):
		self.Name = name
		self.Index = index

# Implementing Actors_Panel
class ARCedActors_Panel( ARCed_Templates.Actors_Panel ):
	def __init__( self, parent ):
		ARCed_Templates.Actors_Panel.__init__( self, parent )
		global Actors
		Actors = {}

	# Handlers for Actors_Panel events.
	def listBoxActors_SelectionChanged( self, event ):
		# TODO: Implement listBoxActors_SelectionChanged
		pass

	def buttonMaximum_Clicked( self, event ):
		# Shows dialog for changing the list capacity
		items = self.listBoxActors.GetItems()
		currentMax = len(items)
		dlg = ARCedChangeMaximum_Dialog.ARCedChangeMaximum_Dialog(self, currentMax)
		if dlg.ShowModal() == wx.ID_OK:
			newMax = dlg.spinCtrlMaximum.GetValue()
			if newMax != currentMax: 
				listItems = []
				if newMax > currentMax:
					listItems = items
					for i in range(newMax - currentMax):
						numStr = format(1 + i + currentMax, '04d') + ': '
						# TODO: Add names of object to the string before adding to list
						# TODO: Implement initialization of objects to populate empty spots
						listItems.append(numStr)
				else:
					for i in range(newMax):
						listItems.append(items[i])
					# TODO: Implement deletion of objects defined outside the new capacity
				self.listBoxActors.Set(listItems)
				print 'List capacity has been set to ' + str(newMax)
		dlg.Destroy()


	def textBoxName_TextChanged( self, event ):
		items = self.listBoxActors.GetItems()
		selected = self.listBoxActors.GetSelections()
		if (len(items) != 0) and (len(selected) != 0):
			
			print 0


		

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


