import wx
import os
import ARCed_Templates
from DatabaseManager import DatabaseManager as DM
from pygame import mixer, sndarray, midi
from Core.RMXP import RGSS1_RPG as RPG
from Core.Cache import RTPFunctions
import Kernel

import numpy as np
os.environ['SDL_VIDEODRIVER'] = 'dummy'


AUDIO_DIRS = ['BGM',  'BGS', 'SE', 'ME']

class ARCedAudioPlayer_Panel( ARCed_Templates.AudioPlayer_Panel ):
	def __init__( self, parent, type='BGM', rpgAudio=None ):
		ARCed_Templates.AudioPlayer_Panel.__init__( self, parent )
		"""Basic constructor for the AudioPlayer_Panel"""
		DM.DrawButtonIcon(self.buttonPlay, 'play_button', True)
		DM.DrawButtonIcon(self.buttonPause, 'pause_button', True)
		DM.DrawButtonIcon(self.buttonStop, 'stop_button', True)
		self.Repeats = [True, True, False, False]
		self.AudioIndex = 0
		self.RPGFiles = [RPG.AudioFile() for i in xrange(4)]
		if type in AUDIO_DIRS:
			self.AudioIndex = AUDIO_DIRS.index(type)
			self.notebookAudio.SetSelection(self.AudioIndex)
			if rpgAudio is not None:
				self.RPGFiles[index] = rpgAudio
		self.RefreshLists()
		if rpgAudio is not None:
			self.SetSound(rpgAudio)
		mixer.init()
		mixer.set_num_channels(4)
		mixer.set_reserved(4)

	def RefreshLists( self ):
		"""Builds a list of all supported audio files from the local and RTP directories"""
		self.AudioFiles = [[] for i in xrange(4)]
		directories = [Kernel.GlobalObjects.get_value('CurrentProjectDir')]
		rtps = Kernel.GlobalObjects.get_value("ARCed_config").get_section("RTPs")
		directories.extend([os.path.expandvars(path) for path in rtps.iteritems()])
		for dir in directories:
			for i in xrange(4):
				path = os.path.normpath(os.path.join(dir, 'Audio', AUDIO_DIRS[i]))
				for entry in [os.path.splitext(entry) for entry in os.listdir(path)]:
					if entry[1] in RTPFunctions._audio_ext:
						self.AudioFiles[i].append(entry[0])
		files = sorted(self.AudioFiles[self.AudioIndex])
		DM.FillWithoutNumber(self.listBoxAudio, [], files)


	def SetSound(self, rpgAudioFile, sound=None):
		"""Initializes the mixer and syncs the controls with the settings"""
		if sound is not None:
			print 'yes'
			self.waveFormPanel.SetSoundArray(sndarray.array(sound))
		self.labelFileName.SetLabel(rpgAudioFile.name)
		self.checkBoxRepeat.SetValue(self.Repeats[self.AudioIndex])
		self.spinCtrlPitch.SetValue(rpgAudioFile.pitch)
		self.spinCtrlVolume.SetValue(rpgAudioFile.volume)
		self.sliderPitch.SetValue(rpgAudioFile.pitch)
		self.sliderVolume.SetValue(rpgAudioFile.volume)

	def GetVolume( self ):
		"""Returns the volume as a float in range of 0.0 and 1.0"""
		return self.spinCtrlVolume.GetValue() / 100.0

	def GetPitch( self ):
		"""Returns the pitch as a float in range of 0.5 and 1.5"""
		return self.spinCtrlPitch.GetValue() / 100.0

	def buttonPlay_Clicked( self, event ):
		self.Mixer = mixer.Sound(TEST_PATH)
		if self._pitch != self.spinCtrlPitch.GetValue():
			self._pitch = self.spinCtrlPitch.GetValue()
			mixer.quit()
			mixer.init(self._pitch)
		self.Mixer.set_volume(self.spinCtrlVolume.GetValue() / 100.0)
		if self.checkBoxRepeat.GetValue(): self.Mixer.play(-1)
		else: self.Mixer.play()

	def buttonPause_Clicked( self, event ):
		"""Pauses current playback"""
		self.Mixer.stop()

		self.Mixer = mixer.Sound(TEST_PATH)
		self.PlayNormalized()

		
	def PlayNormalized( self ):
		"""Converts the sample rate for the sound to play using the mixer's sample rate"""

		mixer.quit()
		mixer.init(self.spinCtrlPitch.GetValue())
		samples = sndarray.samples(self.Mixer)
		inFreq = len(samples)
		outFreq = self.spinCtrlPitch.GetValue()
		lcm = DM.lcm(inFreq, outFreq)
		outRate = lcm / outFreq
		newSample = np.zeros(shape=(inFreq, 2), order='F')
		for i in xrange(0, inFreq, outRate):
			#samples[i][0] *= 1.5
			newSample[i] = samples[i]
		samples = newSample
		sndarray.make_sound(self.Mixer).play()

	def buttonStop_Clicked( self, event ):
		"""Stops current playback"""
		self.Mixer.stop()

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

	def notebookAudio_PageChanged( self, event ):
		"""Updates the list control and the audio file, if any"""
		self.AudioIndex = index = event.GetSelection()
		DM.FillWithoutNumber(self.listBoxAudio, [], self.AudioFiles[index])
		if self.RPGFiles[index].name in self.AudioFiles[index]:
			i = self.AudioFiles[index].index(self.RPGFiles[index].name)
			self.notebookAudio.SetSelection(i)
		self.SetSound(self.RPGFiles[index])

	def checkBoxRepeat_CheckChanged( self, event ):
		"""Sets the repeat action for this type of audio"""
		self.Repeats[self.AudioIndex] = event.Checked()

	def listBoxAudio_SelectionChanged( self, event ):
		pass

	def buttonStopAll_Clicked( self, event ):
		pass

	def buttonOK_Clicked( self, event ):
		pass

	def buttonCancel_Clicked( self, event ):
		pass

	def listBoxAudio_DoubleClick( self, event ):
		
		folder = os.path.join('Audio', AUDIO_DIRS[self.AudioIndex])
		path = RTPFunctions.FindAudioFile(folder, event.GetString())
		rpgfile = RPG.AudioFile(event.GetString(), self.spinCtrlVolume.GetValue(),
			self.spinCtrlPitch.GetValue())
		sound = mixer.Sound(path)
		self.SetSound(rpgfile, sound)
		mixer.Channel(self.AudioIndex).queue(sound)