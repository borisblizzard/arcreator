import wx
import wx.lib.plot as plot
import os
import numpy as np

import ARCed_Templates
from DatabaseManager import DatabaseManager as DM
from pygame import mixer, sndarray
from Core.RMXP import RGSS1_RPG as RPG
from Core.Cache import RTPFunctions

import Kernel

# Set dummy video driver to prevent malfunction on certain platforms
os.environ['SDL_VIDEODRIVER'] = 'dummy'

# List of audio directories that will be read from
if DM.ARC_FORMAT:
	AUDIO_DIRS = ['BGM',  'BGS', 'Sound'] # or whatever...
else:
	AUDIO_DIRS = ['BGM',  'BGS', 'SE', 'ME']

class ARCedAudioPlayer_Panel( ARCed_Templates.AudioPlayer_Panel ):
	def __init__( self, parent, type='BGM', rpgAudio=None ):
		ARCed_Templates.AudioPlayer_Panel.__init__( self, parent )
		"""Basic constructor for the AudioPlayer_Panel"""
		DM.DrawButtonIcon(self.buttonPlay, 'play_button', True)
		DM.DrawButtonIcon(self.buttonPause, 'pause_button', True)
		DM.DrawButtonIcon(self.buttonStop, 'stop_button', True)
		self.waveFormPanel.canvas.Bind(wx.EVT_ERASE_BACKGROUND, 
			Kernel.Protect(self.ControlOnEraseBackground))
		self.SoundFiles = []
		global dirCount
		dirCount = len(AUDIO_DIRS)
		for i in xrange(dirCount):
			list = RTPFunctions.GetFileList(os.path.join('Audio', AUDIO_DIRS[i]), 'audio')
			self.SoundFiles.append(SoundFile(AUDIO_DIRS[i], sorted(list)))
		self.AudioIndex = 0
		if type in AUDIO_DIRS:
			self.AudioIndex = AUDIO_DIRS.index(type)
			self.notebookAudio.SetSelection(self.AudioIndex)
			if rpgAudio is not None:
				self.SoundFiles[index].RPGFile = rpgAudio
		self.RefreshLists()
		if rpgAudio is not None:
			self.SetSound(rpgAudio)
		else:
			self.DrawSound()
		mixer.init()
		mixer.set_num_channels(dirCount)
		mixer.set_reserved(dirCount)

		self.Timer = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.Update, self.Timer)
		self.Timer.Start()

		self.StopWatch = wx.StopWatch()

	def Update(self, event):

		pos = self.SoundFiles[self.AudioIndex].GetPosition()
		self.sliderPosition.SetValue(pos)
		

	def RefreshLists( self ):
		"""Builds a list of all supported audio files from the local and RTP directories"""	
		DM.FillWithoutNumber(self.listBoxAudio, [],
			self.SoundFiles[self.AudioIndex].FileList)

	def SetSound(self, rpgAudioFile ):
		"""Initializes the mixer and syncs the controls with the settings"""
		self.labelFileName.SetLabel(rpgAudioFile.name)
		self.checkBoxRepeat.SetValue(self.SoundFiles[self.AudioIndex].Repeat)
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
		"""Begins playback on the selected channel"""
		index = self.AudioIndex
		self.SoundFiles[index].Timer.Resume()
		if self.SoundFiles[self.AudioIndex].Timer.Time() > 0:
			mixer.Channel(index).unpause()
		else:
			# Implement reloading file
			print 'new'
			sound = self.SoundFiles[index].Sound
			if sound is None:
				return
			if self.SoundFiles[index].Repeat:
				mixer.Channel(index).play(sound, -1)
			else:
				mixer.Channel(index).play(sound)
			self.SoundFiles[index].Timer.Start(0)

	def buttonPause_Clicked( self, event ):
		"""Pauses current playback"""
		mixer.Channel(self.AudioIndex).pause()
		self.SoundFiles[self.AudioIndex].Timer.Pause()

	def buttonStop_Clicked( self, event ):
		"""Stops playback on the selected channel"""
		mixer.Channel(self.AudioIndex).stop()
		self.SoundFiles[self.AudioIndex].Timer.Start(0)
		self.SoundFiles[self.AudioIndex].Timer.Pause()

	def sliderPosition_Scrolled( self, event ):
		# TODO: Implement
		pass
	
	def sliderVolume_Scrolled( self, event ):
		"""Syncs the volume spin control"""
		self.spinCtrlVolume.SetValue(event.GetInt())
		self.AdjustVolume()
	
	def spinCtrlVolume_ValueChanged( self, event ):
		"""Syncs the volume slide control"""
		self.sliderVolume.SetValue(event.GetInt())
		self.AdjustVolume()

	def AdjustVolume(self):
		"""Adjusts volume on the current channel"""
		volume = self.spinCtrlVolume.GetValue()
		self.SoundFiles[self.AudioIndex].SetVolume(volume)
		mixer.Channel(self.AudioIndex).set_volume(volume / 100.0)
	
	def sliderPitch_Scrolled( self, event ):
		"""Syncs the pitch spin control"""
		self.spinCtrlPitch.SetValue(event.GetInt())
	
	def spinCtrlPitch_ValueChanged( self, event ):
		"""Syncs the pitch slide control"""
		self.sliderPitch.SetValue(event.GetInt())

	def notebookAudio_PageChanged( self, event ):
		"""Updates the list control and the audio file, if any"""
		self.AudioIndex = index = event.GetSelection()
		DM.FillWithoutNumber(self.listBoxAudio, [], self.SoundFiles[index].FileList)
		i = self.SoundFiles[index].GetIndex()
		self.listBoxAudio.SetSelection(i)
		self.SetSound(self.SoundFiles[index].RPGFile)
		self.DrawSound()

	def DrawSound( self ):
		"""Updates the waveform on the control"""
		self.waveFormPanel.SetSoundArray(self.SoundFiles[self.AudioIndex].SoundArray)

	def checkBoxRepeat_CheckChanged( self, event ):
		"""Sets the repeat action for this type of audio"""
		self.SoundFiles[self.AudioIndex].Repeat = event.Checked()

	def buttonStopAll_Clicked( self, event ):
		"""Stops playback on all channels"""
		mixer.stop()

	def buttonOK_Clicked( self, event ):
		pass

	def buttonCancel_Clicked( self, event ):
		pass

	def listBoxAudio_DoubleClick( self, event ):
		"""Begins/restarts playback on the current channel using the selected file"""
		index = self.AudioIndex
		folder = os.path.join('Audio', AUDIO_DIRS[index])
		path = RTPFunctions.FindAudioFile(folder, event.GetString())
		rpgfile = RPG.AudioFile(event.GetString(), self.spinCtrlVolume.GetValue(),
			self.spinCtrlPitch.GetValue())
		self.SoundFiles[index].RPGFile = rpgfile
		sound = mixer.Sound(path)

		duration = sound.get_length()
		self.sliderPosition.SetRange(0, duration)
		self.SoundFiles[index].Duration = duration
		self.sliderPosition.SetTickFreq(1, 0)
		y = zip(*sndarray.array(sound))[1]
		# Cut large files down to a max of 30,000 samples
		length = len(y)
		if length > 30000:
			y = y[::length/30000]
		x = [i for i in xrange(len(y))]
		# SHorten the sample size for the graph if need be
		if length > 16000:
			data = np.column_stack((x[::4], y[::4]))
		elif length > 8000:
			data = np.column_stack((x[::2], y[::2]))
		else:
			data = np.column_stack((x, y))
		self.SoundFiles[index].SoundArray = data
		
		self.SetSound(rpgfile)
		self.DrawSound()
		if self.SoundFiles[index].Repeat:
			mixer.Channel(index).play(sound, -1)
		else:
			mixer.Channel(index).play(sound)
		self.SoundFiles[index].Timer.Start(0)

	def ControlOnEraseBackground( self, event ):
		"""Dummy method to override erase event. Prevents flickering on Windows"""
		pass

#--------------------------------------------------------------------------------------
# WaveFormPanel
#--------------------------------------------------------------------------------------

class WaveFormPanel(plot.PlotCanvas):

	def __init__(self, parent, sound_array=None, color=wx.BLUE):
		super(WaveFormPanel, self).__init__(parent, style=wx.SUNKEN_BORDER)
		self.SetEnableTitle(False)
		self.SetEnableLegend(False)
		self.SetEnablePointLabel(False)
		self.SetXSpec('none')
		self.SetYSpec('none')
		self.SetFontSizeAxis(1)
		self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
		self.DrawColor = color
		self.SetEnableAntiAliasing(True)
		self.SetEnableHiRes(True)
		if sound_array is not None:
			self.SetSoundArray(sound_array)
		
	def SetSoundArray(self, sndarray):
		if sndarray is None:
			sndarray = [(0, 0), (1, 0)]
		line = plot.PolyLine(sndarray, colour=self.DrawColor, width=1)
		gc = plot.PlotGraphics([line])
		self.Draw(gc)

#--------------------------------------------------------------------------------------
# SoundFile
#--------------------------------------------------------------------------------------

class SoundFile(object):
	def __init__(self, name, filelist):
		"""Basic constructor for the SoundFile class"""
		self.name = name
		self.Repeat = True
		self.SoundArray = None
		self.RPGFile = RPG.AudioFile()
		self.FileList = filelist
		self.Duration = 0
		self.Timer = wx.StopWatch()

	def GetVolume( self ):
		"""Returns the associates RPG.AudioFile's volume"""
		return self.RPGFile.volume

	def SetVolume( self, volume ):
		"""Sets the associates RPG.AudioFile's volume"""
		self.RPGFile.volume = volume

	def GetPitch( self ):
		"""Returns the associates RPG.AudioFile's pitch"""
		return self.RPGFile.pitch

	def SetPitch( self, pitch ):
		"""Sets the associates RPG.AudioFile's pitch"""
		self.RPGFile.pitch = pitch

	def GetIndex( self, filename=None):
		"""Returns the index of the associated file in the list"""
		if filename is None:
			filename = self.RPGFile.name
		if filename in self.FileList:
			return self.FileList.index(filename)
		return -1

	def GetPosition( self ):
		"""Returns the position of the song if is playing, else 0"""
		if self.Duration == 0:
			return 0
		if self.Timer.Time() > self.Duration * 1000:
			self.Timer.Start(0)
			return 0
		return (self.Timer.Time() / 1000) % self.Duration