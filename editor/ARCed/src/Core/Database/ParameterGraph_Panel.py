import wx
from Core.Database import ARCed_Templates as Templates
from Actors_Panel import GRAPH_COLORS
from Core.Database.Controls import ParameterPlotGraphics, ParameterGraph
import numpy as np
from Core.Database import Manager as DM
from copy import deepcopy
import Kernel
from Core.Panels import PanelBase
#--------------------------------------------------------------------------------------
# ParameterGraph_Panel
#--------------------------------------------------------------------------------------

class ParameterGraph_Panel( Templates.ParameterGraph_Panel, PanelBase ):
    def __init__( self, parent, actor, tabs, index=0, scaled=False):
        """Basic constructor for the ParameterGraph_Panel"""
        Templates.ParameterGraph_Panel.__init__( self, parent )
        global Config
        Config = Kernel.GlobalObjects.get_value('ARCed_config')
        self.Data = deepcopy(actor.parameters)
        self.Actor = actor
        self.TabNames = ['MaxHP', 'MaxSP']
        self.TabNames.extend(tabs)
        self.checkBoxScaled.SetValue(scaled)
        self.MouseDown = False
        self.interactiveGraph.SetFontSizeAxis(8)
        self.interactiveGraph.canvas.Bind(wx.EVT_LEFT_DOWN, 
            Kernel.Protect(self.LeftMouseDown))
        self.interactiveGraph.canvas.Bind(wx.EVT_LEFT_UP, 
            Kernel.Protect(self.LeftMouseUp))
        self.interactiveGraph.canvas.Bind(wx.EVT_MOTION, 
            Kernel.Protect(self.MouseHover))
        self.interactiveGraph.canvas.Bind(wx.EVT_LEAVE_WINDOW,
            Kernel.Protect(self.LeftMouseUp))
        self.interactiveGraph.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
        for tab in tabs:
            panel = wx.Panel(self.noteBookParameters)
            self.noteBookParameters.AddPage(panel, tab)
        self.noteBookParameters.SetSelection(index)
        self.PageIndex = index
        self.RefreshGraph()

        # Bind the panel tot he Panel Manager
        self.BindPanelManager()

    def MouseHover( self, event ):
        """Updates the coordinate display and changes values if MouseDown flag is present"""
        maxValue = self.GetValueMax(self.PageIndex)
        x, y = self.interactiveGraph.GetXY(event)
        x = min(self.Actor.final_level, max(1, x))
        y = min(maxValue, max(0, y))
        self.labelValueX.SetLabel(str(int(x)))
        self.labelValueY.SetLabel(str(int(y)))
        if self.MouseDown:
            self.Data[self.PageIndex, x] = y
            self.RefreshGraph()

    def LeftMouseDown( self, event ):
        """Sets the MouseDown flag to True"""
        self.MouseDown = True

    def LeftMouseUp( self, event ):
        """Sets the MouseDown flag to False"""
        self.MouseDown = False

    def GetValueMax( self, param_index ):
        """Returns the max value for the parameter type"""
        if param_index == 0: return Config.getint('DatabaseLimits', 'ActorHP')
        elif param_index == 1: return Config.getint('DatabaseLimits', 'ActorSP')
        else: return Config.getint('DatabaseLimits', 'ActorParameter')

    def GetData( self ):
        """Returns the parameter data in a format fit to graph"""
        x = np.arange(1, self.Actor.final_level + 1, dtype=int)
        y = [self.Data[self.PageIndex, i] for i in x]
        return np.column_stack((x, y))

    def RefreshGraph( self ):
        """Refresh the displayed graph to reflect the current values"""
        color = GRAPH_COLORS[self.PageIndex]
        name = self.TabNames[self.PageIndex]
        maxValue, data = None, self.GetData()
        if not self.checkBoxScaled.GetValue():
            maxValue = self.GetValueMax(self.PageIndex)
        else:
            maxValue = max(zip(*data)[1])
        self.interactiveGraph.SetData(data, name, color,
            maxvalue=maxValue, maxlevel=self.Actor.final_level,
            minlevel=self.Actor.initial_level)
        
    def checkBoxScaled_CheckChanged(self, event):
        """Refreshes the graph after changing state"""
        self.RefreshGraph()

    def noteBookParameters_PageChanged( self, event ):
        """Changes the index and refreshes the graph for the selected parameter"""
        self.PageIndex = event.GetSelection()
        self.RefreshGraph()
    
    def buttonGenerate_Clicked( self, event ):
        """Create the parameter curve dialog, using the passed index to determine the parameter"""
        from Core.Database.Dialogs import GenerateCurve_Dialog
        actor, i = self.Actor, self.PageIndex
        vRange = (self.Data[i, 1], self.Data[i, actor.final_level])
        lRange = (actor.initial_level, actor.final_level)
        max = self.GetValueMax(i)
        dlg = GenerateCurve_Dialog(self, vRange, lRange, max)
        if dlg.ShowModal() == wx.ID_OK:
            curve = dlg.GenerateCurve()
            for j in xrange(len(curve)):
                lvl = j + actor.initial_level
                self.Data[i, j] = curve[j]
            self.RefreshGraph()
        dlg.Destroy()
    
    def buttonApply_Clicked( self, event ):
        """Sets the altered data to the actor's parameters"""
        # TODO: Will this be dialog?
        self.Actor.parameters = self.Data
        self.GetParent().EndModal(wx.ID_OK)
    
    def buttonClose_Clicked( self, event ):
        """Closes the window without applying changes"""
        # TODO: Will this be dialog?
        self.GetParent().EndModal(wx.ID_CANCEL)