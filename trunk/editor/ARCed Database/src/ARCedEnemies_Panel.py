import wx
import ARCed_Templates
import ARCedChangeMaximum_Dialog
import ARCedChooseGraphic_Dialog
import ARCedChooseTreasure_Dialog
import ARCedEnemyAction_Dialog
from DatabaseManager import DatabaseManager as DM
import Kernel

# Implementing Enemies_Panel
class ARCedEnemies_Panel( ARCed_Templates.Enemies_Panel ):
	def __init__( self, parent, enemy_index=0 ):
		"""Basic constructor for the Enemies panel"""
		ARCed_Templates.Enemies_Panel.__init__( self, parent )
		global Config, DataEnemies, DataStates, DataAnimations, DataElements
		Config = Kernel.GlobalObjects.get_value('ARCed_config')
		try:
			proj = Kernel.GlobalObjects.get_value('PROJECT')
			DataEnemies = proj.getData('Enemies')
			DataAnimations = proj.getData('Animations')
			DataStates = proj.getData('States')
			DataElements = proj.getData('System').elements
		except NameError:
			Kernel.Log('Database opened before Project has been initialized', '[Database:ENEMIES]', True)
			self.Destroy()
		font = wx.Font(8, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		font.SetFaceName(Config.get('Misc', 'NoteFont')) 
		self.textCtrlNotes.SetFont(font)
		default = ['MaxHP:', 'MaxSP:', 'EVA:', 'ATK:', 'PDEF:', 'MDEF:']
		self.ParameterControls = DM.CreateParameterControls(self.panelParameters, 
			self.spinCtrlParameter_ValueChanged, ':', 3, default)
		self.SelectedEnemy = DataEnemies[DM.FixedIndex(enemy_index)]
		self.refreshAll()
		self.listBoxEnemies.SetSelection(enemy_index)
		DM.DrawHeaderBitmap(self.bitmapEnemies, 'Enemies')

	def refreshAll( self ):
		self.refreshEnemyList()
		self.refreshGraphic()
		self.refreshAnimations()
		self.refreshStates()
		self.refreshElements()
		self.refreshValues()

	def refreshEnemyList( self ):
		
		digits = len(Config.get('GameObjects', 'Enemies'))
		DM.FillControl(self.listBoxEnemies, DataEnemies, digits, [])

	def refreshGraphic( self ):
		# TODO: Implement
		pass

	def refreshAnimations( self ):
		"""Refreshes the choices in the user and target animation controls"""
		digits = len(Config.get('GameObjects', 'Animations'))
		DM.FillControl(self.comboBoxTargetAnimation, DataAnimations, digits, ['(None)'])
		DM.FillControl(self.comboBoxAttackAnimation, DataAnimations, digits, ['(None)'])

	def refreshStates( self ):
		"""Clears and refreshes the list of states in the checklist"""
		self.checkListStates.DeleteAllItems()
		names = [DataStates[i].name for i in xrange(DM.FixedIndex(0), len(DataStates))]
		self.checkListStates.AppendItems(names)

	def refreshElements( self ):
		"""Clears and refreshes the list of elements in the checklist"""
		self.checkListElements.Clear()
		self.checkListElements.AppendItems(DataElements[DM.FixedIndex(0):])

	def refreshValues( self ):
		# TODO: Implement
		pass

	
	# Handlers for Enemies_Panel events.
	def listBoxEnemies_SelectionChanged( self, event ):
		# TODO: Implement listBoxEnemies_SelectionChanged
		pass
	
	def buttonMaximum_Clicked( self, event ):
		# TODO: Implement buttonMaximum_Clicked
		pass
	
	def textCtrlName_ValueChanged( self, event ):
		# TODO: Implement textCtrlName_ValueChanged
		pass
	
	def bitmapGraphic_DoubleClick( self, event ):
		# TODO: Implement bitmapGraphic_DoubleClick
		pass
	
	def comboBoxAttackAnimation_SelectionChanged( self, event ):
		# TODO: Implement comboBoxAttackAnimation_SelectionChanged
		pass
	
	def comboBoxTargetAnimation_ValueChanged( self, event ):
		# TODO: Implement comboBoxTargetAnimation_ValueChanged
		pass
	
	def spinCtrlParameter_ValueChanged( self, event ):
		# TODO: Implement spinCtrlParameter_ValueChanged
		pass
	
	def comboBoxExp_Clicked( self, event ):
		# TODO: Implement comboBoxExp_Clicked
		pass
	
	def comboBoxGold_Clicked( self, event ):
		# TODO: Implement comboBoxGold_Clicked
		pass
	
	def comboBoxTreasure_Clicked( self, event ):
		# TODO: Implement comboBoxTreasure_Clicked
		pass
	
	def checkListElements_ValueChanged( self, event ):
		# TODO: Implement checkListElements_ValueChanged
		pass
	
	def checkListStates_ValueChanged( self, event ):
		# TODO: Implement checkListStates_ValueChanged
		pass
	
	def listCtrlAction_DoubleClick( self, event ):
		# TODO: Implement listCtrlAction_DoubleClick
		pass
	
	def textCtrlNotes_TextChanged( self, event ):
		# TODO: Implement textCtrlNotes_TextChanged
		pass
	
	
