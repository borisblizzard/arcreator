# -*- coding: utf-8 -*- 

import wx
import os
import Kernel
from Kernel import Manager as KM
import Core


PyXAL = KM.get_component("PyXAL").object

class XALTestFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        mainsizer = wx.BoxSizer( wx.VERTICAL )
        
        self.mainpanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        panelsizer = wx.BoxSizer( wx.VERTICAL )
        
        self.filepicker = wx.FilePickerCtrl( self.mainpanel, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        panelsizer.Add( self.filepicker, 0, wx.ALL, 5 )
        
        self.playbt = wx.Button( self.mainpanel, wx.ID_ANY, u"play", wx.DefaultPosition, wx.DefaultSize, 0 )
        panelsizer.Add( self.playbt, 0, wx.ALL, 5 )
        
        self.pausebt = wx.Button( self.mainpanel, wx.ID_ANY, u"pause", wx.DefaultPosition, wx.DefaultSize, 0 )
        panelsizer.Add( self.pausebt, 0, wx.ALL, 5 )
        
        self.stopbt = wx.Button( self.mainpanel, wx.ID_ANY, u"stop", wx.DefaultPosition, wx.DefaultSize, 0 )
        panelsizer.Add( self.stopbt, 0, wx.ALL, 5 )
        
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
        if self.sound is not None:
            PyXAL.Mgr.destroySound(self.sound)
        if self.player is not None:
            PyXAL.Mgr.destroyPlayer(self.player)
        self.sound = PyXAL.Mgr.createSound(self.file)
        self.player = PyXAL.Mgr.createPlayer(self.sound)
        print "XAL opened File"
    
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