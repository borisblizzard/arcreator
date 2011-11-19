import wx
import os
import ARCed_Templates
from pyglet import media
import Kernel

class ARCedAudioPlayer_Panel( ARCed_Templates.AudioPlayer_Panel ):
	def __init__( self, parent, filepath ):
		ARCed_Templates.AudioPlayer_Panel.__init__( self, parent )

		self.Bind(wx.EVT_IDLE, Kernel.Protect(self.Update))

		name, ext = os.path.splitext(os.path.basename(filepath))
		self.labelFileName.SetLabel(name)
		self._src = media.StaticSource(media.load(filepath, streaming=True))
		self.Player = media.Player()

	def Update( self, event ):
		if self.Player.source:
			self.Player.dispatch_events()
		elif self.checkBoxRepeat.IsChecked():
			self.Player.queue(self._src)

	def checkBoxRepeat_CheckChanged( self, event ):
		pass
	
	def buttonPlay_Clicked( self, event ):
		if not self.Player.source:
			self.Player.queue(self._src)
			print 'queued'
		self.Player.play()
		
		
	def buttonStop_Clicked( self, event ):
		self.Player.pause()

	def sliderPosition_Scrolled( self, event ):
		pass
	
	def sliderVolume_Scrolled( self, event ):
		"""Syncs the volume spin control"""
		self.spinCtrlVolume.SetValue(event.GetInt())
	
	def spinCtrlVolume_ValueChanged( self, event ):
		"""Syncs the volume slide control"""
		self.sliderVolume.SetValue(event.GetInt())
	
	def sliderPitch_Scrolled( self, event ):
		"""Syncs the pitch spin control"""
		self.spinCtrlPitch.SetValue(event.GetInt())
	
	def spinCtrlPitch_ValueChanged( self, event ):
		"""Syncs the pitch slide control"""
		self.sliderPitch.SetValue(event.GetInt())

	def ControlOnEraseBackground( self, event ):
		"""Dummy method to override erase event. Prevents flickering on Windows"""
		pass


TEST_PATH = "C:/Users/Eric/Documents/RPGXP/Resource Pack/Pandora's Box (RMXP Resources)/Audio/Sound FX/Pack - Misc.B/0053.wav"

app = wx.PySimpleApp( 0 )
frame = wx.Frame( None, wx.ID_ANY, 'ARCed Audio Player', size=(500, 200))
panel = ARCedAudioPlayer_Panel( frame, TEST_PATH )
sizer = wx.BoxSizer( wx.HORIZONTAL )
sizer.Add( panel, 1, wx.ALL|wx.GROW, 5 )
frame.SetSizer(sizer)
frame.Layout()
frame.CenterOnScreen()
frame.Show()
app.MainLoop()
	
	
