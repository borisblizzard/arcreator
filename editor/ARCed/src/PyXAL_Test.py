# -*- coding: utf-8 -*- 
import os
import wx
import wx.lib.plot as plot
import numpy as np
import Kernel
from Kernel import Manager as KM
import Core

PyXAL = KM.get_component("PyXAL").object

#--------------------------------------------------------------------------------------
# WaveFormPanel
#--------------------------------------------------------------------------------------

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
        self.Draw(gc,) # len(sndarray), max(sndarray[0])

class XALTestFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        mainsizer = wx.BoxSizer( wx.VERTICAL )
        
        self.mainpanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        panelsizer = wx.BoxSizer( wx.VERTICAL )
        
        self.filepicker = wx.FilePickerCtrl( self.mainpanel, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        panelsizer.Add( self.filepicker, 0, wx.RIGHT|wx.LEFT|wx.EXPAND|wx.ALL, 5 )
        
        self.playbt = wx.Button( self.mainpanel, wx.ID_ANY, u"play", wx.DefaultPosition, wx.DefaultSize, 0 )
        panelsizer.Add( self.playbt, 0, wx.ALL, 5 )
        
        self.pausebt = wx.Button( self.mainpanel, wx.ID_ANY, u"pause", wx.DefaultPosition, wx.DefaultSize, 0 )
        panelsizer.Add( self.pausebt, 0, wx.ALL, 5 )
        
        self.stopbt = wx.Button( self.mainpanel, wx.ID_ANY, u"stop", wx.DefaultPosition, wx.DefaultSize, 0 )
        panelsizer.Add( self.stopbt, 0, wx.ALL, 5 )

        color = wx.Colour(100, 100, 220, 255)
        self.waveFormPanelRight = WaveFormPanel(self, color=color)
        self.waveFormPanelRight.SetMinSize( wx.Size( -1,64 ) )

        panelsizer.Add(self.waveFormPanelRight, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5  )

        color = wx.Colour(100, 100, 220, 255)
        self.waveFormPanelLeft = WaveFormPanel(self, color=color)
        self.waveFormPanelLeft.SetMinSize( wx.Size( -1,64 ) )

        panelsizer.Add(self.waveFormPanelLeft, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5  )
        
        self.mainpanel.SetSizer( panelsizer )
        self.mainpanel.Layout()
        panelsizer.Fit( self.mainpanel )
        mainsizer.Add( self.mainpanel, 1, wx.EXPAND |wx.ALL, 0 )
        
        self.SetSizer( mainsizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.filepicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_change_file )
        self.playbt.Bind( wx.EVT_BUTTON, self.on_play )
        self.pausebt.Bind( wx.EVT_BUTTON, self.on_pause )
        self.stopbt.Bind( wx.EVT_BUTTON, self.on_stop )
        
        #============================================
        #and here we find out if it's all worked
        self.SetUpXAL()
        
        self.player = None
        self.sound = None
        self.file = None
        

    def SetUpXAL(self): 
        PyXAL.EnableLogging(True, os.path.abspath("log"))
        PyXAL.Init(self.GetHandle(), True)
        print "XAL Setup"
    
    def __del__( self ):
        PyXAL.Destroy()
        print "XAL Destroyed"
    
    def on_change_file( self, event ):
        self.file = str(self.filepicker.GetPath())
        if self.player is not None:
            PyXAL.Mgr.destroyPlayer(self.player)
        if self.sound is not None:
            PyXAL.Mgr.destroySound(self.sound)
        self.sound = PyXAL.Mgr.createSound(self.file)
        self.player = PyXAL.Mgr.createPlayer(self.sound)
        print "XAL opened File"
        array = self.getsoundarray(self.sound)
        right = self.shorten_array(array[:, 0])
        left = self.shorten_array(array[:, 1])
        self.waveFormPanelLeft.SetSoundArray(right)
        self.waveFormPanelRight.SetSoundArray(left)

    def shorten_array(self, y):
        length = len(y)
        if length > 30000:
            y = y[::length/30000]
        x = np.arange(len(y), dtype=int)
        if length > 16000:
            data = np.column_stack((x[::4], y[::4]))
        elif length > 8000:
            data = np.column_stack((x[::2], y[::2]))
        else:
            data = np.column_stack((x, y))
        return data

    def getsoundarray(self, sound):
        typecodes = { 8 : np.int8,   # AUDIO_S8
                      16 : np.int16, # AUDIO_S16
                      24 : np.int32  # 24 bit integers! oh god!
                    }
        data = self.sound.readPcmData()
        size = data[0]
        raw_data = data[1]
        print "length: %s" % len(raw_data)
        print "calc duration: %s" % (float(sound.getSize()) / sound.getChannels() / (sound.getBitsPerSample() / 8) / sound.getSamplingRate())
        print "duration: %s" % sound.getDuration()
        print "sample rate: %s" % sound.getSamplingRate()
        print "samples in data: %s" % (sound.getSize() / sound.getChannels() / (sound.getBitsPerSample() / 8))
        print "bits per sample: %s" % sound.getBitsPerSample()
        print "channels: %s" % sound.getChannels()
        if size > 0:
            typecode = typecodes[sound.getBitsPerSample()]
            if sound.getBitsPerSample() == 24: # ugg 24 bit intergers...
                source = np.fromstring(raw_data, np.int8)
                if sound.getChannels() > 1: # *facepalm* STEREO 24 bit integers, I hate life...
                    #resize/shape the source to a 2 d array 
                    source = np.resize(source, (len(source)/2, sound.getChannels()))
                    #we have to pad the 24 bit integers to 32 bit integers to convert them
                    #so first we calculate the size of an array that has one extra byte
                    new_size_right = int(len(source[:, 1]) * (1 + 1.0 / 3.0))
                    new_size_left = int(len(source[:, 0]) * (1 + 1.0 / 3.0))
                    #make new arrays that size filled with zeros
                    target_right = np.zeros(new_size_right, np.int8)
                    target_left = np.zeros(new_size_left, np.int8)
                    #shift the bytes over from the right channel leaving a 0
                    #it was guess and check to get the byte order right
                    target_right[::4] = source[0::3, 1]
                    target_right[1::4] = source[1::3, 1]
                    target_right[3::4] = source[2::3, 1]
                    #shift the bytes over from the left channel leaving a 0
                    #once again it was guess and check to get the byte order right oddly enough the byte order is DIFFERENT!
                    target_left[::4] = source[0::3, 0]
                    target_left[1::4] = source[2::3, 0]
                    target_left[3::4] = source[1::3, 0]
                    #convert the arrays to strings so they can be reinterpreted as 32 bit integers
                    string_right = target_right.tostring()
                    string_left = target_left.tostring()
                    #make sure we keep memory down (THESE OBJECTS ARE LARGE!)
                    del target_left
                    del target_right
                    del source
                    #create the arrays from the strings using the in32 dtype, we now have the real values
                    array_right = np.fromstring(string_right, typecode)
                    array_left = np.fromstring(string_left, typecode)
                    #stack the arrays together pairing off the values
                    array = np.column_stack((array_right, array_left))
                else: # oh goody only mono 24 bit integers
                    #as above we have to bad the 24 bit integers to 32 bits
                    #calculate the new arrays size with a byte added
                    new_size = int(len(source) * (1 + 1.0 / 3.0))
                    #create that array
                    target = np.zeros(new_size, np.int8)
                    #shift the bytes over leaving a 0
                    #I honestly don;t know if the byte order is right for this one as I don't have any mono wav files to test
                    target[::4] = source[0::3, 0]
                    target[1::4] = source[2::3, 0]
                    target[3::4] = source[1::3, 0]
                    #convert to a string
                    string = target.tostring()
                    #make sure we keep memory down (THESE OBJECTS ARE LARGE!)
                    del target
                    del source
                    #create the new array interpreting as 32bit integers
                    array = np.fromstring(string, typecode)
                    #stack the arrays on top of itself (right and left are the same) so we always return a 2d array
                    array = np.column_stack((array, array))
            else: #oh good Numpy can interpret these strings natively
                #convert the string to an array using a 16 or 8 bit data type
                array = np.fromstring(raw_data, typecode)
                if sound.getChannels() > 1: #we're in stereo so let's reshape the array
                    array = np.resize(array, (len(array)/2, sound.getChannels()))
                else: #not in stereo
                    #stack the arrays on top of itself (right and left are the same) so we always return a 2d array
                    array = np.column_stack((array, array))
        else: # we didn't get any data so lets just return a 1 element 2d array of zeros
            array = np.zeros((1, 2), dtype=np.int8)
        print "array size: %s" % len(array)
        return array
    
    def on_play( self, event ):
        if (self.player is not None) and (self.sound is not None):
            self.player.play()
            print "playing"
    
    def on_pause( self, event ):
        if (self.player is not None) and (self.sound is not None):
            self.player.pause()
            print "pauseing"
        
    def on_stop( self, event):
        if (self.player is not None) and (self.sound is not None):
            self.player.stop()
            print "stoping"
        
        
if __name__ == '__main__':

    provider = wx.SimpleHelpProvider()
    wx.HelpProvider.Set(provider)

    redirect = False
    
    app = wx.App(redirect)
    
    frame = XALTestFrame(None)
    frame.Show(True)
    
    app.MainLoop()