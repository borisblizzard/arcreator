import wx
import ARCed_Templates
import ARCedExpCurve_Dialog
import ARCedGenerateCurve_Dialog

class ARCedActorParameters_Dialog( ARCed_Templates.ActorParameters_Dialog ):
	def __init__( self, parent, actor, limits ):
		""" Initializes window using passed Actor argument to set values """
		ARCed_Templates.ActorParameters_Dialog.__init__( self, parent )
		global Actor, Limits
		Actor, Limits = actor, limits
		self.ParameterTable = Actor.parameters
		PageIndex = 0
		self.spinCtrlLevel.SetRange(1, Limits['finallevel'])
		self.setValueRange()
		self.refreshValues(1)



	
