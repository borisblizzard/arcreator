import wx
import ARCed_Templates
import os
from pygame import mixer as Mixer
from Core.RMXP.RGSS1_RPG import AudioFile
import Kernel

# Implementing ChooseAudio_Dialog
class ChooseAudio_Dialog(ARCed_Templates.ChooseAudio_Dialog ):
	def __init__( self, parent, rtpfolder, loopcount, audiofile=None ):
		"""
		Basic constructor for the ChooseAudio dialog
			@parent - The parent wx.Window instance
			@rtpfolder - The path relative to the root RTP folder
			@loopcount - The number of times to loop when played. Use -1 to make it continuous
			@audiofile - (optional) The RPG.AudioFile instance to have selected
		"""
		ARCed_Templates.ChooseAudio_Dialog.__init__( self, parent )
		Mixer.init()
		global LoopCount
		LoopCount = loopcount
		# TODO: Change this to read the RTP paths from the Kernel
		path = os.path.abspath(''.join([os.environ['COMMONPROGRAMFILES'], 
			'/Enterbrain/RGSS/Standard/', rtpfolder]))
		for fname in os.listdir(path):
			name, ext = os.path.splitext(fname)
			if ext in ['.ogg', '.midi', '.wav']:
				self.listBoxAudio.Append(name, os.path.abspath(''.join([path, '/', fname])))
		if audiofile.name in self.listBoxAudio.GetStrings():
			self.listBoxAudio.SetStringSelection(audiofile.name)
			self.sliderVolume.SetValue(audiofile.volume)
			self.sliderPitch.SetValue(audiofile.volume)
		else:
			self.listBoxAudio.SetSelection(0)

	# Handlers for ChooseAudio_Dialog events.
	def buttonPlay_Clicked( self, event ):
		Mixer.stop()
		index = self.listBoxAudio.GetSelection()
		if index > 0:
			data = self.listBoxAudio.GetClientData(index)
			self.AudioPlayer = Mixer.Sound(data)
			self.AudioPlayer.set_volume(float(self.sliderVolume.GetValue()) / 100)
			self.AudioPlayer.play(LoopCount)
	
	def GetAudio( self ):
		index = self.listBoxAudio.GetSelection()
		if index > 0:
			file = self.listBoxAudio.GetString(index)
			volume = self.sliderVolume.GetValue()
			pitch = self.sliderPitch.GetValue()
			return AudioFile(file, volume, pitch)
		return AudioFile('', 50, 100)

	def buttonStop_Clicked( self, event ):
		"""Stops any playing sound on all channels"""
		Mixer.stop()
	
	def buttonOK_Clicked( self, event ):
		"""Ends dialog and returns an ID of wx.ID_OK"""
		self.EndModal(wx.ID_OK)
	
	def buttonCancel_Clicked( self, event ):
		"""Ends dialog and returns an ID of wx.ID_CANCEL"""
		self.EndModal(wx.ID_CANCEL)
	
	
