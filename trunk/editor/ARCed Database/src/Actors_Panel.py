"""
Contains the functionality of all the events raised on the Actors Database panel
"""
import wx
import wx.lib.plot as plot
import ARCed_Templates
import ChangeMaximum_Dialog
import ExpCurve_Dialog
import ChooseGraphic_Dialog 
import ActorParameters_Dialog
import AddParameter_Dialog
import numpy as np
from DatabaseManager import DatabaseManager as DM

#from DatabaseAction import 
from Core.RMXP import RGSS1_RPG as RPG	   						
import Kernel


GRAPH_COLORS = { 
		0 : wx.Colour(200, 60, 120), 
		1 : wx.Colour(60, 120, 200), 
		2 : wx.Colour(200, 120, 60),
		3 : wx.Colour(120, 200, 60),
		4 : wx.Colour(56, 187, 112),
		5 : wx.Colour(120, 60, 200),
		6 : wx.Colour(60, 200, 120),
		7 : wx.Colour(56, 112, 187),
		8 : wx.Colour(187, 112, 56),
		9 : wx.Colour(112, 187, 56),
		10 : wx.Colour(112, 56, 187),
		11 : wx.Colour(187, 56, 112),
	}


class Actors_Panel(ARCed_Templates.Actors_Panel ):

	def __init__( self, parent, actorIndex=0 ):
		"""Basic constructor for the Actors panel"""
		ARCed_Templates.Actors_Panel.__init__( self, parent )
		# Load the project's game objects into this module's scope
		project = Kernel.GlobalObjects.get_value('PROJECT')
		global Config, DataActors, DataClasses, DataWeapons, DataArmors
		Config = Kernel.GlobalObjects.get_value('ARCed_config')
		try:
			DataActors = project.getData('Actors')
			DataClasses = project.getData('Classes')
			DataWeapons = project.getData('Weapons')
			DataArmors = project.getData('Armors')
		except NameError:
			Kernel.Log('Database opened before Project was initialized', '[Database:ACTOR]', True)
			self.Destroy()
		# Set font for the note control
		font = wx.Font(8, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		font.SetFaceName(Config.get('Misc', 'NoteFont')) 
		self.textCtrlNotes.SetFont(font)
		self.ParamTab = 0
		# Set the ranges for initial and final level spin controls
		max = Config.getint('DatabaseLimits', 'ActorLevel')
		self.spinCtrlInitialLevel.SetRange(1, max)
		self.spinCtrlFinalLevel.SetRange(1, max)
		self.spinCtrlLevel.SetRange(1, max)
		self.glCanvasCharacter.canvas.Bind( wx.EVT_LEFT_DCLICK, 
			Kernel.Protect(self.glCanvasCharacter_DoubleClick))
		self.glCanvasBattler.canvas.Bind( wx.EVT_LEFT_DCLICK, 
			Kernel.Protect(self.glCanvasBattler_DoubleClick))
		self.parameterGraph.canvas.Bind(wx.EVT_LEFT_DCLICK, 
			Kernel.Protect(self.parameterGraph_DoubleClicked))
		# Initialize the selected actor attribute
		if actorIndex >= len(DataActors):
			actorIndex = 0
		self.SelectedActor = DataActors[DM.FixedIndex(actorIndex)]
		# Create the controls for the equipment and set the values for all the controls
		self.CreateEquipmentControls()
		for param in Config.getlist('GameSetup', 'Parameters'):
			self.AddParameterPage(param)
		self.noteBookActorParameters.ChangeSelection(0)
		self.comboBoxExpCurve.SetCursor(wx.STANDARD_CURSOR)
		self.refreshAll()
		DM.DrawHeaderBitmap(self.bitmapActors, 'Actors')
		# Set the initial selection of the list control 
		self.listBoxActors.SetSelection(actorIndex)

	def AddParameterPage( self, title, activate=False ):
		"""Creates a page and adds it to the notebook control"""
		page = wx.Panel( self.noteBookActorParameters )
		self.noteBookActorParameters.AddPage(page, title)
		index = self.noteBookActorParameters.GetPageCount() - 1
		maxlevel = Config.getint('DatabaseLimits', 'ActorLevel')
		for actor in DataActors:
			if actor == None:
				actor = RPG.Actor()
			actor.parameters.resize(index + 1, maxlevel + 1)
			for j in xrange(1, maxlevel):
				actor.parameters[index, j] = 50 + 5 * j
		if activate:
			self.noteBookActorParameters.SetSelection(index)

	def CreateEquipmentControls( self ):
		"""Creates the controls for each equipment type defined in the configuration"""
		if DM.ARC_FORMAT:
			equipment = Config.getlist('GameSetup', 'WeaponSlots')
			equipment.extend(Config.getlist('GameSetup', 'ArmorSlots'))
		else:
			equipment = ['Weapon', 'Shield', 'Helmet', 'Body Armor', 'Accessory']
		sizerEquipment = wx.BoxSizer( wx.VERTICAL )
		self.EquipmentBoxes = []
		self.FixedCheckBoxes = []
		for i in xrange(len(equipment)):
			sizer = wx.BoxSizer( wx.HORIZONTAL )
			label = wx.StaticText( self.scrolledWindowEquipment, wx.ID_ANY, 
				equipment[i], wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_LEFT )
			label.Wrap( -1 )
			sizer.Add( label, 0, wx.TOP|wx.LEFT|wx.RIGHT, 5 )
			comboBox = wx.Choice( self.scrolledWindowEquipment, wx.ID_ANY, 
				wx.DefaultPosition, wx.DefaultSize, [], 0 )
			comboBox.SetDoubleBuffered(True)
			comboBox.Bind( wx.EVT_CHOICE, 
				Kernel.Protect(self.comboBoxEquipment_SelectionChanged) )
			comboBox.Bind( wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground )
			self.EquipmentBoxes.append(comboBox)
			sizer.Add( comboBox, 1, wx.RIGHT|wx.LEFT, 5 )
			checkBox = wx.CheckBox( self.scrolledWindowEquipment, wx.ID_ANY, u"Fixed", 
				wx.DefaultPosition, wx.DefaultSize, 0 )
			checkBox.Bind( wx.EVT_CHECKBOX, 
				 Kernel.Protect(self.checkBoxFixedEquipment_CheckChanged) )
			checkBox.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
			self.FixedCheckBoxes.append(checkBox)
			sizer.Add( checkBox, 0, wx.ALL, 5 )
			sizerEquipment.Add( sizer, 1, wx.EXPAND, 5 )
		self.scrolledWindowEquipment.SetSizer( sizerEquipment )
		self.scrolledWindowEquipment.Layout()
		sizerEquipment.Fit( self.scrolledWindowEquipment )
		self.scrolledWindowEquipment.SetDoubleBuffered(True)

	def refreshActorList( self ):
		"""Refreshes the values in the actor wxListBox control"""
		digits = len(Config.get('GameObjects', 'Actors'))
		DM.FillControl(self.listBoxActors, DataActors, digits, [])

	def refreshClasses( self ):
		"""Refreshes the values in the class wxChoice control"""
		digits = len(Config.get('GameObjects', 'Classes'))
		DM.FillControl(self.comboBoxClass, DataClasses, digits, [])
		
	def refreshWeapons( self ):
		"""Sets the weapon combobox(s) data determined by the actor's class"""
		weaponSlots = len(Config.getlist('GameSetup', 'WeaponSlots'))
		digits = len(Config.get('GameObjects', 'Weapons'))
		for i in xrange(weaponSlots):
			items = ['(None)']
			ids = self.GetWeaponIDs()
			for id in ids:
				if DataWeapons[id] == None:
					DataWeapons[id] = RPG.Weapon()
			items.extend(
				   [''.join([str(DataWeapons[id].id).zfill(digits), ': ',
					DataWeapons[id].name]) for id in ids])
			self.EquipmentBoxes[i].Clear()
			self.EquipmentBoxes[i].AppendItems(items)
			if DM.ARC_FORMAT:
				# TODO: Implement multiple weapon equip
				pass
			else:
				id, index = self.SelectedActor.weapon_id, 0
				if id != 0:
					try:
						index = self.GetWeaponIDs().index(id) + 1
					except ValueError:
						self.SelectedActor.weapon_id = 0
				self.EquipmentBoxes[0].SetSelection(index)

	def refreshArmors( self ):
		"""Sets the armor combo box data determined by the actor's class"""
		weaponSlots = len(Config.getlist('GameSetup', 'WeaponSlots'))
		digits = len(Config.get('GameObjects', 'Armors'))
		kinds = {}
		cypher = [int(k) for k in Config.getlist('GameSetup', 'ArmorSlotKinds')]
		for k in Config.getlist('GameSetup', 'ArmorSlotKinds'):
			key = int(k)
			if not kinds.has_key(key):
				values = ['(None)']
				ids = self.GetArmorIDs(key)
				for id in ids:
					if DataWeapons[id] == None:
						DataWeapons[id] = RPG.Weapon()
				values.extend(
				  [''.join([str(id).zfill(digits), ': ', 
					DataArmors[id].name]) for id in ids])
				kinds[key] = values
		for i in xrange(weaponSlots, len(self.EquipmentBoxes)):
			kind = cypher[i - weaponSlots]
			items = kinds[kind]
			self.EquipmentBoxes[i].Clear()
			self.EquipmentBoxes[i].AppendItems(items)
			index = 0
			exec(''.join(['id = self.SelectedActor.armor', str(i + 1 - weaponSlots), '_id']))
			if id != 0:
				try:
					index = self.GetArmorIDs(kind).index(id) + 1
				except ValueError:
					# If the class changes, the index() method no longer works
					index = 0
					exec(''.join(['self.SelectedActor.armor', str(i + 1 - weaponSlots), '_id = 0']))
			self.EquipmentBoxes[i].SetSelection(index)

	def refreshParameters( self ):
		"""Refreshes the data values on the control"""
		actor = self.SelectedActor
		self.textCtrlName.ChangeValue(actor.name)
		self.comboBoxClass.Select(actor.class_id - 1)
		basis = str(actor.exp_basis)
		inflation = str(actor.exp_inflation)
		text = 'Basis: ' + basis + ', Inflation: ' + inflation
		self.comboBoxExpCurve.SetValue(text)
		self.spinCtrlLevel.SetRange(1, actor.final_level )
		self.refreshValues()
		self.spinCtrlLevel.SetValue(actor.initial_level)
		self.spinCtrlFinalLevel.SetValue(actor.final_level)
		self.spinCtrlInitialLevel.SetRange(1, actor.final_level)

	def refreshFixedEquipment( self ):
		if DM.ARC_FORMAT:
			# TODO: Implement
			pass
		else:
			actor = self.SelectedActor
			self.FixedCheckBoxes[0].SetValue(actor.weapon_fix)
			self.FixedCheckBoxes[1].SetValue(actor.armor1_fix)
			self.FixedCheckBoxes[2].SetValue(actor.armor2_fix)
			self.FixedCheckBoxes[3].SetValue(actor.armor3_fix)
			self.FixedCheckBoxes[4].SetValue(actor.armor4_fix)

	def refreshGraphics( self ):
		"""Refreshes the character and battler graphic for the actor"""
		DM.RenderImage(self.glCanvasCharacter, self.SelectedActor.character_name, 
			self.SelectedActor.character_hue, 'character')
		DM.RenderImage(self.glCanvasBattler, self.SelectedActor.battler_name, 
			self.SelectedActor.battler_hue, 'battler')

	def refreshValues( self, level=None ):
		"""Applies the limits defined for the selected parameter, and updates the value"""
		if level == None:
			level = self.spinCtrlLevel.GetValue()
		self.spinCtrlValue.SetValue(self.GetParameterValue(self.ParamTab, level))
		self.spinCtrlValue.SetRange(1, self.GetValueMax(self.ParamTab))
		if not hasattr(self.SelectedActor, 'note'):
			setattr(self.SelectedActor, 'note', '')
		self.textCtrlNotes.ChangeValue(self.SelectedActor.note)

	def refreshGraph( self ):
		"""Refreshes the graph to reflect the selected actor' values"""
		name = self.noteBookActorParameters.GetPageText(self.ParamTab)
		color = GRAPH_COLORS[self.ParamTab % len(GRAPH_COLORS)]
		maxValue = None
		if not self.checkBoxScaled.GetValue():
			maxValue = self.GetValueMax(self.ParamTab)
		self.parameterGraph.SetData(self.GetParameterData(), name, color,
			maxvalue=maxValue, maxlevel=self.SelectedActor.final_level,
			minlevel=self.SelectedActor.initial_level)

	def refreshAll( self ):
		"""Refreshes all the controls that contain game object values"""
		self.refreshActorList()
		self.refreshClasses()
		self.refreshWeapons()
		self.refreshArmors()
		self.refreshFixedEquipment()
		self.refreshParameters()
		self.refreshGraphics()
		self.refreshGraph()

	def listBoxActors_SelectionChanged( self, event ):
		"""Changes the data on the panel to reflect the values of the selected actor"""
		index = DM.FixedIndex(event.GetSelection())
		if DataActors[index] is None:
			DataActors[index] = RPG.Actor()
		self.SelectedActor = DataActors[index]
		self.refreshWeapons()
		self.refreshArmors()
		self.refreshFixedEquipment()
		self.refreshParameters()
		self.refreshGraphics()

	def SetParameterValue(self, param, level, value):
		"""Sets the newly defined value for the selected actor's parameter"""
		self.SelectedActor.parameters[param, level] = value

	def GetParameterValue( self, index, level ):
		"""Retrieves the value of the current actor's selected parameter for the defined level"""
		if self.SelectedActor.parameters.xsize <= index or self.SelectedActor.parameters.ysize < level:
			maxlevel = Config.getint('DatabaseLimits', 'ActorLevel')
			for actor in DataActors:
				if actor == None:
					actor = RPG.Actor()
				actor.parameters.resize(index + 1, maxlevel + 1)
				for j in xrange(1, maxlevel):
					actor.parameters[index, j] = 50 + 5 * j
		return self.SelectedActor.parameters[index, level]

	def buttonMaximum_Clicked( self, event ):
		"""Starts the Change Maximum dialog"""
		max = Config.getint('GameObjects', 'Actors')
		DM.ChangeDataCapacity(self, self.listBoxActors, DataActors, max)

	def textBoxName_TextChanged( self, event ):
		"""Updates the selected actor's name"""
		DM.UpdateObjectName(self.SelectedActor, event.GetString(),
			self.listBoxActors, len(Config.get('GameObjects', 'Actors')))

	def comboBoxClass_SelectionChanged( self, event ):
		"""Updates the actor's class ID and refreshes the equipment allowed by the class"""
		self.SelectedActor.class_id = DM.FixedIndex(self.comboBoxClass.GetSelection())
		self.refreshWeapons()
		self.refreshArmors()

	def spinCtrlInitialLevel_ValueChanged( self, event ):
		"""Sets the selected actor's initial level to the value of the wxSpinCtrl"""
		self.spinCtrlInitialLevel.SetRange(1, self.spinCtrlFinalLevel.GetValue())
		self.SelectedActor.initial_level = self.spinCtrlInitialLevel.GetValue()
		self.refreshGraph()

	def spinCtrlFinalLevel_ValueChanged( self, event ):
		"""Sets the selected actor's final level to the value of the wxSpinCtrl"""
		final = event.GetInt()
		self.spinCtrlInitialLevel.SetRange(1, final)
		self.spinCtrlLevel.SetRange(1, final)
		self.SelectedActor.final_level = final
		self.refreshGraph()

	def comboBoxExperience_Click( self, event ):
		"""Opens window to generate experience tables"""
		actor = self.SelectedActor
		dlg = ExpCurve_Dialog.ExpCurve_Dialog(self, actor)
		if dlg.ShowModal() == wx.ID_OK:
			# TODO: Fix 'actor' which errors out. Pass the instance to window
			actor.exp_basis = dlg.spinCtrlBasis.GetValue()
			actor.exp_inflation = dlg.spinCtrlInflation.GetValue()
		dlg.Destroy()
		self.refreshParameters()

	def glCanvasCharacter_DoubleClick( self, event ):
		"""Opens dialog to change the character graphic"""
		DM.StartGraphicSelection(self.glCanvasCharacter, 'Graphics/Characters/',
			self.SelectedActor.character_name, self.SelectedActor.character_hue)

	def glCanvasBattler_DoubleClick( self, event ):
		"""Opens dialog to change the battler graphic"""
		DM.StartGraphicSelection(self.glCanvasBattler, 'Graphics/Battler/',
			self.SelectedActor.battler_name, self.SelectedActor.battler_hue)

	def comboBoxEquipment_SelectionChanged( self, event ):
		"""Updates the weapon/armor id for the selected type for the actor"""
		ctrlIndex = self.EquipmentBoxes.index(event.GetEventObject())
		if DM.ARC_FORMAT:
			weaponSlots = len(Config.getlist('GameSetup', 'WeaponSlots'))
		else:
			weaponSlots = 1
		selection = event.GetInt()
		if ctrlIndex == 0:
			# Weapon Changed
			if DM.ARC_FORMAT:
				# TODO: Implement multiple weapon slots
				pass
			else:
				if selection == 0: self.SelectedActor.weapon_id = 0
				else: self.SelectedActor.weapon_id = self.GetWeaponIDs()[selection - 1]
		else:
			# Armor Changed
			if selection == 0:
				exec(''.join(['self.SelectedActor.armor', str(ctrlIndex), '_id = 0']))
			else:
				kinds = Config.getlist('GameSetup', 'ArmorSlotKinds')
				kind = int(kinds[ctrlIndex - weaponSlots])
				exec(''.join(['self.SelectedActor.armor', str(ctrlIndex), '_id = ',
				  str(self.GetArmorIDs(kind)[selection - 1])]))

	def checkBoxFixedEquipment_CheckChanged( self, event ):
		"""Updates the "fixed" states for the selected actor's equipment"""
		ctrlIndex = self.FixedCheckBoxes.index(event.GetEventObject())
		if DM.ARC_FORMAT:
			# TODO: Implement
			weaponSlots = len(Config.getlist('GameSetup', 'WeaponSlots'))
			if ctrlIndex < weaponSlots:
				pass
			else:
				pass
		else: # RMXP
			if ctrlIndex == 0:
				self.SelectedActor.weapon_fix = event.Checked()
			else:
				exec(''.join(['self.SelectedActor.armor', str(ctrlIndex), 
					'_fix = event.Checked()']))

	def spinCtrlParamLevel_ValueChanged( self, event ):
		"""Update the controls on each page when the level is changed"""
		self.refreshValues(self.spinCtrlLevel.GetValue())
		
	def GetValueMax( self, param_index ):
		"""Returns the max value for the parameter type"""
		if param_index == 0: return Config.getint('DatabaseLimits', 'ActorHP')
		elif param_index == 1: return Config.getint('DatabaseLimits', 'ActorSP')
		else: return Config.getint('DatabaseLimits', 'ActorParameter')
	
	def spinCtrlValue_ValueChanged( self, event ):
		"""Updates the actors parameter table with the value"""
		self.SetParameterValue(self.ParamTab, self.spinCtrlLevel.GetValue(), self.spinCtrlValue.GetValue())
		self.refreshGraph()

	def buttonGenerateCurve_Clicked( self, event):
		"""Create the parameter curve dialog, using the passed index to determine the parameter"""
		from GenerateCurve_Dialog import GenerateCurve_Dialog
		actor, i = self.SelectedActor, self.ParamTab
		vRange = (actor.parameters[i, 1], actor.parameters[i, actor.final_level])
		lRange = (actor.initial_level, actor.final_level)
		max = self.GetValueMax(i)
		dlg = GenerateCurve_Dialog(self, vRange, lRange, max)
		if dlg.ShowModal() == wx.ID_OK:
			curve = dlg.GenerateCurve()
			for j in xrange(len(curve)):
				lvl = j + actor.initial_level
				actor.parameters[i, j] = curve[j]
			self.refreshGraph()
		dlg.Destroy()

	def noteBookParameters_PageChanged( self, event ):
		"""Sets the index of the page when the tab is traversed"""
		self.ParamTab = event.GetSelection()
		if not DM.ARC_FORMAT:
			self.buttonRemoveParameter.Enabled = (self.ParamTab > 5)
		else:
			self.buttonRemoveParameter.Enabled = self.noteBookActorParameters.GetPageCount >= 1
		self.refreshGraph()
		self.refreshValues()

	def GetParameterData( self ):
		"""Returns the parameter data in a format fit to graph"""
		params = self.SelectedActor.parameters
		x = np.arange(1, self.SelectedActor.final_level + 1, dtype=int)
		y = [params[self.ParamTab, i] for i in x]
		return np.column_stack((x, y))

	def checkBoxScaled_CheckChanged(self, event):
		"""Refreshes the graph after changing state"""
		self.refreshGraph()

	def buttonQuickA_Clicked( self, event ):
		"""Generates a quick curve setting within a range"""
		self.GenerateQuickCurve(0.75)

	def buttonQuickB_Clicked( self, event ):
		"""Generates a quick curve setting within a range"""
		self.GenerateQuickCurve(0.65)

	def buttonQuickC_Clicked( self, event ):
		"""Generates a quick curve setting within a range"""
		self.GenerateQuickCurve(0.55)

	def buttonQuickD_Clicked( self, event ):
		"""Generates a quick curve setting within a range"""
		self.GenerateQuickCurve(0.45)

	def buttonQuickE_Clicked( self, event ):
		"""Generates a quick curve setting within a range"""
		self.GenerateQuickCurve(0.35)

	def GenerateQuickCurve(self, percent):
		"""Generates a quick random curve, ensuring it falls within a range"""
		from random import randint
		actor, index = self.SelectedActor, self.ParamTab
		limit = self.GetValueMax(index)
		max, mod = int(limit * percent), int(limit * 0.05)
		upper, min = randint(max - mod, max + mod), max / 10
		mod /= 10
		lower = randint(min - mod, min + mod)
		init, final = actor.initial_level, actor.final_level
		for i in np.arange(init, final + 1, dtype=int):
			actor.parameters[index, i] = int(DM.CalculateParameter(lower, 
				upper, 0, i, init, final))
		self.refreshGraph()

	def parameterGraph_DoubleClicked( self, event ):
		"""Opens the larger graph panel for interactive editing"""
		from ParameterGraph_Panel import ParameterGraph_Panel
		tabs, data = [], self.SelectedActor.parameters
		for i in xrange(2, self.noteBookActorParameters.GetPageCount()):
			tabs.append(self.noteBookActorParameters.GetPageText(i))
		dlg = wx.Dialog(self, title='Parameter Growth', size=(640,480), 
			style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		dlgSizer = wx.BoxSizer( wx.VERTICAL )
		panel = ParameterGraph_Panel(dlg, self.SelectedActor, tabs, 
			self.ParamTab, self.checkBoxScaled.GetValue())
		dlgSizer.Add( panel, 1, wx.EXPAND, 5)
		dlg.SetSizer(dlgSizer)
		dlg.Layout()
		dlg.Centre( wx.BOTH )
		if dlg.ShowModal() == wx.ID_OK:
			self.refreshGraph()

	def buttonAddParameter_Clicked( self, event ):
		"""Opens dialog for the user to create a custom parameter"""
		dialog = AddParameter_Dialog.AddParameter_Dialog( self )
		if (dialog.ShowModal() == wx.ID_OK):
			paramName = dialog.textCtrlParameterName.GetLineText(0)
			self.AddParameterPage(paramName)

	def buttonRemoveParameter_Clicked( self, event ):
		"""Removes the selected page from the tab control and resizes the actors' parameter tables"""
		params = self.SelectedActor.parameters
		for i in xrange(self.ParamTab, params.xsize - 1):
			params[i, :] = params[i + 1, :]
		params.resize(params.xsize - 1, Config.getint('DatabaseLimits', 'ActorLevel') + 1)
		try:
			self.noteBookActorParameters.RemovePage(self.ParamTab)
		except wx.PyAssertionError:
			# There is a strange bug with wx on Windows that raises this exception when 
			# a page is deleted. Removing the page works fine, but it throws the 
			# exception regardless, so this little empty catch is required... :P
			pass
		if self.ParamTab >= self.noteBookActorParameters.GetPageCount():
			self.ParamTab -= 1
		self.noteBookActorParameters.SetSelection(self.ParamTab)

	def textCtrlNotes_TextChanged( self, event ):
		"""Updates the notes for the selected actor"""
		self.SelectedActor.note = event.GetString()

	def GetWeaponIDs( self ):
		"""Returns the ID of the weapon found at index in the actor's weapon set"""
		return DataClasses[self.SelectedActor.class_id].weapon_set
	
	def GetArmorIDs( self, kind ):
		"""Returns all actor armor IDs that are of type 'kind'"""
		ids = DataClasses[self.SelectedActor.class_id].armor_set
		filtered = []
		for id in ids:
			if DataArmors[id].kind == kind:
				filtered.append(id)
		return filtered

#--------------------------------------------------------------------------------------
# ParameterPlotGraphics
#--------------------------------------------------------------------------------------

class ParameterPlotGraphics(plot.PlotGraphics):

	def __init__(self, *args, **kwargs):
		"""Basic constructor for the ParameterPlotGraphics"""
		self._yLim= kwargs.pop('YLimit', None)
		self._xLim = kwargs.pop('XLimit', None)
		plot.PlotGraphics.__init__(self, *args, **kwargs)

	def boundingBox(self):
		"""Calculates the bounds of the box, factoring in custom values"""
		bounds = plot.PlotGraphics.boundingBox(self)
		Min, Max = [bounds[0][0], bounds[1][0]], [bounds[0][1], bounds[1][1]]
		if self._yLim is not None:
			Min[1], Max[1] = self._yLim[0], self._yLim[1]
		if self._xLim is not None:
			Min[0], Max[0] = self._xLim[0], self._xLim[1]
		return plot._Numeric.array(Min), plot._Numeric.array(Max)
		
#--------------------------------------------------------------------------------------
# ParameterGraph
#--------------------------------------------------------------------------------------

class ParameterGraph(plot.PlotCanvas):

	def __init__(self, parent, data=None, color='orange'):
		"""Basic constructor for the ParameterGraph"""
		super(ParameterGraph, self).__init__(parent, style=wx.SUNKEN_BORDER)
		self.SetEnableTitle(False)
		self.SetEnableLegend(False)
		self.SetEnablePointLabel(False)
		self.SetFontSizeAxis(6)
		self.SetXSpec('min')
		self.SetYSpec('min')
		self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
		self.SetEnableAntiAliasing(True)
		self.DrawColor = color
		self.canvas.Bind(wx.EVT_ERASE_BACKGROUND, self.DoNothing)
		if data is not None:
			self.SetData(data)

	def DoNothing( self, event ):
		"""Prevent flickering on Windows"""
		pass

	def SetData(self, data=None, statName='', color=None, maxvalue=None, 
			maxlevel=None, minlevel=1):
		"""Sets the data to plot and draws the graph"""
		if data is None:
			data = [(0, 0), (1, 0)]
		if color is not None:
			self.DrawColor = color
		line = plot.PolyLine(data, colour=self.DrawColor, width=3)
		xLim = yLim = None
		if maxvalue is not None:
			yLim = [0, maxvalue]
		if maxlevel is not None:
			xLim = [minlevel, maxlevel]
		gc = ParameterPlotGraphics([line], xLabel='Level', yLabel=statName,
			XLimit=xLim, YLimit=yLim)
		self.Draw(gc)

	