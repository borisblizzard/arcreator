import os

import wx
from wx import glcanvas

import pyglet
from pyglet import gl

import numpy

import cache

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
        self.sizer.Fit(self)

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

    def processPaintEvent(self, event):
        '''Process the drawing event.'''
        self.canvas.SetCurrent()

        # This is a 'perfect' time to initialize OpenGL ... only if we need to
        if not self.GLinitialized:
            self.OnInitGL()
            self.GLinitialized = True

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
        gl.glOrtho(0, width, 0, height, 1, -1)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        #pyglet stuff

        # Wrap text to the width of the window
        if self.GLinitialized:
            self.pygletcontext.set_current()
            self.update_object_resize()
            
    def OnDraw(self, *args, **kwargs):
        "Draw the window."
        #clear the context
        self.pygletcontext.set_current()
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
        
    def update_object_resize(self):
        '''called when the window recieves only if opengl is initialized'''
        pass
        
    def draw_objects(self):
        '''called in the middle of ondraw after the buffer has been cleared'''
        pass
       
   
rtppath = "%PROGRAMFILES%/Common Files/Enterbrain/RGSS/Standard"
RTP_Location = os.path.normpath(os.path.expandvars(rtppath))

class Tilemap(object):
    
    def __init__(self, data, tileset="", autotiles=[]):
        self.cache = cache.PygletCache()
        self.data = data
        self.tile_ids = numpy.zeros(data.shape)
        self.batch = pyglet.graphics.Batch()
        self.sprites = []
        self.blank_tile = pyglet.image.create(32, 32)
        self.x = self.oldx = self.y = self.oldy = 0
        self.autotile_names = autotiles
        self.tileset_name = tileset
        self.ordered_groups = []
        for i in range(3):
            self.ordered_groups.append(pyglet.graphics.OrderedGroup(i))
        self.tiles = self.create_tilemap()
            
        
    def create_tilemap(self):
        shape = self.data.shape
        sprites = numpy.empty(shape, dtype=object)
        for x in range(shape[0]):
            for y in range(shape[1]):
                for z in range(shape[2]):
                    xpos = x * 32
                    ypos = ((shape[1] - y) * 32) - 32
                    sprite = pyglet.sprite.Sprite(self.blank_tile, xpos, ypos, 
                                                  batch=self.batch, group=self.ordered_groups[z])
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
                print "empty auto tile"
                bitmap = pyglet.image.create(32, 32)
        #normal tile
        else:
            #get the tile bitmap
            bitmap = self.cache.Tile(self.tileset_name, id, 0, RTP_Location)
            if not bitmap:
                bitmap = self.cache.Tile(self.tileset_name, id, 0, RTP_Location)
            if not bitmap:
                flag = True
                print "empty tile"
                bitmap = pyglet.image.create(32, 32)
        #draw the tile to the surface
        if flag:
            print "empty tile"
        tile.image = bitmap
        
    def translate(self, x, y):
        for sprite in self.sprites:
            sprite.set_position(sprite.x + x, sprite.y + y)
        
    def Draw(self):
        self.batch.draw()
        
    def  __del__(self):
        self.destroy()
        