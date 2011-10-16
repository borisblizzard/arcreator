import wx
import ARCed_Templates
import ARCedExpCurve_Dialog
import ARCedGenerateCurve_Dialog

class ARCedActorParameters_Dialog( ARCed_Templates.ActorParameters_Dialog ):
	def __init__( self, parent, actor, limits ):
		""" Initializes window using passed Actor argument to set values """
		ARCed_Templates.ActorParameters_Dialog.__init__( self, parent )
		global Actor
		Actor = actor
		self.ParameterTable = Actor.parameters
		self.PageIndex = 0
		self.Limits = limits
		self.spinCtrlLevel.SetRange(1, self.Limits['finallevel'])
		self.setValueRange()
		self.refreshValues(1)

	def changeLevel( self, event ):
		""" Update the controls on each page when the level is changed """
		self.refreshValues(self.spinCtrlLevel.GetValue())

	def refreshValues( self, level=None ):
		""" Applies the limits defined for the selected parameter, and updates the value """
		if level == None:
			level = self.spinCtrlLevel.GetValue()
		self.setValueRange()
		self.spinCtrlValue.SetValue(self.ParameterTable[self.PageIndex, level])
		
	def setValueRange( self ):
		if self.PageIndex == 0:
			self.spinCtrlValue.SetRange(0, self.Limits['maxhp'])
		elif self.PageIndex == 1:
			self.spinCtrlValue.SetRange(0, self.Limits['maxsp'])
		elif self.PageIndex == 2:
			self.spinCtrlValue.SetRange(0, self.Limits['maxstr'])
		elif self.PageIndex == 3:
			self.spinCtrlValue.SetRange(0, self.Limits['maxdex'])
		elif self.PageIndex == 4:
			self.spinCtrlValue.SetRange(0, self.Limits['maxagi'])
		elif self.PageIndex == 5:
			self.spinCtrlValue.SetRange(0, self.Limits['maxint'])

	def drawCurve( self, parameterList, text ):
		size = self.bitmapGraph.GetSize()
		bitmap = wx.Bitmap(size.GetWidth, size.GetHeight)
		step = size.GetWidth() / actor.final_level

		brush = wx.Brush(wx.RED, step)
		
		for value in xrange(1, len(actor.final_level), step):
			


			pass
		pass


	def bitmapGraph_LeftClick( self, event ):
		print 'CLICKED'
	
	def bitmapGraph_LeftDown( self, event ):
		print 'DOWN'
	
	def bitmapGraph_LeftUp( self, event ):
		print 'UP'
	
	def spinCtrlValue_ValueChanged( self, event ):
		self.ParameterTable[self.PageIndex, self.spinCtrlLevel.GetValue()] = self.spinCtrlValue.GetValue()

	def buttonGenerateCurve_Clicked( self, event):
		""" Create the parameter curve dialog, using the passed index to determine the parameter """
		dlg = ARCedGenerateCurve_Dialog.ARCedGenerateCurve_Dialog(self, self.PageIndex)
		if dlg.ShowModal() == wx.ID_OK:
			# TODO: Implement curve modification
			print 'New Curve Generated'
		dlg.Destroy()

	def noteBookParameters_PageChanged( self, event ):
		""" Sets the index of the page when the tab is traversed """
		# Fix for Windows. Using wxNotebook#GetSelection() returns inconsistent results, while reading
		# it from the wxNoteBookEvent#GetSelection() is accurate
		self.PageIndex = event.GetSelection()
		print self.PageIndex
		self.refreshValues()

	def buttonQuickA_Clicked( self, event ):
		print 'A'

	def buttonQuickB_Clicked( self, event ):
		print 'B'

	def buttonQuickC_Clicked( self, event ):
		print 'C'

	def buttonQuickD_Clicked( self, event ):
		print 'D'

	def buttonQuickE_Clicked( self, event ):
		print 'E'
	
	def buttonOK_Clicked( self, event ):
		""" Close the dialog and return wx.ID_OK """
		self.EndModal(wx.ID_OK)
	
	def buttonCancel_Clicked( self, event ):
		""" Close the dialog and return wx.ID_CANCEL """
		self.EndModal(wx.ID_CANCEL)
	
