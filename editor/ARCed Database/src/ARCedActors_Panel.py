"""
Contains the functionality of all the events raised on the Actors Database panel
"""
import wx
import ARCed_Templates
import ARCedChangeMaximum_Dialog
import ARCedExpCurve_Dialog
import ARCedGenerateCurve_Dialog
import ARCedChooseGraphic_Dialog 
import ARCedActorParameters_Dialog
import ARCedAddParameter_Dialog
from DatabaseManager import DatabaseManager as DM

#from DatabaseAction import 
from Core.RMXP import RGSS1_RPG as RPG	   						
import Kernel

class ARCedActors_Panel( ARCed_Templates.Actors_Panel ):

	def __init__( self, parent, actorIndex=0 ):
		"""Basic constructor for the Actors panel"""
		ARCed_Templates.Actors_Panel.__init__( self, parent )
		# Load the project's game objects into this module's scope
		project = Kernel.GlobalObjects.get_value('PROJECT')
		global Config, DataActors, DataClasses, DataWeapons, DataArmors
		Config = Kernel.GlobalObjects.get_value('ARCed_config')
		try:
			DataActors = project.getData('Actors')
			DataClasses = project.getData('Classes')
			DataWeapons = project.getData('Weapons')
			DataArmors = project.getData('Armors')
		except NameError:
			Kernel.Log('Database opened before Project was initialized', '[Database:ACTOR]', True)
			self.Destroy()
		# Set font for the note control
		font = wx.Font(8, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		font.SetFaceName(Config.get('Misc', 'NoteFont')) 
		self.textCtrlNotes.SetFont(font)
		self.ParamTab = 0
		# Set the ranges for initial and final level spin controls
		max = Config.getint('DatabaseLimits', 'ActorLevel')
		self.spinCtrlInitialLevel.SetRange(1, max)
		self.spinCtrlFinalLevel.SetRange(1, max)
		self.spinCtrlLevel.SetRange(1, max)
		# Initialize the selected actor attribute
		if actorIndex >= len(DataActors):
			actorIndex = 0
		self.SelectedActor = DataActors[DM.FixedIndex(actorIndex)]
		# Create the controls for the equipment and set the values for all the controls
		self.CreateEquipmentControls()
		for param in Config.getlist('GameSetup', 'Parameters'):
			self.AddParameterPage(param)
		self.noteBookActorParameters.ChangeSelection(0)
		self.comboBoxExpCurve.SetCursor(wx.STANDARD_CURSOR)
		self.refreshAll()
		DM.DrawHeaderBitmap(self.bitmapActors, 'Actors')
		# Set the initial selection of the list control 
		self.listBoxActors.SetSelection(actorIndex)

	def AddParameterPage( self, title, activate=False ):
		"""Creates a page and adds it to the notebook control"""
		page = wx.Panel( self.noteBookActorParameters )
		self.noteBookActorParameters.AddPage(page, title)
		if activate:
			index = self.noteBookActorParameters.GetPageCount() - 1
			self.noteBookActorParameters.SetSelection(index)

	def bitmapParameterGraph_Clicked( self, event ):
		pass


	def CreateEquipmentControls( self ):
		"""Creates the controls for each equipment type defined in the configuration"""
		if DM.ARC_FORMAT:
			equipment = Config.getlist('GameSetup', 'WeaponSlots')
			equipment.extend(Config.getlist('GameSetup', 'ArmorSlots'))
		else:
			equipment = ['Weapon', 'Shield', 'Helmet', 'Body Armor', 'Accessory']
		sizerEquipment = wx.BoxSizer( wx.VERTICAL )
		self.EquipmentBoxes = []
		self.FixedCheckBoxes = []
		for i in xrange(len(equipment)):
			sizer = wx.BoxSizer( wx.HORIZONTAL )
			label = wx.StaticText( self.scrolledWindowEquipment, wx.ID_ANY, 
				equipment[i], wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_LEFT )
			label.Wrap( -1 )
			sizer.Add( label, 0, wx.TOP|wx.LEFT|wx.RIGHT, 5 )
			comboBox = wx.Choice( self.scrolledWindowEquipment, wx.ID_ANY, 
				wx.DefaultPosition, wx.DefaultSize, [], 0 )
			comboBox.SetDoubleBuffered(True)
			comboBox.Bind( wx.EVT_CHOICE, 
				Kernel.Protect(self.comboBoxEquipment_SelectionChanged) )
			self.EquipmentBoxes.append(comboBox)
			sizer.Add( comboBox, 1, wx.RIGHT|wx.LEFT, 5 )
			checkBox = wx.CheckBox( self.scrolledWindowEquipment, wx.ID_ANY, u"Fixed", 
				wx.DefaultPosition, wx.DefaultSize, 0 )
			checkBox.Bind( wx.EVT_CHECKBOX, 
				 Kernel.Protect(self.checkBoxFixedEquipment_CheckChanged) )
			self.FixedCheckBoxes.append(checkBox)
			sizer.Add( checkBox, 0, wx.ALL, 5 )
			sizerEquipment.Add( sizer, 1, wx.EXPAND, 5 )
		self.scrolledWindowEquipment.SetSizer( sizerEquipment )
		self.scrolledWindowEquipment.Layout()
		sizerEquipment.Fit( self.scrolledWindowEquipment )

	def refreshActorList( self ):
		"""Refreshes the values in the actor wxListBox control"""
		digits = len(Config.get('GameObjects', 'Actors'))
		DM.FillControl(self.listBoxActors, DataActors, digits, [])

	def refreshClasses( self ):
		"""Refreshes the values in the class wxChoice control"""
		digits = len(Config.get('GameObjects', 'Classes'))
		DM.FillControl(self.comboBoxClass, DataClasses, digits, [])
		
	def refreshWeapons( self ):
		"""Sets the weapon combobox(s) data determined by the actor's class"""
		weaponSlots = len(Config.getlist('GameSetup', 'WeaponSlots'))
		digits = len(Config.get('GameObjects', 'Weapons'))
		data = [('(None)', 0)]
		for id in DataClasses[self.SelectedActor.class_id].weapon_set:
			if DataWeapons[id] == None: DataWeapons[id] = RPG.Weapon()
			data.append((''.join([str(DataWeapons[id].id).zfill(digits), ': ', 
				DataWeapons[id].name]), DataWeapons[id].id))
		for i in xrange(weaponSlots):
			self.EquipmentBoxes[i].Clear()
			for d in data:
				self.EquipmentBoxes[i].Append(d[0], d[1])
		if DM.ARC_FORMAT:
			# TODO: Implement
			pass
		else:
			id = self.SelectedActor.weapon_id
			for i in xrange(self.EquipmentBoxes[0].GetCount()):
				if self.EquipmentBoxes[0].GetClientData(i) == id:
					self.EquipmentBoxes[0].SetSelection(i)
					break

	def refreshArmors( self ):
		"""Sets the armor comboboxes data determined by the actor's class"""
		weaponSlots = len(Config.getlist('GameSetup', 'WeaponSlots'))
		digits = len(Config.get('GameObjects', 'Armors'))
		kinds = [int(k) for k in Config.getlist('GameSetup', 'ArmorSlotKinds')]
		data = []
		for id in DataClasses[self.SelectedActor.class_id].armor_set:
			if DataArmors[id] == None: DataArmors[id] = RPG.Armor()
			armor = DataArmors[id]
			data.append(("".join([str(armor.id).zfill(digits), ': ', armor.name]), armor.id))
		for i in xrange(weaponSlots, len(self.EquipmentBoxes)):
			self.EquipmentBoxes[i].Clear()
			self.EquipmentBoxes[i].Append('(None)', 0)
			for d in data:
				if DataArmors[d[1]].kind == kinds[i - weaponSlots]:
					self.EquipmentBoxes[i].Append(d[0], d[1])
			exec(''.join(['id = self.SelectedActor.armor', str(i), '_id']))
			for j in xrange(self.EquipmentBoxes[i].GetCount()):
				if self.EquipmentBoxes[i].GetClientData(j) == id:
					self.EquipmentBoxes[i].SetSelection(j)
					break

	def refreshParameters( self ):
		"""Refreshes the data values on the control"""
		actor = self.SelectedActor
		self.textCtrlName.ChangeValue(actor.name)
		self.comboBoxClass.Select(actor.class_id - 1)
		basis = str(actor.exp_basis)
		inflation = str(actor.exp_inflation)
		text = 'Basis: ' + basis + ', Inflation: ' + inflation
		self.comboBoxExpCurve.SetValue(text)
		self.spinCtrlLevel.SetRange(1, actor.final_level )
		self.refreshValues()
		self.spinCtrlLevel.SetValue(actor.initial_level)
		self.spinCtrlFinalLevel.SetValue(actor.final_level)
		self.spinCtrlInitialLevel.SetRange(1, actor.final_level)

	def refreshFixedEquipment( self ):
		if DM.ARC_FORMAT:
			# TODO: Implement
			pass
		else:
			actor = self.SelectedActor
			self.FixedCheckBoxes[0].SetValue(actor.weapon_fix)
			self.FixedCheckBoxes[1].SetValue(actor.armor1_fix)
			self.FixedCheckBoxes[2].SetValue(actor.armor2_fix)
			self.FixedCheckBoxes[3].SetValue(actor.armor3_fix)
			self.FixedCheckBoxes[4].SetValue(actor.armor4_fix)

	def refreshGraphics( self ):
		"""Refreshes the character and battler graphic for the actor"""
		DM.RenderImage(self.glCanvasCharacter, self.SelectedActor.character_name, 
			self.SelectedActor.character_hue, 'character')
		DM.RenderImage(self.glCanvasBattler, self.SelectedActor.battler_name, 
			self.SelectedActor.battler_hue, 'battler')

	def refreshAll( self ):
		"""Refreshes all the controls that contain game object values"""
		self.refreshActorList()
		self.refreshClasses()
		self.refreshWeapons()
		self.refreshArmors()
		self.refreshFixedEquipment()
		self.refreshParameters()
		self.refreshGraphics()

	def listBoxActors_SelectionChanged( self, event ):
		"""Changes the data on the panel to reflect the values of the selected actor"""
		index = DM.FixedIndex(event.GetSelection())
		if DataActors[index] is None:
			DataActors[index] = RPG.Actor()
		self.SelectedActor = DataActors[index]
		self.refreshWeapons()
		self.refreshArmors()
		self.refreshFixedEquipment()
		self.refreshParameters()
		self.refreshGraphics()

	def SetParameterValue(self, param, level, value):
		"""Sets the newly defined value for the selected actor's parameter"""
		self.SelectedActor.parameters[param, level] = value

	def GetParameterValue( self, index, level ):
		"""Retrieves the value of the current actor's selected parameter for the defined level"""
		if self.SelectedActor.parameters.xsize <= index or self.SelectedActor.parameters.ysize < level:
			maxlevel = Config.getint('DatabaseLimits', 'ActorLevel')
			for actor in DataActors:
				if actor == None:
					actor = RPG.Actor()
				print index + 1, maxlevel + 1
				actor.parameters.resize(index + 1, maxlevel + 1)
				for j in xrange(1, maxlevel):
					actor.parameters[index, j] = 50 + 5 * j
		return self.SelectedActor.parameters[index, level]

	def buttonMaximum_Clicked( self, event ):
		"""Starts the Change Maximum dialog"""
		max = Config.getint('GameObjects', 'Actors')
		DM.ChangeDataCapacity(self, self.listBoxActors, DataActors, max)

	def textBoxName_TextChanged( self, event ):
		"""Updates the selected actor's name"""
		DM.UpdateObjectName(self.SelectedActor, event.GetString(),
			self.listBoxActors, len(Config.get('GameObjects', 'Actors')))

	def comboBoxClass_SelectionChanged( self, event ):
		"""Removes any initial equipment that may be equipped if the chosen class does not permit"""
		self.SelectedActor.class_id = DM.FixedIndex(self.comboBoxClass.GetSelection())

		weaponSlots = len(Config.getlist('GameSetup', 'WeaponSlots'))
		ids = [c.GetClientData(c.GetSelection()) for c in self.EquipmentBoxes]
		weaponIds = ids[:weaponSlots]
		armorIds = ids[weaponSlots:]
		weaponSet = DataClasses[self.SelectedActor.class_id].weapon_set
		armorSet = DataClasses[self.SelectedActor.class_id].armor_set

		for i in xrange(len(weaponIds)):
			if weaponIds[i] not in weaponSet:
				if DM.ARC_FORMAT:
					# TODO: Implement 
					pass
				else:
					self.SelectedActor.weapon_id = 0
		for i in xrange(len(armorIds)):
			if armorIds[i] not in armorSet:
				if DM.ARC_FORMAT:
					# TODO: Implement 
					pass
				else:
					if armorIds[i] is not None:
						kind = str(DataArmors[armorIds[i]].kind + 1)
						exec(''.join(['self.SelectedActor.armor', kind, '_id = 0']))
		self.refreshWeapons()
		self.refreshArmors()


	def spinCtrlInitialLevel_ValueChanged( self, event ):
		"""Sets the selected actor's initial level to the value of the wxSpinCtrl"""
		self.spinCtrlInitialLevel.SetRange(1, self.spinCtrlFinalLevel.GetValue())
		self.SelectedActor.initial_level = self.spinCtrlInitialLevel.GetValue()

	def spinCtrlFinalLevel_ValueChanged( self, event ):
		"""Sets the selected actor's final level to the value of the wxSpinCtrl"""
		final = event.GetInt()
		self.spinCtrlInitialLevel.SetRange(1, final)
		self.spinCtrlLevel.SetRange(1, final)
		self.SelectedActor.final_level = final

	def comboBoxExperience_Click( self, event ):
		"""Opens window to generate experience tables"""
		actor = self.SelectedActor
		dlg = ARCedExpCurve_Dialog.ARCedExpCurve_Dialog(self, actor)
		if dlg.ShowModal() == wx.ID_OK:
			# TODO: Fix 'actor' which errors out
			actor.exp_basis = dlg.spinCtrlBasis.GetValue()
			actor.exp_inflation = dlg.spinCtrlInflation.GetValue()
		dlg.Destroy()
		self.refreshParameters()

	def glCanvasCharacter_DoubleClick( self, event ):
		"""Opens dialog to change the character graphic"""
		pass

	def glCanvasBattler_DoubleClick( self, event ):
		"""Opens dialog to change the battler graphic"""
		pass

	def comboBoxEquipment_SelectionChanged( self, event ):
		"""Updates the weapon/armor id for the selected type for the actor"""
		ctrlIndex = self.EquipmentBoxes.index(event.GetEventObject())
		if DM.ARC_FORMAT:
			# TODO: Implement
			weaponSlots = len(Config.getlist('GameSetup', 'WeaponSlots'))
			if ctrlIndex < weaponSlots:
				pass
			else:
				pass
		else: # RMXP
			if ctrlIndex == 0:
				self.SelectedActor.weapon_id = event.GetClientData()
			else:
				exec(''.join(['self.SelectedActor.armor', str(ctrlIndex), 
					'_id = event.GetClientData()']))

	def checkBoxFixedEquipment_CheckChanged( self, event ):
		"""Updates the "fixed" states for the selected actor's equipment"""
		ctrlIndex = self.FixedCheckBoxes.index(event.GetEventObject())
		if DM.ARC_FORMAT:
			# TODO: Implement
			weaponSlots = len(Config.getlist('GameSetup', 'WeaponSlots'))
			if ctrlIndex < weaponSlots:
				pass
			else:
				pass
		else: # RMXP
			if ctrlIndex == 0:
				self.SelectedActor.weapon_fix = event.Checked()
			else:
				exec(''.join(['self.SelectedActor.armor', str(ctrlIndex), 
					'_fix = event.Checked()']))

	def spinCtrlParamLevel_ValueChanged( self, event ):
		"""Update the controls on each page when the level is changed"""
		self.refreshValues(self.spinCtrlLevel.GetValue())

	def refreshValues( self, level=None ):
		"""Applies the limits defined for the selected parameter, and updates the value"""
		if level == None:
			level = self.spinCtrlLevel.GetValue()
		self.spinCtrlValue.SetValue(self.GetParameterValue(self.ParamTab, level))
		self.spinCtrlValue.SetRange(1, self.GetValueMax(self.ParamTab))
		if not hasattr(self.SelectedActor, 'note'):
			setattr(self.SelectedActor, 'note', '')
		self.textCtrlNotes.ChangeValue(self.SelectedActor.note)
		
	def GetValueMax( self, param_index ):
		""" """
		if param_index == 0: return Config.getint('DatabaseLimits', 'ActorHP')
		elif param_index == 1: return Config.getint('DatabaseLimits', 'ActorSP')
		else: return Config.getint('DatabaseLimits', 'ActorParameter')
	
	def spinCtrlValue_ValueChanged( self, event ):
		"""Updates the actors parameter table with the value"""
		self.SetParameterValue(self.ParamTab, self.spinCtrlLevel.GetValue(), self.spinCtrlValue.GetValue())

	def buttonGenerateCurve_Clicked( self, event):
		"""Create the parameter curve dialog, using the passed index to determine the parameter"""
		dlg = ARCedGenerateCurve_Dialog.ARCedGenerateCurve_Dialog(self, self.ParamTab)
		if dlg.ShowModal() == wx.ID_OK:
			# TODO: Implement curve modification
			pass
		dlg.Destroy()

	def noteBookParameters_PageChanged( self, event ):
		"""Sets the index of the page when the tab is traversed"""
		self.ParamTab = event.GetSelection()
		if not DM.ARC_FORMAT:
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
		"""Opens dialog for the user to create a custom parameter"""
		dialog = ARCedAddParameter_Dialog.ARCedAddParameter_Dialog( self )
		if (dialog.ShowModal() == wx.ID_OK):
			paramName = dialog.textCtrlParameterName.GetLineText(0)
			self.AddParameterPage(paramName)

	def buttonRemoveParameter_Clicked( self, event ):
		"""Removes the selected page from the tab control and resizes the actors' parameter tables"""
		params = self.SelectedActor.parameters
		for i in xrange(self.ParamTab, params.xsize - 1):
			params[i, :] = params[i + 1, :]
		params.resize(params.xsize - 1, Config.getint('DatabaseLimits', 'ActorLevel') + 1)
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

	def textCtrlNotes_TextChanged( self, event ):
		"""Updates the notes for the selected actor"""
		self.SelectedActor.note = event.GetString()