import wx
import ARCed_Templates
import ARCedExpCurve_Dialog
import ARCedGenerateCurve_Dialog

class ARCedActorParameters_Dialog( ARCed_Templates.ActorParameters_Dialog ):
	def __init__( self, parent, parameter_table, limits ):
		""" Initializes window using passed Actor argument to set values """
		ARCed_Templates.ActorParameters_Dialog.__init__( self, parent )
		self.ParameterTable = parameter_table
		# Set limits for the controls determined by the external .ini file
		maxLevel = limits['finallevel']
		self.spinCtrlLevelMaxHP.SetRange(1, maxLevel)
		self.spinCtrlLevelMaxSP.SetRange(1, maxLevel)
		self.spinCtrlLevelStr.SetRange(1, maxLevel)
		self.spinCtrlLevelDex.SetRange(1, maxLevel)
		self.spinCtrlLevelAgi.SetRange(1, maxLevel)
		self.spinCtrlLevelInt.SetRange(1, maxLevel)
		self.spinCtrlValueMaxHP.SetRange(0, limits['maxhp'])
		self.spinCtrlValueMaxSP.SetRange(0, limits['maxsp'])
		self.spinCtrlValueStr.SetRange(0, limits['maxstr'])
		self.spinCtrlValueDex.SetRange(0, limits['maxdex'])
		self.spinCtrlValueAgi.SetRange(0, limits['maxagi'])
		self.spinCtrlValueInt.SetRange(0, limits['maxint'])

	def changeLevel( self, event ):
		""" Update the controls on each page when the level is changed """
		index = self.noteBookActorParameters.GetSelection()
		level = 1
		if index == 0:
			level = self.spinCtrlLevelMaxHP.GetValue()
		elif index == 1:
			level = self.spinCtrlLevelMaxSP.GetValue()
		elif index == 2:
			level = self.spinCtrlLevelStr.GetValue()
		elif index == 3:
			level = self.spinCtrlLevelDex.GetValue()
		elif index == 4:
			level = self.spinCtrlLevelAgi.GetValue()
		elif index == 5:
			level = self.spinCtrlLevelInt.GetValue()
		self.spinCtrlLevelMaxHP.SetValue(level)
		self.spinCtrlLevelMaxSP.SetValue(level)
		self.spinCtrlLevelStr.SetValue(level)
		self.spinCtrlLevelDex.SetValue(level)
		self.spinCtrlLevelAgi.SetValue(level)
		self.spinCtrlLevelInt.SetValue(level)
		self.spinCtrlValueMaxHP.SetValue(self.ParameterTable[0, level])
		self.spinCtrlValueMaxSP.SetValue(self.ParameterTable[1, level])
		self.spinCtrlValueStr.SetValue(self.ParameterTable[2, level])
		self.spinCtrlValueDex.SetValue(self.ParameterTable[3, level])
		self.spinCtrlValueAgi.SetValue(self.ParameterTable[4, level])
		self.spinCtrlValueInt.SetValue(self.ParameterTable[5, level])
	
	def buttonGenerateMaxHP_Clicked( self, event ):
		self.generateCurve(0)
	
	def bitmapGraphMaxHP_LeftClick( self, event ):
		# TODO: Implement bitmapGraphMaxHP_LeftClick
		pass
	
	def bitmapGraphMaxHP_LeftDown( self, event ):
		# TODO: Implement bitmapGraphMaxHP_LeftDown
		pass
	
	def bitmapGraphMaxHP_LeftUp( self, event ):
		# TODO: Implement bitmapGraphMaxHP_LeftUp
		pass
	
	def buttonGenerateMaxSP_Clicked( self, event ):
		self.generateCurve(1)
	
	def bitmapGraphMaxSP_LeftClick( self, event ):
		# TODO: Implement bitmapGraphMaxSP_LeftClick
		pass
	
	def bitmapGraphMaxSP_LeftDown( self, event ):
		# TODO: Implement bitmapGraphMaxSP_LeftDown
		pass
	
	def bitmapGraphMaxSP_LeftUp( self, event ):
		# TODO: Implement bitmapGraphMaxSP_LeftUp
		pass
	
	def buttonGenerateStr_Clicked( self, event ):
		self.generateCurve(2)

	def bitmapGraphStr_LeftClick( self, event ):
		# TODO: Implement bitmapGraphStr_LeftClick
		pass
	
	def bitmapGraphStr_LeftDown( self, event ):
		# TODO: Implement bitmapGraphStr_LeftDown
		pass
	
	def bitmapGraphStr_LeftUp( self, event ):
		# TODO: Implement bitmapGraphStr_LeftUp
		pass

	def buttonGenerateDex_Clicked( self, event ):
		self.generateCurve(3)
	
	def bitmapGraphDex_LeftClick( self, event ):
		# TODO: Implement bitmapGraphDex_LeftClick
		pass
	
	def bitmapGraphDex_LeftDown( self, event ):
		# TODO: Implement bitmapGraphDex_LeftDown
		pass
	
	def bitmapGraphDex_LeftUp( self, event ):
		# TODO: Implement bitmapGraphDex_LeftUp
		pass
	
	def buttonGenerateAgi_Clicked( self, event ):
		self.generateCurve(4)
	
	def bitmapGraphAgi_LeftClick( self, event ):
		# TODO: Implement bitmapGraphAgi_LeftClick
		pass
	
	def bitmapGraphAgi_LeftDown( self, event ):
		# TODO: Implement bitmapGraphAgi_LeftDown
		pass
	
	def bitmapGraphAgi_LeftUp( self, event ):
		# TODO: Implement bitmapGraphAgi_LeftUp
		pass
	
	def buttonGenerateInt_Clicked( self, event ):
		self.generateCurve(5)
	
	def bitmapGraphInt_LeftClick( self, event ):
		# TODO: Implement bitmapGraphInt_LeftClick
		pass
	
	def bitmapGraphInt_LeftDown( self, event ):
		# TODO: Implement bitmapGraphInt_LeftDown
		pass
	
	def bitmapGraphInt_LeftUp( self, event ):
		# TODO: Implement bitmapGraphInt_LeftUp
		pass
	
	def buttonOK_Clicked( self, event ):
		""" Close the dialog and return wx.ID_OK """
		self.EndModal(wx.ID_OK)
	
	def buttonCancel_Clicked( self, event ):
		""" Close the dialog and return wx.ID_CANCEL """
		self.EndModal(wx.ID_CANCEL)

	def generateCurve(self, parameterIndex):
		""" Create the parameter curve dialog, using the passed index to determine the parameter """
		dlg = ARCedGenerateCurve_Dialog.ARCedGenerateCurve_Dialog(self, parameterIndex)
		if dlg.ShowModal() == wx.ID_OK:
			# TODO: Implement curve modification
			print 'New Curve Generated'
		dlg.Destroy()

	def buttonQuickA_Clicked( self, event ):
		print 'A'
		pass

	def buttonQuickB_Clicked( self, event ):
		print 'B'
		pass

	def buttonQuickC_Clicked( self, event ):
		print 'C'
		pass

	def buttonQuickD_Clicked( self, event ):
		print 'D'
		pass

	def buttonQuickE_Clicked( self, event ):
		print 'E'
		pass
	
	
