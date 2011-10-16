import wx
import ARCed_Templates

class ARCedExpCurve_Dialog( ARCed_Templates.ExpCurve_Dialog ):
	def __init__( self, parent, actor, limits):
		""" Initializes the window and sets the values for the controls """
		ARCed_Templates.ExpCurve_Dialog.__init__( self, parent )
		minBasis, maxBasis = limits['minexpbasis'], limits['maxexpbasis']
		minInflation, maxInflation = limits['minexpinflation'], limits['maxexpinflation']
		self.spinCtrlBasis.SetRange(minBasis, maxBasis)
		self.spinCtrlInflation.SetRange(minInflation, maxInflation)
		self.sliderBasis.SetRange(minBasis, maxBasis)
		self.sliderInflation.SetRange(minInflation, maxInflation)
		self.spinCtrlBasis.SetValue(actor.exp_basis)
		self.spinCtrlInflation.SetValue(actor.exp_inflation)
		font = wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		if not font.SetFaceName('Consolas'):
			font.SetFaceName('Courier New')
		self.textCtrlNext.SetFont(font)
		self.textCtrlTotal.SetFont(font)
		global MaxLevel, FinalLevel, StyleNext, StyleTotal, StyleNormal
		MaxLevel = limits['finallevel']
		FinalLevel = actor.final_level
		StyleNext = wx.TextAttr(wx.Color(0, 128, 0))
		StyleTotal = wx.TextAttr(wx.Color(128, 0, 0))
		self.refreshExpTable()

	def refreshExpTable(self):
		""" Refreshes the text on the screen to display the experience table using the defined values """
		expList = self.generateExpList()
		levelDigits = len(str(FinalLevel))
		expDigits = len(str(max(expList)))
		strings = []
		if self.noteBookExpList.GetSelection() == 1:
			for i in range(1, FinalLevel + 1):
				strings.append('L' + str(i).rjust(levelDigits) + ': ' + str(expList[i] - expList[i - 1]).rjust(expDigits))
			lines = ["    ".join(row) for row in self.columnSplit(strings, 4)]
			self.textCtrlNext.ChangeValue("\n".join(lines))
			for y in range(len(lines)):
				for c in range(4):
					start = self.textCtrlNext.XYToPosition(0, y)
					pos = (start + levelDigits + 3) + ((levelDigits + 7 + expDigits) * c)
					self.textCtrlNext.SetStyle(pos, pos + expDigits, StyleNext)
		else:
			for i in range(1, FinalLevel + 1):
				strings.append('L' + str(i).rjust(levelDigits) + ': ' + str(expList[i]).rjust(expDigits))
			lines = ["    ".join(row) for row in self.columnSplit(strings, 4)]
			self.textCtrlTotal.ChangeValue("\n".join(lines))
			for y in range(len(lines)):
				for c in range(4):
					start = self.textCtrlTotal.XYToPosition(0, y)
					pos = (start + levelDigits + 3) + ((levelDigits + 7 + expDigits) * c)
					self.textCtrlTotal.SetStyle(pos, pos + expDigits, StyleTotal)

	def columnSplit(self, list, columns):
		""" Splits a list into column lists and returns a list of rows """
		rows = len(list) / columns
		if len(list) % columns:
			rows += 1
		return [list[i::rows] for i in range(rows)]

	def generateExpList(self):
		""" Calculates the experience list based on the basis and inflation, then returns it """
		expList = [0, 0]
		basis = self.spinCtrlBasis.GetValue()
		inflation = self.spinCtrlInflation.GetValue()
		pow_i = 2.4 + inflation / 100.0 # TODO: Maybe add editor setting for 'pow_i' ???
		for i in range(2, MaxLevel + 1):
			if i > FinalLevel:
				expList.append(0)
			else:
				n = basis * ((i + 3) ** pow_i) / (5 ** pow_i)
				expList.append(expList[i - 1] + int(n))
		return expList
	
	def sliderBasis_Scrolled( self, event ):
		""" Sync the spin control and refresh the experience list """
		self.spinCtrlBasis.SetValue(self.sliderBasis.GetValue())
		self.refreshExpTable()
	
	def spinCtrlBasis__ValueChanged( self, event ):
		""" Sync the slider control and refresh the table """
		self.sliderBasis.SetValue(self.spinCtrlBasis.GetValue())
		self.refreshExpTable()
	
	def sliderInflation_Scrolled( self, event ):
		""" Sync the spin control and refresh the experience list """
		self.spinCtrlInflation.SetValue(self.sliderInflation.GetValue())
		self.refreshExpTable()
	
	def spinCtrlInflation_ValueChanged( self, event ):
		""" Sync the slider control and refresh the table """
		self.sliderInflation.SetValue(self.spinCtrlInflation.GetValue())
		self.refreshExpTable()
	
	def buttonOK_Clicked( self, event ):
		""" End the dialog and return wx.ID_OK """
		self.EndModal(wx.ID_OK)
	
	def buttonCancel_Clicked( self, event ):
		""" End the dialog and return ID_CANCEL """
		self.EndModal(wx.ID_CANCEL)