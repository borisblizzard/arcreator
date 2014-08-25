'''
Created on Dec 20, 2010

core plugin module
'''
#preimport these so that they are there when the compiled copmponents try 
from . import _ext


def late_bind():
    global Actions, ARC_Data, Panels, MapEditor, Cache, Controls, Data, Database, DatabaseActions, Dialogs, Frames
    global Icons, Layouts, Menues, PanelManager, Project, PyXAL, RPGutil, RMXP, PygletWX, EditorGLPanel

    from . import PygletWX

    from . import Actions
    from . import ARC_Data

    from . import Panels
    from . import PanelManager

    from . import MapEditor
    from . import EventEditor

    from . import Cache
    
    from . import RPGutil
    from . import RMXP
    RMXP.late_bind()
    
    from . import EditorGLPanel

    from . import Data
    from . import Database
    from . import DatabaseActions

    
    
    from . import Dialogs
    from . import Controls
    from . import Frames
    from . import Layouts
    from . import Menues

    from . import Icons 

    from . import PyXAL

    

    

    from . import Project
    
    #late binding
    Database.late_bind()
    EventEditor.late_bind()
    MapEditor.late_bind()
    


    #===== Regester the Core ======
    from . import register


