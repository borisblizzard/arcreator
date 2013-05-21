import wx
from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')

Templates = Core.Database.Welder_Templates
#--------------------------------------------------------------------------------------
# EventEditor_Panel
#--------------------------------------------------------------------------------------

# Implementing EventEditor_Panel
class EventEditor_Panel( Templates.EventEditor_Panel ):
    def __init__( self, parent, event):
        Templates.EventEditor_Panel.__init__( self, parent )
        self.event = event
    
    # Handlers for EventEditor_Panel events.
    def buttonNewPage_Clicked( self, event ):
        # TODO: Implement buttonNewPage_Clicked
        pass
    
    def buttonCopyPage_Clicked( self, event ):
        # TODO: Implement buttonCopyPage_Clicked
        pass
    
    def buttonPastePage_Clicked( self, event ):
        # TODO: Implement buttonPastePage_Clicked
        pass
    
    def buttonDeletePage_Clicked( self, event ):
        # TODO: Implement buttonDeletePage_Clicked
        pass
    
    def buttonClearPage_Clicked( self, event ):
        # TODO: Implement buttonClearPage_Clicked
        pass
    
    def buttonOK_Clicked( self, event ):
        # TODO: Implement buttonOK_Clicked
        pass
    
    def buttonCancel_Clicked( self, event ):
        # TODO: Implement buttonCancel_Clicked
        pass
    
    def buttonApply_Clicked( self, event ):
        # TODO: Implement buttonApply_Clicked
        pass
    
    
