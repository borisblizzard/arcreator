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
        if wx.VERSION >= (2,6):
            self.context = glcanvas.GLContext(self.canvas)
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
        if wx.VERSION >= (2,9):
            wx.CallAfter(self.doSetViewport)
        else:
            self.doSetViewport()
        event.Skip()

    def doSetViewport(self):
        if wx.VERSION >= (2,9):
            self.PrepareGL()
            # Make sure the frame is shown before calling SetCurrent.
            self.Show()
            self.canvas.SetCurrent(self.context)
            size = self.GetGLExtents()
            self.winsize = (size.width, size.height)
            self.width, self.height = size.width, size.height
            if self.width < 0:
                self.width = 1
            if self.height < 0:
                self.height = 1
            self.OnReshape(size.width, size.height)
            self.canvas.Refresh(False)
        else:
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


    def PrepareGL(self):
        if wx.VERSION >= (2,9):
            self.canvas.SetCurrent(self.context)
        else:
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
        #call the super metho
        super(wx.Panel, self).Destroy()

    #==========================================================================f
    # GLFrame OpenGL Event Handlers
    #==========================================================================
 
    def OnInitGL(self):
        '''Initialize OpenGL for use in the window.'''
        #create a pyglet context for this panel
        #self.pygletcontext = gl.Context(gl.current_context)
        if pyglet.version > "1.1.4":
            self.pygletcontext = PygletWXContext()
        else:
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
        gl.glViewport(0, 0, width, height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(0, width, 0, height, 1, -1)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        if self.GLinitialized:
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


class PygletWXContext(gl.Context):
    
    def __init__(self, config=None, context_share=None):
        self.config = config
        self.context_share = context_share
        self.canvas = None
        
        if context_share:
            self.object_space = context_share.object_space
        else:
            self.object_space = gl.ObjectSpace()
    
    
    def attach(self, canvas=None):
        pass

    def detach(self):
        pass
    
    def set_current(self):        
        # XXX not per-thread
        gl.current_context = self
        
        # XXX
        gl.gl_info.set_active_context()
        gl.glu_info.set_active_context()
        
        # Implement workarounds
        if not self._info:
            self._info = gl.gl_info.GLInfo()
            self._info.set_active_context()
            for attr, check in self._workaround_checks:
                setattr(self, attr, check(self._info))
        
        # Release textures and buffers on this context scheduled for deletion.
        # Note that the garbage collector may introduce a race condition,
        # so operate on a copy of the textures/buffers and remove the deleted
        # items using list slicing (which is an atomic operation)
        if self.object_space._doomed_textures:
            textures = self.object_space._doomed_textures[:]
            textures = (gl.GLuint * len(textures))(*textures)
            gl.glDeleteTextures(len(textures), textures)
            self.object_space._doomed_textures[0:len(textures)] = []
        if self.object_space._doomed_buffers:
            buffers = self.object_space._doomed_buffers[:]
            buffers = (gl.GLuint * len(buffers))(*buffers)
            gl.glDeleteBuffers(len(buffers), buffers)
            self.object_space._doomed_buffers[0:len(buffers)] = []
    
