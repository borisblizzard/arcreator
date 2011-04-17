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
from pyglet import gl

#load our libaries
import Core
import pygletwx
from cache import PygletCache as Cache

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

    def __init__(self, parent, map, tilesets, toolbar, id=wx.ID_ANY):
        super(TilemapPanel, self).__init__(parent, id, wx.DefaultPosition, wx.Size(800, 600), 
              wx.VSCROLL | wx.HSCROLL)
        
        #set data
        self.map = map
        self.tilesets = tilesets
        self.NeedRedraw = False
        self.activeLayer = 0
        self.toolbar = toolbar
        self.toolbar.mapwin = self
        self.translateX = 0
        self.translateY = 0
        
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
        
        
    def SetOrigin(self):
        size = self.GetGLExtents()
        gl.glViewport(0, 0,  size.width,  size.height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(0,  size.width, 0,  size.height, -1, 1)
        x = -self.GetScrollPos(wx.HORIZONTAL)
        y = -(self.map.height * 32) + size.height + self.GetScrollPos(wx.VERTICAL)
        gl.glTranslatef(x, y, 0)
        self.translateX = x
        self.translateY = y
        self.tilemap.setDimXY(-x, -y)
        gl.glMatrixMode(gl.GL_MODELVIEW)
    
    def create_objects(self):
        '''create opengl objects when opengl is initialized'''
        data = self.map.data._data
        tileset = self.tilesets[self.map.tileset_id]
        self.cache = Cache()
        self.tilemap = pygletwx.Tilemap(data, self.cache, tileset.tileset_name, tileset.autotile_names)
        self.SetActiveLayer(self.activeLayer)
        
    def update_object_resize(self, width, height):
        '''called when the window recieves only if opengl is initialized'''
        #update the scrollbar widths
        self.SetOrigin()
        size = self.GetVirtualSizeTuple()
        self.SetScrollbar(wx.HORIZONTAL, self.GetScrollPos(wx.HORIZONTAL), size[0], 
                          self.map.width * 32, refresh=True)
        self.SetScrollbar(wx.VERTICAL, self.GetScrollPos(wx.VERTICAL), size[1], 
                          self.map.height * 32, refresh=True)
        self.tilemap.UpdateDimmingSprite(width, height)
        
    def draw_objects(self):
        '''called in the middle of ondraw after the buffer has been cleared'''
        self.tilemap.update()
        self.tilemap.Draw()
        
    def Update(self, event):
        self.PrepareGL() 
        if self.NeedRedraw:
            self.OnDraw()
            self.NeedRedraw = False
            
    def update_scroll_pos(self, event):
        self.OnScroll(event.GetOrientation(), event.GetPosition())
        event.Skip()
        
    def scroll_lineup(self, event):
        orient = event.GetOrientation()
        pos = self.GetScrollPos(orient)
        new_pos = pos - 1
        if new_pos < 0:
            new_pos = 0
        if new_pos > self.GetScrollRange(orient):
            new_pos = self.GetScrollRange(orient)
        self.OnScroll(orient, new_pos)
        
    def scroll_linedown(self, event):
        orient = event.GetOrientation()
        pos = self.GetScrollPos(orient)
        new_pos = pos + 1
        if new_pos < 0:
            new_pos = 0
        if new_pos > self.GetScrollRange(orient):
            new_pos = self.GetScrollRange(orient)
        self.OnScroll(orient, new_pos)
        
    def scroll_pageup(self, event):
        orient = event.GetOrientation()
        pos = self.GetScrollPos(orient)
        new_pos = pos - 32
        if new_pos < 0:
            new_pos = 0
        if new_pos > self.GetScrollRange(orient):
            new_pos = self.GetScrollRange(orient)
        self.OnScroll(orient, new_pos)
        
    def scroll_pagedown(self, event):
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
        self.SetOrigin()
        self.OnDraw()
        self.SetScrollbar(orient, pos, thumb, range, refresh=True)
        
    def SetActiveLayer(self, layer):
        self.tilemap.setDimXY(-self.translateX, -self.translateY)
        self.activeLayer = layer
        print "activelayer set"
        self.tilemap.SetActiveLayer(layer)
        self.OnDraw()
    
    def SetLayerDimming(self, bool):
        self.tilemap.SetLayerDimming(bool)
        self.OnDraw()

class MapPanel(wx.Panel):
    
    def __init__(self, parent, map, tilesets,  id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
        '''lays out a toolbar and the map window'''
        super(MapPanel, self).__init__(parent, id, pos, size, style)
        #set data
        self.map = map
        self.tilesets = tilesets
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        #toolbar
        self.Create_Toolbar()
        #map
        self.mapwin = TilemapPanel(self, self.map, self.tilesets, self.toolbar)
        self.sizer.Add(self.mapwin, 1, wx.EXPAND)
        #set the sizer and layout the panel
        self.SetSizer(self.sizer)
        self.Layout()
           
    def Create_Toolbar(self):
        '''creates the toolbar and adds tools'''
        self.toolbar = MapToolbar(self, self.map)
        self.sizer.Add(self.toolbar, 0, wx.EXPAND)
        
        
class MapToolbar(wx.ToolBar):
    
    def __init__(self, parent, map, style=0):
        '''Toolbar for the map editor'''
        super(MapToolbar, self).__init__(parent, style=style)
        
        self.map = map
        self.mapwin = None
        self.layers = self.map.data._data.shape[2]
        self.layerChoiceIDs = {}
        self.layerSet = False
        self.SetupToolIDs()
        self.SetupTools()
        self.BindToolEvents()
        
    def SetupTools(self):
        tsize = (16,16)
        new_bmp =  wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, tsize)
        self.SetToolBitmapSize(tsize)
        #add layer tools
        #generate choice list 
        layerChoices = self.GenLayerChoices()
        self.layerChoice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition,
                                    wx.DefaultSize, layerChoices, 0)
        self.layerChoice.SetSelection(0)
        self.AddControl(self.layerChoice)
        self.AddSeparator() 
        # a dimlayers choice box
        self.dimLayersCB = wx.CheckBox(self, label="Dim Layers")
        self.dimLayersCB.SetValue(True)
        self.AddControl(self.dimLayersCB)
        self.AddSeparator() 
        
        self.Realize() 
         
    def GenLayerChoices(self):
        choices = []
        self.layerChoiceIDs = {}
        for z in range(self.map.data._data.shape[2]):
            choice = "Layer %s" % (z + 1)
            self.layerChoiceIDs[choice] = z
            choices.append(choice)
        return choices

    def BindToolEvents(self):
        #layer choice
        self.Bind(wx.EVT_CHOICE, self.OnLayerChoice, self.layerChoice)
        self.Bind(wx.EVT_UPDATE_UI, self.UpdateLayerChoices, self.layerChoice)
        #dim layers box
        self.Bind(wx.EVT_CHECKBOX, self.OnDimLayersChoice, self.dimLayersCB)
    
    def SetupToolIDs(self):
        self.layer1ID = 1
        self.layer2ID = 2
        self.layer3ID = 3
        self.layer4ID = 4
        self.PenID = 5
        self.RecID = 6
        self.ElipID = 7
        self.BucketID = 8
        self.SelectID = 9
                
    def OnDimLayersChoice(self, event):
        if self.mapwin is not None:
            self.mapwin.SetLayerDimming(event.IsChecked())
    
    def OnLayerChoice(self, event):
        self.layerSet = False
        if self.mapwin is not None:
            self.layerSet = True
            layer = self.layerChoiceIDs[self.layerChoice.GetItems()[self.layerChoice.GetSelection()]]
            self.mapwin.SetActiveLayer(layer)
    
    def UpdateLayerChoices(self, event): 
        if not(self.layers == self.map.data._data.shape[2]):
            self.layers = self.map.data._data.shape[2]
            choices = self.GenLayerChoices()
            self.layerChoice.SetItems(choices)
        if (self.mapwin is not None) and (not self.layerSet):
            self.layerSet = True
            selection = self.layerChoice.GetSelection()
            items = self.layerChoice.GetItems()
            layer = self.layerChoiceIDs[items[selection]]
            self.mapwin.SetActiveLayer(layer) 
            
        
    
class TestFrame(wx.Frame):
    '''A simple class for using OpenGL with wxPython.'''

    def __init__(self, parent, id, title, pos=wx.DefaultPosition,
                 size=wx.Size(800, 600), style=wx.DEFAULT_FRAME_STYLE,
                 name='frame'):
        super(TestFrame, self).__init__(parent, id, title, pos, size, style, name)
        
        self.mainsizer = wx.BoxSizer(wx.HORIZONTAL)
        #self.GLPanel1 = TestGlPanel(self)
        #self.mainsizer.Add(self.GLPanel1, 1, wx.EXPAND, 5)
        #self.GLPanel2 = TestGlPanel(self, wx.ID_ANY, (20, 20))
        #self.mainsizer.Add(self.GLPanel2, 1, wx.EXPAND, 5)
        
        self.map = self.load_data('data/Map001.xppy')
        self.tilesets = self.load_data('data/Tilesets.xppy')
        
        self.MapEditorPanel = MapPanel(self, self.map, self.tilesets)
        self.mainsizer.Add(self.MapEditorPanel, 1, wx.EXPAND, 5)
        
        self.SetSizer(self.mainsizer)
        self.Layout()

        
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