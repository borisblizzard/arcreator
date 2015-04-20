import wx
#--------------------------------------------------------------------------------------
# ImageCheckList
#--------------------------------------------------------------------------------------

class ImageCheckList(wx.ListCtrl):

	def __init__(self, parent, states=None, imagelist=None, items=[], nullstate=0):
		super(ImageCheckList, self).__init__(parent, wx.ID_ANY, wx.DefaultPosition, 
			wx.DefaultSize, wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		if None not in [states, imagelist]:
			self.SetStates(states, imagelist)
		self.InsertColumn(0, '')
		self.NullState = nullstate
		self.AppendItems(items)
		self.SetDoubleBuffered(True)

	def Clear( self ):
		self.DeleteAllItems()

	def AppendItems(self, items ):
		for i in range(len(items)):
			self.InsertStringItem(i, items[i], 0)

	def GetNumberStates( self ):
		return len(self._states)

	def GetStates( self ):
		return self._states

	def SetStates( self, states, imagelist ):
		if len(states) != imagelist.GetImageCount():
			from exceptions import ValueError
			raise ValueError
		self._states = states
		self.AssignImageList( imagelist, wx.IMAGE_LIST_SMALL)

	def ChangeState( self, event, increment ):
		index = self.HitTest(event.GetPosition())[0]
		if index >= 0:
			imgIndex = self.GetItem(index).GetImage()
			imgIndex = (imgIndex + increment) % self.GetNumberStates()
			self.SetItemImage(index, imgIndex)
			return index, self._states[imgIndex]
		return None

	def GetChecked( self ):
		checked = []
		for i in range(self.GetItemCount()):
			if self.GetItem(i).GetImage() != self.NullState:
				checked.append(i)
		return checked

	def SetChecked( self, indices, state=1):
		for i in range(self.GetItemCount()):
			if i in indices:
				self.SetItemImage(i, state)
			else:
				self.SetItemImage(i, self.NullState)