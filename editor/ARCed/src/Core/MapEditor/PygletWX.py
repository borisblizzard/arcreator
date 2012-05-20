import wx
from wx import glcanvas
import pyglet
pyglet.options['shadow_window'] = False
from pyglet import gl
from pyglet.gl import GLException
import numpy
import rabbyt

import Kernel
from Kernel import Manager as KM

class PygletGLPanel(wx.Panel):

    '''A simple class for using pyglet OpenGL with wxPython.'''

    def __init__(self, parent, id, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        # Forcing a no full repaint to stop flickering
        style = style | wx.NO_FULL_REPAINT_ON_RESIZE
        #call super function
        super(PygletGLPanel, self).__init__(parent, id, pos, size, style)
        #init gl canvas data
        self.GLinitialized = False
        attribList = (glcanvas.WX_GL_RGBA, # RGBA
                      glcanvas.WX_GL_DOUBLEBUFFER, # Double Buffered
                      glcanvas.WX_GL_DEPTH_SIZE, 24) # 24 bit
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
        self.PrepareGL()
        if self.canvas.GetContext():
            # Make sure the frame is shown before calling SetCurrent.
            self.Show()
            self.canvas.SetCurrent()
            size = self.GetGLExtents()
            self.winsize = (size.width, size.height)
            self.width, self.height = size.width, size.height
            if self.width < 0:
                self.width = 1
            if self.height < 0:
                self.height = 1
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
        #self.pygletcontext = gl.Context(gl.current_context)
        self.pygletcontext = gl.Context()
        self.pygletcontext.set_current()
        #normal gl init
        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        gl.glEnable(gl.GL_TEXTURE_2D)
        gl.glClearColor(1, 1, 1, 1)
        
        #create objects to draw
        self.create_objects()
                                         
    def OnReshape(self, width, height):
        '''Reshape the OpenGL viewport based on the dimensions of the window.'''
        #CORRECT WIDTH AND HEIGHT
        if width <= 0:
            width = 1
        if height <= 0:
            height = 1
        if self.GLinitialized:
            self.pygletcontext.set_current()
            self.update_object_resize(width, height)
        gl.glViewport(0, 0, width, height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(0, width, 0, height, 1, -1)
        gl.glMatrixMode(gl.GL_MODELVIEW)
            
            
    def OnDraw(self, *args, **kwargs):
        "Draw the window."
        #clear the context
        gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)
        #draw objects
        self.draw_objects()
        #update screen
        self.SwapBuffers()
            
    #==========================================================================
    # To be implemented by a sub class
    #==========================================================================
   
    def create_objects(self):
        '''create opengl objects when opengl is initialized'''
        pass
        
    def update_object_resize(self, width, height):
        '''called when the window receives only if opengl is initialized'''
        pass
        
    def draw_objects(self):
        '''called in the middle of ondraw after the buffer has been cleared'''
        pass