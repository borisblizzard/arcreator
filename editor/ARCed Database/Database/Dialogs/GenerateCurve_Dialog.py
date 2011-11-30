import wx
import Database.ARCed_Templates as Templates
import wx.lib.agw.floatspin as floatspin
import numpy as np
from DatabaseManager import DatabaseManager as DM
import Kernel

class GenerateCurve_Dialog( Templates.GenerateCurve_Dialog ):
	def __init__( self, parent, vRange, lRange, max):
		"""Basic constructor for the GenerateCurve_Dialog"""
		ARCed_Templates.GenerateCurve_Dialog.__init__( self, parent )
		self.spinCtrlInitial.SetRange(0, max)
		self.spinCtrlFinal.SetRange(0, max)
		self.spinCtrlSpeed.SetRange(-10, 10)
		self.spinCtrlSpeed.SetIncrement(0.25)
		self.spinCtrlSpeed.SetDigits(2)
		self.spinCtrlInitial.SetValue(vRange[0])
		self.spinCtrlFinal.SetValue(vRange[1])
		self.LevelRange = lRange
		self.spinCtrlSpeed.Bind(floatspin.EVT_FLOATSPIN,
			Kernel.Protect(self.spinCtrlSpeed_ValueChanged))

	def GenerateCurve(self):
		"""Generates the curve using the chosen values and returns it"""
		min = self.spinCtrlInitial.GetValue()
		max = self.spinCtrlFinal.GetValue()
		init = self.LevelRange[0]
		final = self.LevelRange[1]
		speed = self.spinCtrlSpeed.GetValue()
		values = np.zeros(final + 1, dtype=int)
		for i in np.arange(init, final + 1, dtype=int):
			values[i] = int(DM.CalculateParameter(min, max, speed, i, init, final))
		return values

	def sliderSpeed_Scrolled( self, event ):
		"""Syncs the actor spin control"""
		self.spinCtrlSpeed.SetValue(event.GetInt())

	def spinCtrlSpeed_ValueChanged( self, event ):
		"""Syncs the slide controls"""
		self.sliderSpeed.SetValue(self.spinCtrlSpeed.GetValue())

	def buttonOK_Clicked( self, event ):
		"""End the dialog and return wx.ID_OK"""
		self.EndModal(wx.ID_OK)

	def buttonCancel_Clicked( self, event ):
		"""End the dialog and return wx.ID_CANCEL"""
		self.EndModal(wx.ID_CANCEL)


