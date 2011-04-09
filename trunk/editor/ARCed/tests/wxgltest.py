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
        super(TilemapPanel, self).__init__(parent, id, wx.DefaultPosition, wx.DefaultSize, 0)
        self.map = map
        self.tilesets = tilesets
        
    def create_objects(self):
        '''create opengl objects when opengl is initialized'''
        data = self.map.data._data
        tileset = self.tilesets[self.map.tileset_id]
        self.tilemap = pygletwx.Tilemap(data, tileset.tileset_name, tileset.autotile_names)
        
    def update_object_resize(self):
        '''called when the window recieves only if opengl is initialized'''
        pass
        
    def draw_objects(self):
        '''called in the middle of ondraw after the buffer has been cleared'''
        self.tilemap.update()
        self.tilemap.Draw()

class TestFrame(wx.Frame):
    '''A simple class for using OpenGL with wxPython.'''

    def __init__(self, parent, id, title, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE,
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