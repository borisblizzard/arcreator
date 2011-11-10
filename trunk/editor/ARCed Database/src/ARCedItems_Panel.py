import wx
import ARCed_Templates
import ARCedChooseGraphic_Dialog

from Core.RMXP import RGSS1_RPG as RPG	
from DatabaseManager import DatabaseManager as DM
import Kernel

class ARCedItems_Panel( ARCed_Templates.Items_Panel ):
	def __init__( self, parent, item_index=0 ):
		ARCed_Templates.Items_Panel.__init__( self, parent )
		global Config
		global DataItems, DataStates, DataElements, DataCommonEvents, DataAnimations
		Config = Kernel.GlobalObjects.get_value('ARCed_config')
		try:
			proj = Kernel.GlobalObjects.get_value('PROJECT')
			DataItems = proj.getData('Items')
			DataStates = proj.getData('States')
			DataElements = proj.getData('System').elements
			DataAnimations = proj.getData('Animations')
			DataCommonEvents = proj.getData('CommonEvents')
		except NameError:
			Kernel.Log('Database opened before Project has been initialized', '[Database:ITEMS]', True)
			self.Destroy()
		self.listCtrlStates.AssignImageList(DM.GetAddSubImageList(), wx.IMAGE_LIST_SMALL)
		font = wx.Font(8, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		font.SetFaceName(Config.get('Misc', 'NoteFont')) 
		self.textCtrlNotes.SetFont(font)
		DM.DrawButtonIcon(self.bitmapButtonAudioTest, 'play_button', True)
		self.comboBoxMenuSE.SetCursor(wx.STANDARD_CURSOR)
		self.SelectedItem = DataItems[DM.FixedIndex(item_index)]
		self.refreshAll()
		self.listBoxItems.SetSelection(item_index)
		DM.DrawHeaderBitmap(self.bitmapItems, 'Items')

	def setRange( self ):
		pass

	def refreshItems( self ):
		"""Refreshes the values in the item wxListBox control"""
		digits = len(Config.get('GameObjects', 'Items'))
		DM.FillControl(self.listBoxItems, DataItems, digits, [])

	def refreshElements( self ):
		"""Clears and refreshes the list of elements in the checklist"""
		start = DM.FixedIndex(0)
		DM.FillWithoutNumber(self.checkListElements, [], DataElements[start:])

	def refreshStates( self ):
		"""Clears and refreshes the list of states in the checklist"""
		self.listCtrlStates.DeleteAllItems()
		start = DM.FixedIndex(0)
		names = [DataStates[i].name for i in xrange(start, len(DataStates))]
		self.listCtrlStates.InsertColumn(0, '')
		for i in xrange(len(names)):
			self.listCtrlStates.InsertStringItem(i, names[i], 0)

	def refreshParameters( self ):
		"""Refreshes the defined parameters"""
		self.comboBoxParameter.Clear()
		params = ['(None)', 'MaxHP', 'MaxSP']
		if DM.ARC_FORMAT:
			params.extend(Config.getlist('Misc', 'Parameters'))
		else:
			params.extend(['STR', 'DEX', 'AGI', 'INT'])
		self.comboBoxParameter.AppendItems(params)

	def refreshAnimations( self ):
		"""Refreshes the choices in the user and target animation controls"""
		digits = len(Config.get('GameObjects', 'Animations'))
		DM.FillControl(self.comboBoxTargetAnimation, DataAnimations, digits, ['(None)'])
		DM.FillControl(self.comboBoxUserAnimation, DataAnimations, digits, ['(None)'])

	def refreshCommonEvents( self ):
		"""Refreshes the common events in the combo box"""
		digits = len(Config.get('GameObjects', 'CommonEvents'))
		DM.FillControl(self.comboBoxCommonEvent, DataCommonEvents, digits, ['(None)'])

	def refreshValues( self ):
		""" """
		item = self.SelectedItem
		self.textCtrlName.ChangeValue(item.name)
		self.textCtrlDescription.ChangeValue(item.description)
		self.labelIconName.SetLabel(item.icon_name)
		DM.DrawButtonIcon(self.bitmapButtonIcon, item.icon_name, False)
		self.comboBoxScope.SetSelection(item.scope)
		self.comboBoxOccasion.SetSelection(item.occasion)
		self.comboBoxUserAnimation.SetSelection(item.animation1_id)
		self.comboBoxTargetAnimation.SetSelection(item.animation2_id)
		self.comboBoxMenuSE.SetValue(item.menu_se.name)
		self.comboBoxCommonEvent.SetSelection(item.common_event_id)
		self.spinCtrlPrice.SetValue(item.price)
		if item.consumable: index = 0
		else: index = 1
		self.comboBoxConsumable.SetSelection(index)
		self.comboBoxParameter.SetSelection(item.parameter_type)
		self.spinCtrlParameterInc.SetValue(item.parameter_points)
		self.spinCtrlRecrHPRate.SetValue(item.recover_hp_rate)
		self.spinCtrlRecrHP.SetValue(item.recover_hp)
		self.spinCtrlRecrSPRate.SetValue(item.recover_sp_rate)
		self.spinCtrlRecrSP.SetValue(item.recover_sp)
		self.spinCtrlHitRate.SetValue(item.hit)
		self.spinCtrlPDEF.SetValue(item.pdef_f)
		self.spinCtrlMDEF.SetValue(item.mdef_f)
		self.spinCtrlVariance.SetValue(item.variance)
		if DM.ARC_FORMAT:
			addstates = self.SelectedSkill.plus_state_set
			minusstates = self.SelectedSkill.minus_state_set
			indices = item.element_set
		else:
			addstates = [id - 1 for id in item.plus_state_set]
			minusstates = [id - 1 for id in item.minus_state_set]
			indices = [i - 1 for i in item.element_set]
		self.checkListElements.SetChecked(indices)
		for i in xrange(self.listCtrlStates.GetItemCount()):
			if i in addstates:
				self.listCtrlStates.SetItemImage(i, 1)
			elif i in minusstates:
				self.listCtrlStates.SetItemImage(i, 2)
			else:
				self.listCtrlStates.SetItemImage(i, 0)

		if not hasattr(item, 'note'):
			setattr(item, 'note', '')
		self.textCtrlNotes.ChangeValue(item.note)



	def refreshAll( self ):
		"""Refreshes all the controls on the panel"""
		self.refreshItems()
		self.refreshElements()
		self.refreshStates()
		self.refreshParameters()
		self.refreshAnimations()
		self.refreshCommonEvents()
		self.refreshValues()

	def listBoxItems_SelectionChanged( self, event ):
		"""Changes the selected item"""
		index = DM.FixedIndex(event.GetInt())
		if DataItems[index] == None:
			DataItems[index] = RPG.Item() 
		self.SelectedItem = DataItems[index]
		self.refreshValues()

	def buttonMaximum_Clicked( self, event ):
		"""Starts the Change Maximum dialog"""
		max = Config.getint('GameObjects', 'Items')
		DM.ChangeDataCapacity(self, self.listBoxItems, DataItems, max)

	def textCtrlName_TextChanged( self, event ):
		"""Updates the selected items's name"""
		DM.UpdateObjectName(self.SelectedItem, event.GetString(),
			self.listBoxItems, len(Config.get('GameObjects', 'Items')))

	def bitmapButtonIcon_Clicked( self, event ):
		"""Opens dialog to select an icon for the selected skill"""
		DM.ChooseGraphic('Graphics/Icon/', self.SelectedItem.icon_name, 0, False)

	def bitmapButtonAudioTest_Clicked( self, event ):
		"""Plays the sound effect as a quick test without opening the dialog"""
		DM.TestSFX(self.SelectedItem.menu_se)

	def textCtrlDescription_TextChange( self, event ):
		"""Updates the selected item's description"""
		self.SelectedItem.description = event.GetString()

	def comboBoxScope_SelectionChanged( self, event ):
		"""Updates the selected item's scope"""
		self.SelectedItem.scope = event.GetInt()

	def comboBoxUserAnimation_SelectionChanged( self, event ):
		"""Updates the selected item's user animation"""
		self.SelectedItem.animation1_id = DM.FixedIndex(event.GetInt())

	def comboBoxMenuSE_Clicked( self, event ):
		"""Opens the dialog for selecting the audio file to use"""
		self.listBoxItems.SetFocus()
		audio = DM.ChooseAudio(self, 'Audio/SE/', self.SelectedItem.menu_se, 0)
		self.SelectedItem.menu_se = audio
		self.comboBoxMenuSE.SetValue(audio.name)

	def comboBoxOccasion_SelectionChanged( self, event ):
		"""Updates the selected item's occasion"""
		self.SelectedItem.occasion = event.GetInt()

	def comboBoxTargetAnimation_SelectionChanged( self, event ):
		"""Updates the selected item's target animation"""
		self.SelectedItem.animation2_id = DM.FixedIndex(event.GetInt())

	def comboBoxCommonEvent_SelectionChanged( self, event ):
		"""Updates the selected item's common event"""
		self.SelectedItem.common_event_id = event.GetInt()

	def spinCtrlPrice_ValueChanged( self, event ):
		"""Updates the selected item's price"""
		self.SelectedItem.price = event.GetInt()

	def spinCtrlRecrHPPercent_ValueChanged( self, event ):
		"""Updates the selected item's recovery HP percent"""
		self.SelectedItem.recover_hp_rate = event.GetInt()

	def spinCtrlHitRate_ValueChanged( self, event ):
		"""Updates the selected item's hit rate"""
		self.SelectedItem.hit = event.GetInt()

	def comboBoxConsumable_SelectionChanged( self, event ):
		"""Updates the selected item's consumable flag"""
		self.SelectedItem.consumable = (event.GetInt() == 0)

	def spinCtrlRecrHP_ValueChanged( self, event ):
		"""Updates the selected item's recovery HP"""
		self.SelectedItem.recover_hp = event.GetInt()

	def spinCtrlPDEF_ValueChanged( self, event ):
		"""Updates the selected item's PDEF"""
		self.SelectedItem.pdef_f = event.GetInt()

	def comboBoxParameter_SelectionChanged( self, event ):
		"""Updates the selected item's parameter type"""
		self.SelectedItem.parameter_type = event.GetInt()

	def spinCtrlRecrSPPercent_ValueChanged( self, event ):
		"""Updates the selected item's recover SP percent"""
		self.SelectedItem.recover_sp_rate = event.GetInt()

	def spinCtrlMDEF_ValueChanged( self, event ):
		"""Updates the selected item's MDEF"""
		self.SelectedItem.mdef_f = event.GetInt()

	def spinCtrlParameterInc_ValueChanged( self, event ):
		"""Updates the selected item's parameter points"""
		self.SelectedItem.parameter_points = event.GetInt()

	def spinCtrlRecrSP_ValueChanged( self, event ):
		"""Updates the selected item's recovery SP"""
		self.SelectedItem.recover_sp = event.GetInt()

	def spinCtrlVariance_ValueChanged( self, event ):
		"""Updates the selected item's variance"""
		self.SelectedItem.variance = event.GetInt()

	def checkListElements_CheckChanged( self, event ):
		"""Updates the selected item's element set"""
		set = [DM.FixedIndex(i) for i in self.checkListElements.GetChecked()]
		self.SelectedItem.element_set = set

	def listCtrlStates_LeftClicked( self, event ):
		"""Cycles the State change up one"""
		DM.ChangeSkillStates(self.listCtrlStates, self.SelectedItem, event, 1)

	def listCtrlStates_RightClicked( self, event ):
		"""Cycles the State change down one"""
		DM.ChangeSkillStates(self.listCtrlStates, self.SelectedItem, event, -1)

	def textCtrlNotes_TextChanged( self, event ):
		"""Sets the note for the selected skill"""
		self.SelectedItem.note = event.GetString()

