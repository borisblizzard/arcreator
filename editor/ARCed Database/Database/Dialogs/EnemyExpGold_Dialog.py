import wx
import Database.ARCed_Templates as Templates

class EnemyExpGold_Dialog( Templates.EnemyExpGold_Dialog ):
	def __init__( self, parent, label, max, current=0, variance=None ):
		"""Basic constructor for the dialog"""
		ARCed_Templates.EnemyExpGold_Dialog.__init__( self, parent )
		self.labelType.SetLabel(label)
		self.spinCtrlValue.SetRange(0, max)
		self.spinCtrlVariance.SetRange(0, max)
		self.spinCtrlValue.SetValue(current)
		if variance == None: self.spinCtrlVariance.Disable()
		else: self.spinCtrlVariance.SetValue(variance)

	def GetValues( self ):
		"""Returns the value defined and the variance in a two element tuple"""
		return (self.spinCtrlValue.GetValue(), self.spinCtrlVariance.GetValue())
	
	def buttonOK_Clicked( self, event ):
		"""Closes the dialog and returns wx.ID_OK"""
		self.EndModal(wx.ID_OK)
	
	def buttonCancel_Clicked( self, event ):
		"""Closes the dialog and returns wx.ID_CANCEL"""
		self.EndModal(wx.ID_CANCEL)
	
	
