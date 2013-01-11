import wx
from Core.Database import ARCed_Templates as Templates
import wx.lib.agw.floatspin as floatspin
import numpy as np
from Core.Database import Manager as DM
import Kernel

# TODO: THIS NEEDS FIXED UP STILL! 

import Boot
Boot.ConfigManager.LoadConfig()

# Implementing ExpGrid_Dialog
class ExpGrid_Dialog( Templates.ExpGrid_Dialog ):
	def __init__( self, parent, actor ):
		"""Basic constructor for the ExpGrid_Dialog"""
		Templates.ExpGrid_Dialog.__init__( self, parent )
		# Set the options for the spin float control
		self.spinCtrlSpeed.SetRange(-10, 10)
		self.spinCtrlSpeed.SetIncrement(0.25)
		self.spinCtrlSpeed.SetDigits(2)
		self.spinCtrlSpeed.Bind(floatspin.EVT_FLOATSPIN,
			Kernel.Protect(self.spinCtrlSpeed_ValueChanged))
		# Apply settings for the controls
		font = wx.Font(8, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		self.expGrid.SetDefaultCellFont(font)
		self.PageIndex = 0
		self.NextColor = wx.Colour(0, 128, 0)
		self.TotalColor = wx.Colour(128, 0, 0)
		self.Actor = actor
		rowCount = self.Actor.final_level / 4
		self.spinCtrlBasis.SetValue(actor.exp_basis)
		self.spinCtrlInflation.SetValue(actor.exp_inflation)
		# Create "exp_table" attribute if it does not exist
		if not hasattr(actor, 'exp_list'):
			setattr(actor, 'exp_list', self.GenerateInflationList())
		# Create rows and set the "level" cells
		if rowCount * 5 < self.Actor.final_level:
			rowCount += 1
		self.expGrid.AppendRows(rowCount)
		levelColumns, valueColumns = [0, 2, 4, 6, 8], [1, 3, 5, 7, 9] 
		for i in xrange(actor.final_level):
			row = i % rowCount
			vCol = valueColumns[i / rowCount]
			lCol = levelColumns[i / rowCount]
			text = ''.join(['LV: ', str(i + 1)])
			self.expGrid.SetCellTextColour(row, vCol, self.NextColor)
			self.expGrid.SetCellValue(row, lCol, text)
		# Draw the values on the grid
		self.RefreshTable()

	def RefreshTable( self ):
		"""Refreshes the values to show the experience table"""
		valueColumns = [1, 3, 5, 7, 9]
		count, rowCount = 0, self.expGrid.NumberRows
		if self.checkBoxCurveGeneration.GetValue(): 
			expList = self.Actor.exp_list = self.GenerateCurvedList()
		else: 
			expList = self.Actor.exp_list = self.GenerateInflationList()
		self.expGrid.BeginBatch()
		for i in xrange(self.Actor.final_level):
			row = i % rowCount
			column = valueColumns[i / rowCount]
			if self.PageIndex == 0: value = str(expList[i + 1] - expList[i])
			else: value = str(expList[i + 1])
			text = ''.join([value, "\t"])
			self.expGrid.SetCellValue(row, column, text)
		self.expGrid.AutoSizeColumns()
		self.expGrid.SetDefaultRowSize(8, True)
		self.expGrid.EndBatch()
		if not self.checkBoxCurveGeneration.GetValue():
			self.spinCtrlMinValue.SetValue(expList[2])
			self.spinCtrlMaxValue.SetValue(expList[-1])

	def GenerateCurvedList( self ):
		"""Generates the curve using the chosen values and returns it"""
		min = self.spinCtrlMinValue.GetValue()
		max = self.spinCtrlMaxValue.GetValue()
		final = self.Actor.final_level
		speed = self.spinCtrlSpeed.GetValue()
		values = np.zeros(final + 1, dtype=int)
		for i in xrange(2, final + 1):
			values[i] = int(DM.CalculateParameter(min, max, speed, i, 2, final))
		return values

	def GenerateInflationList(self):
		"""Calculates the experience list based on the basis and inflation, then returns it"""
		expList = np.zeros(self.Actor.final_level + 1, dtype=int)
		basis = self.spinCtrlBasis.GetValue()
		inflation = self.spinCtrlInflation.GetValue()
		pow_i = 2.4 + inflation / 100.0 
		for i in xrange(2, self.Actor.final_level + 1):
			n = basis * ((i + 3) ** pow_i) / (5 ** pow_i)
			expList[i] = min(expList[i - 1] + int(n), 2147483647)
		return expList

	def columnSplit(self, list, columns):
		"""Splits a list into column lists and returns a list of rows"""
		rows = len(list) / columns
		if len(list) % columns:
			rows += 1
		return [list[i::rows] for i in xrange(rows)]

	def noteBookExpCurve_PageChanged( self, event ):
		"""Changes the page index and refreshes the table"""
		self.PageIndex = event.GetSelection()
		if self.PageIndex == 0: color = self.NextColor
		else: color = self.TotalColor
		for row in xrange(self.expGrid.NumberRows):
			for col in [1, 3, 5, 7, 9]:
				self.expGrid.SetCellTextColour(row, col, color)
		self.RefreshTable()
	
	def sliderBasis_Scrolled( self, event ):
		"""Sync the spin control and refresh the experience list"""
		self.spinCtrlBasis.SetValue(self.sliderBasis.GetValue())
		self.RefreshTable()
	
	def spinCtrlBasis__ValueChanged( self, event ):
		"""Sync the slider control and refresh the table"""
		self.sliderBasis.SetValue(self.spinCtrlBasis.GetValue())
		self.RefreshTable()
	
	def sliderInflation_Scrolled( self, event ):
		"""Sync the spin control and refresh the experience list"""
		self.spinCtrlInflation.SetValue(self.sliderInflation.GetValue())
		self.RefreshTable()
	
	def spinCtrlInflation_ValueChanged( self, event ):
		"""Sync the slider control and refresh the table"""
		self.sliderInflation.SetValue(self.spinCtrlInflation.GetValue())
		self.RefreshTable()
	
	def buttonOK_Clicked( self, event ):
		"""End the dialog and return wx.ID_OK"""
		self.EndModal(wx.ID_OK)
	
	def sliderSpeed_Scrolled( self, event ):
		"""Syncs the actor spin control"""
		self.spinCtrlSpeed.SetValue(event.GetInt())
		self.RefreshTable()

	def spinCtrlSpeed_ValueChanged( self, event ):
		"""Syncs the slide controls"""
		self.sliderSpeed.SetValue(self.spinCtrlSpeed.GetValue())
		self.RefreshTable()

	def spinCtrlMaxValue_ValueChanged( self, event ):
		"""Refreshes the experience list using the new value"""
		self.RefreshTable()

	def spinCtrlMinValue_ValueChanged( self, event ):
		"""Refreshes the experience list using the new value"""
		self.RefreshTable()

	def buttonCancel_Clicked( self, event ):
		"""End the dialog and return wx.ID_CANCEL"""
		self.EndModal(wx.ID_CANCEL)

	def buttonGraphEditor_Clicked( self, event ):
		"""Opens the dialog to display a visual representation of the experience table"""
		init, final = self.Actor.initial_level, self.Actor.final_level
		expList = self.GenerateInflationList()[init:final]
		levels = [i for i in xrange(init, final)]
		data = np.column_stack((levels, expList))
		maxV = max(expList)
		dlg = ExpGraphEditor_Dialog(self, data, 'Experience', 'blue', maxV, final, init)
		dlg.ShowModal()

	def checkBoxCurveGeneration_CheckChanged( self, event ):
		"""Enable/Disable controls depending on experience curve mode"""
		checked = event.Checked()
		self.sliderBasis.Enable(not checked)
		self.sliderInflation.Enable(not checked)
		self.spinCtrlBasis.Enable(not checked)
		self.spinCtrlInflation.Enable(not checked)
		self.spinCtrlMinValue.Enable(checked)
		self.spinCtrlMaxValue.Enable(checked)
		self.sliderSpeed.Enable(checked)
		self.spinCtrlSpeed.Enable(checked)
		self.buttonGraphEditor.Enable(checked)

		
#--------------------------------------------------------------------------------------

class ExpGraphEditor_Dialog( Templates.ExpGraph_Dialog ):
	def __init__( self, parent, *args):
		"""Basic constructor for the ExpGraph_Dialog"""
		Templates.ExpGraph_Dialog.__init__( self, parent )
		self.graphPanel.SetData(*args)
	
	def buttonOK_Clicked( self, event ):
		"""Closes the dialog"""
		self.EndModal(wx.ID_OK)

	def buttonCancel_Clicked( self, event ):
		"""Closes the dialog"""
		self.EndModal(wx.ID_CANCEL)
	
	
