'''
Created on Dec 20, 2010

core plugin module
'''
#preimport these so that they are there when the compiled copmponents try 
import _ext


def late_bind():
    global Actions, ARC_Data, Panels, MapEditor, Cache, Controls, Data, Database, DatabaseActions, Dialogs, Frames
    global Icons, Layouts, Menues, PanelManager, Project, PyXAL, RPGutil, RMXP, PygletWX, EditorGLPanel

    import PygletWX

    import Actions
    import ARC_Data

    import Panels
    import PanelManager

    import MapEditor
    import EventEditor

    import Cache
    
    import RPGutil
    import RMXP
    RMXP.late_bind()
    
    import EditorGLPanel

    import Data
    import Database
    import DatabaseActions

    
    
    import Dialogs
    import Controls
    import Frames
    import Layouts
    import Menues

    import Icons 

    import PyXAL

    

    

    import Project
    
    #late binding
    Database.late_bind()
    EventEditor.late_bind()
    MapEditor.late_bind()
    


    #===== Regester the Core ======
    import register


