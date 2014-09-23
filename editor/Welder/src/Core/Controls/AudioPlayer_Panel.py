import os
import sys
import numpy as np
import wx
import wx.lib.plot as plot
from datetime import timedelta

# Simple flag since currently pitch changing is only compatible with
# DirectSound
PITCH_ENABLED = sys.platform == 'win32'

from PyitectConsumes import PanelBase, AudioPlayer_Panel_Template, RTPFunctions
from PyitectConsumes import RGSS1_RPG as RPG
from PyitectConsumes import DatabaseManager as DM

if DM.ARC_FORMAT:
    AUDIO_DIRECTORIES = ['BGM', 'BGS', 'Sound']  # TODO: Sound?
else:
    AUDIO_DIRECTORIES = ['BGM', 'BGS', 'ME', 'SE']
# -------------------------------------------------------------------------
# AudioPlayer_Panel
# -------------------------------------------------------------------------


class AudioPlayer_Panel(AudioPlayer_Panel_Template, PanelBase):

    def __init__(self, parent, rpgfile=None, directory=None):
        """Basic constructor for the AudioPlayer"""

        # obtain a PyXAL interface
        AudioPlayer_Panel_Template.__init__(self, parent)
        # Set up the panel
        self.AudioIndex = 0
        if directory is not None:
            if directory in AUDIO_DIRECTORIES:
                self.AudioIndex = AUDIO_DIRECTORIES.index(directory)
            else:
                message = str.format("Directory \"{}\" does not exist.",
                                     os.path.join('Audio', directory))
                raise ValueError(message)
        DM.DrawButtonIcon(self.buttonPlay, 'play_button', True)
        DM.DrawButtonIcon(self.buttonPause, 'pause_button', True)
        DM.DrawButtonIcon(self.buttonStop, 'stop_button', True)
        self.waveFormPanelLeft.canvas.Bind(
            wx.EVT_ERASE_BACKGROUND, self.ControlOnEraseBackground)
        self.waveFormPanelRight.canvas.Bind(
            wx.EVT_ERASE_BACKGROUND, self.ControlOnEraseBackground)
        for dir in AUDIO_DIRECTORIES[1:]:
            self.notebookAudio.AddPage(wx.Panel(self.notebookAudio), dir)
        self.RefreshFileLists()
        # Setup the timer for updating the scroll bar
        self.UpdateTimer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Update)
        self.UpdateTimer.Start()
        # Disable scroll function if pitch changing is not permitted
        self.sliderPitch.Enable(PITCH_ENABLED)
        # Set the passed audio file, if, any, as the current selection"""
        self.Channels = [AudioChannel() for i in AUDIO_DIRECTORIES]
        if rpgfile is not None and dir is not None:
            self.Channels[self.AudioIndex].rpgaudio = rpgfile
        self.RefreshActivePage()

        # Bind the panel tot he Panel Manager
        self.BindPanelManager()

    def GetAudio(self):
        # TODO: Implement
        return RPG.AudioFile()

    def Update(self, event):
        """Updates the scrolling for the position slide control"""
        chan = self.Channels[self.AudioIndex]
        if chan.player is not None and chan.player.isPlaying():
            self.sliderPosition.SetValue(chan.GetOffset())
        del (chan)

    def RefreshFileLists(self):
        """Builds a list of filenames for each type of audio"""
        self.files = []
        for dir in AUDIO_DIRECTORIES:
            folder = os.path.join('Audio', dir)
            list = ['(None)']
            list.extend(RTPFunctions.GetFileList(folder, 'audio'))
            self.files.append(list)

    def RefreshActivePage(self):
        """Refreshes all the controls on the tab to reflect the current channel"""
        chan = self.Channels[self.AudioIndex]
        DM.FillWithoutNumber(
            self.listBoxAudio, [], self.files[self.AudioIndex])
        if chan.rpgaudio.name != '':
            index = self.files[self.AudioIndex].index(chan.rpgaudio.name)
        else:
            index = 0
        self.checkBoxRepeat.SetValue(chan.Repeat)
        self.RefreshFileLabel(chan)
        self.listBoxAudio.SetSelection(index)
        self.sliderVolume.SetValue(chan.rpgaudio.volume)
        self.sliderPitch.SetValue(chan.rpgaudio.pitch)
        self.spinCtrlVolume.SetValue(chan.rpgaudio.volume)
        self.spinCtrlPitch.SetValue(chan.rpgaudio.pitch)
        self.waveFormPanelLeft.SetSoundArray(chan.LeftChannel)
        self.waveFormPanelRight.SetSoundArray(chan.RightChannel)

    def RefreshFileLabel(self, channel):
        """Refreshes the labels for the filename and the duration"""
        if channel.player is None or channel.rpgaudio.name == '':
            if self.checkBoxMicroseconds.GetValue():
                labels = '(None)', '[0:00:00.000000]'
            else:
                labels = '(None)', '[0:00:00]'
        else:
            if self.checkBoxMicroseconds.GetValue():
                labels = (channel.rpgaudio.name,
                          str.format('[{}]', timedelta(seconds=channel.GetDuration())))
            else:
                labels = (channel.rpgaudio.name,
                          str.format('[{}]', timedelta(seconds=np.ceil(channel.GetDuration()))))
        self.labelFileName.SetLabel(labels[0])
        self.labelFileDuration.SetLabel(labels[1])

    def notebookAudio_PageChanged(self, event):
        """Updates the controls on the page to display the current file, if any"""
        self.AudioIndex = event.GetSelection()
        self.RefreshActivePage()

    def listBoxAudio_DoubleClick(self, event):
        """Plays the selected file with current settings"""
        self.PlayFile(event.GetInt())

    def PlayFile(self, index):
        """Plays the currently selected file"""
        chan = self.Channels[self.AudioIndex]
        name = self.listBoxAudio.GetStringSelection()
        if index == 0 or name not in self.files[self.AudioIndex]:
            if chan.player is not None:
                chan.SetFile(RPG.AudioFile(), '')
            self.waveFormPanelLeft.SetSoundArray(None)
            self.waveFormPanelRight.SetSoundArray(None)
            return
        volume = self.spinCtrlVolume.GetValue()
        pitch = self.spinCtrlPitch.GetValue()
        folder = os.path.join('Audio', AUDIO_DIRECTORIES[self.AudioIndex])
        path = RTPFunctions.FindAudioFile(folder, name)
        chan.SetFile(RPG.AudioFile(name, volume, pitch), path)
        chan.Play(chan.Repeat)
        self.sliderPosition.SetRange(0, chan.GetDuration())
        self.waveFormPanelLeft.SetSoundArray(chan.LeftChannel)
        self.waveFormPanelRight.SetSoundArray(chan.RightChannel)
        self.RefreshFileLabel(chan)
        del (chan)

    def sliderVolume_Scrolled(self, event):
        """Sets the volume of the sound. Changes player volume if playing."""
        self.spinCtrlVolume.SetValue(event.GetInt())
        self.Channels[self.AudioIndex].SetVolume(event.GetInt())

    def spinCtrlVolume_ValueChanged(self, event):
        """Sets the volume of the sound. Changes player volume if playing."""
        self.sliderVolume.SetValue(event.GetInt())
        self.Channels[self.AudioIndex].SetVolume(event.GetInt())

    def sliderPitch_Scrolled(self, event):
        """Changes the pitch of the sound if PITCH_ENABLED flag is present"""
        pitch = event.GetInt()
        self.spinCtrlPitch.SetValue(pitch)
        self.Channels[self.AudioIndex].SetPitch(pitch)

    def spinCtrlPitch_ValueChanged(self, event):
        """Changes the pitch of the sound if PITCH_ENABLED flag is present"""
        pitch = event.GetInt()
        self.sliderPitch.SetValue(pitch)
        self.Channels[self.AudioIndex].SetPitch(pitch)

    def sliderPosition_Scrolled(self, event):
        # TODO: Implement seek functions?
        pass

    def buttonPlay_Clicked(self, event):
        """Plays the selected file"""
        index = self.listBoxAudio.GetSelection()
        if index != -1:
            self.PlayFile(index)

    def buttonPause_Clicked(self, event):
        """Pauses playback on the current channel"""
        chan = self.Channels[self.AudioIndex]
        if chan.player is not None and chan.player.isPlaying():
            chan.player.pause()

    def buttonStop_Clicked(self, event):
        """Stops playback on the current channel"""
        chan = self.Channels[self.AudioIndex]
        if chan.player is not None:
            chan.player.stop()

    def buttonStopAll_Clicked(self, event):
        """Stops playback on all channels"""
        for chan in self.Channels:
            if chan.player is not None:
                chan.player.stop()

    def checkBoxRepeat_CheckChanged(self, event):
        """Sets the repeat flag on the current channel"""
        self.Channels[self.AudioIndex].Repeat = event.Checked()

    def ControlOnEraseBackground(self, event):
        """Reduces flicker on MSW by doing nothing"""
        pass

    def checkBoxMicroseconds_CheckChanged(self, event):
        """Changes flag to display microseconds in duration label"""
        self.RefreshActivePage()

    def buttonOK_Clicked(self, event):
        """Closes the window and returns wx.ID_OK"""
        self.GetParent().EndModal(wx.ID_OK)

    def buttonCancel_Clicked(self, event):
        """Closes the window and returns wx.ID_CANCEL"""
        self.GetParent().EndModal(wx.ID_CANCEL)

# -------------------------------------------------------------------------
# AudioChannel
# -------------------------------------------------------------------------


class AudioChannel(object):

    def __init__(self):
        """Basic constructor for an AudioChannel object"""
        # obtain a PyXAL interface
        self.PyXAL = DM.getPyXAL()
        self.player = None
        self.sound = None
        self.rpgaudio = RPG.AudioFile()
        self.LeftChannel = None
        self.RightChannel = None
        self.file = None
        self.Repeat = False

    def SetFile(self, rpgfile, filepath):
        """Sets the current player and sound"""
        self.rpgaudio = rpgfile
        if not (self.file == filepath):
            self.file = filepath
            if self.sound is not None:
                self.PyXAL.Mgr.destroySound(self.sound)
                del (self.sound)
            if self.player is not None:
                self.PyXAL.Mgr.destroyPlayer(self.player)
                del(self.player)
            if filepath == '' or rpgfile.name == '':
                self.sound = self.player = self.RightChannel = self.LeftChannel = None
                return
            self.sound = self.PyXAL.Mgr.createSound(self.file)
            self.player = self.PyXAL.Mgr.createPlayer(self.sound)
            array = self._getsoundarray(self.sound)
            self.RightChannel = self._shorten_array(array[:, 0])
            self.LeftChannel = self._shorten_array(array[:, 1])
            del (array)

    def SetVolume(self, volume):
        """Sets the volume of the audio file"""
        self.rpgaudio.volume = volume
        if self.player is not None and self.player.isPlaying():
            self.player.setGain(volume / 100.0)

    def SetPitch(self, pitch):
        """Sets the pitch of the audio file"""
        if not PITCH_ENABLED:
            return
        self.rpgaudio.pitch = pitch
        if self.player is not None and self.player.isPlaying():
            self.player.setPitch(pitch / 100.0)

    def GetVolume(self):
        """Returns the current setting for this file's volume"""
        return self.rpgaudio.volume

    def GetPitch(self):
        """Returns the current setting for this file's pitch"""
        return self.rpgaudio.pitch

    def GetLength(self):
        """Returns the length of the file, in bytes"""
        return self._length

    def GetDuration(self):
        """Returns the duration of the current sound, if any"""
        if self.sound is not None:
            return self.sound.getDuration()
        return 0

    def GetOffset(self):
        """Returns the offset, if any, of the current sound"""
        if self.player is not None:
            return self.player.getTimePosition()
        return 0

    def GetChannels(self):
        """Returns the number of channels the sound object has, if any"""
        if self.sound is not None:
            return self.sound.getChannels()
        return 0

    def GetSampleRate(self):
        """Returns the sampling rate of the sound object, if any"""
        if self.sound is not None:
            return self.sound.getSamplingRate()
        return 0

    def _shorten_array(self, y):
        """Shortens the number of elements in the sound array if there are too many"""
        length = len(y)
        if length > 30000:
            y = y[::length / 30000]
        x = np.arange(len(y), dtype=int)
        if length > 16000:
            data = np.column_stack((x[::4], y[::4]))
        elif length > 8000:
            data = np.column_stack((x[::2], y[::2]))
        else:
            data = np.column_stack((x, y))
        return data

    def _getsoundarray(self, sound):
        """Returns an array of data that represents the sound object"""
        typecodes = {8: np.int8,   # AUDIO_S8
                     16: np.int16,  # AUDIO_S16
                     24: np.int32  # 24 bit integers! oh god!
                     }
        size, raw_data = self.sound.readPcmData()
        if size > 0:
            typecode = typecodes[sound.getBitsPerSample()]
            if sound.getBitsPerSample() == 24:
                source = np.fromstring(raw_data, np.int8)
                if sound.getChannels() > 1:
                    source = np.resize(
                        source, (len(source) / 2, sound.getChannels()))
                    new_size_right = int(len(source[:, 1]) * (1 + 1.0 / 3.0))
                    new_size_left = int(len(source[:, 0]) * (1 + 1.0 / 3.0))
                    target_right = np.zeros(new_size_right, np.int8)
                    target_left = np.zeros(new_size_left, np.int8)
                    target_right[::4] = source[0::3, 1]
                    target_right[1::4] = source[1::3, 1]
                    target_right[3::4] = source[2::3, 1]
                    target_left[::4] = source[0::3, 0]
                    target_left[1::4] = source[2::3, 0]
                    target_left[3::4] = source[1::3, 0]
                    string_right = target_right.tostring()
                    string_left = target_left.tostring()
                    del target_left
                    del target_right
                    del source
                    array_right = np.fromstring(string_right, typecode)
                    array_left = np.fromstring(string_left, typecode)
                    array = np.column_stack((array_right, array_left))
                else:
                    new_size = int(len(source) * (1 + 1.0 / 3.0))
                    target = np.zeros(new_size, np.int8)
                    target[::4] = source[0::3, 0]
                    target[1::4] = source[2::3, 0]
                    target[3::4] = source[1::3, 0]
                    string = target.tostring()
                    del target
                    del source
                    array = np.fromstring(string, typecode)
                    array = np.column_stack((array, array))
            else:
                array = np.fromstring(raw_data, typecode)
                if sound.getChannels() > 1:  # Stereo
                    array = np.resize(
                        array, (len(array) / 2, sound.getChannels()))
                else:  # Mono
                    array = np.column_stack((array, array))
        else:
            array = np.zeros((1, 2), dtype=np.int8)
        del (size)
        del (raw_data)
        return array

    def Play(self, loop=False):
        """Starts playback of the current file and applies volume and pitch settings"""
        if (self.player is not None) and (self.sound is not None):
            self.player.play(looping=loop)
            self.player.setGain(self.rpgaudio.volume / 100.0)
            if PITCH_ENABLED:
                self.player.setPitch(self.rpgaudio.pitch / 100.0)

    def Pause(self):
        """Pauses playback"""
        if (self.player is not None) and (self.sound is not None):
            self.player.pause()

    def Stop(self):
        """Stops playback"""
        if (self.player is not None) and (self.sound is not None):
            self.player.stop()

# -------------------------------------------------------------------------
# WaveFormPanel
# -------------------------------------------------------------------------


class WaveFormPanel(plot.PlotCanvas):

    def __init__(self, parent, sound_array=None, color=wx.BLUE):
        """Basic constructor for the WaveFormPanel"""
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
        """Sets the data array and redraws the data"""
        if sndarray is None:
            sndarray = [(0, 0), (1, 0)]
        line = plot.PolyLine(sndarray, colour=self.DrawColor, width=1)
        gc = plot.PlotGraphics([line])
        self.Draw(gc)
        del (gc)
        del (line)
        del (sndarray)
