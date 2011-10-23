'''
Contains the functionality of all the events raised on the Actors Database panel

'''
import wx
import ARCed_Templates
import ARCedChangeMaximum_Dialog 
import ARCedExpCurve_Dialog
import ARCedGenerateCurve_Dialog
import ARCedChooseGraphic_Dialog 
import ARCedActorParameters_Dialog
import ARCedAddParameter_Dialog

#from DatabaseAction import 
# import DatabasePackage

import PIL.Image
from RGSS1_RPG import RPG	   						
import Kernel
from Kernel import Manager as KM

#---------------------------------------------------------------------------
# TEST STUFF
#---------------------------------------------------------------------------
import maxvalues
ARC_FORMAT = False
import os
GraphicsDir = os.path.abspath(os.environ['COMMONPROGRAMFILES'] + 
							  '\\Enterbrain\RGSS\Standard\\Graphics')


class ARCedActors_Panel( ARCed_Templates.Actors_Panel ):
	def __init__( self, parent, actorIndex=0 ):
		''' Initializes the Actors panel '''
		ARCed_Templates.Actors_Panel.__init__( self, parent )
		proj = Kernel.GlobalObjects.get_value('PROJECT')
		global Limits, ActorLimits
		global DataActors, DataClasses, DataWeapons, DataArmors
		try:
			DataActors = proj.getData('Actors')
			DataClasses = proj.getData('Classes')
			DataWeapons = proj.getData('Weapons')
			DataArmors = proj.getData('Armors')
		except NameError:
			Kernel.Log('Database opened before Project has been initialized', '[Database:ACTOR]', True)
			self.Destroy()
		Limits = Kernel.GlobalObjects.get_value('DatabaseConfiguration').GameObjects
		ActorLimits = Kernel.GlobalObjects.get_value('DatabaseConfiguration').Actors
		self.ParamTab = 0
		self.spinCtrlFinalLevel.SetRange(1, ActorLimits['finallevel'])
		self.SelectedActor = DataActors[self.FixedIndex(0)]
		self.refreshAll()

	def SetParameterValue(self, param, level, value):
		''' Sets the newly defined value for the selected actor's parameter '''
		self.SelectedActor.parameters[param, level] = value

	def GetParameterValue( self, index, level ):
		''' Retrieves the value of the current actor's selected parameter for the defined level '''
		if self.SelectedActor.parameters.xsize <= index:
			for actor in DataActors:
				if actor == None:
					continue
				actor.parameters.resize(index + 1, ActorLimits['finallevel'])
				for i in xrange(1, ActorLimits['finallevel']):
					actor.parameters[index, i] = 50 + 5 * i
		return self.SelectedActor.parameters[index, level]

	def refreshActorList(self):
		''' Refreshes the values in the actor wxListBox control '''
		self.listBoxActors.Clear()
		for i, actor in enumerate(DataActors):
			if not ARC_FORMAT and i == 0:
				continue
			self.listBoxActors.Append(str(i).zfill(len(str(Limits['actors']))) + ': ' + actor.name)

	def refreshClasses(self):
		''' Refreshes the values in the class wxChoice control '''
		self.comboBoxClass.Clear()
		for i, klass in enumerate(DataClasses):
			if not ARC_FORMAT and i == 0:
				continue
			self.comboBoxClass.Append(str(i).zfill(len(str(Limits['classes']))) + ': ' + klass.name)
		self.comboBoxClass.Select(self.SelectedActor.class_id - 1)

	def refreshWeapons(self):
		''' Refreshes the values in the weapon wxChoice control '''
		self.comboBoxWeapon.Clear()
		self.comboBoxWeapon.Append('(None)')
		weapon_set = DataClasses[self.SelectedActor.class_id].weapon_set
		wpnIndex = 0
		for i, weapon in enumerate(DataWeapons):
			if i == 0 or i not in weapon_set:
				continue
			self.comboBoxWeapon.Append(str(i).zfill(len(str(Limits['weapons']))) + ': ' + weapon.name)
			if self.SelectedActor.weapon_id == i:
				wpnIndex = self.comboBoxWeapon.GetCount() - 1
		self.comboBoxWeapon.Select(wpnIndex)

	def refreshArmors(self):
		''' Refreshes the values in the wxChoice controls for shield, helmet,  armor, and accessory '''
		# TODO: This needs massively improved, and needs to be more modular, but works for now  
		# Use a ListCtrl?
		# Create this dynamically instead of like this
		armorBoxes = [self.comboBoxShield, self.comboBoxHelmet, 
				self.comboBoxBodyArmor, self.comboBoxAccessory]
		armorFixChecks = [self.checkBoxShield, self.checkBoxHelmet,
				self.checkBoxBodyArmor, self.checkBoxAccessory]
		armorFixes = [self.SelectedActor.armor1_fix, self.SelectedActor.armor2_fix,
				self.SelectedActor.armor3_fix, self.SelectedActor.armor4_fix]
		currentArmor = [self.SelectedActor.armor1_id, self.SelectedActor.armor2_id,
				self.SelectedActor.armor3_id, self.SelectedActor.armor4_id]
		armorIndices = []
		armor_set = DataClasses[self.SelectedActor.class_id].armor_set

		for i in xrange(len(armorBoxes)):
			armorBoxes[i].Clear()
			armorBoxes[i].Append('(None)')
			armorIndices.append(0)
			armorFixChecks[i].SetValue(armorFixes[i])
			
		for i, armor in enumerate(DataArmors):
			if i == 0 or i not in armor_set:
				continue
			text = str(i).zfill(len(str(Limits['armors']))) + ': ' + armor.name
			armorBoxes[armor.kind].Append(text)
			if currentArmor[armor.kind] == i:
				armorIndices[armor.kind] = armorBoxes[armor.kind].GetCount() - 1

		for i in xrange(len(armorBoxes)):
			armorFixChecks[i].SetValue(armorFixes[i])
			armorBoxes[i].Select(armorIndices[i])

	def refreshParameters(self):
		self.textCtrlName.ChangeValue(self.SelectedActor.name)
		self.comboBoxClass.Select(self.SelectedActor.class_id - 1)
		basis = str(self.SelectedActor.exp_basis)
		inflation = str(self.SelectedActor.exp_inflation)
		text = 'Basis: ' + basis + ', Inflation: ' + inflation
		self.comboBoxExpCurve.SetValue(text)
		self.refreshValues()


	def getFilePath(self, root, filename):
		path = None
		for entry in os.listdir(root):
			if os.path.splitext(entry)[0] == filename:
				path = root + '\\' + entry
				break
		return path

	def BitmapFromFile(self, imgFilename ) :
		pilImg = PIL.Image.open( imgFilename )
		
		wxImg = wx.EmptyImage( *pilImg.size )      
		print wxImg
		if pilImg.mode[-1] == 'A':
			pilRgbStr = pilImg.convert( 'RGB').tostring()
			wxImg.SetData( pilRgbStr )
			pilImgStr = pilImg.convert( 'RGBA' ).tostring() 
			wxImg.SetAlphaData( pilImgStr[3::4]  )
		wxBmap = wxImg.ConvertToBitmap()
		return wxBmap

	def refreshGraphics(self, image=-1):
		if image == -1 or image == 0:
			path = self.getFilePath(GraphicsDir + '\\Characters', self.SelectedActor.character_name )
			bitmap = wx.EmptyBitmap(1, 1)
			bitmap.LoadFile(path, wx.BITMAP_TYPE_ANY)
			self.bitmapCharacterGraphic.SetBitmap(bitmap)
		if image == -1 or image == 1:
			path = self.getFilePath(GraphicsDir + '\\Battlers', self.SelectedActor.battler_name )
			bitmap = wx.EmptyBitmap(1, 1)
			bitmap.LoadFile(path, wx.BITMAP_TYPE_ANY)
			self.bitmapBattlerGraphic.SetBitmap(bitmap)
			
	def bitmapBox_OnPaint(self, event):
		sender = event.GetEventObject()
		color = sender.GetBackgroundColour()
		dc = wx.PaintDC(sender) 
		dc.SetBackground(wx.Brush(color, wx.SOLID))
		dc.Clear() 
		image =  sender.GetBitmap()
		dc.DrawBitmap(image, 0, 0, True)

	def refreshAll(self):
		''' Refreshes all the controls that contain game object values '''
		self.refreshActorList()
		self.refreshClasses()
		self.refreshWeapons()
		self.refreshArmors()
		self.refreshParameters()
		self.refreshGraphics()

	def listBoxActors_SelectionChanged( self, event ):
		''' Changes the data on the panel to reflect the values of the selected actor '''
		index = self.FixedIndex(event.GetSelection())
		if DataActors[index] == None:
			DataActors[index] = RPG.Actor()
		self.SelectedActor = DataActors[index]
		self.refreshWeapons()
		self.refreshArmors()
		self.refreshParameters()
		self.refreshGraphics()

	def buttonMaximum_Clicked( self, event ):
		''' Shows dialog for changing the list capacity '''
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
					DataActors.extend(newActors)
					self.listBoxActors.InsertItems(newLabels, currentMax)
				else:
					if self.FixedIndex(self.listBoxActors.GetSelection()) >= newMax:
						self.listBoxActors.Select(newMax - 1)
					del DataActors[newMax:currentMax]
					for i in reversed(range(currentMax)):
						if i >= newMax:
							self.listBoxActors.Delete(i)
						else:
							break;
		dlg.Destroy()

	def textBoxName_TextChanged( self, event ):
		''' Renames the selected actor and syncs text with the ListBox control '''
		index = self.listBoxActors.GetSelection()
		name = self.textCtrlName.GetLineText(0)
		self.SelectedActor.name = name
		self.listBoxActors.SetString(index, str(self.FixedIndex(index)).zfill(len(str(Limits['actors']))) + 
			': ' + name)

	def comboBoxClass_SelectionChanged( self, event ):
		# TODO: Improve this...
		''' Removes any initial equipment that may be equipped if the chosen class does not permit '''
		class_index = self.FixedIndex(self.comboBoxClass.GetSelection())
		wpn_index = self.comboBoxWeapon.GetSelection()
		armor_indices = [
				   self.comboBoxShield.GetSelection(),
				   self.comboBoxHelmet.GetSelection(),
				   self.comboBoxBodyArmor.GetSelection(),
				   self.comboBoxAccessory.GetSelection()
				]
		if wpn_index not in DataClasses[class_index].weapon_set:
			self.comboBoxWeapon.SetSelection(0)
			self.SelectedActor.weapon_id = 0
		for armor_index in armor_indices:
			if armor_index not in DataClasses[class_index].armor_set:
				if DataArmors[armor_index].kind == 0: # Shield
					self.comboBoxShield.SetSelection(0)
					self.SelectedActor.armor1_id = 0
				elif DataArmors[armor_index].kind == 1: # Helmet
					self.comboBoxHelmet.SetSelection(0)
					self.SelectedActor.armor2_id = 0
				elif DataArmors[armor_index].kind == 2: # Body Armor
					self.comboBoxBodyArmor.SetSelection(0)
					self.SelectedActor.armor3_id = 0
				elif DataArmors[armor_index].kind == 3: # Accessory
					self.comboBoxAccessory.SetSelection(0)
					self.SelectedActor.armor4_id = 0
		self.refreshWeapons()
		self.refreshArmors()

	def spinCtrlInitialLevel_ValueChanged( self, event ):
		''' Sets the selected actor's initial level to the value of the wxSpinCtrl '''
		self.SelectedActor.initial_level = self.spinCtrlInitialLevel.GetValue()

	def spinCtrlFinalLevel_ValueChanged( self, event ):
		''' Sets the selected actor's final level to the value of the wxSpinCtrl '''
		self.SelectedActor.final_level = self.spinCtrlFinalLevel.GetValue()

	def comboBoxExperience_Click( self, event ):
		''' Opens window to generate experience tables '''
		# TODO: Create and use custom control instead of relying on focus changes
		self.bitmapCharacterGraphic.SetFocus()
		dlg = ARCedExpCurve_Dialog.ARCedExpCurve_Dialog(self, self.SelectedActor, ActorLimits)
		if dlg.ShowModal() == wx.ID_OK:
			actor.exp_basis = dlg.spinCtrlBasis.GetValue()
			actor.exp_inflation = dlg.spinCtrlInflation.GetValue()
		dlg.Destroy()
		self.refreshParameters()

	def bitmapCharacterGraphic_Click( self, event ):
		''' Opens dialog to change the character graphic '''
		# TODO: Change how the 'path' is read
		path = GraphicsDir + '/Characters'
		name = self.SelectedActor.character_name
		hue = self.SelectedActor.character_hue
		dlg = ARCedChooseGraphic_Dialog.ARCedChooseGraphic_Dialog(self, path, name, hue)
		if dlg.ShowModal() == wx.ID_OK:
			index = dlg.listBoxGraphics.GetSelection()
			self.SelectedActor.character_name = dlg.listBoxGraphics.GetString(index)
			self.SelectedActor.character_hue = dlg.sliderHue.GetValue()
			self.refreshGraphics(0)
		dlg.Destroy()

	def bitmapBattlerGraphic_Click( self, event ):
		''' Opens dialog to change the battler graphic '''
		# TODO: Change how the 'path' is read
		path = GraphicsDir + '/Battlers'
		name = self.SelectedActor.battler_name
		hue = self.SelectedActor.battler_hue
		dlg = ARCedChooseGraphic_Dialog.ARCedChooseGraphic_Dialog(self, path, name, hue)
		if dlg.ShowModal() == wx.ID_OK:
			index = dlg.listBoxGraphics.GetSelection()
			self.SelectedActor.battler_name = dlg.listBoxGraphics.GetString(index)
			self.SelectedActor.battler_hue = dlg.sliderHue.GetValue()
			self.refreshGraphics(1)
		dlg.Destroy()

	def getArmorSet(self, class_id, armor_kind):
		''' Returns a list of armor IDs of a certain kind for a specific class '''
		set = [0]
		for id in DataClasses[class_id].armor_set:
			if DataArmors[id].kind == armor_kind:
				set.append(id)
		return set

	def comboBoxWeapon_SelectionChanged( self, event ):
		''' Changes the value for the selected actor's initial weapon_id '''
		wpnSet = DataClasses[self.SelectedActor.class_id].weapon_set
		if wpnSet[0] != 0:
			wpnSet.insert(0, 0)
		self.SelectedActor.weapon_id = wpnSet[self.comboBoxWeapon.GetSelection()]

	def comboBoxShield_SelectionChanged( self, event ):
		''' Changes the value for the selected actor's initial armor1_id '''
		armorSet = self.getArmorSet(self.SelectedActor.class_id, 0)
		self.SelectedActor.armor1_id = armorSet[self.comboBoxShield.GetSelection()]

	def comboBoxHelmet_SelectionChanged( self, event ):
		''' Changes the value for the selected actor's initial armor2_id '''
		armorSet = self.getArmorSet(self.SelectedActor.class_id, 1)
		self.SelectedActor.armor2_id = armorSet[self.comboBoxHelmet.GetSelection()]

	def comboBoxBodyArmor_SelectionChanged( self, event ):
		''' Changes the value for the selected actor's initial armor3_id '''
		armorSet = self.getArmorSet(self.SelectedActor.class_id, 2)
		self.SelectedActor.armor3_id = armorSet[self.comboBoxBodyArmor.GetSelection()]

	def comboBoxAccessory_SelectionChanged( self, event ):
		''' Changes the value for the selected actor's initial armor4_id '''
		armorSet = self.getArmorSet(self.SelectedActor.class_id, 3)
		self.SelectedActor.armor4_id = armorSet[self.comboBoxAccessory.GetSelection()]

	def checkBoxWeapon_CheckChanged( self, event ):
		''' Toggles the "fixed" state of the actor's weapon '''
		self.SelectedActor.weapon_fix = self.checkBoxWeapon.GetValue()

	def checkBoxShield_CheckChanged( self, event ):
		''' Toggles the "fixed" state of the actor's shield '''
		self.SelectedActor.armor1_fix = self.checkBoxShield.GetValue()

	def checkBoxHelmet_CheckChanged( self, event ):
		''' Toggles the "fixed" state of the actor's helmet '''
		self.SelectedActor.armor2_fix = self.checkBoxHelmet.GetValue()

	def checkBoxBodyArmor_CheckChanged( self, event ):
		''' Toggles the "fixed" state of the actor's body armor '''
		self.SelectedActor.armor3_fix = self.checkBoxBodyArmor.GetValue()

	def checkBoxAccessory_CheckChanged( self, event ):
		''' Toggles the "fixed" state of the actor's accessory '''
		self.SelectedActor.armor4_fix = self.checkBoxAccessory.GetValue()

	def spinCtrlParamLevel_ValueChanged( self, event ):
		''' Update the controls on each page when the level is changed '''
		self.refreshValues(self.spinCtrlLevel.GetValue())

	def refreshValues( self, level=None ):
		''' Applies the limits defined for the selected parameter, and updates the value '''
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
		''' Create the parameter curve dialog, using the passed index to determine the parameter '''
		dlg = ARCedGenerateCurve_Dialog.ARCedGenerateCurve_Dialog(self, self.ParamTab)
		if dlg.ShowModal() == wx.ID_OK:
			# TODO: Implement curve modification
			pass
		dlg.Destroy()

	def noteBookParameters_PageChanged( self, event ):
		''' Sets the index of the page when the tab is traversed '''
		# Fix for Windows. Using wxNotebook#GetSelection() can return inconsistent results, while reading
		# it from the wxNoteBookEvent#GetSelection() is accurate
		self.ParamTab = event.GetSelection()
		if not ARC_FORMAT:
			self.buttonRemoveParameter.Enabled = (self.ParamTab > 5)
		else:
			self.buttonRemoveParameter.Enabled = self.noteBookActorParameters.GetPageCount >= 1
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
		''' Opens dialog for the user to create a custom parameter '''
		dialog = ARCedAddParameter_Dialog.ARCedAddParameter_Dialog(self)
		if (dialog.ShowModal() == wx.ID_OK):
			paramName = dialog.textCtrlParameterName.GetLineText(0)
			tab = wx.Panel(self.noteBookActorParameters)
			self.noteBookActorParameters.AddPage(tab, paramName)

	def buttonRemoveParameter_Clicked( self, event ):
		''' Removes the selected page from the tab control and resizes the actors' parameter tables '''
		params = self.SelectedActor.parameters
		for i in xrange(self.ParamTab, params.xsize - 1):
			params[i, :] = params[i + 1, :]
		params.resize(params.xsize - 1, 100)
		try:
			self.noteBookActorParameters.RemovePage(self.ParamTab)
		except wx.PyAssertionError:
			# There is a strange bug with wx on Windows that raises this exception when a page is
			# deleted. Removing the page works fine, but it throws the exception regardless, so
			# this little empty catch is required... :P
			pass
		if self.ParamTab >= self.noteBookActorParameters.GetPageCount():
			self.ParamTab -= 1
		self.noteBookActorParameters.SetSelection(self.ParamTab)


	@staticmethod
	def FixedIndex(index):
		''' Returns the correct starting index for game data structure depending on the current format '''
		if ARC_FORMAT:
			return index
		else:
			return index + 1