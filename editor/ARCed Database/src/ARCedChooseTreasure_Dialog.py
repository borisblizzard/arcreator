import wx
from ARCed_Templates import ChooseTreasure_Dialog
from DatabaseManager import DatabaseManager as DM
import Kernel

class ARCedChooseTreasure_Dialog( ChooseTreasure_Dialog ):
	def __init__( self, parent, current ):
		ChooseTreasure_Dialog.__init__( self, parent )
		proj = Kernel.GlobalObjects.get_value('PROJECT')
		global Config, DataItems, DataWeapons, DataArmors, TreasureIndex
		Config = Kernel.GlobalObjects.get_value('ARCed_config')
		TreasureIndex = 0
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
		self.refreshTreasureList()

	def refreshTreasureList( self ):
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
	
	def listCtrlTreasure_ItemSelected( self, event ):
		# TODO: Implement listCtrlTreasure_ItemSelected
		pass
	
	def listCtrlTreasure_KeyPressed( self, event ):

		index = -1
		index = self.listCtrlTreasure.GetNextItem(index, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
		if index != -1 and event.GetKeyCode() == 0x007F: # ALT 
			self.getTreasure(index, True)
			self.refreshTreasureList()
		event.Skip()

	def getTreasure(self, index, delete=False):
		
		if index < len(self.Treasure[0]):
			if delete:
				del(self.Treasure[0][index])
			else:
				return self.Treasure[0][index]
		elif index < len(self.Treasure[0]) + len(self.Treasure[1]):
			if delete:
				del(self.Treasure[1][index - len(self.Treasure[0])])
			else:
				return self.Treasure[1][index - len(self.Treasure[0])]
		else:
			if delete:
				del(self.Treasure[2][index - len(self.Treasure[0]) - len(self.Treasure[1])])
			else:
				return self.Treasure[2][index - len(self.Treasure[0]) - len(self.Treasure[1])]


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
		TreasureIndex = index
		for i in xrange(3):
			if i == TreasureIndex:
				self._combos[i].Enable()
			else:
				self._combos[i].Disable()
				self._combos[i].SetLabel('')
	
	def buttonAdd_Clicked( self, event ):
		# TODO: Implement buttonAdd_Clicked
		pass
	
	def buttonRemove_Clicked( self, event ):
		# TODO: Implement buttonRemove_Clicked
		pass
	
	def buttonOK_Clicked( self, event ):
		# TODO: Implement buttonOK_Clicked
		pass
	
	def buttonCancel_Clicked( self, event ):
		# TODO: Implement buttonCancel_Clicked
		pass
	
	
