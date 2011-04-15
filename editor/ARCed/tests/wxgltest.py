import os
import cPickle


try:
    import wx
    from wx import glcanvas
except ImportError:
    raise ImportError, "Required dependency wx.glcanvas not present"
    
try:
    from numpy import *
except ImportError:
    raise ImportError, "Required dependency numpy not present"
    
import pyglet

#load our libaries
import Core
import pygletwx

class TestGlPanel(pygletwx.GLPanel):
    
    def __init__(self, parent, id=wx.ID_ANY, pos=(10, 10)):
        super(TestGlPanel, self).__init__(parent, id, wx.DefaultPosition, wx.DefaultSize, 0)
        self.spritepos = pos
        
    def create_objects(self):
        '''create opengl objects when opengl is initialized'''
        FOO_IMAGE = pyglet.image.load('foo.png')
        self.batch = pyglet.graphics.Batch()
        self.sprite = pyglet.sprite.Sprite(FOO_IMAGE, batch=self.batch)
        self.sprite.x = self.spritepos[0]
        self.sprite.y = self.spritepos[1]
        self.sprite2 = pyglet.sprite.Sprite(FOO_IMAGE, batch=self.batch)
        self.sprite2.x = self.spritepos[0] + 30
        self.sprite2.y = self.spritepos[1] + 20
        
    def update_object_resize(self):
        '''called when the window recieves only if opengl is initialized'''
        pass
        
    def draw_objects(self):
        '''called in the middle of ondraw after the buffer has been cleared'''
        self.batch.draw()
        
class TilemapPanel(pygletwx.GLPanel):

    def __init__(self, parent, map, tilesets, id=wx.ID_ANY):
        super(TilemapPanel, self).__init__(parent, id, wx.DefaultPosition, (800, 600), 
              wx.VSCROLL | wx.HSCROLL)
        
        #set data
        self.map = map
        self.tilesets = tilesets
        self.NeedRedraw = False
        
        #set up scrollbars
        size = self.GetVirtualSizeTuple()
        width = self.map.width * 32
        height = self.map.height * 32
        self.SetScrollbar(wx.HORIZONTAL, 0, size[0], width, refresh=True)
        self.SetScrollbar(wx.VERTICAL, 0, size[1], height, refresh=True)
        
        #scrollbar event
        self.Bind(wx.EVT_SCROLLWIN_TOP, self.scroll_top)
        self.Bind(wx.EVT_SCROLLWIN_BOTTOM, self.scroll_bottom)
        self.Bind(wx.EVT_SCROLLWIN_LINEUP, self.scroll_lineup)
        self.Bind(wx.EVT_SCROLLWIN_LINEDOWN, self.scroll_linedown)
        self.Bind(wx.EVT_SCROLLWIN_PAGEUP, self.scroll_pageup)
        self.Bind(wx.EVT_SCROLLWIN_PAGEDOWN, self.scroll_pagedown)
        self.Bind(wx.EVT_SCROLLWIN_THUMBTRACK, self.update_scroll_pos)
        self.Bind(wx.EVT_SCROLLWIN_THUMBRELEASE, self.update_scroll_pos)
        # UI update
        self.Bind(wx.EVT_UPDATE_UI, self.Update) 
        
    def Update(self, event):
        self.PrepareGL() 
        if self.NeedRedraw:
            self.OnDraw()
            self.NeedRedraw = False
            
    def update_scroll_pos(self, event):
        print 'Scroll To Pos'
        self.OnScroll(event.GetOrientation(), event.GetPosition())
        self.NeedRedraw = True
        event.Skip()
        
    def scroll_lineup(self, event):
        print 'Scroll Line Up'
        orient = event.GetOrientation()
        pos = self.GetScrollPos(orient)
        new_pos = pos - 1
        if new_pos < 0:
            new_pos = 0
        if new_pos > self.GetScrollRange(orient):
            new_pos = self.GetScrollRange(orient)
        self.OnScroll(orient, new_pos)
        
    def scroll_linedown(self, event):
        print 'Scroll Line Down'
        orient = event.GetOrientation()
        pos = self.GetScrollPos(orient)
        new_pos = pos + 1
        if new_pos < 0:
            new_pos = 0
        if new_pos > self.GetScrollRange(orient):
            new_pos = self.GetScrollRange(orient)
        self.OnScroll(orient, new_pos)
        
    def scroll_pageup(self, event):
        print 'Scroll Page up'
        orient = event.GetOrientation()
        pos = self.GetScrollPos(orient)
        new_pos = pos - 32
        if new_pos < 0:
            new_pos = 0
        if new_pos > self.GetScrollRange(orient):
            new_pos = self.GetScrollRange(orient)
        self.OnScroll(orient, new_pos)
        
    def scroll_pagedown(self, event):
        print 'Scroll Page Down'
        orient = event.GetOrientation()
        pos = self.GetScrollPos(orient)
        new_pos = pos + 32
        if new_pos < 0:
            new_pos = 0
        if new_pos > self.GetScrollRange(orient):
            new_pos = self.GetScrollRange(orient)
        self.OnScroll(orient, new_pos)
        
    def scroll_top(self, event):
        print 'Scroll Top'
    def scroll_bottom(self, event):
        print 'Scroll Bottom'
        
    def OnScroll(self, orient, pos):
        size = self.GetVirtualSizeTuple()
        if orient == wx.HORIZONTAL:
            thumb = size[0]
            range = self.map.width * 32
        elif orient == wx.VERTICAL:
            thumb = size[1]
            range = self.map.height * 32
        else:
            print orient
            print wx.HORIZONTAL
            print wx.VERTICAL
        
        self.SetScrollbar(orient, pos, thumb, range, refresh=True)
        
    def create_objects(self):
        '''create opengl objects when opengl is initialized'''
        data = self.map.data._data
        tileset = self.tilesets[self.map.tileset_id]
        self.tilemap = pygletwx.Tilemap(data, tileset.tileset_name, tileset.autotile_names)
        
    def update_object_resize(self):
        '''called when the window recieves only if opengl is initialized'''
        #update the scrollbar widths
        size = self.GetVirtualSizeTuple()
        self.SetScrollbar(wx.HORIZONTAL, self.GetScrollPos(wx.HORIZONTAL), size[0], 
                          self.map.width * 32, refresh=True)
        self.SetScrollbar(wx.VERTICAL, self.GetScrollPos(wx.VERTICAL), size[1], 
                          self.map.height * 32, refresh=True)
        
    def draw_objects(self):
        '''called in the middle of ondraw after the buffer has been cleared'''
        self.tilemap.update()
        self.tilemap.Draw()

class TestFrame(wx.Frame):
    '''A simple class for using OpenGL with wxPython.'''

    def __init__(self, parent, id, title, pos=wx.DefaultPosition,
                 size=(800, 600), style=wx.DEFAULT_FRAME_STYLE,
                 name='frame'):
        super(TestFrame, self).__init__(parent, id, title, pos, size, style, name)
        
        self.mainsizer = wx.BoxSizer(wx.HORIZONTAL)
        #self.GLPanel1 = TestGlPanel(self)
        #self.mainsizer.Add(self.GLPanel1, 1, wx.EXPAND, 5)
        #self.GLPanel2 = TestGlPanel(self, wx.ID_ANY, (20, 20))
        #self.mainsizer.Add(self.GLPanel2, 1, wx.EXPAND, 5)
        
        self.map = self.load_data('data/Map001.xppy')
        self.tilesets = self.load_data('data/Tilesets.xppy')
        
        self.TilemapPanel = TilemapPanel(self, self.map, self.tilesets)
        self.mainsizer.Add(self.TilemapPanel, 1, wx.EXPAND, 5)
        
        self.SetSizer(self.mainsizer)
        self.mainsizer.Fit(self)
        
        
        
        print self.map.data._data.shape
        
    def load_data(self, filename):
        f = open(os.path.normpath(filename), 'rb')
        data = cPickle.load(f)
        f.close()
        return data

    

app = wx.App(redirect=False)
frame = TestFrame(None, wx.ID_ANY, 'GL Window')
frame.Show()

app.MainLoop()
app.Destroy()