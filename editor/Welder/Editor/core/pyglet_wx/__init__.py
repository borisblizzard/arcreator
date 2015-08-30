from .pyglet_wx import PygletWXContext
from .pyglet_wx import PygletGLPanel
from .pyglet_wx import EditorGLPanel

def on_enable():
    print("forcing PygletWX load to ensure proper pyglet import")
