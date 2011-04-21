import os

import wx
from wx import glcanvas

import pyglet
from pyglet import gl

import numpy

class GLPanel(wx.Panel):

    '''A simple class for using OpenGL with wxPython.'''

    def __init__(self, parent, id, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        # Forcing a no full repaint to stop flickering
        style = style | wx.NO_FULL_REPAINT_ON_RESIZE
        #call super function
        super(GLPanel, self).__init__(parent, id, pos, size, style)

        #init gl canvas data
        self.GLinitialized = False
        attribList = (glcanvas.WX_GL_RGBA, # RGBA
                      glcanvas.WX_GL_DOUBLEBUFFER, # Double Buffered
                      glcanvas.WX_GL_DEPTH_SIZE, 32) # 24 bit
        # Create the canvas
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.canvas = glcanvas.GLCanvas(self, attribList=attribList)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Layout()

        # bind events
        self.canvas.Bind(wx.EVT_ERASE_BACKGROUND, self.processEraseBackgroundEvent)
        self.canvas.Bind(wx.EVT_SIZE, self.processSizeEvent)
        self.canvas.Bind(wx.EVT_PAINT, self.processPaintEvent)
        
    #==========================================================================
    # Canvas Proxy Methods
    #==========================================================================
    def GetGLExtents(self):
        '''Get the extents of the OpenGL canvas.'''
        return self.canvas.GetClientSize()

    def SwapBuffers(self):
        '''Swap the OpenGL buffers.'''
        self.canvas.SwapBuffers()

    #==========================================================================
    # wxPython Window Handlers
    #==========================================================================
    def processEraseBackgroundEvent(self, event):
        '''Process the erase background event.'''
        pass # Do nothing, to avoid flashing on MSWin

    def processSizeEvent(self, event):
        '''Process the resize event.'''
        if self.canvas.GetContext():
            # Make sure the frame is shown before calling SetCurrent.
            self.Show()
            self.canvas.SetCurrent()
            size = self.GetGLExtents()
            self.winsize = (size.width, size.height)
            self.width, self.height = size.width, size.height
            self.OnReshape(size.width, size.height)
            self.canvas.Refresh(False)
        event.Skip()

    def PrepareGL(self):
        self.canvas.SetCurrent()

        #initialize OpenGL only if we need to
        if not self.GLinitialized:
            self.OnInitGL()
            self.GLinitialized = True
            size = self.GetGLExtents()
            self.OnReshape(size.width, size.height)
            
        self.pygletcontext.set_current()
    
    def processPaintEvent(self, event):
        '''Process the drawing event.''' 
        self.PrepareGL()
        self.OnDraw()
        event.Skip()
        
    def Destroy(self):
        #clean up the pyglet OpenGL context
        self.pygletcontext.destroy()
        #call the super method
        super(wx.Panel, self).Destroy()

    #==========================================================================
    # GLFrame OpenGL Event Handlers
    #==========================================================================
    def OnInitGL(self):
        '''Initialize OpenGL for use in the window.'''
        #create a pyglet context for this panel
        self.pygletcontext = gl.Context(gl.current_context)
        self.pygletcontext.set_current()
        #normal gl init
        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        gl.glEnable(gl.GL_TEXTURE_2D)
        gl.glShadeModel(gl.GL_SMOOTH)
        gl.glClearColor(1, 1, 1, 1)
        
        #create objects to draw
        self.create_objects()
                                         
    def OnReshape(self, width, height):
        '''Reshape the OpenGL viewport based on the dimensions of the window.'''
        gl.glViewport(0, 0, width, height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        if width <= 0:
            width = 1
        if height <= 0:
            height = 1
        gl.glOrtho(0, width, 0, height, 1, -1)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        #pyglet stuff

        if self.GLinitialized:
            self.pygletcontext.set_current()
            self.update_object_resize(width, height)
            
    def OnDraw(self, *args, **kwargs):
        "Draw the window."
        #clear the context
        gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)
        #draw objects
        self.draw_objects()
        #update screen
        self.SwapBuffers()
            
    #==========================================================================
    # To be implamented by a sub class
    #==========================================================================
    def create_objects(self):
        '''create opengl objects when opengl is initialized'''
        pass
        
    def update_object_resize(self, width, height):
        '''called when the window recieves only if opengl is initialized'''
        pass
        
    def draw_objects(self):
        '''called in the middle of ondraw after the buffer has been cleared'''
        pass
       
rtppath = "%PROGRAMFILES%/Common Files/Enterbrain/RGSS/Standard"
RTP_Location = os.path.normpath(os.path.expandvars(rtppath))
Project_Location = ""

class EventStruct(object):

    def __init__(self, x, y, tile_id, name, hue, direction, pattern):
        self.x = x
        self.y = y
        self.tile_id = tile_id
        self.name = name
        self.hue = hue
        self.direction = direction
        self.pattern = pattern
        

class EventGrid(object):
    
    def __init__(self, map, cache, tileset=""):
        self.map = map
        self.cache = cache
        self.tileset_name = tileset
        self.renderingBatch = pyglet.graphics.Batch()
        self.backgroundGroup = pyglet.graphics.OrderedGroup(1)
        self.spriteGroup = pyglet.graphics.OrderedGroup(2)
        self.events = {}
        self.sprites = {}
        self.setupOutline()
        self.update()
        
    def setupOutline(self):
        outlineEdgePattern = pyglet.image.SolidColorImagePattern((255, 255, 255, 255))
        eventOutline = outlineEdgePattern.create_image(24, 24).get_texture()
        outlineBackPattern = pyglet.image.SolidColorImagePattern((255, 255, 255, 80))
        background = outlineBackPattern.create_image(22, 22)
        eventOutline.blit_into(background, 1, 1, 0)
        self.eventOutline = eventOutline.get_image_data()
    
    def setEventGraphic(self, key):
        #get event
        event = self.events[key] 
        #if the graphic is a tile
        if event.tile_id >= 384:
            bitmap = self.cache.Tile(self.tileset_name, event.tile_id, event.hue, Project_Location)
            if not bitmap:
                bitmap = self.cache.Tile(self.tileset_name, event.tile_id, event.hue, RTP_Location)
            if bitmap:
                rect = (5, 5, 22, 22)
        #other wise the graphic is a sprite
        else:
            bitmap = self.cache.Character(event.name, event.hue, Project_Location)
            if not bitmap:
                bitmap = self.cache.Character(event.name, event.hue, RTP_Location)
            if bitmap:
                cw = bitmap.width / 4
                ch = bitmap.height / 4
                sx = event.pattern * cw
                sy = (event.direction - 2) / 2 * ch
                rect = (sx + (cw - 22) / 2, bitmap.height - sy - ch / 2 - 5, 22, 22)
        
        #draw a portion of the event graphic
        if bitmap:
            image = pyglet.image.create(32, 32).get_texture()
            reagion = bitmap.get_region(*rect)
            image.blit_into(reagion, 5, 5, 0)
            
        xpos = event.x * 32
        ypos = ((self.map.height - event.y) * 32) - 32
        if not self.sprites.has_key(key) or self.sprites[key][0] is None:
            sprite = None
            if bitmap: 
               sprite = pyglet.sprite.Sprite(image, x=xpos, y=ypos, batch=self.renderingBatch, group=self.spriteGroup)
            
            background = pyglet.sprite.Sprite(self.eventOutline, x=xpos + 4, y=ypos + 4, 
                                 batch=self.renderingBatch, group=self.backgroundGroup)
            
            self.sprites[key] = [sprite, background]
        else:
            if bitmap:
                self.sprites[key][0].image = image 
            else:
                self.sprites[key][0].delete()
                self.sprites[key][0] = None
            
    def updateEvent(self, key):
        #get event
        flag = False
        mapEvent = self.map.events[key]
        graphic = self.map.events[key].pages[0].graphic
        if not self.events.has_key(key):
            event = EventStruct(mapEvent.x, mapEvent.y, graphic.tile_id, graphic.character_name,  
                                graphic.character_hue, graphic.direction, graphic.pattern)
            self.events[key] = event
            flag = True
        else:
            event = self.events[key]
            if event.x != mapEvent.x:
                event.x = mapEvent.x
            if event.y != mapEvent.x:
                event.y = mapEvent.y
            if event.tile_id != graphic.tile_id:
                flag = True
                event.tile_id = graphic.tile_id
            if event.name != graphic.character_name:
                flag = True
                event.name = graphic.character_name
            if event.hue != graphic.character_hue:
                flag = True
                event.hue = graphic.character_hue
            if event.direction != graphic.direction:
                flag = True
                event.direction = graphic.direction
            if event.pattern != graphic.pattern:
                flag = True
                event.pattern = graphic.pattern 
        if flag:
            self.setEventGraphic(key)
        #test values that are drawn to see if the graphic (or position) need to be updated
    
    def update(self):
        removed = list(set(self.events.keys()) - set(self.map.events.keys()))
        for key in removed:
            for sprite in self.events[key]:
                if sprite is not None:
                    sprite.delete()
            del self.events[key]
        for key in self.map.events.iterkeys():
            self.updateEvent(key)
            
    def Draw(self):
        self.renderingBatch.draw()
        
    def  __del__(self):
        self.destroy()
        
    def destroy(self):
        for group in self.sprites.itervalues():
            for sprite in group:
                if sprite is not None:
                    sprite.delete()

class TileGrid(object):

    def __init__(self, map):
        self.map = map
        self.sprites = []
        self.grid_image = pyglet.image.create(32, 32)
        self.renderingBatch = pyglet.graphics.Batch()
        self.setupGridImage()
        self.createGrid()
        
    def setupGridImage(self):
        self.black_pattern = pyglet.image.SolidColorImagePattern((0, 0, 0, 255))
        self.grid_image = self.black_pattern.create_image(32, 32).get_texture()
        self.cut_pattern = pyglet.image.create(30, 30)
        self.grid_image.blit_into(self.cut_pattern, 1, 1, 0)
        
    def createGrid(self):
        for x in range(self.map.width):
            for y in range(self.map.height):
                xpos = x * 32
                ypos = ((self.map.height - y) * 32) - 32
                sprite = pyglet.sprite.Sprite(self.grid_image, x=xpos, y=ypos, batch=self.renderingBatch)
                sprite.opacity = 80
                self.sprites.append(sprite)
                
    def Draw(self):
        self.renderingBatch.draw()
        
    def  __del__(self):
        self.destroy()
        
    def destroy(self):
        for sprite in self.sprites:
            sprite.delete()
                
class Tilemap(object):
    
    def __init__(self, data, cache, tileset="", autotiles=[]):
        self.cache = cache
        self.data = data
        self.tile_ids = numpy.zeros(data.shape)
        self.renderingBatches = []
        self.sprites = []
        self.blank_tile = pyglet.image.create(32, 32)
        self.dimmingImagePatteren = None
        self.dimmingImage = None
        self.dimmingSprite = None
        self.dimmingSpriteWidth = 0
        self.dimmingSpriteHeight = 0
        self.activeLayer = 0
        self.LayerDimming = True
        self.x = self.oldx = self.y = self.oldy = 0
        self.autotile_names = autotiles
        self.tileset_name = tileset
        self.ordered_groups = []
        for i in range(self.data.shape[2]):
            self.ordered_groups.append(pyglet.graphics.OrderedGroup(i))
            self.renderingBatches.append(pyglet.graphics.Batch())
        self.tiles = self.createTilemap()
    
    def UpdateDimmingSprite(self, width, height):
        if width != self.dimmingSpriteWidth or height != self.dimmingSpriteHeight:
            self.dimmingSpriteWidth = width
            self.dimmingSpriteHeight = height
            if self.dimmingImagePatteren is None:
                self.dimmingImagePatteren = pyglet.image.SolidColorImagePattern((0, 0, 0, 255))
            self.dimmingImage = self.dimmingImagePatteren.create_image(width, height).get_texture()
            self.dimmingSprite = pyglet.sprite.Sprite(self.dimmingImage, 0, 0)
            self.dimmingSprite.opacity = 180
            #self.dimmingSprite.draw()
    def setDimXY(self, x, y):
        if self.dimmingSprite is not None:
            self.dimmingSprite.set_position(x, y)
            
    def createTilemap(self):
        shape = self.data.shape
        sprites = numpy.empty(shape, dtype=object)
        for x in range(shape[0]):
            for y in range(shape[1]):
                for z in range(shape[2]):
                    xpos = x * 32
                    ypos = ((shape[1] - y) * 32) - 32
                    sprite = pyglet.sprite.Sprite(self.blank_tile, xpos, ypos, 
                                                  batch=self.renderingBatches[z], group=self.ordered_groups[z])
                    sprites[x, y, z] = sprite
                    self.sprites.append(sprite)
        return sprites
                
    def destroy(self):
        for sprite in self.sprites:
            sprite.delete()
            
    def update(self):
        indexes = numpy.argwhere(self.data != self.tile_ids)
        self.tile_ids = self.data[:]
        for index in indexes:
            self.set_image(self.tiles[tuple(index)], self.tile_ids[tuple(index)])
        
    
    def set_image(self, tile, id):
        flag = False
        #get the tile bitmap
        if id < 384:
            if id <= 47:
                bitmap = pyglet.image.create(32, 32)
            else:
                #get the filename
                autotile = self.autotile_names[int(id) / 48 - 1]
                #get the right pattern
                pattern = id % 48
                #collect the tile form the cache checking the local project folder
                #and the system RTP folder
                bitmap = self.cache.AutotilePattern(autotile, pattern, RTP_Location)
                if not bitmap:
                    bitmap = self.cache.AutotilePattern(autotile, pattern, RTP_Location)
                if not bitmap:
                    flag = True
                    print "could not get autotile"
                    bitmap = pyglet.image.create(32, 32)
        #normal tile
        else:
            #get the tile bitmap
            bitmap = self.cache.Tile(self.tileset_name, id, 0, RTP_Location)
            if not bitmap:
                bitmap = self.cache.Tile(self.tileset_name, id, 0, RTP_Location)
            if not bitmap:
                flag = True
                print "could not get tile"
                bitmap = pyglet.image.create(32, 32)
        #draw the tile to the surface
        tile.image = bitmap
        
    def translate(self, x, y):
        for sprite in self.sprites:
            sprite.set_position(sprite.x + x, sprite.y + y)
            
    def SetLayerOpacity(self, layer, opacity):
        layer = self.tiles[:, :, layer]
        for sprite in layer.flatten():
            sprite.opacity = opacity
            
    def SetActiveLayer(self, layer):
        self.activeLayer = layer
        if layer == (self.data.shape[2] + 1):
            for z in range(self.data.shape[2]):
                self.SetLayerOpacity(z, 255)
        else:
            if self.LayerDimming:
                for z in range(self.data.shape[2]):
                    if z <= self.activeLayer:
                        self.SetLayerOpacity(z, 255)
                    else:
                        self.SetLayerOpacity(z, 80)
    
    def SetLayerDimming(self, bool):
        self.LayerDimming = bool
        if self.LayerDimming:
            for z in range(self.data.shape[2]):
                if z <= self.activeLayer:
                    self.SetLayerOpacity(z, 255)
                else:
                    self.SetLayerOpacity(z, 80)
        else:
            for z in range(self.data.shape[2]):
                self.SetLayerOpacity(z, 255)
        
    def Draw(self):
        for z in range(len(self.renderingBatches)):
            if z == self.activeLayer and self.LayerDimming: #and z != 0
                if self.dimmingSprite is not None:
                    self.dimmingSprite.draw()
            self.renderingBatches[z].draw()
            
    def  __del__(self):
        self.destroy()
        