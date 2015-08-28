from .PygletWX import PygletWXContext
from .PygletWX import PygletGLPanel
from .PygletWX import EditorGLPanel

def on_enable():
    print("forcing PygletWX load to ensure proper pyglet import")
