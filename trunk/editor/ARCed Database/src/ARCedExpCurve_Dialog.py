import wx
import ARCed_Templates
import Kernel
from Kernel import Manager as KM

class ARCedExpCurve_Dialog( ARCed_Templates.ExpCurve_Dialog ):
	def __init__( self, parent, actor ):
		"""Basic constructor for the Experience Curve Dialog"""
		ARCed_Templates.ExpCurve_Dialog.__init__( self, parent )
		Config = Kernel.GlobalObjects.get_value('ARCed_config')
		minBasis = Config.getint('Actors', 'MinExpBasis')
		maxBasis = Config.getint('Actors', 'MaxExpBasis')
		minInflation = Config.getint('Actors', 'MinExpInflation')
		maxInflation = Config.getint('Actors', 'MaxExpInflation')
		self.spinCtrlBasis.SetRange(minBasis, maxBasis)
		self.spinCtrlInflation.SetRange(minInflation, maxInflation)
		self.sliderBasis.SetRange(minBasis, maxBasis)
		self.sliderInflation.SetRange(minInflation, maxInflation)
		self.spinCtrlBasis.SetValue(actor.exp_basis)
		self.spinCtrlInflation.SetValue(actor.exp_inflation)
		font = wx.Font(8, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		if not font.SetFaceName('Consolas'):
			font.SetFaceName('Courier New')
		self.textCtrlExpList.SetFont(font)
		global MaxLevel, FinalLevel, StyleNext, StyleTotal
		MaxLevel = Config.getint('Actors', 'MaxLevel')
		FinalLevel = actor.final_level
		StyleNext = wx.TextAttr(wx.Color(0, 128, 0))
		StyleTotal = wx.TextAttr(wx.Color(128, 0, 0))
		self.PageIndex = 0
		self.refreshExpTable()

	def refreshExpTable(self):
		"""Refreshes the text on the screen to display the experience table using the defined values"""
		expList = self.generateExpList()
		levelDigits = len(str(FinalLevel))
		expDigits = len(str(max(expList)))
		if self.PageIndex == 0:
			strings = [''.join(['L', str(i).rjust(levelDigits), ': ', 
				str(expList[i] - expList[i - 1]).rjust(expDigits)]) for i in xrange(1, FinalLevel + 1)]
			lines = ["    ".join(row) for row in self.columnSplit(strings, 4)]
			self.textCtrlExpList.ChangeValue("\n".join(lines))
			for y in xrange(len(lines)):
				for c in xrange(4):
					start = self.textCtrlExpList.XYToPosition(0, y)
					pos = (start + levelDigits + 3) + ((levelDigits + 7 + expDigits) * c)
					self.textCtrlExpList.SetStyle(pos, pos + expDigits, StyleNext)
		elif self.PageIndex == 1:
			strings = [''.join(['L', str(i).rjust(levelDigits), ': ', 
				str(expList[i]).rjust(expDigits)]) for i in xrange(1, FinalLevel + 1)]
			lines = ["    ".join(row) for row in self.columnSplit(strings, 4)]
			self.textCtrlExpList.ChangeValue("\n".join(lines))
			for y in xrange(len(lines)):
				for c in xrange(4):
					start = self.textCtrlExpList.XYToPosition(0, y)
					pos = (start + levelDigits + 3) + ((levelDigits + 7 + expDigits) * c)
					self.textCtrlExpList.SetStyle(pos, pos + expDigits, StyleTotal)

	def columnSplit(self, list, columns):
		"""Splits a list into column lists and returns a list of rows"""
		rows = len(list) / columns
		if len(list) % columns:
			rows += 1
		return [list[i::rows] for i in xrange(rows)]

	def generateExpList(self):
		"""Calculates the experience list based on the basis and inflation, then returns it"""
		expList = [0, 0]
		basis = self.spinCtrlBasis.GetValue()
		inflation = self.spinCtrlInflation.GetValue()
		pow_i = 2.4 + inflation / 100.0 # TODO: Maybe add editor setting for 'pow_i' ???
		for i in xrange(2, MaxLevel + 1):
			if i > FinalLevel:
				expList.append(0)
			else:
				n = basis * ((i + 3) ** pow_i) / (5 ** pow_i)
				expList.append(expList[i - 1] + int(n))
		return expList
	
	def sliderBasis_Scrolled( self, event ):
		"""Sync the spin control and refresh the experience list"""
		self.spinCtrlBasis.SetValue(self.sliderBasis.GetValue())
		self.refreshExpTable()
	
	def spinCtrlBasis__ValueChanged( self, event ):
		"""Sync the slider control and refresh the table"""
		self.sliderBasis.SetValue(self.spinCtrlBasis.GetValue())
		self.refreshExpTable()
	
	def sliderInflation_Scrolled( self, event ):
		"""Sync the spin control and refresh the experience list"""
		self.spinCtrlInflation.SetValue(self.sliderInflation.GetValue())
		self.refreshExpTable()
	
	def spinCtrlInflation_ValueChanged( self, event ):
		"""Sync the slider control and refresh the table"""
		self.sliderInflation.SetValue(self.spinCtrlInflation.GetValue())
		self.refreshExpTable()

	def noteBookExpCurve_PageChanged( self, event ):
		self.PageIndex = event.GetSelection()
		"""Refreshes the page that was switched to since only the visible page is being refreshed normally"""
		self.refreshExpTable()
	
	def buttonOK_Clicked( self, event ):
		"""End the dialog and return wx.ID_OK"""
		self.EndModal(wx.ID_OK)
	
	def buttonCancel_Clicked( self, event ):
		"""End the dialog and return wx.ID_CANCEL"""
		self.EndModal(wx.ID_CANCEL)