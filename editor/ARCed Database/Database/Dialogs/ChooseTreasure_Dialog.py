import wx
import Database.ARCed_Templates as Templates
from DatabaseManager import DatabaseManager as DM
import Kernel

class ChooseTreasure_Dialog( Templates.ChooseTreasure_Dialog ):
	def __init__( self, parent, current ):
		ARCed_Templates.ChooseTreasure_Dialog.__init__( self, parent )
		proj = Kernel.GlobalObjects.get_value('PROJECT')
		global Config, DataItems, DataWeapons, DataArmors
		Config = Kernel.GlobalObjects.get_value('ARCed_config')
		self._treasureIndex = 0
		DataItems = proj.getData('Items')
		DataWeapons = proj.getData('Weapons')
		DataArmors = proj.getData('Armors')
		digits = len(Config.get('GameObjects', 'Items'))
		DM.FillControl(self.comboBoxItem, DataItems, digits, [])
		digits = len(Config.get('GameObjects', 'Weapons'))
		DM.FillControl(self.comboBoxWeapon, DataWeapons, digits, [])
		digits = len(Config.get('GameObjects', 'Armors'))
		DM.FillControl(self.comboBoxArmor, DataArmors, digits, [])
		self.Treasure = current
		self.listCtrlTreasure.InsertColumn(0, "Type", wx.LIST_FORMAT_CENTRE, 64)
		self.listCtrlTreasure.InsertColumn(1, "Chance", wx.LIST_FORMAT_CENTRE, 64)
		self.listCtrlTreasure.InsertColumn(2, "Treasure", width=160)
		self.listCtrlTreasure.InsertColumn(3, "Quantity", wx.LIST_FORMAT_CENTRE, 64)
		self._combos = [self.comboBoxItem, self.comboBoxWeapon, self.comboBoxArmor]
		self.spinCtrlQuantity.SetRange(1, 
			Config.getint('GameSetup', 'MaxItemCapacity'))
		self.refreshTreasureList()

	def refreshTreasureList( self ):
		"""Refreshes the list of treasures in the lict control"""
		count = 0
		self.listCtrlTreasure.DeleteAllItems()
		for i in xrange(3):
			if i == 0: type, src = 'Item', DataItems
			elif i == 1: type, src = 'Weapon', DataWeapons
			else: type, src = 'Armor', DataArmors
			for treasure in self.Treasure[i]:
				self.listCtrlTreasure.InsertStringItem(count, type)
				self.listCtrlTreasure.SetStringItem(count, 1, str(treasure[1]) + '%')
				self.listCtrlTreasure.SetStringItem(count, 2, src[treasure[0]].name)
				self.listCtrlTreasure.SetStringItem(count, 3, str(treasure[2]))
				count += 1

	def listCtrlTreasure_KeyPressed( self, event ):
		"""Provides functionality for using the delete key to remove treasures"""
		if event.GetKeyCode() == 0x007F: 
			index = -1
			index = self.listCtrlTreasure.GetNextItem(index, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
			if index != -1:
				self.getTreasure(index, True)
				self.refreshTreasureList()
		event.Skip()

	def getTreasure(self, index, delete=False):
		"""Returns the associated tuple data for the selected object"""
		if index < len(self.Treasure[0]):
			if delete: del(self.Treasure[0][index])
			else: return self.Treasure[0][index]
		elif index < len(self.Treasure[0]) + len(self.Treasure[1]):
			if delete: del(self.Treasure[1][index - len(self.Treasure[0])])
			else: return self.Treasure[1][index - len(self.Treasure[0])]
		else:
			if delete: del(self.Treasure[2][index - len(self.Treasure[0]) - len(self.Treasure[1])])
			else: return self.Treasure[2][index - len(self.Treasure[0]) - len(self.Treasure[1])]

	def radioButtonNone_Clicked( self, event ):
		"""Activates/Deactivates the combo boxes"""
		self.activateTreasureBox(-1)
	
	def radioButtonItem_Clicked( self, event ):
		"""Activates/Deactivates the combo boxes"""
		self.activateTreasureBox(0)
	
	def radioButtonWeapon_Clicked( self, event ):
		"""Activates/Deactivates the combo boxes"""
		self.activateTreasureBox(1)

	def radioButtonArmor_Clicked( self, event ):
		"""Activates/Deactivates the combo boxes"""
		self.activateTreasureBox(2)

	def activateTreasureBox( self, index ):
		"""Sets the active combo box depending on the selected radio button"""
		self._treasureIndex = index
		for i in xrange(3):
			if i == self._treasureIndex:
				self._combos[i].Enable()
			else:
				self._combos[i].Disable()
				self._combos[i].SetLabel('')
	
	def buttonAdd_Clicked( self, event ):
		"""Adds the defined treasure to the list"""
		id = DM.FixedIndex(self._combos[self._treasureIndex].GetSelection())
		if id is not None and id >= DM.FixedIndex(0):
			qty = self.spinCtrlQuantity.GetValue()
			prob = self.spinCtrlProbability.GetValue()
			treasure = (id, prob, qty)
			self.Treasure[self._treasureIndex].append(treasure)
			self.refreshTreasureList()
	
	def buttonRemove_Clicked( self, event ):
		"""Deletes the selected treasure if one is selected"""
		index = -1
		index = self.listCtrlTreasure.GetNextItem(index, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
		if index != -1:
			self.getTreasure(index, True)
			self.refreshTreasureList()
	
	def buttonOK_Clicked( self, event ):
		"""Ends the dialog and returns wx.ID_OK"""
		self.EndModal(wx.ID_OK)
	
	def buttonCancel_Clicked( self, event ):
		"""Ends the dialog and returns wx.ID_CANCEL"""
		self.EndModal(wx.ID_CANCEL)
	
	
