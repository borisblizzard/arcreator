import wx
import ARCed_Templates
import ARCedChangeMaximum_Dialog
import ARCedActors_Panel as actPanel

from __test__ import ParameterGraph as test # TODO: Uh, change this from "test"

import Kernel
from Kernel import Manager as KM

'''
TODO:
- Create ini config for colors, and read from that (also line color, marker color, marker style, line style?)
- Implement creating the ticks dynamically depending on the min/max values
- Add labels
- Implement iteration though curve to set values for the parameter
- Re-implement changing number of points 
- Implement elastic points
- Remove flicker on resize by waiting until panel is completely done, then re-draw graph 
- Make the last 3 connecting points/line segments invisible and unclickable
'''


# Implementing ParameterGraph_Panel 
class ARCedParameterGraph_Panel( ARCed_Templates.ParameterGraph_Panel ):
	def __init__( self, parent, actor, data=None, param_index=0, maxValue=9999):       
		ARCed_Templates.ParameterGraph_Panel.__init__( self, parent )

		self.Actor = actor
		range = [1, maxValue]
		data = []
		for ary in self.Actor.parameters[param_index, :]:
			data.append(ary[0])
		self.Graph = test(self.graphPanel, data, maxValue) #!
		#self.Graph.Canvas.mpl_connect('motion_notify_event', self.graphPanel_MouseMotion)


	def graphPanel_OnSize( self, event ):
		''' Resizes the graph to match the size of the control '''
		pixels = tuple( self.graphPanel.GetClientSize() )
		# This is basically a hack to interface wx with matplotlib
		# Cause problems on PC's with non-standard resolutions?
		self.Graph.SetSize( pixels )
		self.Graph.Canvas.SetSize( pixels )
		self.Graph.Figure.set_size_inches( float( pixels[0] )/self.Graph.Figure.get_dpi(),
										float( pixels[1] )/self.Graph.Figure.get_dpi() )

	def buttonChangeMax_Clicked( self, event ):
		max = self.Actor.final_level
		current = self.Graph.PointMax
		dlg = ARCedChangeMaximum_Dialog.ARCedChangeMaximum_Dialog(self, current, 1, max)
		if dlg.ShowModal() == wx.ID_OK:
			self.Graph.SetRawData(pointmax=dlg.spinCtrlMaximum.GetValue())
			self.spinCtrlVertex.SetRange(0, self.Graph.PointMax)
		dlg.Destroy()

	def checkBoxPoints_CheckChanged( self, event ):
		self.Graph.ShowVerts = self.checkBoxPoints.GetValue()
		self.Graph.Line.set_visible(self.Graph.ShowVerts)
		if not self.Graph.ShowVerts: 
			self.Graph.ActivePoint = None
		#self.Graph.Canvas.draw()

	def buttonOK_Clicked( self, event ):
		print 'OK'
	
	def buttonCancel_Clicked( self, event ):
		print 'CANCEL'
	
	def graphPanel_MouseMotion( self, event ):
		pass
		#self.labelLevel.SetLabel('Level: ' + str(self.Graph.MouseX))
		#self.labelValue.SetLabel('Value: ' + str(self.Graph.MouseY))

from RGSS1_RPG import RPG
app = wx.PySimpleApp( 0 )
frame = wx.Frame( None, wx.ID_ANY, 'Parameter Curve', size=(800,600) )
panel = ARCedParameterGraph_Panel( frame, RPG.Actor() )
frame.CenterOnScreen()
frame.Show()
app.MainLoop()

