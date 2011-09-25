# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 30 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.combo

###########################################################################
## Class Actors_Panel
###########################################################################

class Actors_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		ActorListSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapActors = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/Actors.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
		self.bitmapActors.SetMinSize( wx.Size( 150,26 ) )
		self.bitmapActors.SetMaxSize( wx.Size( 150,26 ) )
		
		ActorListSizer.Add( self.bitmapActors, 0, wx.ALL|wx.EXPAND, 5 )
		
		listBoxActorsChoices = []
		self.listBoxActors = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxActorsChoices, wx.LB_SINGLE|wx.CLIP_CHILDREN )
		ActorListSizer.Add( self.listBoxActors, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonMaximum = wx.Button( self, wx.ID_ANY, u"Change Maximum...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		ActorListSizer.Add( self.buttonMaximum, 0, wx.ALL|wx.EXPAND, 5 )
		
		MainSizer.Add( ActorListSizer, 25, wx.EXPAND, 5 )
		
		staticSizerActors = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		sizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelName.Wrap( -1 )
		sizer3.Add( self.labelName, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer3.Add( self.textCtrlName, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelClass = wx.StaticText( self, wx.ID_ANY, u"Class:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelClass.Wrap( -1 )
		sizer3.Add( self.labelClass, 0, wx.ALL, 5 )
		
		comboBoxClassChoices = []
		self.comboBoxClass = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxClassChoices, 0 )
		self.comboBoxClass.SetSelection( -1 )
		sizer3.Add( self.comboBoxClass, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelInitialLevel = wx.StaticText( self, wx.ID_ANY, u"Initial Level:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelInitialLevel.Wrap( -1 )
		sizer4.Add( self.labelInitialLevel, 1, wx.EXPAND|wx.ALL, 5 )
		
		self.labelFinalLevel = wx.StaticText( self, wx.ID_ANY, u"Final Level:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelFinalLevel.Wrap( -1 )
		sizer4.Add( self.labelFinalLevel, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizer3.Add( sizer4, 0, wx.EXPAND, 5 )
		
		sizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.spinCtrlInitialLevel = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 65535, 1 )
		sizer5.Add( self.spinCtrlInitialLevel, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.spinCtrlFinalLevel = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 999, 99 )
		sizer5.Add( self.spinCtrlFinalLevel, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizer3.Add( sizer5, 0, wx.EXPAND, 5 )
		
		self.labelExpCurve = wx.StaticText( self, wx.ID_ANY, u"Experience Curve:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelExpCurve.Wrap( -1 )
		sizer3.Add( self.labelExpCurve, 0, wx.ALL, 5 )
		
		comboBoxExpCurveChoices = []
		self.comboBoxExpCurve = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, comboBoxExpCurveChoices, 0 )
		sizer3.Add( self.comboBoxExpCurve, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelCharacterGraphic = wx.StaticText( self, wx.ID_ANY, u"Character Graphic:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelCharacterGraphic.Wrap( -1 )
		sizer3.Add( self.labelCharacterGraphic, 0, wx.ALL, 5 )
		
		self.bitmapCharacterGraphic = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/Character.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER )
		sizer3.Add( self.bitmapCharacterGraphic, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelBattlerGraphic = wx.StaticText( self, wx.ID_ANY, u"Battler Graphic:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBattlerGraphic.Wrap( -1 )
		sizer3.Add( self.labelBattlerGraphic, 0, wx.ALL, 5 )
		
		self.bitmapBattlerGraphic = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/Battler.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER )
		sizer3.Add( self.bitmapBattlerGraphic, 0, wx.ALL, 5 )
		
		sizer1.Add( sizer3, 25, wx.EXPAND, 5 )
		
		staticSizerActors.Add( sizer1, 35, wx.EXPAND, 5 )
		
		sizer2 = wx.BoxSizer( wx.VERTICAL )
		
		sizerParameters = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Parameters" ), wx.HORIZONTAL )
		
		sizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapMaxHP = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/MaxHP.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		sizer6.Add( self.bitmapMaxHP, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.bitmapSTR = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/Str.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		sizer6.Add( self.bitmapSTR, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.bitmapAGI = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/Agi.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		sizer6.Add( self.bitmapAGI, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizerParameters.Add( sizer6, 1, wx.EXPAND, 5 )
		
		sizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapMaxSP = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/MaxSP.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		sizer7.Add( self.bitmapMaxSP, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.bitmapDEX = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/Dex.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		sizer7.Add( self.bitmapDEX, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.bitmapINT = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/Int.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		sizer7.Add( self.bitmapINT, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizerParameters.Add( sizer7, 1, wx.EXPAND, 5 )
		
		sizer2.Add( sizerParameters, 65, wx.EXPAND|wx.ALL, 5 )
		
		sizerStartEquipment = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Initial Equipment" ), wx.HORIZONTAL )
		
		sizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelWeapon = wx.StaticText( self, wx.ID_ANY, u"Weapon:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.labelWeapon.Wrap( -1 )
		sizer8.Add( self.labelWeapon, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.labelShield = wx.StaticText( self, wx.ID_ANY, u"Shield:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.labelShield.Wrap( -1 )
		sizer8.Add( self.labelShield, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.labelHelmet = wx.StaticText( self, wx.ID_ANY, u"Helmet:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.labelHelmet.Wrap( -1 )
		sizer8.Add( self.labelHelmet, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.labelBodyArmor = wx.StaticText( self, wx.ID_ANY, u"Body Armor:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.labelBodyArmor.Wrap( -1 )
		sizer8.Add( self.labelBodyArmor, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.labelAccessory1 = wx.StaticText( self, wx.ID_ANY, u"Accessory 1:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.labelAccessory1.Wrap( -1 )
		sizer8.Add( self.labelAccessory1, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.labelAccessory2 = wx.StaticText( self, wx.ID_ANY, u"Accessory 2:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.labelAccessory2.Wrap( -1 )
		sizer8.Add( self.labelAccessory2, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizerStartEquipment.Add( sizer8, 0, wx.EXPAND, 5 )
		
		sizer9 = wx.BoxSizer( wx.VERTICAL )
		
		comboBoxWeaponChoices = [ u"(None)" ]
		self.comboBoxWeapon = wx.ComboBox( self, wx.ID_ANY, u"(None)", wx.DefaultPosition, wx.DefaultSize, comboBoxWeaponChoices, wx.CB_DROPDOWN )
		sizer9.Add( self.comboBoxWeapon, 1, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxShieldChoices = [ u"(None)" ]
		self.comboBoxShield = wx.ComboBox( self, wx.ID_ANY, u"(None)", wx.DefaultPosition, wx.DefaultSize, comboBoxShieldChoices, wx.CB_DROPDOWN )
		sizer9.Add( self.comboBoxShield, 1, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxHelmetChoices = [ u"(None)" ]
		self.comboBoxHelmet = wx.ComboBox( self, wx.ID_ANY, u"(None)", wx.DefaultPosition, wx.DefaultSize, comboBoxHelmetChoices, wx.CB_DROPDOWN )
		sizer9.Add( self.comboBoxHelmet, 1, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxBodyArmorChoices = [ u"(None)" ]
		self.comboBoxBodyArmor = wx.ComboBox( self, wx.ID_ANY, u"(None)", wx.DefaultPosition, wx.DefaultSize, comboBoxBodyArmorChoices, wx.CB_DROPDOWN )
		sizer9.Add( self.comboBoxBodyArmor, 1, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxAccessory1Choices = [ u"(None)" ]
		self.comboBoxAccessory1 = wx.ComboBox( self, wx.ID_ANY, u"(None)", wx.DefaultPosition, wx.DefaultSize, comboBoxAccessory1Choices, wx.CB_DROPDOWN )
		sizer9.Add( self.comboBoxAccessory1, 1, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxAccessory2Choices = [ u"(None)" ]
		self.comboBoxAccessory2 = wx.ComboBox( self, wx.ID_ANY, u"(None)", wx.DefaultPosition, wx.DefaultSize, comboBoxAccessory2Choices, wx.CB_DROPDOWN )
		sizer9.Add( self.comboBoxAccessory2, 0, wx.ALL|wx.EXPAND, 5 )
		
		sizerStartEquipment.Add( sizer9, 1, wx.EXPAND, 5 )
		
		sizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelFixedWeapon = wx.CheckBox( self, wx.ID_ANY, u"Fixed", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer10.Add( self.labelFixedWeapon, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.labelFixedShield = wx.CheckBox( self, wx.ID_ANY, u"Fixed", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer10.Add( self.labelFixedShield, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.labelFixedHelmet = wx.CheckBox( self, wx.ID_ANY, u"Fixed", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer10.Add( self.labelFixedHelmet, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.labelFixedBodyArmor = wx.CheckBox( self, wx.ID_ANY, u"Fixed", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer10.Add( self.labelFixedBodyArmor, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.labelFixedAccessory1 = wx.CheckBox( self, wx.ID_ANY, u"Fixed", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer10.Add( self.labelFixedAccessory1, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.labelFixedAccessory2 = wx.CheckBox( self, wx.ID_ANY, u"Fixed", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer10.Add( self.labelFixedAccessory2, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizerStartEquipment.Add( sizer10, 0, wx.EXPAND, 5 )
		
		sizer2.Add( sizerStartEquipment, 35, wx.ALL|wx.EXPAND, 5 )
		
		staticSizerActors.Add( sizer2, 75, wx.EXPAND, 5 )
		
		MainSizer.Add( staticSizerActors, 75, wx.EXPAND|wx.ALL, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		# Connect Events
		self.listBoxActors.Bind( wx.EVT_LISTBOX, self.listBoxActors_SelectionChanged )
		self.buttonMaximum.Bind( wx.EVT_BUTTON, self.buttonMaximum_Clicked )
		self.textCtrlName.Bind( wx.EVT_TEXT, self.textBoxName_TextChanged )
		self.comboBoxClass.Bind( wx.EVT_CHOICE, self.comboBoxClass_SelectionChanged )
		self.spinCtrlInitialLevel.Bind( wx.EVT_SPINCTRL, self.spinCtrlInitialLevel_ValueChanged )
		self.spinCtrlFinalLevel.Bind( wx.EVT_SPINCTRL, self.spinCtrlFinalLevel_ValueChanged )
		self.comboBoxExpCurve.Bind( wx.EVT_LEFT_DCLICK, self.comboBoxExperience_Click )
		self.bitmapCharacterGraphic.Bind( wx.EVT_LEFT_DCLICK, self.bitmapCharacterGraphic_Click )
		self.bitmapBattlerGraphic.Bind( wx.EVT_LEFT_DCLICK, self.bitmapBattlerGraphic_Click )
		self.bitmapMaxHP.Bind( wx.EVT_LEFT_DCLICK, self.bitmapMaxHP_Click )
		self.bitmapSTR.Bind( wx.EVT_LEFT_DCLICK, self.bitmapStr_Click )
		self.bitmapAGI.Bind( wx.EVT_LEFT_DCLICK, self.bitmapAgi_Click )
		self.bitmapMaxSP.Bind( wx.EVT_LEFT_DCLICK, self.bitmapMaxSP_Click )
		self.bitmapDEX.Bind( wx.EVT_LEFT_DCLICK, self.bitmapDex_Click )
		self.bitmapINT.Bind( wx.EVT_LEFT_DCLICK, self.bitmapInt_Click )
		self.comboBoxWeapon.Bind( wx.EVT_COMBOBOX, self.comboBoxWeapon_SelectionChanged )
		self.comboBoxShield.Bind( wx.EVT_COMBOBOX, self.comboBoxShield_SelectionChanged )
		self.comboBoxHelmet.Bind( wx.EVT_COMBOBOX, self.comboBoxHelmet_SelectionChanged )
		self.comboBoxBodyArmor.Bind( wx.EVT_COMBOBOX, self.comboBoxBodyArmor_SelectionChanged )
		self.comboBoxAccessory1.Bind( wx.EVT_COMBOBOX, self.comboBoxAccessory1_SelectionChanged )
		self.comboBoxAccessory2.Bind( wx.EVT_COMBOBOX, self.comboBoxAccessory2_SelectionChanged )
		self.labelFixedWeapon.Bind( wx.EVT_CHECKBOX, self.checkBoxWeapon_CheckChanged )
		self.labelFixedShield.Bind( wx.EVT_CHECKBOX, self.checkBoxShield_CheckChanged )
		self.labelFixedHelmet.Bind( wx.EVT_CHECKBOX, self.checkBoxHelmet_CheckChanged )
		self.labelFixedBodyArmor.Bind( wx.EVT_CHECKBOX, self.checkBoxBodyArmor_CheckChanged )
		self.labelFixedAccessory1.Bind( wx.EVT_CHECKBOX, self.checkBoxAccessory1_CheckChanged )
		self.labelFixedAccessory2.Bind( wx.EVT_CHECKBOX, self.checkBoxAccessory2_CheckChanged )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def listBoxActors_SelectionChanged( self, event ):
		event.Skip()
	
	def buttonMaximum_Clicked( self, event ):
		event.Skip()
	
	def textBoxName_TextChanged( self, event ):
		event.Skip()
	
	def comboBoxClass_SelectionChanged( self, event ):
		event.Skip()
	
	def spinCtrlInitialLevel_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlFinalLevel_ValueChanged( self, event ):
		event.Skip()
	
	def comboBoxExperience_Click( self, event ):
		event.Skip()
	
	def bitmapCharacterGraphic_Click( self, event ):
		event.Skip()
	
	def bitmapBattlerGraphic_Click( self, event ):
		event.Skip()
	
	def bitmapMaxHP_Click( self, event ):
		event.Skip()
	
	def bitmapStr_Click( self, event ):
		event.Skip()
	
	def bitmapAgi_Click( self, event ):
		event.Skip()
	
	def bitmapMaxSP_Click( self, event ):
		event.Skip()
	
	def bitmapDex_Click( self, event ):
		event.Skip()
	
	def bitmapInt_Click( self, event ):
		event.Skip()
	
	def comboBoxWeapon_SelectionChanged( self, event ):
		event.Skip()
	
	def comboBoxShield_SelectionChanged( self, event ):
		event.Skip()
	
	def comboBoxHelmet_SelectionChanged( self, event ):
		event.Skip()
	
	def comboBoxBodyArmor_SelectionChanged( self, event ):
		event.Skip()
	
	def comboBoxAccessory1_SelectionChanged( self, event ):
		event.Skip()
	
	def comboBoxAccessory2_SelectionChanged( self, event ):
		event.Skip()
	
	def checkBoxWeapon_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxShield_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxHelmet_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxBodyArmor_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxAccessory1_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxAccessory2_CheckChanged( self, event ):
		event.Skip()
	

###########################################################################
## Class Classes_Panel
###########################################################################

class Classes_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		ClassListSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapClasses = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/Classes.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
		self.bitmapClasses.SetMinSize( wx.Size( 150,26 ) )
		self.bitmapClasses.SetMaxSize( wx.Size( 150,26 ) )
		
		ClassListSizer.Add( self.bitmapClasses, 0, wx.ALL|wx.EXPAND, 5 )
		
		listBoxClassesChoices = []
		self.listBoxClasses = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxClassesChoices, wx.LB_SINGLE|wx.CLIP_CHILDREN )
		ClassListSizer.Add( self.listBoxClasses, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonMaximum = wx.Button( self, wx.ID_ANY, u"Change Maximum...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		ClassListSizer.Add( self.buttonMaximum, 0, wx.ALL|wx.EXPAND, 5 )
		
		MainSizer.Add( ClassListSizer, 25, wx.EXPAND, 5 )
		
		staticSizerClasses = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		bSizer65 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelName.Wrap( -1 )
		bSizer65.Add( self.labelName, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer65.Add( self.textCtrlName, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelWeapons = wx.StaticText( self, wx.ID_ANY, u"Equippable Weapons:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelWeapons.Wrap( -1 )
		bSizer65.Add( self.labelWeapons, 0, wx.ALL|wx.EXPAND, 5 )
		
		checkListWeaponsChoices = []
		self.checkListWeapons = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListWeaponsChoices, 0 )
		bSizer65.Add( self.checkListWeapons, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer68 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonWeaponAll = wx.Button( self, wx.ID_ANY, u"All", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer68.Add( self.buttonWeaponAll, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonWeaponNone = wx.Button( self, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer68.Add( self.buttonWeaponNone, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		bSizer65.Add( bSizer68, 0, wx.EXPAND, 5 )
		
		staticSizerClasses.Add( bSizer65, 30, wx.EXPAND, 5 )
		
		bSizer66 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer651 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelPosition = wx.StaticText( self, wx.ID_ANY, u"Position:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPosition.Wrap( -1 )
		bSizer651.Add( self.labelPosition, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxPositionChoices = []
		self.comboBoxPosition = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxPositionChoices, 0 )
		self.comboBoxPosition.SetSelection( 0 )
		bSizer651.Add( self.comboBoxPosition, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelArmors = wx.StaticText( self, wx.ID_ANY, u"Equippable Armors:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelArmors.Wrap( -1 )
		bSizer651.Add( self.labelArmors, 0, wx.ALL|wx.EXPAND, 5 )
		
		checkListArmorsChoices = []
		self.checkListArmors = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListArmorsChoices, 0 )
		bSizer651.Add( self.checkListArmors, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer681 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonArmorAll = wx.Button( self, wx.ID_ANY, u"All", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer681.Add( self.buttonArmorAll, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonArmorNone = wx.Button( self, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer681.Add( self.buttonArmorNone, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		bSizer651.Add( bSizer681, 0, wx.EXPAND, 5 )
		
		bSizer66.Add( bSizer651, 1, wx.EXPAND, 5 )
		
		staticSizerClasses.Add( bSizer66, 30, wx.EXPAND, 5 )
		
		bSizer67 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer74 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelElements = wx.StaticText( self, wx.ID_ANY, u"Element Efficiency:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelElements.Wrap( -1 )
		bSizer74.Add( self.labelElements, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.labelStates = wx.StaticText( self, wx.ID_ANY, u"State Efficiency:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelStates.Wrap( -1 )
		bSizer74.Add( self.labelStates, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer67.Add( bSizer74, 0, wx.EXPAND, 5 )
		
		bSizer75 = wx.BoxSizer( wx.HORIZONTAL )
		
		checkListElementsChoices = []
		self.checkListElements = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListElementsChoices, wx.LB_HSCROLL|wx.LB_MULTIPLE|wx.LB_NEEDED_SB )
		bSizer75.Add( self.checkListElements, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		checkListStatesChoices = []
		self.checkListStates = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListStatesChoices, wx.LB_HSCROLL|wx.LB_MULTIPLE|wx.LB_NEEDED_SB )
		bSizer75.Add( self.checkListStates, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer67.Add( bSizer75, 60, wx.EXPAND, 5 )
		
		bSizer76 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelSkills = wx.StaticText( self, wx.ID_ANY, u"Skills to Learn:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelSkills.Wrap( -1 )
		bSizer76.Add( self.labelSkills, 0, wx.ALL, 5 )
		
		self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VIRTUAL|wx.LC_VRULES )
		bSizer76.Add( self.m_listCtrl1, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer67.Add( bSizer76, 40, wx.EXPAND, 5 )
		
		staticSizerClasses.Add( bSizer67, 40, wx.EXPAND, 5 )
		
		MainSizer.Add( staticSizerClasses, 75, wx.EXPAND|wx.ALL, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		# Connect Events
		self.listBoxClasses.Bind( wx.EVT_LISTBOX, self.listBoxActors_SelectionChanged )
		self.buttonMaximum.Bind( wx.EVT_BUTTON, self.buttonMaximum_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def listBoxActors_SelectionChanged( self, event ):
		event.Skip()
	
	def buttonMaximum_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class Skills_Panel
###########################################################################

class Skills_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		SkillListSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapSkills = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/Skills.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
		self.bitmapSkills.SetMinSize( wx.Size( 150,26 ) )
		self.bitmapSkills.SetMaxSize( wx.Size( 150,26 ) )
		
		SkillListSizer.Add( self.bitmapSkills, 0, wx.ALL|wx.EXPAND, 5 )
		
		listBoxSkillsChoices = []
		self.listBoxSkills = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxSkillsChoices, wx.LB_SINGLE|wx.CLIP_CHILDREN )
		self.listBoxSkills.SetToolTipString( u"Select the item to edit" )
		
		SkillListSizer.Add( self.listBoxSkills, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonMaximum = wx.Button( self, wx.ID_ANY, u"Change Maximum...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.buttonMaximum.SetToolTipString( u"Change the maximum of available items" )
		
		SkillListSizer.Add( self.buttonMaximum, 0, wx.ALL|wx.EXPAND, 5 )
		
		MainSizer.Add( SkillListSizer, 25, wx.EXPAND, 5 )
		
		staticSizerItems = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		sizer1 = wx.BoxSizer( wx.VERTICAL )
		
		sizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelName.Wrap( -1 )
		sizer3.Add( self.labelName, 1, wx.ALL, 5 )
		
		self.labelIcon = wx.StaticText( self, wx.ID_ANY, u"Icon:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelIcon.Wrap( -1 )
		sizer3.Add( self.labelIcon, 1, wx.ALL, 5 )
		
		sizer1.Add( sizer3, 0, wx.EXPAND, 5 )
		
		sizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textCtrlName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textCtrlName.SetToolTipString( u"The item name." )
		
		sizer4.Add( self.textCtrlName, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		comboBoxIconChoices = [ u"(None)" ]
		self.comboBoxIcon = wx.ComboBox( self, wx.ID_ANY, u"(None)", wx.DefaultPosition, wx.DefaultSize, comboBoxIconChoices, 0 )
		self.comboBoxIcon.SetToolTipString( u"The icon associated with the item" )
		
		sizer4.Add( self.comboBoxIcon, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer1.Add( sizer4, 0, wx.EXPAND, 5 )
		
		self.labelDescription = wx.StaticText( self, wx.ID_ANY, u"Description:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelDescription.Wrap( -1 )
		sizer1.Add( self.labelDescription, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.extCtrlDescription = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.extCtrlDescription.SetToolTipString( u"Comment displayed when the item is selected" )
		
		sizer1.Add( self.extCtrlDescription, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelScope = wx.StaticText( self, wx.ID_ANY, u"Scope:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelScope.Wrap( -1 )
		sizer8.Add( self.labelScope, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxScopeChoices = [ u"None", u"One Enemy", u"All Enemies", u"One Ally", u"All Allies", u"One Ally (HP 0)", u"All Allies (HP 0)", u"The User", u"One Ally or Enemy", u"Everyone" ]
		self.comboBoxScope = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxScopeChoices, 0 )
		self.comboBoxScope.SetSelection( 0 )
		self.comboBoxScope.SetToolTipString( u"Item's target area of influence." )
		
		sizer8.Add( self.comboBoxScope, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelUserAnimation = wx.StaticText( self, wx.ID_ANY, u"User Animation:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelUserAnimation.Wrap( -1 )
		sizer8.Add( self.labelUserAnimation, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxUserAnimationChoices = [ u"(None)" ]
		self.comboBoxUserAnimation = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxUserAnimationChoices, 0 )
		self.comboBoxUserAnimation.SetSelection( 0 )
		self.comboBoxUserAnimation.SetToolTipString( u"Animation displayed on the user when used in battle." )
		
		sizer8.Add( self.comboBoxUserAnimation, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelMenuSE = wx.StaticText( self, wx.ID_ANY, u"Menu Use SE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMenuSE.Wrap( -1 )
		sizer8.Add( self.labelMenuSE, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxMenuSEChoices = []
		self.comboBoxMenuSE = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxMenuSEChoices, 0 )
		self.comboBoxMenuSE.SetToolTipString( u"Sound effect played when using this item on the menu screen" )
		
		sizer8.Add( self.comboBoxMenuSE, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizer6.Add( sizer8, 1, wx.EXPAND, 5 )
		
		sizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelOccasion = wx.StaticText( self, wx.ID_ANY, u"Occasion:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelOccasion.Wrap( -1 )
		sizer9.Add( self.labelOccasion, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxOccasionChoices = [ u"Always", u"Only in Battle", u"Only from Menu", u"Never" ]
		self.comboBoxOccasion = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxOccasionChoices, 0 )
		self.comboBoxOccasion.SetSelection( 0 )
		self.comboBoxOccasion.SetToolTipString( u"Screen(s) where the item can be used." )
		
		sizer9.Add( self.comboBoxOccasion, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelTargetAnimation = wx.StaticText( self, wx.ID_ANY, u"Target Animation:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTargetAnimation.Wrap( -1 )
		sizer9.Add( self.labelTargetAnimation, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxTargetAnimationChoices = [ u"(None)" ]
		self.comboBoxTargetAnimation = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxTargetAnimationChoices, 0 )
		self.comboBoxTargetAnimation.SetSelection( 0 )
		self.comboBoxTargetAnimation.SetToolTipString( u"Animation displayed on the target when used in battle." )
		
		sizer9.Add( self.comboBoxTargetAnimation, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelCommonEvent = wx.StaticText( self, wx.ID_ANY, u"Common Event:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelCommonEvent.Wrap( -1 )
		sizer9.Add( self.labelCommonEvent, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxCommonEventChoices = [ u"(None)" ]
		self.comboBoxCommonEvent = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxCommonEventChoices, 0 )
		self.comboBoxCommonEvent.SetSelection( 0 )
		self.comboBoxCommonEvent.SetToolTipString( u"Common event called when item is used." )
		
		sizer9.Add( self.comboBoxCommonEvent, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizer6.Add( sizer9, 1, wx.EXPAND, 5 )
		
		sizer1.Add( sizer6, 0, wx.EXPAND, 5 )
		
		sizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelSPCost = wx.StaticText( self, wx.ID_ANY, u"SP Cost:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelSPCost.Wrap( -1 )
		sizer10.Add( self.labelSPCost, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrSPCost = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.SP_WRAP, 0, 999999999, 0 )
		self.spinCtrSPCost.SetToolTipString( u"The price of the item in shops. Set to 0 to make item unsellable." )
		
		sizer10.Add( self.spinCtrSPCost, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelStrF = wx.StaticText( self, wx.ID_ANY, u"STR-F:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelStrF.Wrap( -1 )
		sizer10.Add( self.labelStrF, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlStrF = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 0 )
		self.spinCtrlStrF.SetToolTipString( u"Recovered HP, as percentage of max HP" )
		
		sizer10.Add( self.spinCtrlStrF, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelHitRate = wx.StaticText( self, wx.ID_ANY, u"Hit Rate:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelHitRate.Wrap( -1 )
		sizer10.Add( self.labelHitRate, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlHitRate = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 100 )
		self.spinCtrlHitRate.SetToolTipString( u"Success rate in percentage of item use, not affected by target's parameters." )
		
		sizer10.Add( self.spinCtrlHitRate, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer7.Add( sizer10, 1, wx.EXPAND, 5 )
		
		sizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelPower = wx.StaticText( self, wx.ID_ANY, u"Power:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPower.Wrap( -1 )
		sizer11.Add( self.labelPower, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlPower = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -999999999, 999999999, 0 )
		sizer11.Add( self.spinCtrlPower, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelDexF = wx.StaticText( self, wx.ID_ANY, u"DEX-F:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelDexF.Wrap( -1 )
		sizer11.Add( self.labelDexF, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlDexF = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 0 )
		self.spinCtrlDexF.SetToolTipString( u"Amount of recovered HP. An odd value allows for creation of an attack item." )
		
		sizer11.Add( self.spinCtrlDexF, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelPDEF = wx.StaticText( self, wx.ID_ANY, u"PDEF-F:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPDEF.Wrap( -1 )
		sizer11.Add( self.labelPDEF, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlPDEF = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 0 )
		self.spinCtrlPDEF.SetToolTipString( u"Coefficient indicating how much of the target's physical defense influences the effects. Set high for physical attack items." )
		
		sizer11.Add( self.spinCtrlPDEF, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer7.Add( sizer11, 1, wx.EXPAND, 5 )
		
		sizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelAtkF = wx.StaticText( self, wx.ID_ANY, u"ATK-F:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAtkF.Wrap( -1 )
		sizer12.Add( self.labelAtkF, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlAtkF = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 0 )
		sizer12.Add( self.spinCtrlAtkF, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labeAgiF = wx.StaticText( self, wx.ID_ANY, u"AGI-F:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labeAgiF.Wrap( -1 )
		sizer12.Add( self.labeAgiF, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlAgiF = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 0 )
		self.spinCtrlAgiF.SetToolTipString( u"Recovered SP, as percentage of max SP" )
		
		sizer12.Add( self.spinCtrlAgiF, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelMDEF = wx.StaticText( self, wx.ID_ANY, u"MDEF-F:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMDEF.Wrap( -1 )
		sizer12.Add( self.labelMDEF, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlMDEF = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 0 )
		self.spinCtrlMDEF.SetToolTipString( u"Coefficient indicating how much of the target's magic defense influences the effects. Set high for magical attack items." )
		
		sizer12.Add( self.spinCtrlMDEF, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer7.Add( sizer12, 1, wx.EXPAND, 5 )
		
		sizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelEvaF = wx.StaticText( self, wx.ID_ANY, u"EVA-F:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelEvaF.Wrap( -1 )
		sizer13.Add( self.labelEvaF, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlEvaF = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 0 )
		self.spinCtrlEvaF.SetToolTipString( u"Value of the parameter to increase by." )
		
		sizer13.Add( self.spinCtrlEvaF, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelIntF = wx.StaticText( self, wx.ID_ANY, u"INT-F:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelIntF.Wrap( -1 )
		sizer13.Add( self.labelIntF, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlIntF = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 0 )
		self.spinCtrlIntF.SetToolTipString( u"Amount of recovered SP. An odd value allows for creation of an attack item." )
		
		sizer13.Add( self.spinCtrlIntF, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelVariance = wx.StaticText( self, wx.ID_ANY, u"Variance:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelVariance.Wrap( -1 )
		sizer13.Add( self.labelVariance, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlVariance = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 15 )
		self.spinCtrlVariance.SetToolTipString( u"Degree of fluctuation in final effect strength. The effect strength value varies only by this percentage. 15 is average." )
		
		sizer13.Add( self.spinCtrlVariance, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer7.Add( sizer13, 1, wx.EXPAND, 5 )
		
		sizer1.Add( sizer7, 1, wx.EXPAND, 5 )
		
		staticSizerItems.Add( sizer1, 60, wx.EXPAND, 5 )
		
		sizer2 = wx.BoxSizer( wx.VERTICAL )
		
		sizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelElements = wx.StaticText( self, wx.ID_ANY, u"Element:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelElements.Wrap( -1 )
		sizer14.Add( self.labelElements, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.labelStates = wx.StaticText( self, wx.ID_ANY, u"State Change:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelStates.Wrap( -1 )
		sizer14.Add( self.labelStates, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizer2.Add( sizer14, 0, wx.EXPAND, 5 )
		
		sizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		checkListElementsChoices = []
		self.checkListElements = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListElementsChoices, wx.LB_HSCROLL|wx.LB_NEEDED_SB|wx.CLIP_CHILDREN )
		self.checkListElements.SetToolTipString( u"Set the element attributes for the item. The effect strength varies according the their strengths/weaknesses." )
		
		sizer15.Add( self.checkListElements, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		checkListStatesChoices = []
		self.checkListStates = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListStatesChoices, wx.LB_NEEDED_SB|wx.CLIP_CHILDREN )
		self.checkListStates.SetToolTipString( u"Indicates the item's states set [+] and cleared [-] on the target. The success rate is determined by the target's strengths/weaknesses." )
		
		sizer15.Add( self.checkListStates, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer2.Add( sizer15, 1, wx.EXPAND, 5 )
		
		self.labelNotes = wx.StaticText( self, wx.ID_ANY, u"Notes:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelNotes.Wrap( -1 )
		sizer2.Add( self.labelNotes, 0, wx.ALL, 5 )
		
		self.textCtrlNotes = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.CLIP_CHILDREN )
		self.textCtrlNotes.SetToolTipString( u"Any user notes for this item. These notes can also be referenced via scripts." )
		
		sizer2.Add( self.textCtrlNotes, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		staticSizerItems.Add( sizer2, 40, wx.EXPAND, 5 )
		
		MainSizer.Add( staticSizerItems, 75, wx.EXPAND|wx.ALL, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		# Connect Events
		self.listBoxSkills.Bind( wx.EVT_LISTBOX, self.listBoxSkills_SelectionChanged )
		self.buttonMaximum.Bind( wx.EVT_BUTTON, self.buttonMaximum_Clicked )
		self.textCtrlName.Bind( wx.EVT_TEXT, self.textCtrlName_TextChanged )
		self.comboBoxIcon.Bind( wx.EVT_COMBOBOX, self.comboBoxIcon_SelectionChanged )
		self.extCtrlDescription.Bind( wx.EVT_TEXT, self.textCtrlDescription_TextChange )
		self.comboBoxScope.Bind( wx.EVT_CHOICE, self.comboBoxScope_SelectionChanged )
		self.comboBoxUserAnimation.Bind( wx.EVT_CHOICE, self.comboBoxUserAnimation_SelectionChanged )
		self.comboBoxMenuSE.Bind( wx.EVT_LEFT_DOWN, self.comboBoxMenuSE_Clicked )
		self.comboBoxOccasion.Bind( wx.EVT_CHOICE, self.comboBoxOccasion_SelectionChanged )
		self.comboBoxTargetAnimation.Bind( wx.EVT_CHOICE, self.comboBoxTargetAnimation_SelectionChanged )
		self.comboBoxCommonEvent.Bind( wx.EVT_CHOICE, self.comboBoxCommonEvent_SelectionChanged )
		self.spinCtrSPCost.Bind( wx.EVT_SPINCTRL, self.spinCtrlSPCost_ValueChanged )
		self.spinCtrlStrF.Bind( wx.EVT_SPINCTRL, self.spinCtrlStrF_ValueChanged )
		self.spinCtrlHitRate.Bind( wx.EVT_SPINCTRL, self.spinCtrlHitRate_ValueChanged )
		self.spinCtrlPower.Bind( wx.EVT_SPINCTRL, self.spinCtrlPower_ValueChanged )
		self.spinCtrlDexF.Bind( wx.EVT_SPINCTRL, self.spinCtrlDexF_ValueChanged )
		self.spinCtrlPDEF.Bind( wx.EVT_SPINCTRL, self.spinCtrlPDEF_ValueChanged )
		self.spinCtrlAtkF.Bind( wx.EVT_SPINCTRL, self.spinCtrlAtkF_ValueChanged )
		self.spinCtrlAgiF.Bind( wx.EVT_SPINCTRL, self.spinCtrlAgiF_ValueChanged )
		self.spinCtrlMDEF.Bind( wx.EVT_SPINCTRL, self.spinCtrlMDEF_ValueChanged )
		self.spinCtrlEvaF.Bind( wx.EVT_SPINCTRL, self.spinCtrlEvaF_ValueChanged )
		self.spinCtrlIntF.Bind( wx.EVT_SPINCTRL, self.spinCtrlIntF_ValueChanged )
		self.spinCtrlVariance.Bind( wx.EVT_SPINCTRL, self.spinCtrlVariance_ValueChanged )
		self.checkListElements.Bind( wx.EVT_CHECKLISTBOX, self.checkListElements_CheckChanged )
		self.checkListStates.Bind( wx.EVT_CHECKLISTBOX, self.checkListStates_CheckChanged )
		self.textCtrlNotes.Bind( wx.EVT_TEXT, self.textCtrlNotes_TextChanged )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def listBoxSkills_SelectionChanged( self, event ):
		event.Skip()
	
	def buttonMaximum_Clicked( self, event ):
		event.Skip()
	
	def textCtrlName_TextChanged( self, event ):
		event.Skip()
	
	def comboBoxIcon_SelectionChanged( self, event ):
		event.Skip()
	
	def textCtrlDescription_TextChange( self, event ):
		event.Skip()
	
	def comboBoxScope_SelectionChanged( self, event ):
		event.Skip()
	
	def comboBoxUserAnimation_SelectionChanged( self, event ):
		event.Skip()
	
	def comboBoxMenuSE_Clicked( self, event ):
		event.Skip()
	
	def comboBoxOccasion_SelectionChanged( self, event ):
		event.Skip()
	
	def comboBoxTargetAnimation_SelectionChanged( self, event ):
		event.Skip()
	
	def comboBoxCommonEvent_SelectionChanged( self, event ):
		event.Skip()
	
	def spinCtrlSPCost_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlStrF_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlHitRate_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlPower_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlDexF_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlPDEF_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlAtkF_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlAgiF_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlMDEF_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlEvaF_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlIntF_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlVariance_ValueChanged( self, event ):
		event.Skip()
	
	def checkListElements_CheckChanged( self, event ):
		event.Skip()
	
	def checkListStates_CheckChanged( self, event ):
		event.Skip()
	
	def textCtrlNotes_TextChanged( self, event ):
		event.Skip()
	

###########################################################################
## Class Items_Panel
###########################################################################

class Items_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		ItemListSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapItems = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/Items.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
		self.bitmapItems.SetMinSize( wx.Size( 150,26 ) )
		self.bitmapItems.SetMaxSize( wx.Size( 150,26 ) )
		
		ItemListSizer.Add( self.bitmapItems, 0, wx.ALL|wx.EXPAND, 5 )
		
		listBoxItemsChoices = []
		self.listBoxItems = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxItemsChoices, wx.LB_SINGLE|wx.CLIP_CHILDREN )
		self.listBoxItems.SetToolTipString( u"Select the item to edit" )
		
		ItemListSizer.Add( self.listBoxItems, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonMaximum = wx.Button( self, wx.ID_ANY, u"Change Maximum...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.buttonMaximum.SetToolTipString( u"Change the maximum of available items" )
		
		ItemListSizer.Add( self.buttonMaximum, 0, wx.ALL|wx.EXPAND, 5 )
		
		MainSizer.Add( ItemListSizer, 25, wx.EXPAND, 5 )
		
		staticSizerItems = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		sizer1 = wx.BoxSizer( wx.VERTICAL )
		
		sizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelName.Wrap( -1 )
		sizer3.Add( self.labelName, 1, wx.ALL, 5 )
		
		self.labelIcon = wx.StaticText( self, wx.ID_ANY, u"Icon:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelIcon.Wrap( -1 )
		sizer3.Add( self.labelIcon, 1, wx.ALL, 5 )
		
		sizer1.Add( sizer3, 0, wx.EXPAND, 5 )
		
		sizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textCtrlName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textCtrlName.SetToolTipString( u"The item name." )
		
		sizer4.Add( self.textCtrlName, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		comboBoxIconChoices = [ u"(None)" ]
		self.comboBoxIcon = wx.ComboBox( self, wx.ID_ANY, u"(None)", wx.DefaultPosition, wx.DefaultSize, comboBoxIconChoices, 0 )
		self.comboBoxIcon.SetToolTipString( u"The icon associated with the item" )
		
		sizer4.Add( self.comboBoxIcon, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer1.Add( sizer4, 0, wx.EXPAND, 5 )
		
		self.labelDescription = wx.StaticText( self, wx.ID_ANY, u"Description:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelDescription.Wrap( -1 )
		sizer1.Add( self.labelDescription, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.extCtrlDescription = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.extCtrlDescription.SetToolTipString( u"Comment displayed when the item is selected" )
		
		sizer1.Add( self.extCtrlDescription, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelScope = wx.StaticText( self, wx.ID_ANY, u"Scope:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelScope.Wrap( -1 )
		sizer8.Add( self.labelScope, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxScopeChoices = [ u"None", u"One Enemy", u"All Enemies", u"One Ally", u"All Allies", u"One Ally (HP 0)", u"All Allies (HP 0)", u"The User", u"One Ally or Enemy", u"Everyone" ]
		self.comboBoxScope = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxScopeChoices, 0 )
		self.comboBoxScope.SetSelection( 0 )
		self.comboBoxScope.SetToolTipString( u"Item's target area of influence." )
		
		sizer8.Add( self.comboBoxScope, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelUserAnimation = wx.StaticText( self, wx.ID_ANY, u"User Animation:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelUserAnimation.Wrap( -1 )
		sizer8.Add( self.labelUserAnimation, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxUserAnimationChoices = [ u"(None)" ]
		self.comboBoxUserAnimation = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxUserAnimationChoices, 0 )
		self.comboBoxUserAnimation.SetSelection( 0 )
		self.comboBoxUserAnimation.SetToolTipString( u"Animation displayed on the user when used in battle." )
		
		sizer8.Add( self.comboBoxUserAnimation, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelMenuSE = wx.StaticText( self, wx.ID_ANY, u"Menu Use SE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMenuSE.Wrap( -1 )
		sizer8.Add( self.labelMenuSE, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxMenuSEChoices = []
		self.comboBoxMenuSE = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, comboBoxMenuSEChoices, 0 )
		self.comboBoxMenuSE.SetToolTipString( u"Sound effect played when using this item on the menu screen" )
		
		sizer8.Add( self.comboBoxMenuSE, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizer6.Add( sizer8, 1, wx.EXPAND, 5 )
		
		sizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelOccasion = wx.StaticText( self, wx.ID_ANY, u"Occasion:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelOccasion.Wrap( -1 )
		sizer9.Add( self.labelOccasion, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxOccasionChoices = [ u"Always", u"Only in Battle", u"Only from Menu", u"Never" ]
		self.comboBoxOccasion = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxOccasionChoices, 0 )
		self.comboBoxOccasion.SetSelection( 0 )
		self.comboBoxOccasion.SetToolTipString( u"Screen(s) where the item can be used." )
		
		sizer9.Add( self.comboBoxOccasion, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelTargetAnimation = wx.StaticText( self, wx.ID_ANY, u"Target Animation:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTargetAnimation.Wrap( -1 )
		sizer9.Add( self.labelTargetAnimation, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxTargetAnimationChoices = [ u"(None)" ]
		self.comboBoxTargetAnimation = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxTargetAnimationChoices, 0 )
		self.comboBoxTargetAnimation.SetSelection( 0 )
		self.comboBoxTargetAnimation.SetToolTipString( u"Animation displayed on the target when used in battle." )
		
		sizer9.Add( self.comboBoxTargetAnimation, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelCommonEvent = wx.StaticText( self, wx.ID_ANY, u"Common Event:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelCommonEvent.Wrap( -1 )
		sizer9.Add( self.labelCommonEvent, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxCommonEventChoices = [ u"(None)" ]
		self.comboBoxCommonEvent = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxCommonEventChoices, 0 )
		self.comboBoxCommonEvent.SetSelection( 0 )
		self.comboBoxCommonEvent.SetToolTipString( u"Common event called when item is used." )
		
		sizer9.Add( self.comboBoxCommonEvent, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizer6.Add( sizer9, 1, wx.EXPAND, 5 )
		
		sizer1.Add( sizer6, 0, wx.EXPAND, 5 )
		
		sizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelPrice = wx.StaticText( self, wx.ID_ANY, u"Price:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPrice.Wrap( -1 )
		sizer10.Add( self.labelPrice, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlPrice = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 999999999, 0 )
		self.spinCtrlPrice.SetToolTipString( u"The price of the item in shops. Set to 0 to make item unsellable." )
		
		sizer10.Add( self.spinCtrlPrice, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelRecrHPPercent = wx.StaticText( self, wx.ID_ANY, u"Recr HP %:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelRecrHPPercent.Wrap( -1 )
		sizer10.Add( self.labelRecrHPPercent, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlRecrHP = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -10000, 10000, 0 )
		self.spinCtrlRecrHP.SetToolTipString( u"Recovered HP, as percentage of max HP" )
		
		sizer10.Add( self.spinCtrlRecrHP, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelHitRate = wx.StaticText( self, wx.ID_ANY, u"Hit Rate:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelHitRate.Wrap( -1 )
		sizer10.Add( self.labelHitRate, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlHitRate = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 100 )
		self.spinCtrlHitRate.SetToolTipString( u"Success rate in percentage of item use, not affected by target's parameters." )
		
		sizer10.Add( self.spinCtrlHitRate, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer7.Add( sizer10, 1, wx.EXPAND, 5 )
		
		sizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelConsumable = wx.StaticText( self, wx.ID_ANY, u"Consumable:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelConsumable.Wrap( -1 )
		sizer11.Add( self.labelConsumable, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxConsumableChoices = [ u"Yes", u"No" ]
		self.comboBoxConsumable = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxConsumableChoices, 0 )
		self.comboBoxConsumable.SetSelection( 0 )
		self.comboBoxConsumable.SetToolTipString( u"Set to \"Yes\" to have item quantity deplete after using." )
		
		sizer11.Add( self.comboBoxConsumable, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelRecrHP = wx.StaticText( self, wx.ID_ANY, u"Recr HP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelRecrHP.Wrap( -1 )
		sizer11.Add( self.labelRecrHP, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlRecrHP = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		self.spinCtrlRecrHP.SetToolTipString( u"Amount of recovered HP. An odd value allows for creation of an attack item." )
		
		sizer11.Add( self.spinCtrlRecrHP, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelPDEF = wx.StaticText( self, wx.ID_ANY, u"PDEF-F:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPDEF.Wrap( -1 )
		sizer11.Add( self.labelPDEF, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlPDEF = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		self.spinCtrlPDEF.SetToolTipString( u"Coefficient indicating how much of the target's physical defense influences the effects. Set high for physical attack items." )
		
		sizer11.Add( self.spinCtrlPDEF, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer7.Add( sizer11, 1, wx.EXPAND, 5 )
		
		sizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelParameter = wx.StaticText( self, wx.ID_ANY, u"Parameter:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelParameter.Wrap( -1 )
		sizer12.Add( self.labelParameter, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxParameterChoices = [ u"(None)", u"MaxHP", u"MaxSP", u"STR", u"DEX", u"AGI", u"INT" ]
		self.comboBoxParameter = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxParameterChoices, 0 )
		self.comboBoxParameter.SetSelection( 0 )
		self.comboBoxParameter.SetToolTipString( u"Type of parameter that can be increased permanently." )
		
		sizer12.Add( self.comboBoxParameter, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelRecrSPPercent = wx.StaticText( self, wx.ID_ANY, u"Recr SP %:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelRecrSPPercent.Wrap( -1 )
		sizer12.Add( self.labelRecrSPPercent, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlRecrSP = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0 )
		self.spinCtrlRecrSP.SetToolTipString( u"Recovered SP, as percentage of max SP" )
		
		sizer12.Add( self.spinCtrlRecrSP, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelMDEF = wx.StaticText( self, wx.ID_ANY, u"MDEF-F:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMDEF.Wrap( -1 )
		sizer12.Add( self.labelMDEF, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlMDEF = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		self.spinCtrlMDEF.SetToolTipString( u"Coefficient indicating how much of the target's magic defense influences the effects. Set high for magical attack items." )
		
		sizer12.Add( self.spinCtrlMDEF, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer7.Add( sizer12, 1, wx.EXPAND, 5 )
		
		sizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelParameterInc = wx.StaticText( self, wx.ID_ANY, u"Param Inc:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelParameterInc.Wrap( -1 )
		sizer13.Add( self.labelParameterInc, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlParameterInc = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		self.spinCtrlParameterInc.SetToolTipString( u"Value of the parameter to increase by." )
		
		sizer13.Add( self.spinCtrlParameterInc, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelRecrSP = wx.StaticText( self, wx.ID_ANY, u"Recr SP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelRecrSP.Wrap( -1 )
		sizer13.Add( self.labelRecrSP, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlRecrSP = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		self.spinCtrlRecrSP.SetToolTipString( u"Amount of recovered SP. An odd value allows for creation of an attack item." )
		
		sizer13.Add( self.spinCtrlRecrSP, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelVariance = wx.StaticText( self, wx.ID_ANY, u"Variance:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelVariance.Wrap( -1 )
		sizer13.Add( self.labelVariance, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlVariance = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0 )
		self.spinCtrlVariance.SetToolTipString( u"Degree of fluctuation in final effect strength. The effect strength value varies only by this percentage. 15 is average." )
		
		sizer13.Add( self.spinCtrlVariance, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer7.Add( sizer13, 1, wx.EXPAND, 5 )
		
		sizer1.Add( sizer7, 1, wx.EXPAND, 5 )
		
		staticSizerItems.Add( sizer1, 60, wx.EXPAND, 5 )
		
		sizer2 = wx.BoxSizer( wx.VERTICAL )
		
		sizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelElements = wx.StaticText( self, wx.ID_ANY, u"Element:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelElements.Wrap( -1 )
		sizer14.Add( self.labelElements, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.labelStates = wx.StaticText( self, wx.ID_ANY, u"State Change:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelStates.Wrap( -1 )
		sizer14.Add( self.labelStates, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizer2.Add( sizer14, 0, wx.EXPAND, 5 )
		
		sizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		checkListElementsChoices = []
		self.checkListElements = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListElementsChoices, wx.LB_HSCROLL|wx.LB_NEEDED_SB|wx.CLIP_CHILDREN )
		self.checkListElements.SetToolTipString( u"Set the element attributes for the item. The effect strength varies according the their strengths/weaknesses." )
		
		sizer15.Add( self.checkListElements, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		checkListStatesChoices = []
		self.checkListStates = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListStatesChoices, wx.LB_NEEDED_SB|wx.CLIP_CHILDREN )
		self.checkListStates.SetToolTipString( u"Indicates the item's states set [+] and cleared [-] on the target. The success rate is determined by the target's strengths/weaknesses." )
		
		sizer15.Add( self.checkListStates, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer2.Add( sizer15, 1, wx.EXPAND, 5 )
		
		self.labelNotes = wx.StaticText( self, wx.ID_ANY, u"Notes:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelNotes.Wrap( -1 )
		sizer2.Add( self.labelNotes, 0, wx.ALL, 5 )
		
		self.textCtrlNotes = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.CLIP_CHILDREN )
		self.textCtrlNotes.SetToolTipString( u"Any user notes for this item. These notes can also be referenced via scripts." )
		
		sizer2.Add( self.textCtrlNotes, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		staticSizerItems.Add( sizer2, 40, wx.EXPAND, 5 )
		
		MainSizer.Add( staticSizerItems, 75, wx.EXPAND|wx.ALL, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		# Connect Events
		self.listBoxItems.Bind( wx.EVT_LISTBOX, self.listBoxItems_SelectionChanged )
		self.buttonMaximum.Bind( wx.EVT_BUTTON, self.buttonMaximum_Clicked )
		self.textCtrlName.Bind( wx.EVT_TEXT, self.textCtrlName_TextChanged )
		self.comboBoxIcon.Bind( wx.EVT_COMBOBOX, self.comboBoxIcon_SelectionChanged )
		self.extCtrlDescription.Bind( wx.EVT_TEXT, self.textCtrlDescription_TextChange )
		self.comboBoxScope.Bind( wx.EVT_CHOICE, self.comboBoxScope_SelectionChanged )
		self.comboBoxUserAnimation.Bind( wx.EVT_CHOICE, self.comboBoxUserAnimation_SelectionChanged )
		self.comboBoxMenuSE.Bind( wx.EVT_COMBOBOX, self.comboBoxMenuSE_SelectionChanged )
		self.comboBoxOccasion.Bind( wx.EVT_CHOICE, self.comboBoxOccasion_SelectionChanged )
		self.comboBoxTargetAnimation.Bind( wx.EVT_CHOICE, self.comboBoxTargetAnimation_SelectionChanged )
		self.comboBoxCommonEvent.Bind( wx.EVT_CHOICE, self.comboBoxCommonEvent_SelectionChanged )
		self.spinCtrlPrice.Bind( wx.EVT_SPINCTRL, self.spinCtrlPrice_ValueChanged )
		self.spinCtrlRecrHP.Bind( wx.EVT_SPINCTRL, self.spinCtrlRecrHPPercent_ValueChanged )
		self.spinCtrlHitRate.Bind( wx.EVT_SPINCTRL, self.spinCtrlHitRate_ValueChanged )
		self.comboBoxConsumable.Bind( wx.EVT_CHOICE, self.comboBoxConsumable_SelectionChanged )
		self.spinCtrlRecrHP.Bind( wx.EVT_SPINCTRL, self.spinCtrlRecrHP_ValueChanged )
		self.spinCtrlPDEF.Bind( wx.EVT_SPINCTRL, self.spinCtrlPDEF_ValueChanged )
		self.comboBoxParameter.Bind( wx.EVT_CHOICE, self.comboBoxParameter_SelectionChanged )
		self.spinCtrlRecrSP.Bind( wx.EVT_SPINCTRL, self.spinCtrlRecrSPPercent_ValueChanged )
		self.spinCtrlMDEF.Bind( wx.EVT_SPINCTRL, self.spinCtrlMDEF_ValueChanged )
		self.spinCtrlParameterInc.Bind( wx.EVT_SPINCTRL, self.spinCtrlParameterInc_ValueChanged )
		self.spinCtrlRecrSP.Bind( wx.EVT_SPINCTRL, self.spinCtrlRecrSP_ValueChanged )
		self.spinCtrlVariance.Bind( wx.EVT_SPINCTRL, self.spinCtrlVariance_ValueChanged )
		self.checkListElements.Bind( wx.EVT_CHECKLISTBOX, self.checkListElements_CheckChanged )
		self.checkListStates.Bind( wx.EVT_CHECKLISTBOX, self.checkListStates_CheckChanged )
		self.textCtrlNotes.Bind( wx.EVT_TEXT, self.textCtrlNotes_TextChanged )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def listBoxItems_SelectionChanged( self, event ):
		event.Skip()
	
	def buttonMaximum_Clicked( self, event ):
		event.Skip()
	
	def textCtrlName_TextChanged( self, event ):
		event.Skip()
	
	def comboBoxIcon_SelectionChanged( self, event ):
		event.Skip()
	
	def textCtrlDescription_TextChange( self, event ):
		event.Skip()
	
	def comboBoxScope_SelectionChanged( self, event ):
		event.Skip()
	
	def comboBoxUserAnimation_SelectionChanged( self, event ):
		event.Skip()
	
	def comboBoxMenuSE_SelectionChanged( self, event ):
		event.Skip()
	
	def comboBoxOccasion_SelectionChanged( self, event ):
		event.Skip()
	
	def comboBoxTargetAnimation_SelectionChanged( self, event ):
		event.Skip()
	
	def comboBoxCommonEvent_SelectionChanged( self, event ):
		event.Skip()
	
	def spinCtrlPrice_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlRecrHPPercent_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlHitRate_ValueChanged( self, event ):
		event.Skip()
	
	def comboBoxConsumable_SelectionChanged( self, event ):
		event.Skip()
	
	def spinCtrlRecrHP_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlPDEF_ValueChanged( self, event ):
		event.Skip()
	
	def comboBoxParameter_SelectionChanged( self, event ):
		event.Skip()
	
	def spinCtrlRecrSPPercent_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlMDEF_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlParameterInc_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlRecrSP_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlVariance_ValueChanged( self, event ):
		event.Skip()
	
	def checkListElements_CheckChanged( self, event ):
		event.Skip()
	
	def checkListStates_CheckChanged( self, event ):
		event.Skip()
	
	def textCtrlNotes_TextChanged( self, event ):
		event.Skip()
	

###########################################################################
## Class Weapons_Panel
###########################################################################

class Weapons_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		WeaponsListSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapWeapons = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/Weapons.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
		self.bitmapWeapons.SetMinSize( wx.Size( 150,26 ) )
		self.bitmapWeapons.SetMaxSize( wx.Size( 150,26 ) )
		
		WeaponsListSizer.Add( self.bitmapWeapons, 0, wx.ALL|wx.EXPAND, 5 )
		
		listBoxWeaponsChoices = []
		self.listBoxWeapons = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxWeaponsChoices, wx.LB_SINGLE|wx.CLIP_CHILDREN )
		self.listBoxWeapons.SetToolTipString( u"Select the item to edit" )
		
		WeaponsListSizer.Add( self.listBoxWeapons, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonMaximum = wx.Button( self, wx.ID_ANY, u"Change Maximum...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.buttonMaximum.SetToolTipString( u"Change the maximum of available items" )
		
		WeaponsListSizer.Add( self.buttonMaximum, 0, wx.ALL|wx.EXPAND, 5 )
		
		MainSizer.Add( WeaponsListSizer, 25, wx.EXPAND, 5 )
		
		staticSizerWeapons = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		sizer1 = wx.BoxSizer( wx.VERTICAL )
		
		sizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelName.Wrap( -1 )
		sizer3.Add( self.labelName, 1, wx.ALL, 5 )
		
		self.labelIcon = wx.StaticText( self, wx.ID_ANY, u"Icon:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelIcon.Wrap( -1 )
		sizer3.Add( self.labelIcon, 1, wx.ALL, 5 )
		
		sizer1.Add( sizer3, 0, wx.EXPAND, 5 )
		
		sizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textCtrlName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textCtrlName.SetToolTipString( u"The item name." )
		
		sizer4.Add( self.textCtrlName, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		comboBoxIconChoices = [ u"(None)" ]
		self.comboBoxIcon = wx.ComboBox( self, wx.ID_ANY, u"(None)", wx.DefaultPosition, wx.DefaultSize, comboBoxIconChoices, 0 )
		self.comboBoxIcon.SetToolTipString( u"The icon associated with the item" )
		
		sizer4.Add( self.comboBoxIcon, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer1.Add( sizer4, 0, wx.EXPAND, 5 )
		
		self.labelDescription = wx.StaticText( self, wx.ID_ANY, u"Description:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelDescription.Wrap( -1 )
		sizer1.Add( self.labelDescription, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.extCtrlDescription = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.extCtrlDescription.SetToolTipString( u"Comment displayed when the item is selected" )
		
		sizer1.Add( self.extCtrlDescription, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelUserAnimation = wx.StaticText( self, wx.ID_ANY, u"User Animation:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelUserAnimation.Wrap( -1 )
		sizer8.Add( self.labelUserAnimation, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxUserAnimationChoices = [ u"(None)" ]
		self.comboBoxUserAnimation = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxUserAnimationChoices, 0 )
		self.comboBoxUserAnimation.SetSelection( 0 )
		self.comboBoxUserAnimation.SetToolTipString( u"Animation displayed on the user when used in battle." )
		
		sizer8.Add( self.comboBoxUserAnimation, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizer6.Add( sizer8, 1, wx.EXPAND, 5 )
		
		sizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelTargetAnimation = wx.StaticText( self, wx.ID_ANY, u"Target Animation:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTargetAnimation.Wrap( -1 )
		sizer9.Add( self.labelTargetAnimation, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxOccasionChoices = [ u"(None)" ]
		self.comboBoxOccasion = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxOccasionChoices, 0 )
		self.comboBoxOccasion.SetSelection( 0 )
		self.comboBoxOccasion.SetToolTipString( u"Screen(s) where the item can be used." )
		
		sizer9.Add( self.comboBoxOccasion, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizer6.Add( sizer9, 1, wx.EXPAND, 5 )
		
		sizer1.Add( sizer6, 0, wx.EXPAND, 5 )
		
		sizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelPrice = wx.StaticText( self, wx.ID_ANY, u"Price:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPrice.Wrap( -1 )
		sizer10.Add( self.labelPrice, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlPrice = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 9999999, 0 )
		self.spinCtrlPrice.SetToolTipString( u"Recovered HP, as percentage of max HP" )
		
		sizer10.Add( self.spinCtrlPrice, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelStrPlus = wx.StaticText( self, wx.ID_ANY, u"STR+:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelStrPlus.Wrap( -1 )
		sizer10.Add( self.labelStrPlus, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlStrPlus = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -65535, 65535, 0 )
		self.spinCtrlStrPlus.SetToolTipString( u"Success rate in percentage of item use, not affected by target's parameters." )
		
		sizer10.Add( self.spinCtrlStrPlus, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer7.Add( sizer10, 1, wx.EXPAND, 5 )
		
		sizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelAtk = wx.StaticText( self, wx.ID_ANY, u"ATK:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAtk.Wrap( -1 )
		sizer11.Add( self.labelAtk, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlAtk = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -65535, 65535, 0 )
		self.spinCtrlAtk.SetToolTipString( u"Amount of recovered HP. An odd value allows for creation of an attack item." )
		
		sizer11.Add( self.spinCtrlAtk, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelDexPlus = wx.StaticText( self, wx.ID_ANY, u"DEX+:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelDexPlus.Wrap( -1 )
		sizer11.Add( self.labelDexPlus, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlDexPlus = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -65535, 65535, 0 )
		self.spinCtrlDexPlus.SetToolTipString( u"Coefficient indicating how much of the target's physical defense influences the effects. Set high for physical attack items." )
		
		sizer11.Add( self.spinCtrlDexPlus, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer7.Add( sizer11, 1, wx.EXPAND, 5 )
		
		sizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelPdef = wx.StaticText( self, wx.ID_ANY, u"PDEF:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPdef.Wrap( -1 )
		sizer12.Add( self.labelPdef, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlPdef = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -65535, 65535, 0 )
		self.spinCtrlPdef.SetToolTipString( u"Recovered SP, as percentage of max SP" )
		
		sizer12.Add( self.spinCtrlPdef, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelAgiPlus = wx.StaticText( self, wx.ID_ANY, u"AGI+:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAgiPlus.Wrap( -1 )
		sizer12.Add( self.labelAgiPlus, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlAgiPlus = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -65535, 65535, 0 )
		self.spinCtrlAgiPlus.SetToolTipString( u"Coefficient indicating how much of the target's magic defense influences the effects. Set high for magical attack items." )
		
		sizer12.Add( self.spinCtrlAgiPlus, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer7.Add( sizer12, 1, wx.EXPAND, 5 )
		
		sizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelMdef = wx.StaticText( self, wx.ID_ANY, u"MDEF:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMdef.Wrap( -1 )
		sizer13.Add( self.labelMdef, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlMdef = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -65535, 65535, 0 )
		self.spinCtrlMdef.SetToolTipString( u"Amount of recovered SP. An odd value allows for creation of an attack item." )
		
		sizer13.Add( self.spinCtrlMdef, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelIntPlus = wx.StaticText( self, wx.ID_ANY, u"INT+:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelIntPlus.Wrap( -1 )
		sizer13.Add( self.labelIntPlus, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlIntPlus = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -65535, 65535, 0 )
		self.spinCtrlIntPlus.SetToolTipString( u"Degree of fluctuation in final effect strength. The effect strength value varies only by this percentage. 15 is average." )
		
		sizer13.Add( self.spinCtrlIntPlus, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer7.Add( sizer13, 1, wx.EXPAND, 5 )
		
		sizer1.Add( sizer7, 1, wx.EXPAND, 5 )
		
		staticSizerWeapons.Add( sizer1, 60, wx.EXPAND, 5 )
		
		sizer2 = wx.BoxSizer( wx.VERTICAL )
		
		sizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelElements = wx.StaticText( self, wx.ID_ANY, u"Element:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelElements.Wrap( -1 )
		sizer14.Add( self.labelElements, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.labelStates = wx.StaticText( self, wx.ID_ANY, u"State Change:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelStates.Wrap( -1 )
		sizer14.Add( self.labelStates, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizer2.Add( sizer14, 0, wx.EXPAND, 5 )
		
		sizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		checkListElementsChoices = []
		self.checkListElements = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListElementsChoices, wx.LB_HSCROLL|wx.LB_NEEDED_SB|wx.CLIP_CHILDREN )
		self.checkListElements.SetToolTipString( u"Set the element attributes for the item. The effect strength varies according the their strengths/weaknesses." )
		
		sizer15.Add( self.checkListElements, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		checkListStatesChoices = []
		self.checkListStates = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListStatesChoices, wx.LB_NEEDED_SB|wx.CLIP_CHILDREN )
		self.checkListStates.SetToolTipString( u"Indicates the item's states set [+] and cleared [-] on the target. The success rate is determined by the target's strengths/weaknesses." )
		
		sizer15.Add( self.checkListStates, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer2.Add( sizer15, 1, wx.EXPAND, 5 )
		
		self.labelNotes = wx.StaticText( self, wx.ID_ANY, u"Notes:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelNotes.Wrap( -1 )
		sizer2.Add( self.labelNotes, 0, wx.ALL, 5 )
		
		self.textCtrlNotes = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.CLIP_CHILDREN )
		self.textCtrlNotes.SetToolTipString( u"Any user notes for this item. These notes can also be referenced via scripts." )
		
		sizer2.Add( self.textCtrlNotes, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		staticSizerWeapons.Add( sizer2, 40, wx.EXPAND, 5 )
		
		MainSizer.Add( staticSizerWeapons, 75, wx.EXPAND|wx.ALL, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		# Connect Events
		self.listBoxWeapons.Bind( wx.EVT_LISTBOX, self.listBoxWeapons_SelectionChanged )
		self.buttonMaximum.Bind( wx.EVT_BUTTON, self.buttonMaximum_Clicked )
		self.textCtrlName.Bind( wx.EVT_TEXT, self.textCtrlName_TextChanged )
		self.comboBoxIcon.Bind( wx.EVT_COMBOBOX, self.comboBoxIcon_SelectionChanged )
		self.extCtrlDescription.Bind( wx.EVT_TEXT, self.textCtrlDescription_TextChange )
		self.comboBoxUserAnimation.Bind( wx.EVT_CHOICE, self.comboBoxUserAnimation_SelectionChanged )
		self.comboBoxOccasion.Bind( wx.EVT_CHOICE, self.comboBoxOccasion_SelectionChanged )
		self.spinCtrlPrice.Bind( wx.EVT_SPINCTRL, self.spinCtrlPrice_ValueChanged )
		self.spinCtrlStrPlus.Bind( wx.EVT_SPINCTRL, self.spinCtrlStrPlus_ValueChanged )
		self.spinCtrlAtk.Bind( wx.EVT_SPINCTRL, self.spinCtrlAtk_ValueChanged )
		self.spinCtrlDexPlus.Bind( wx.EVT_SPINCTRL, self.spinCtrlDexPlus_ValueChanged )
		self.spinCtrlPdef.Bind( wx.EVT_SPINCTRL, self.spinCtrlPdef_ValueChanged )
		self.spinCtrlAgiPlus.Bind( wx.EVT_SPINCTRL, self.spinCtrlAgiPlus_ValueChanged )
		self.spinCtrlMdef.Bind( wx.EVT_SPINCTRL, self.spinCtrlMdef_ValueChanged )
		self.spinCtrlIntPlus.Bind( wx.EVT_SPINCTRL, self.spinCtrlIntPlus_ValueChanged )
		self.checkListElements.Bind( wx.EVT_CHECKLISTBOX, self.checkListElements_CheckChanged )
		self.checkListStates.Bind( wx.EVT_CHECKLISTBOX, self.checkListStates_CheckChanged )
		self.textCtrlNotes.Bind( wx.EVT_TEXT, self.textCtrlNotes_TextChanged )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def listBoxWeapons_SelectionChanged( self, event ):
		event.Skip()
	
	def buttonMaximum_Clicked( self, event ):
		event.Skip()
	
	def textCtrlName_TextChanged( self, event ):
		event.Skip()
	
	def comboBoxIcon_SelectionChanged( self, event ):
		event.Skip()
	
	def textCtrlDescription_TextChange( self, event ):
		event.Skip()
	
	def comboBoxUserAnimation_SelectionChanged( self, event ):
		event.Skip()
	
	def comboBoxOccasion_SelectionChanged( self, event ):
		event.Skip()
	
	def spinCtrlPrice_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlStrPlus_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlAtk_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlDexPlus_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlPdef_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlAgiPlus_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlMdef_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlIntPlus_ValueChanged( self, event ):
		event.Skip()
	
	def checkListElements_CheckChanged( self, event ):
		event.Skip()
	
	def checkListStates_CheckChanged( self, event ):
		event.Skip()
	
	def textCtrlNotes_TextChanged( self, event ):
		event.Skip()
	

###########################################################################
## Class Armors_Panel
###########################################################################

class Armors_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		ArmorsListSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapArmors = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/Armors.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
		self.bitmapArmors.SetMinSize( wx.Size( 150,26 ) )
		self.bitmapArmors.SetMaxSize( wx.Size( 150,26 ) )
		
		ArmorsListSizer.Add( self.bitmapArmors, 0, wx.ALL|wx.EXPAND, 5 )
		
		listBoxArmorsChoices = []
		self.listBoxArmors = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxArmorsChoices, wx.LB_SINGLE|wx.CLIP_CHILDREN )
		self.listBoxArmors.SetToolTipString( u"Select the item to edit" )
		
		ArmorsListSizer.Add( self.listBoxArmors, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonMaximum = wx.Button( self, wx.ID_ANY, u"Change Maximum...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.buttonMaximum.SetToolTipString( u"Change the maximum of available items" )
		
		ArmorsListSizer.Add( self.buttonMaximum, 0, wx.ALL|wx.EXPAND, 5 )
		
		MainSizer.Add( ArmorsListSizer, 25, wx.EXPAND, 5 )
		
		staticSizerArmors = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		sizer1 = wx.BoxSizer( wx.VERTICAL )
		
		sizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelName.Wrap( -1 )
		sizer3.Add( self.labelName, 1, wx.ALL, 5 )
		
		self.labelIcon = wx.StaticText( self, wx.ID_ANY, u"Icon:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelIcon.Wrap( -1 )
		sizer3.Add( self.labelIcon, 1, wx.ALL, 5 )
		
		sizer1.Add( sizer3, 0, wx.EXPAND, 5 )
		
		sizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textCtrlName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textCtrlName.SetToolTipString( u"The item name." )
		
		sizer4.Add( self.textCtrlName, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		comboBoxIconChoices = [ u"(None)" ]
		self.comboBoxIcon = wx.ComboBox( self, wx.ID_ANY, u"(None)", wx.DefaultPosition, wx.DefaultSize, comboBoxIconChoices, 0 )
		self.comboBoxIcon.SetToolTipString( u"The icon associated with the item" )
		
		sizer4.Add( self.comboBoxIcon, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer1.Add( sizer4, 0, wx.EXPAND, 5 )
		
		self.labelDescription = wx.StaticText( self, wx.ID_ANY, u"Description:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelDescription.Wrap( -1 )
		sizer1.Add( self.labelDescription, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.extCtrlDescription = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.extCtrlDescription.SetToolTipString( u"Comment displayed when the item is selected" )
		
		sizer1.Add( self.extCtrlDescription, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelKindAnimation = wx.StaticText( self, wx.ID_ANY, u"Kind:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelKindAnimation.Wrap( -1 )
		sizer8.Add( self.labelKindAnimation, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxKindChoices = [ u"Shield", u"Helmet", u"Body Armor", u"Accessory" ]
		self.comboBoxKind = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxKindChoices, 0 )
		self.comboBoxKind.SetSelection( 0 )
		self.comboBoxKind.SetToolTipString( u"Animation displayed on the user when used in battle." )
		
		sizer8.Add( self.comboBoxKind, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizer6.Add( sizer8, 1, wx.EXPAND, 5 )
		
		sizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelAutoState = wx.StaticText( self, wx.ID_ANY, u"Auto State:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAutoState.Wrap( -1 )
		sizer9.Add( self.labelAutoState, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxAutoStateChoices = [ u"(None)" ]
		self.comboBoxAutoState = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxAutoStateChoices, 0 )
		self.comboBoxAutoState.SetSelection( 0 )
		self.comboBoxAutoState.SetToolTipString( u"Screen(s) where the item can be used." )
		
		sizer9.Add( self.comboBoxAutoState, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizer6.Add( sizer9, 1, wx.EXPAND, 5 )
		
		sizer1.Add( sizer6, 0, wx.EXPAND, 5 )
		
		sizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelPrice = wx.StaticText( self, wx.ID_ANY, u"Price:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPrice.Wrap( -1 )
		sizer10.Add( self.labelPrice, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlPrice = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 9999999, 0 )
		self.spinCtrlPrice.SetToolTipString( u"Recovered HP, as percentage of max HP" )
		
		sizer10.Add( self.spinCtrlPrice, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelStrPlus = wx.StaticText( self, wx.ID_ANY, u"STR+:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelStrPlus.Wrap( -1 )
		sizer10.Add( self.labelStrPlus, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlStrPlus = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -65535, 65535, 0 )
		self.spinCtrlStrPlus.SetToolTipString( u"Success rate in percentage of item use, not affected by target's parameters." )
		
		sizer10.Add( self.spinCtrlStrPlus, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer7.Add( sizer10, 1, wx.EXPAND, 5 )
		
		sizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelPdef = wx.StaticText( self, wx.ID_ANY, u"PDEF:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPdef.Wrap( -1 )
		sizer11.Add( self.labelPdef, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlPdef = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -65535, 65535, 0 )
		self.spinCtrlPdef.SetToolTipString( u"Amount of recovered HP. An odd value allows for creation of an attack item." )
		
		sizer11.Add( self.spinCtrlPdef, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelDexPlus = wx.StaticText( self, wx.ID_ANY, u"DEX+:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelDexPlus.Wrap( -1 )
		sizer11.Add( self.labelDexPlus, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlDexPlus = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -65535, 65535, 0 )
		self.spinCtrlDexPlus.SetToolTipString( u"Coefficient indicating how much of the target's physical defense influences the effects. Set high for physical attack items." )
		
		sizer11.Add( self.spinCtrlDexPlus, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer7.Add( sizer11, 1, wx.EXPAND, 5 )
		
		sizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelMdef = wx.StaticText( self, wx.ID_ANY, u"MDEF:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMdef.Wrap( -1 )
		sizer12.Add( self.labelMdef, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlMdef = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -65535, 65535, 0 )
		self.spinCtrlMdef.SetToolTipString( u"Recovered SP, as percentage of max SP" )
		
		sizer12.Add( self.spinCtrlMdef, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelAgiPlus = wx.StaticText( self, wx.ID_ANY, u"AGI+:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAgiPlus.Wrap( -1 )
		sizer12.Add( self.labelAgiPlus, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlAgiPlus = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -65535, 65535, 0 )
		self.spinCtrlAgiPlus.SetToolTipString( u"Coefficient indicating how much of the target's magic defense influences the effects. Set high for magical attack items." )
		
		sizer12.Add( self.spinCtrlAgiPlus, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer7.Add( sizer12, 1, wx.EXPAND, 5 )
		
		sizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelEva = wx.StaticText( self, wx.ID_ANY, u"EVA:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelEva.Wrap( -1 )
		sizer13.Add( self.labelEva, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlEva = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -65535, 65535, 0 )
		self.spinCtrlEva.SetToolTipString( u"Amount of recovered SP. An odd value allows for creation of an attack item." )
		
		sizer13.Add( self.spinCtrlEva, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelIntPlus = wx.StaticText( self, wx.ID_ANY, u"INT+:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelIntPlus.Wrap( -1 )
		sizer13.Add( self.labelIntPlus, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlIntPlus = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -65535, 65535, 0 )
		self.spinCtrlIntPlus.SetToolTipString( u"Degree of fluctuation in final effect strength. The effect strength value varies only by this percentage. 15 is average." )
		
		sizer13.Add( self.spinCtrlIntPlus, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer7.Add( sizer13, 1, wx.EXPAND, 5 )
		
		sizer1.Add( sizer7, 1, wx.EXPAND, 5 )
		
		staticSizerArmors.Add( sizer1, 60, wx.EXPAND, 5 )
		
		sizer2 = wx.BoxSizer( wx.VERTICAL )
		
		sizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelElements = wx.StaticText( self, wx.ID_ANY, u"Element Defense:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelElements.Wrap( -1 )
		sizer14.Add( self.labelElements, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.labelStates = wx.StaticText( self, wx.ID_ANY, u"State Defense:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelStates.Wrap( -1 )
		sizer14.Add( self.labelStates, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizer2.Add( sizer14, 0, wx.EXPAND, 5 )
		
		sizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		checkListElementsChoices = []
		self.checkListElements = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListElementsChoices, wx.LB_HSCROLL|wx.LB_NEEDED_SB|wx.CLIP_CHILDREN )
		self.checkListElements.SetToolTipString( u"Set the element attributes for the item. The effect strength varies according the their strengths/weaknesses." )
		
		sizer15.Add( self.checkListElements, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		checkListStatesChoices = []
		self.checkListStates = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListStatesChoices, wx.LB_NEEDED_SB|wx.CLIP_CHILDREN )
		self.checkListStates.SetToolTipString( u"Indicates the item's states set [+] and cleared [-] on the target. The success rate is determined by the target's strengths/weaknesses." )
		
		sizer15.Add( self.checkListStates, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer2.Add( sizer15, 1, wx.EXPAND, 5 )
		
		self.labelNotes = wx.StaticText( self, wx.ID_ANY, u"Notes:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelNotes.Wrap( -1 )
		sizer2.Add( self.labelNotes, 0, wx.ALL, 5 )
		
		self.textCtrlNotes = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.CLIP_CHILDREN )
		self.textCtrlNotes.SetToolTipString( u"Any user notes for this item. These notes can also be referenced via scripts." )
		
		sizer2.Add( self.textCtrlNotes, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		staticSizerArmors.Add( sizer2, 40, wx.EXPAND, 5 )
		
		MainSizer.Add( staticSizerArmors, 75, wx.EXPAND|wx.ALL, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		# Connect Events
		self.listBoxArmors.Bind( wx.EVT_LISTBOX, self.listBoxWeapons_SelectionChanged )
		self.buttonMaximum.Bind( wx.EVT_BUTTON, self.buttonMaximum_Clicked )
		self.textCtrlName.Bind( wx.EVT_TEXT, self.textCtrlName_TextChanged )
		self.comboBoxIcon.Bind( wx.EVT_COMBOBOX, self.comboBoxIcon_SelectionChanged )
		self.extCtrlDescription.Bind( wx.EVT_TEXT, self.textCtrlDescription_TextChange )
		self.comboBoxKind.Bind( wx.EVT_CHOICE, self.comboBoxKind_SelectionChanged )
		self.comboBoxAutoState.Bind( wx.EVT_CHOICE, self.comboBoxAutoState_SelectionChanged )
		self.spinCtrlPrice.Bind( wx.EVT_SPINCTRL, self.spinCtrlPrice_ValueChanged )
		self.spinCtrlStrPlus.Bind( wx.EVT_SPINCTRL, self.spinCtrlStrPlus_ValueChanged )
		self.spinCtrlPdef.Bind( wx.EVT_SPINCTRL, self.spinCtrlPdef_ValueChanged )
		self.spinCtrlDexPlus.Bind( wx.EVT_SPINCTRL, self.spinCtrlDexPlus_ValueChanged )
		self.spinCtrlMdef.Bind( wx.EVT_SPINCTRL, self.spinCtrlMdef_ValueChanged )
		self.spinCtrlAgiPlus.Bind( wx.EVT_SPINCTRL, self.spinCtrlAgiPlus_ValueChanged )
		self.spinCtrlEva.Bind( wx.EVT_SPINCTRL, self.spinCtrlEva_ValueChanged )
		self.spinCtrlIntPlus.Bind( wx.EVT_SPINCTRL, self.spinCtrlIntPlus_ValueChanged )
		self.checkListElements.Bind( wx.EVT_CHECKLISTBOX, self.checkListElements_CheckChanged )
		self.checkListStates.Bind( wx.EVT_CHECKLISTBOX, self.checkListStates_CheckChanged )
		self.textCtrlNotes.Bind( wx.EVT_TEXT, self.textCtrlNotes_TextChanged )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def listBoxWeapons_SelectionChanged( self, event ):
		event.Skip()
	
	def buttonMaximum_Clicked( self, event ):
		event.Skip()
	
	def textCtrlName_TextChanged( self, event ):
		event.Skip()
	
	def comboBoxIcon_SelectionChanged( self, event ):
		event.Skip()
	
	def textCtrlDescription_TextChange( self, event ):
		event.Skip()
	
	def comboBoxKind_SelectionChanged( self, event ):
		event.Skip()
	
	def comboBoxAutoState_SelectionChanged( self, event ):
		event.Skip()
	
	def spinCtrlPrice_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlStrPlus_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlPdef_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlDexPlus_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlMdef_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlAgiPlus_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlEva_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlIntPlus_ValueChanged( self, event ):
		event.Skip()
	
	def checkListElements_CheckChanged( self, event ):
		event.Skip()
	
	def checkListStates_CheckChanged( self, event ):
		event.Skip()
	
	def textCtrlNotes_TextChanged( self, event ):
		event.Skip()
	

###########################################################################
## Class Enemies_Panel
###########################################################################

class Enemies_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		EnemiesListSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapEnemies = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/Enemies.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
		self.bitmapEnemies.SetMinSize( wx.Size( 150,26 ) )
		self.bitmapEnemies.SetMaxSize( wx.Size( 150,26 ) )
		
		EnemiesListSizer.Add( self.bitmapEnemies, 0, wx.ALL|wx.EXPAND, 5 )
		
		listBoxEnemiesChoices = []
		self.listBoxEnemies = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxEnemiesChoices, wx.LB_SINGLE|wx.CLIP_CHILDREN )
		self.listBoxEnemies.SetToolTipString( u"Select the item to edit" )
		
		EnemiesListSizer.Add( self.listBoxEnemies, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonMaximum = wx.Button( self, wx.ID_ANY, u"Change Maximum...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.buttonMaximum.SetToolTipString( u"Change the maximum of available items" )
		
		EnemiesListSizer.Add( self.buttonMaximum, 0, wx.ALL|wx.EXPAND, 5 )
		
		MainSizer.Add( EnemiesListSizer, 25, wx.EXPAND, 5 )
		
		staticSizerEnemies = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		sizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelName.Wrap( -1 )
		sizer2.Add( self.labelName, 0, wx.ALL, 5 )
		
		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer2.Add( self.m_textCtrl21, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelBattlerGraphic = wx.StaticText( self, wx.ID_ANY, u"Battler Graphic:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBattlerGraphic.Wrap( -1 )
		sizer2.Add( self.labelBattlerGraphic, 0, wx.ALL, 5 )
		
		self.bitmapBattlerGraphic = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/Ghost.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER )
		sizer2.Add( self.bitmapBattlerGraphic, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelAttackAnimation = wx.StaticText( self, wx.ID_ANY, u"Attack Animation:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAttackAnimation.Wrap( -1 )
		sizer2.Add( self.labelAttackAnimation, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxAttackAnimationChoices = [ u"(None)" ]
		self.comboBoxAttackAnimation = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxAttackAnimationChoices, 0 )
		self.comboBoxAttackAnimation.SetSelection( 0 )
		sizer2.Add( self.comboBoxAttackAnimation, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelExp = wx.StaticText( self, wx.ID_ANY, u"EXP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelExp.Wrap( -1 )
		sizer5.Add( self.labelExp, 1, wx.ALL, 5 )
		
		self.labelGold = wx.StaticText( self, wx.ID_ANY, u"Gold:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelGold.Wrap( -1 )
		sizer5.Add( self.labelGold, 1, wx.ALL, 5 )
		
		sizer2.Add( sizer5, 0, wx.EXPAND, 5 )
		
		sizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.spinCtrlExp = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer6.Add( self.spinCtrlExp, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.spinCtrlGold = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer6.Add( self.spinCtrlGold, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer2.Add( sizer6, 0, wx.EXPAND, 5 )
		
		sizer1.Add( sizer2, 30, wx.EXPAND, 5 )
		
		sizer3 = wx.BoxSizer( wx.VERTICAL )
		
		sizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelMaxHP = wx.StaticText( self, wx.ID_ANY, u"MaxHP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMaxHP.Wrap( -1 )
		sizer10.Add( self.labelMaxHP, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlMaxHP = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer10.Add( self.spinCtrlMaxHP, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelStr = wx.StaticText( self, wx.ID_ANY, u"STR:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelStr.Wrap( -1 )
		sizer10.Add( self.labelStr, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlStr = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer10.Add( self.spinCtrlStr, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelAgi = wx.StaticText( self, wx.ID_ANY, u"AGI:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAgi.Wrap( -1 )
		sizer10.Add( self.labelAgi, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlAgi = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer10.Add( self.spinCtrlAgi, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelAtk = wx.StaticText( self, wx.ID_ANY, u"ATK:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAtk.Wrap( -1 )
		sizer10.Add( self.labelAtk, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlAtk = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer10.Add( self.spinCtrlAtk, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelMdef = wx.StaticText( self, wx.ID_ANY, u"MDEF:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMdef.Wrap( -1 )
		sizer10.Add( self.labelMdef, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlMdef = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer10.Add( self.spinCtrlMdef, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizer7.Add( sizer10, 1, wx.EXPAND, 5 )
		
		sizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelMaxSP = wx.StaticText( self, wx.ID_ANY, u"MaxSP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMaxSP.Wrap( -1 )
		sizer11.Add( self.labelMaxSP, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlMaxSP = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer11.Add( self.spinCtrlMaxSP, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelDex = wx.StaticText( self, wx.ID_ANY, u"DEX:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelDex.Wrap( -1 )
		sizer11.Add( self.labelDex, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlDex = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer11.Add( self.spinCtrlDex, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelInt = wx.StaticText( self, wx.ID_ANY, u"INT:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelInt.Wrap( -1 )
		sizer11.Add( self.labelInt, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlIni = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer11.Add( self.spinCtrlIni, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelPdef = wx.StaticText( self, wx.ID_ANY, u"PDEF:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPdef.Wrap( -1 )
		sizer11.Add( self.labelPdef, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlPdef = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer11.Add( self.spinCtrlPdef, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelEva = wx.StaticText( self, wx.ID_ANY, u"EVA:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelEva.Wrap( -1 )
		sizer11.Add( self.labelEva, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlEva = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer11.Add( self.spinCtrlEva, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizer7.Add( sizer11, 1, wx.EXPAND, 5 )
		
		sizer3.Add( sizer7, 1, wx.EXPAND, 5 )
		
		self.labelTargetAnimation = wx.StaticText( self, wx.ID_ANY, u"Target Animation:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTargetAnimation.Wrap( -1 )
		sizer3.Add( self.labelTargetAnimation, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxTargetAnimationChoices = [ u"(None)" ]
		self.comboBoxTargetAnimation = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxTargetAnimationChoices, 0 )
		self.comboBoxTargetAnimation.SetSelection( 0 )
		sizer3.Add( self.comboBoxTargetAnimation, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelTreasure = wx.StaticText( self, wx.ID_ANY, u"Treasure:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTreasure.Wrap( -1 )
		sizer3.Add( self.labelTreasure, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxTreasureChoices = [ u"(None)" ]
		self.comboBoxTreasure = wx.ComboBox( self, wx.ID_ANY, u"(None)", wx.DefaultPosition, wx.DefaultSize, comboBoxTreasureChoices, 0 )
		sizer3.Add( self.comboBoxTreasure, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizer1.Add( sizer3, 30, wx.EXPAND, 5 )
		
		sizer4 = wx.BoxSizer( wx.VERTICAL )
		
		sizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelElements = wx.StaticText( self, wx.ID_ANY, u"Element Efficiency:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelElements.Wrap( -1 )
		sizer8.Add( self.labelElements, 1, wx.ALL, 5 )
		
		self.labelStates = wx.StaticText( self, wx.ID_ANY, u"State Efficiency:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelStates.Wrap( -1 )
		sizer8.Add( self.labelStates, 1, wx.ALL, 5 )
		
		sizer4.Add( sizer8, 0, wx.EXPAND, 5 )
		
		sizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		checkListElementsChoices = []
		self.checkListElements = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListElementsChoices, 0 )
		sizer9.Add( self.checkListElements, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		checkListStatesChoices = []
		self.checkListStates = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListStatesChoices, 0 )
		sizer9.Add( self.checkListStates, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer4.Add( sizer9, 1, wx.EXPAND, 5 )
		
		self.labelNotes = wx.StaticText( self, wx.ID_ANY, u"Notes:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelNotes.Wrap( -1 )
		sizer4.Add( self.labelNotes, 0, wx.ALL, 5 )
		
		self.textCtrlNotes = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.CLIP_CHILDREN )
		self.textCtrlNotes.SetToolTipString( u"Any user notes for this item. These notes can also be referenced via scripts." )
		
		sizer4.Add( self.textCtrlNotes, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizer1.Add( sizer4, 40, wx.EXPAND, 5 )
		
		staticSizerEnemies.Add( sizer1, 70, wx.EXPAND, 5 )
		
		self.labelAction = wx.StaticText( self, wx.ID_ANY, u"Action:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAction.Wrap( -1 )
		staticSizerEnemies.Add( self.labelAction, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.listCtrlActions = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON|wx.LC_REPORT )
		staticSizerEnemies.Add( self.listCtrlActions, 30, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		MainSizer.Add( staticSizerEnemies, 75, wx.EXPAND|wx.ALL, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		# Connect Events
		self.listBoxEnemies.Bind( wx.EVT_LISTBOX, self.listBoxEnemies_SelectionChanged )
		self.buttonMaximum.Bind( wx.EVT_BUTTON, self.buttonMaximum_Clicked )
		self.m_textCtrl21.Bind( wx.EVT_TEXT, self.textCtrlName_ValueChanged )
		self.bitmapBattlerGraphic.Bind( wx.EVT_LEFT_DCLICK, self.bitmapGraphic_DoubleClick )
		self.comboBoxAttackAnimation.Bind( wx.EVT_CHOICE, self.comboBoxAttackAnimation_SelectionChanged )
		self.spinCtrlExp.Bind( wx.EVT_SPINCTRL, self.spinCtrlExp_ValueChanged )
		self.spinCtrlGold.Bind( wx.EVT_SPINCTRL, self.spinCtrlGold_ValueChanged )
		self.spinCtrlMaxHP.Bind( wx.EVT_SPINCTRL, self.spinCtrlMaxHP_ValueChanged )
		self.spinCtrlStr.Bind( wx.EVT_SPINCTRL, self.spinCtrlStr_ValueChanged )
		self.spinCtrlAgi.Bind( wx.EVT_SPINCTRL, self.spinCtrlAgi_ValueChanged )
		self.spinCtrlAtk.Bind( wx.EVT_SPINCTRL, self.spinCtrlAtk_ValueChanged )
		self.spinCtrlMdef.Bind( wx.EVT_SPINCTRL, self.spinCtrlMdef_ValueChanged )
		self.spinCtrlMaxSP.Bind( wx.EVT_SPINCTRL, self.spinCtrlMaxSP_ValueChanged )
		self.spinCtrlDex.Bind( wx.EVT_SPINCTRL, self.spinCtrlDex_ValueChanged )
		self.spinCtrlIni.Bind( wx.EVT_SPINCTRL, self.spinCtrlInt_ValueChanged )
		self.spinCtrlPdef.Bind( wx.EVT_SPINCTRL, self.spinCtrlPdef_ValueChanged )
		self.spinCtrlEva.Bind( wx.EVT_SPINCTRL, self.spinCtrlEva_ValueChanged )
		self.comboBoxTargetAnimation.Bind( wx.EVT_CHOICE, self.comboBoxTargetAnimation_ValueChanged )
		self.comboBoxTreasure.Bind( wx.EVT_COMBOBOX, self.comboBoxTreasure_ValueChanged )
		self.checkListElements.Bind( wx.EVT_CHECKLISTBOX, self.checkListElements_ValueChanged )
		self.checkListStates.Bind( wx.EVT_CHECKLISTBOX, self.checkListStates_ValueChanged )
		self.textCtrlNotes.Bind( wx.EVT_TEXT, self.textCtrlNotes_TextChanged )
		self.listCtrlActions.Bind( wx.EVT_LEFT_DCLICK, self.listCtrlAction_DoubleClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def listBoxEnemies_SelectionChanged( self, event ):
		event.Skip()
	
	def buttonMaximum_Clicked( self, event ):
		event.Skip()
	
	def textCtrlName_ValueChanged( self, event ):
		event.Skip()
	
	def bitmapGraphic_DoubleClick( self, event ):
		event.Skip()
	
	def comboBoxAttackAnimation_SelectionChanged( self, event ):
		event.Skip()
	
	def spinCtrlExp_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlGold_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlMaxHP_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlStr_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlAgi_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlAtk_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlMdef_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlMaxSP_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlDex_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlInt_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlPdef_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlEva_ValueChanged( self, event ):
		event.Skip()
	
	def comboBoxTargetAnimation_ValueChanged( self, event ):
		event.Skip()
	
	def comboBoxTreasure_ValueChanged( self, event ):
		event.Skip()
	
	def checkListElements_ValueChanged( self, event ):
		event.Skip()
	
	def checkListStates_ValueChanged( self, event ):
		event.Skip()
	
	def textCtrlNotes_TextChanged( self, event ):
		event.Skip()
	
	def listCtrlAction_DoubleClick( self, event ):
		event.Skip()
	

###########################################################################
## Class Troops_Panel
###########################################################################

class Troops_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		TroopsListSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapTroops = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/Troops.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
		self.bitmapTroops.SetMinSize( wx.Size( 150,26 ) )
		self.bitmapTroops.SetMaxSize( wx.Size( 150,26 ) )
		
		TroopsListSizer.Add( self.bitmapTroops, 0, wx.ALL|wx.EXPAND, 5 )
		
		listBoxTroopsChoices = []
		self.listBoxTroops = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxTroopsChoices, wx.LB_SINGLE|wx.CLIP_CHILDREN )
		self.listBoxTroops.SetToolTipString( u"Select the item to edit" )
		
		TroopsListSizer.Add( self.listBoxTroops, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonMaximum = wx.Button( self, wx.ID_ANY, u"Change Maximum...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.buttonMaximum.SetToolTipString( u"Change the maximum of available items" )
		
		TroopsListSizer.Add( self.buttonMaximum, 0, wx.ALL|wx.EXPAND, 5 )
		
		MainSizer.Add( TroopsListSizer, 25, wx.EXPAND, 5 )
		
		staticSizerEnemies = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelName.Wrap( -1 )
		staticSizerEnemies.Add( self.labelName, 0, wx.ALL, 5 )
		
		sizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textCtrlName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer1.Add( self.textCtrlName, 40, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonAutoname = wx.Button( self, wx.ID_ANY, u"Autoname", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		sizer1.Add( self.buttonAutoname, 20, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonBattleback = wx.Button( self, wx.ID_ANY, u"[ED] Battleback...", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		sizer1.Add( self.buttonBattleback, 20, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonBattleTest = wx.Button( self, wx.ID_ANY, u"Battle Test...", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		sizer1.Add( self.buttonBattleTest, 20, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		staticSizerEnemies.Add( sizer1, 0, wx.EXPAND, 5 )
		
		sizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bitmapTroopLayout = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/Battleback.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER )
		sizer2.Add( self.bitmapTroopLayout, 70, wx.ALL|wx.EXPAND, 5 )
		
		sizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonAddEnemy = wx.Button( self, wx.ID_ANY, u"<", wx.DefaultPosition, wx.Size( 23,-1 ), 0 )
		sizer4.Add( self.buttonAddEnemy, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.buttonRemoveEnemy = wx.Button( self, wx.ID_ANY, u">", wx.DefaultPosition, wx.Size( 23,-1 ), 0 )
		sizer4.Add( self.buttonRemoveEnemy, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.buttonClearTroops = wx.Button( self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.Size( 23,-1 ), 0 )
		sizer4.Add( self.buttonClearTroops, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.buttonAlignTroops = wx.Button( self, wx.ID_ANY, u"A", wx.DefaultPosition, wx.Size( 23,-1 ), 0 )
		sizer4.Add( self.buttonAlignTroops, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sizer2.Add( sizer4, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		listBoxEnemiesChoices = []
		self.listBoxEnemies = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxEnemiesChoices, 0 )
		sizer2.Add( self.listBoxEnemies, 30, wx.ALL|wx.EXPAND, 5 )
		
		staticSizerEnemies.Add( sizer2, 40, wx.EXPAND, 5 )
		
		sizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelBattleEvent = wx.StaticText( self, wx.ID_ANY, u"Battle Event:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBattleEvent.Wrap( -1 )
		sizer5.Add( self.labelBattleEvent, 0, wx.ALL, 5 )
		
		self.buttonNewPage = wx.Button( self, wx.ID_ANY, u"New\nEvent Page", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer5.Add( self.buttonNewPage, 1, wx.ALL, 5 )
		
		self.buttonCopyPage = wx.Button( self, wx.ID_ANY, u"Copy\nEvent Page", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer5.Add( self.buttonCopyPage, 1, wx.ALL, 5 )
		
		self.buttonPastePage = wx.Button( self, wx.ID_ANY, u"Paste\nEvent Page", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer5.Add( self.buttonPastePage, 1, wx.ALL, 5 )
		
		self.buttonDeletePage = wx.Button( self, wx.ID_ANY, u"Delete\nEvent Page", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer5.Add( self.buttonDeletePage, 1, wx.ALL, 5 )
		
		self.buttonClearPage = wx.Button( self, wx.ID_ANY, u"Clear\nEvent Page", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer5.Add( self.buttonClearPage, 1, wx.ALL, 5 )
		
		sizer3.Add( sizer5, 0, wx.EXPAND, 5 )
		
		self.notebookEventsTabControl = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panelEventPageTemplate = wx.Panel( self.notebookEventsTabControl, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer169 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer170 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelCondition = wx.StaticText( self.panelEventPageTemplate, wx.ID_ANY, u"Condition:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelCondition.Wrap( -1 )
		bSizer170.Add( self.labelCondition, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxConditionChoices = []
		self.comboBoxCondition = wx.ComboBox( self.panelEventPageTemplate, wx.ID_ANY, u"Don't Run", wx.DefaultPosition, wx.DefaultSize, comboBoxConditionChoices, 0 )
		bSizer170.Add( self.comboBoxCondition, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.labelSpan = wx.StaticText( self.panelEventPageTemplate, wx.ID_ANY, u"Span:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelSpan.Wrap( -1 )
		bSizer170.Add( self.labelSpan, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxSpanChoices = [ u"Battle", u"Turn", u"Moment" ]
		self.comboBoxSpan = wx.Choice( self.panelEventPageTemplate, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxSpanChoices, 0 )
		self.comboBoxSpan.SetSelection( 0 )
		bSizer170.Add( self.comboBoxSpan, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer169.Add( bSizer170, 0, wx.EXPAND, 5 )
		
		listBoxEventsChoices = [ u">@" ]
		self.listBoxEvents = wx.ListBox( self.panelEventPageTemplate, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxEventsChoices, 0 )
		bSizer169.Add( self.listBoxEvents, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.panelEventPageTemplate.SetSizer( bSizer169 )
		self.panelEventPageTemplate.Layout()
		bSizer169.Fit( self.panelEventPageTemplate )
		self.notebookEventsTabControl.AddPage( self.panelEventPageTemplate, u"1", False )
		
		sizer3.Add( self.notebookEventsTabControl, 1, wx.ALL|wx.EXPAND, 5 )
		
		staticSizerEnemies.Add( sizer3, 60, wx.EXPAND, 5 )
		
		MainSizer.Add( staticSizerEnemies, 75, wx.EXPAND|wx.ALL, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		# Connect Events
		self.listBoxTroops.Bind( wx.EVT_LISTBOX, self.listBoxTroops_SelectionChanged )
		self.buttonMaximum.Bind( wx.EVT_BUTTON, self.buttonMaximum_Clicked )
		self.textCtrlName.Bind( wx.EVT_TEXT, self.textCtrlName_ValueChanged )
		self.buttonAutoname.Bind( wx.EVT_BUTTON, self.buttonAutoname_Clicked )
		self.buttonBattleback.Bind( wx.EVT_BUTTON, self.buttonBattleback_Click )
		self.buttonBattleTest.Bind( wx.EVT_BUTTON, self.buttonBattleTest_Click )
		self.buttonAddEnemy.Bind( wx.EVT_BUTTON, self.buttonAddEnemy_Click )
		self.buttonRemoveEnemy.Bind( wx.EVT_BUTTON, self.buttonRemoveEnemy_Click )
		self.buttonClearTroops.Bind( wx.EVT_BUTTON, self.buttonClearTroop_Click )
		self.buttonAlignTroops.Bind( wx.EVT_BUTTON, self.buttonAlignTroop_Click )
		self.listBoxEnemies.Bind( wx.EVT_LISTBOX, self.listBox )
		self.buttonNewPage.Bind( wx.EVT_BUTTON, self.buttonNewEventPage_Click )
		self.buttonCopyPage.Bind( wx.EVT_BUTTON, self.buttonCopyEventPage_Click )
		self.buttonPastePage.Bind( wx.EVT_BUTTON, self.buttonPasteEventPage_Click )
		self.buttonDeletePage.Bind( wx.EVT_BUTTON, self.buttonDeleteEventPage_Click )
		self.buttonClearPage.Bind( wx.EVT_BUTTON, self.buttonClearEventPage_Click )
		self.comboBoxCondition.Bind( wx.EVT_LEFT_UP, self.comboBoxCondition_Clicked )
		self.comboBoxSpan.Bind( wx.EVT_CHOICE, self.comboBoxSpan_ValueChanged )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def listBoxTroops_SelectionChanged( self, event ):
		event.Skip()
	
	def buttonMaximum_Clicked( self, event ):
		event.Skip()
	
	def textCtrlName_ValueChanged( self, event ):
		event.Skip()
	
	def buttonAutoname_Clicked( self, event ):
		event.Skip()
	
	def buttonBattleback_Click( self, event ):
		event.Skip()
	
	def buttonBattleTest_Click( self, event ):
		event.Skip()
	
	def buttonAddEnemy_Click( self, event ):
		event.Skip()
	
	def buttonRemoveEnemy_Click( self, event ):
		event.Skip()
	
	def buttonClearTroop_Click( self, event ):
		event.Skip()
	
	def buttonAlignTroop_Click( self, event ):
		event.Skip()
	
	def listBox( self, event ):
		event.Skip()
	
	def buttonNewEventPage_Click( self, event ):
		event.Skip()
	
	def buttonCopyEventPage_Click( self, event ):
		event.Skip()
	
	def buttonPasteEventPage_Click( self, event ):
		event.Skip()
	
	def buttonDeleteEventPage_Click( self, event ):
		event.Skip()
	
	def buttonClearEventPage_Click( self, event ):
		event.Skip()
	
	def comboBoxCondition_Clicked( self, event ):
		event.Skip()
	
	def comboBoxSpan_ValueChanged( self, event ):
		event.Skip()
	

###########################################################################
## Class States_Panel
###########################################################################

class States_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		StatesListSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapStates = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/States.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
		self.bitmapStates.SetMinSize( wx.Size( 150,26 ) )
		self.bitmapStates.SetMaxSize( wx.Size( 150,26 ) )
		
		StatesListSizer.Add( self.bitmapStates, 0, wx.ALL|wx.EXPAND, 5 )
		
		listBoxStatesChoices = []
		self.listBoxStates = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxStatesChoices, wx.LB_SINGLE|wx.CLIP_CHILDREN )
		self.listBoxStates.SetToolTipString( u"Select the item to edit" )
		
		StatesListSizer.Add( self.listBoxStates, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonMaximum = wx.Button( self, wx.ID_ANY, u"Change Maximum...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.buttonMaximum.SetToolTipString( u"Change the maximum of available items" )
		
		StatesListSizer.Add( self.buttonMaximum, 0, wx.ALL|wx.EXPAND, 5 )
		
		MainSizer.Add( StatesListSizer, 25, wx.EXPAND, 5 )
		
		staticSizerStates = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		sizer1 = wx.BoxSizer( wx.VERTICAL )
		
		sizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelName.Wrap( -1 )
		sizer12.Add( self.labelName, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer12.Add( self.textCtrlName, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelAnimation = wx.StaticText( self, wx.ID_ANY, u"Animation:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAnimation.Wrap( -1 )
		sizer12.Add( self.labelAnimation, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxAnimationChoices = []
		self.comboBoxAnimation = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxAnimationChoices, 0 )
		self.comboBoxAnimation.SetSelection( 0 )
		sizer12.Add( self.comboBoxAnimation, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelRestriction = wx.StaticText( self, wx.ID_ANY, u"Restriction:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelRestriction.Wrap( -1 )
		sizer12.Add( self.labelRestriction, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxRestrictionChoices = []
		self.comboBoxRestriction = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxRestrictionChoices, 0 )
		self.comboBoxRestriction.SetSelection( 0 )
		sizer12.Add( self.comboBoxRestriction, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizer4.Add( sizer12, 1, wx.EXPAND, 5 )
		
		sizerParameters = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.checkBoxNonresistance = wx.CheckBox( self, wx.ID_ANY, u"Nonresistance", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerParameters.Add( self.checkBoxNonresistance, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.checkBoxRegardHP0 = wx.CheckBox( self, wx.ID_ANY, u"Regard as HP 0", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerParameters.Add( self.checkBoxRegardHP0, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.checkBoxNoExp = wx.CheckBox( self, wx.ID_ANY, u"Can't Get EXP", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerParameters.Add( self.checkBoxNoExp, 0, wx.ALL, 5 )
		
		self.checkBoxNoEvade = wx.CheckBox( self, wx.ID_ANY, u"Can't Evade", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerParameters.Add( self.checkBoxNoEvade, 0, wx.ALL, 5 )
		
		self.checkBoxSlipDamage = wx.CheckBox( self, wx.ID_ANY, u"Slip Damage", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerParameters.Add( self.checkBoxSlipDamage, 0, wx.ALL, 5 )
		
		sizer4.Add( sizerParameters, 1, wx.ALL, 5 )
		
		sizer1.Add( sizer4, 0, wx.EXPAND, 5 )
		
		sizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelRating = wx.StaticText( self, wx.ID_ANY, u"Rating:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelRating.Wrap( -1 )
		sizer5.Add( self.labelRating, 1, wx.ALL, 5 )
		
		self.labelHitPercentage = wx.StaticText( self, wx.ID_ANY, u"Hit Rate %:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelHitPercentage.Wrap( -1 )
		sizer5.Add( self.labelHitPercentage, 1, wx.ALL, 5 )
		
		self.labelMaxHPPercentage = wx.StaticText( self, wx.ID_ANY, u"MaxHP %:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMaxHPPercentage.Wrap( -1 )
		sizer5.Add( self.labelMaxHPPercentage, 1, wx.ALL, 5 )
		
		self.labelMaxSPPercentage = wx.StaticText( self, wx.ID_ANY, u"MaxSP %:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMaxSPPercentage.Wrap( -1 )
		sizer5.Add( self.labelMaxSPPercentage, 1, wx.ALL, 5 )
		
		sizer1.Add( sizer5, 0, wx.EXPAND, 5 )
		
		sizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.spinCtrlRating = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer6.Add( self.spinCtrlRating, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.spinCtrlHitRate = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer6.Add( self.spinCtrlHitRate, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.spinCtrlMaxHP = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer6.Add( self.spinCtrlMaxHP, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.spinCtrlMaxSP = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer6.Add( self.spinCtrlMaxSP, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer1.Add( sizer6, 0, wx.EXPAND, 5 )
		
		sizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelStrPercentage = wx.StaticText( self, wx.ID_ANY, u"STR %:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelStrPercentage.Wrap( -1 )
		sizer7.Add( self.labelStrPercentage, 1, wx.ALL, 5 )
		
		self.labelDexPercentage = wx.StaticText( self, wx.ID_ANY, u"DEX %:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelDexPercentage.Wrap( -1 )
		sizer7.Add( self.labelDexPercentage, 1, wx.ALL, 5 )
		
		self.labelAgiPercentage = wx.StaticText( self, wx.ID_ANY, u"AGI %:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAgiPercentage.Wrap( -1 )
		sizer7.Add( self.labelAgiPercentage, 1, wx.ALL, 5 )
		
		self.labelIntPercentage = wx.StaticText( self, wx.ID_ANY, u"INT %:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelIntPercentage.Wrap( -1 )
		sizer7.Add( self.labelIntPercentage, 1, wx.ALL, 5 )
		
		sizer1.Add( sizer7, 0, wx.EXPAND, 5 )
		
		sizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.spinCtrlStr = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer8.Add( self.spinCtrlStr, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.spinCtrlDex = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer8.Add( self.spinCtrlDex, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.spinCtrlAgi = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer8.Add( self.spinCtrlAgi, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.spinCtrlInt = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer8.Add( self.spinCtrlInt, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer1.Add( sizer8, 0, wx.EXPAND, 5 )
		
		sizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelAtkPercentage = wx.StaticText( self, wx.ID_ANY, u"ATK %:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAtkPercentage.Wrap( -1 )
		sizer9.Add( self.labelAtkPercentage, 1, wx.ALL, 5 )
		
		self.labelPdefPercentage = wx.StaticText( self, wx.ID_ANY, u"PDEF %:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPdefPercentage.Wrap( -1 )
		sizer9.Add( self.labelPdefPercentage, 1, wx.ALL, 5 )
		
		self.labelMdefPercentage = wx.StaticText( self, wx.ID_ANY, u"MDEF %:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMdefPercentage.Wrap( -1 )
		sizer9.Add( self.labelMdefPercentage, 1, wx.ALL, 5 )
		
		self.lavelEvaPercentage = wx.StaticText( self, wx.ID_ANY, u"EVA %:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lavelEvaPercentage.Wrap( -1 )
		sizer9.Add( self.lavelEvaPercentage, 1, wx.ALL, 5 )
		
		sizer1.Add( sizer9, 0, wx.EXPAND, 5 )
		
		sizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.spinCtrlAtk = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer10.Add( self.spinCtrlAtk, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.spinCtrlPdef = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer10.Add( self.spinCtrlPdef, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.spinCtrlMdef = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer10.Add( self.spinCtrlMdef, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.spinCtrlEva = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer10.Add( self.spinCtrlEva, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer1.Add( sizer10, 0, wx.EXPAND, 5 )
		
		sizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Release Conditions" ), wx.VERTICAL )
		
		self.lcheckBoxReleaseEnd = wx.CheckBox( self, wx.ID_ANY, u"Release at the end of battle", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer11.Add( self.lcheckBoxReleaseEnd, 0, wx.ALL, 5 )
		
		sizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelAfter = wx.StaticText( self, wx.ID_ANY, u"After", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAfter.Wrap( -1 )
		sizer13.Add( self.labelAfter, 0, wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlConditionTurns = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer13.Add( self.spinCtrlConditionTurns, 1, wx.TOP|wx.BOTTOM, 5 )
		
		self.labelTurns = wx.StaticText( self, wx.ID_ANY, u"turns,", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTurns.Wrap( -1 )
		sizer13.Add( self.labelTurns, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.spinCtrlConditionTurnPercent = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer13.Add( self.spinCtrlConditionTurnPercent, 1, wx.TOP|wx.BOTTOM, 5 )
		
		self.labelChance1 = wx.StaticText( self, wx.ID_ANY, u"% chance.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelChance1.Wrap( -1 )
		sizer13.Add( self.labelChance1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		sizer11.Add( sizer13, 0, wx.EXPAND, 5 )
		
		sizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelPhysical = wx.StaticText( self, wx.ID_ANY, u"Each physical damage deal,", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPhysical.Wrap( -1 )
		sizer14.Add( self.labelPhysical, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.spinCtrlConditionPhysical = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer14.Add( self.spinCtrlConditionPhysical, 1, wx.TOP|wx.BOTTOM, 5 )
		
		self.labelChance2 = wx.StaticText( self, wx.ID_ANY, u"% chance.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelChance2.Wrap( -1 )
		sizer14.Add( self.labelChance2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizer11.Add( sizer14, 0, wx.EXPAND, 5 )
		
		sizer1.Add( sizer11, 0, wx.EXPAND|wx.ALL, 5 )
		
		staticSizerStates.Add( sizer1, 50, wx.EXPAND, 5 )
		
		sizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelElements = wx.StaticText( self, wx.ID_ANY, u"Element Defense:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelElements.Wrap( -1 )
		sizer2.Add( self.labelElements, 0, wx.ALL, 5 )
		
		checkListElementsChoices = []
		self.checkListElements = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListElementsChoices, 0 )
		sizer2.Add( self.checkListElements, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		staticSizerStates.Add( sizer2, 25, wx.EXPAND, 5 )
		
		sizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelStates = wx.StaticText( self, wx.ID_ANY, u"State Change:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelStates.Wrap( -1 )
		sizer3.Add( self.labelStates, 0, wx.ALL, 5 )
		
		checkListStatesChoices = []
		self.checkListStates = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListStatesChoices, 0 )
		sizer3.Add( self.checkListStates, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		staticSizerStates.Add( sizer3, 25, wx.EXPAND, 5 )
		
		MainSizer.Add( staticSizerStates, 75, wx.EXPAND|wx.ALL, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		# Connect Events
		self.listBoxStates.Bind( wx.EVT_LISTBOX, self.listBoxStates_SelectionChanged )
		self.buttonMaximum.Bind( wx.EVT_BUTTON, self.buttonMaximum_Clicked )
		self.textCtrlName.Bind( wx.EVT_TEXT, self.textCtrlName_ValueChanged )
		self.comboBoxAnimation.Bind( wx.EVT_CHOICE, self.comboBoxAnimation_SelectionChanged )
		self.comboBoxRestriction.Bind( wx.EVT_CHOICE, self.comboBoxRestriction_SelectionChanged )
		self.checkBoxNonresistance.Bind( wx.EVT_CHECKBOX, self.checkBoxNonresistance_CheckChanged )
		self.checkBoxRegardHP0.Bind( wx.EVT_CHECKBOX, self.checkBoxHP0_CheckChanged )
		self.checkBoxNoExp.Bind( wx.EVT_CHECKBOX, self.checkBoxNoExp_CheckChanged )
		self.checkBoxNoEvade.Bind( wx.EVT_CHECKBOX, self.checkBoxNoEvade_CheckChanged )
		self.checkBoxSlipDamage.Bind( wx.EVT_CHECKBOX, self.checkBoxSlipDamage_CheckChanged )
		self.spinCtrlRating.Bind( wx.EVT_SPINCTRL, self.spinCtrlRating_ValueChanged )
		self.spinCtrlHitRate.Bind( wx.EVT_SPINCTRL, self.spinCtrlHitRate_ValueChanged )
		self.spinCtrlMaxHP.Bind( wx.EVT_SPINCTRL, self.spinCtrlMaxHP_ValueChanged )
		self.spinCtrlMaxSP.Bind( wx.EVT_SPINCTRL, self.spinCtrlMaxSP_ValueChanged )
		self.spinCtrlStr.Bind( wx.EVT_SPINCTRL, self.spinCtrlStr_ValueChanged )
		self.spinCtrlDex.Bind( wx.EVT_SPINCTRL, self.spinCtrlDex_ValueChanged )
		self.spinCtrlAgi.Bind( wx.EVT_SPINCTRL, self.spinCtrlAgi_ValueChanged )
		self.spinCtrlInt.Bind( wx.EVT_SPINCTRL, self.spinCtrlInt_ValueChanged )
		self.spinCtrlAtk.Bind( wx.EVT_SPINCTRL, self.spinCtrlAtk_ValueChanged )
		self.spinCtrlPdef.Bind( wx.EVT_SPINCTRL, self.spinCtrlPdef_ValueChanged )
		self.spinCtrlMdef.Bind( wx.EVT_SPINCTRL, self.spinCtrlMdef_ValueChanged )
		self.spinCtrlEva.Bind( wx.EVT_SPINCTRL, self.spinCtrlEva_ValueChanged )
		self.lcheckBoxReleaseEnd.Bind( wx.EVT_CHECKBOX, self.checkBoxBattleRelease_CheckChanged )
		self.spinCtrlConditionTurns.Bind( wx.EVT_SPINCTRL, self.spinCtrlTurns_ValueChanged )
		self.spinCtrlConditionTurnPercent.Bind( wx.EVT_SPINCTRL, self.spinCtrlTurnPercent_ValueChanged )
		self.spinCtrlConditionPhysical.Bind( wx.EVT_SPINCTRL, self.spinCtrlPhysical_ValueChanged )
		self.checkListElements.Bind( wx.EVT_CHECKLISTBOX, self.checkListElements_CheckChanged )
		self.checkListStates.Bind( wx.EVT_CHECKLISTBOX, self.checkListStates_CheckChanged )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def listBoxStates_SelectionChanged( self, event ):
		event.Skip()
	
	def buttonMaximum_Clicked( self, event ):
		event.Skip()
	
	def textCtrlName_ValueChanged( self, event ):
		event.Skip()
	
	def comboBoxAnimation_SelectionChanged( self, event ):
		event.Skip()
	
	def comboBoxRestriction_SelectionChanged( self, event ):
		event.Skip()
	
	def checkBoxNonresistance_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxHP0_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxNoExp_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxNoEvade_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxSlipDamage_CheckChanged( self, event ):
		event.Skip()
	
	def spinCtrlRating_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlHitRate_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlMaxHP_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlMaxSP_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlStr_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlDex_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlAgi_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlInt_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlAtk_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlPdef_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlMdef_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlEva_ValueChanged( self, event ):
		event.Skip()
	
	def checkBoxBattleRelease_CheckChanged( self, event ):
		event.Skip()
	
	def spinCtrlTurns_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlTurnPercent_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlPhysical_ValueChanged( self, event ):
		event.Skip()
	
	def checkListElements_CheckChanged( self, event ):
		event.Skip()
	
	def checkListStates_CheckChanged( self, event ):
		event.Skip()
	

###########################################################################
## Class Animations_Panel
###########################################################################

class Animations_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		AnimationsListSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapAnimations = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/Animations.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
		self.bitmapAnimations.SetMinSize( wx.Size( 150,26 ) )
		self.bitmapAnimations.SetMaxSize( wx.Size( 150,26 ) )
		
		AnimationsListSizer.Add( self.bitmapAnimations, 0, wx.ALL|wx.EXPAND, 5 )
		
		listBoxAnimationsChoices = []
		self.listBoxAnimations = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxAnimationsChoices, wx.LB_SINGLE|wx.CLIP_CHILDREN )
		self.listBoxAnimations.SetToolTipString( u"Select the item to edit" )
		
		AnimationsListSizer.Add( self.listBoxAnimations, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonMaximum = wx.Button( self, wx.ID_ANY, u"Change Maximum...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.buttonMaximum.SetToolTipString( u"Change the maximum of available items" )
		
		AnimationsListSizer.Add( self.buttonMaximum, 0, wx.ALL|wx.EXPAND, 5 )
		
		MainSizer.Add( AnimationsListSizer, 25, wx.EXPAND, 5 )
		
		staticSizerAnimations = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		sizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelName.Wrap( -1 )
		sizer4.Add( self.labelName, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer4.Add( self.textCtrlName, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelGraphic = wx.StaticText( self, wx.ID_ANY, u"Animation Graphic:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelGraphic.Wrap( -1 )
		sizer4.Add( self.labelGraphic, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxGraphicChoices = [ u"(None)" ]
		self.comboBoxGraphic = wx.ComboBox( self, wx.ID_ANY, u"(None)", wx.DefaultPosition, wx.DefaultSize, comboBoxGraphicChoices, 0 )
		sizer4.Add( self.comboBoxGraphic, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelPosition = wx.StaticText( self, wx.ID_ANY, u"Position:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPosition.Wrap( -1 )
		sizer7.Add( self.labelPosition, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.labelFrames = wx.StaticText( self, wx.ID_ANY, u"Frames:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelFrames.Wrap( -1 )
		sizer7.Add( self.labelFrames, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizer4.Add( sizer7, 0, wx.EXPAND, 5 )
		
		sizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		comboBoxPositionChoices = [ u"Top", u"Middle", u"Bottom", u"Screen" ]
		self.comboBoxPosition = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxPositionChoices, 0 )
		self.comboBoxPosition.SetSelection( 0 )
		sizer8.Add( self.comboBoxPosition, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		comboBoxFramesChoices = []
		self.comboBoxFrames = wx.ComboBox( self, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, comboBoxFramesChoices, 0 )
		sizer8.Add( self.comboBoxFrames, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer4.Add( sizer8, 0, wx.EXPAND, 5 )
		
		sizer1.Add( sizer4, 30, 0, 5 )
		
		self.listCtrlTiming = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON|wx.LC_REPORT )
		sizer1.Add( self.listCtrlTiming, 70, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		staticSizerAnimations.Add( sizer1, 0, wx.EXPAND, 5 )
		
		sizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonBack = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 56,-1 ), 0 )
		sizer5.Add( self.buttonBack, 0, wx.ALL, 5 )
		
		listBoxFrameChoices = []
		self.listBoxFrame = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 56,-1 ), listBoxFrameChoices, wx.LB_ALWAYS_SB )
		sizer5.Add( self.listBoxFrame, 1, wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonNext = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.Size( 56,-1 ), 0 )
		sizer5.Add( self.buttonNext, 0, wx.ALL, 5 )
		
		sizer2.Add( sizer5, 0, wx.EXPAND, 5 )
		
		self.bitmapPallette = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/AnimationSample1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER )
		sizer2.Add( self.bitmapPallette, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizer6 = wx.BoxSizer( wx.VERTICAL )
		
		sizer6.SetMinSize( wx.Size( 100,-1 ) ) 
		self.buttonBattler = wx.Button( self, wx.ID_ANY, u"[ED] Battler...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer6.Add( self.buttonBattler, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.buttonPaste = wx.Button( self, wx.ID_ANY, u"Paste Last", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer6.Add( self.buttonPaste, 0, wx.TOP|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonCopy = wx.Button( self, wx.ID_ANY, u"Copy Frames...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer6.Add( self.buttonCopy, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonClear = wx.Button( self, wx.ID_ANY, u"Clear Frames...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer6.Add( self.buttonClear, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonTweening = wx.Button( self, wx.ID_ANY, u"Tweening...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer6.Add( self.buttonTweening, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonCellBatch = wx.Button( self, wx.ID_ANY, u"Cell Batch...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer6.Add( self.buttonCellBatch, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonEntireSlide = wx.Button( self, wx.ID_ANY, u"Entire Slide...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer6.Add( self.buttonEntireSlide, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonPlayHit = wx.Button( self, wx.ID_ANY, u"Play Hit", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer6.Add( self.buttonPlayHit, 0, wx.TOP|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonPlayMiss = wx.Button( self, wx.ID_ANY, u"Play Miss", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer6.Add( self.buttonPlayMiss, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizer2.Add( sizer6, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		staticSizerAnimations.Add( sizer2, 60, wx.EXPAND, 5 )
		
		sizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_scrolledWindow3 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.ALWAYS_SHOW_SB|wx.HSCROLL|wx.SUNKEN_BORDER|wx.VSCROLL )
		self.m_scrolledWindow3.SetScrollRate( 5, 5 )
		bSizer196 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bitmapAnimationFrames = wx.StaticBitmap( self.m_scrolledWindow3, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/AnimationSample2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer196.Add( self.bitmapAnimationFrames, 0, wx.ALL, 5 )
		
		self.m_scrolledWindow3.SetSizer( bSizer196 )
		self.m_scrolledWindow3.Layout()
		bSizer196.Fit( self.m_scrolledWindow3 )
		sizer3.Add( self.m_scrolledWindow3, 1, wx.ALL|wx.EXPAND, 5 )
		
		staticSizerAnimations.Add( sizer3, 35, wx.EXPAND, 5 )
		
		MainSizer.Add( staticSizerAnimations, 75, wx.EXPAND|wx.ALL, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		# Connect Events
		self.listBoxAnimations.Bind( wx.EVT_LISTBOX, self.listBoxAnimations_SelectionChanged )
		self.buttonMaximum.Bind( wx.EVT_BUTTON, self.buttonMaximum_Clicked )
		self.textCtrlName.Bind( wx.EVT_TEXT, self.textCtrlName_ValueChanged )
		self.comboBoxGraphic.Bind( wx.EVT_LEFT_DOWN, self.comboBoxGraphic_Clicked )
		self.comboBoxPosition.Bind( wx.EVT_CHOICE, self.comboBoxPosition_SelectionChanged )
		self.comboBoxFrames.Bind( wx.EVT_LEFT_DOWN, self.comboBoxFrames_Clicked )
		self.buttonBack.Bind( wx.EVT_BUTTON, self.buttonBack_Clicked )
		self.listBoxFrame.Bind( wx.EVT_LISTBOX, self.listBoxFrames_SelectionChanged )
		self.buttonNext.Bind( wx.EVT_BUTTON, self.buttonNext_Clicked )
		self.buttonBattler.Bind( wx.EVT_BUTTON, self.buttonBattler_Clicked )
		self.buttonPaste.Bind( wx.EVT_BUTTON, self.buttonPaste_Clicked )
		self.buttonCopy.Bind( wx.EVT_BUTTON, self.buttonCopy_Clicked )
		self.buttonClear.Bind( wx.EVT_BUTTON, self.buttonClear_Clicked )
		self.buttonTweening.Bind( wx.EVT_BUTTON, self.buttonTweening_Clicked )
		self.buttonCellBatch.Bind( wx.EVT_BUTTON, self.buttonCellBatch_Clicked )
		self.buttonEntireSlide.Bind( wx.EVT_BUTTON, self.buttonEntireSlide_Clicked )
		self.buttonPlayHit.Bind( wx.EVT_BUTTON, self.buttonPlayHit_Clicked )
		self.buttonPlayMiss.Bind( wx.EVT_BUTTON, self.buttonPlayMiss_Clicked )
		self.bitmapAnimationFrames.Bind( wx.EVT_LEFT_DOWN, self.bitmapAnimationFrames_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def listBoxAnimations_SelectionChanged( self, event ):
		event.Skip()
	
	def buttonMaximum_Clicked( self, event ):
		event.Skip()
	
	def textCtrlName_ValueChanged( self, event ):
		event.Skip()
	
	def comboBoxGraphic_Clicked( self, event ):
		event.Skip()
	
	def comboBoxPosition_SelectionChanged( self, event ):
		event.Skip()
	
	def comboBoxFrames_Clicked( self, event ):
		event.Skip()
	
	def buttonBack_Clicked( self, event ):
		event.Skip()
	
	def listBoxFrames_SelectionChanged( self, event ):
		event.Skip()
	
	def buttonNext_Clicked( self, event ):
		event.Skip()
	
	def buttonBattler_Clicked( self, event ):
		event.Skip()
	
	def buttonPaste_Clicked( self, event ):
		event.Skip()
	
	def buttonCopy_Clicked( self, event ):
		event.Skip()
	
	def buttonClear_Clicked( self, event ):
		event.Skip()
	
	def buttonTweening_Clicked( self, event ):
		event.Skip()
	
	def buttonCellBatch_Clicked( self, event ):
		event.Skip()
	
	def buttonEntireSlide_Clicked( self, event ):
		event.Skip()
	
	def buttonPlayHit_Clicked( self, event ):
		event.Skip()
	
	def buttonPlayMiss_Clicked( self, event ):
		event.Skip()
	
	def bitmapAnimationFrames_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class Tilesets_Panel
###########################################################################

class Tilesets_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		TilesetsListSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapTilesets = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/Tilesets.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
		self.bitmapTilesets.SetMinSize( wx.Size( 150,26 ) )
		self.bitmapTilesets.SetMaxSize( wx.Size( 150,26 ) )
		
		TilesetsListSizer.Add( self.bitmapTilesets, 0, wx.ALL|wx.EXPAND, 5 )
		
		listBoxTilesetsChoices = []
		self.listBoxTilesets = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxTilesetsChoices, wx.LB_SINGLE|wx.CLIP_CHILDREN )
		self.listBoxTilesets.SetToolTipString( u"Select the item to edit" )
		
		TilesetsListSizer.Add( self.listBoxTilesets, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonMaximum = wx.Button( self, wx.ID_ANY, u"Change Maximum...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.buttonMaximum.SetToolTipString( u"Change the maximum of available items" )
		
		TilesetsListSizer.Add( self.buttonMaximum, 0, wx.ALL|wx.EXPAND, 5 )
		
		MainSizer.Add( TilesetsListSizer, 25, wx.EXPAND, 5 )
		
		staticSizerTilesets = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		sizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelName.Wrap( -1 )
		sizer1.Add( self.labelName, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer1.Add( self.textCtrlName, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelTileset = wx.StaticText( self, wx.ID_ANY, u"Tileset Graphic:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTileset.Wrap( -1 )
		sizer1.Add( self.labelTileset, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.comboBoxTileset = wx.combo.BitmapComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, "", 0 ) 
		sizer1.Add( self.comboBoxTileset, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelAutotiles = wx.StaticText( self, wx.ID_ANY, u"Autotile Graphics:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAutotiles.Wrap( -1 )
		sizer1.Add( self.labelAutotiles, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.comboBoxAutotiles1 = wx.combo.BitmapComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, "", 0 ) 
		sizer1.Add( self.comboBoxAutotiles1, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.comboBoxAutotiles2 = wx.combo.BitmapComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, "", 0 ) 
		sizer1.Add( self.comboBoxAutotiles2, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.comboBoxAutotiles3 = wx.combo.BitmapComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, "", 0 ) 
		sizer1.Add( self.comboBoxAutotiles3, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.comboBoxAutotiles4 = wx.combo.BitmapComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, "", 0 ) 
		sizer1.Add( self.comboBoxAutotiles4, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.comboBoxAutotiles5 = wx.combo.BitmapComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, "", 0 ) 
		sizer1.Add( self.comboBoxAutotiles5, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.comboBoxAutotiles6 = wx.combo.BitmapComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, "", 0 ) 
		sizer1.Add( self.comboBoxAutotiles6, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.comboBoxAutotiles7 = wx.combo.BitmapComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, "", 0 ) 
		sizer1.Add( self.comboBoxAutotiles7, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelPanorama = wx.StaticText( self, wx.ID_ANY, u"Panorama Graphic:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPanorama.Wrap( -1 )
		sizer1.Add( self.labelPanorama, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxPanoramaChoices = []
		self.comboBoxPanorama = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, comboBoxPanoramaChoices, 0 )
		sizer1.Add( self.comboBoxPanorama, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelFog = wx.StaticText( self, wx.ID_ANY, u"Fog Graphic:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelFog.Wrap( -1 )
		sizer1.Add( self.labelFog, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxFogChoices = []
		self.comboBoxFog = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, comboBoxFogChoices, 0 )
		sizer1.Add( self.comboBoxFog, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelBattleback = wx.StaticText( self, wx.ID_ANY, u"Battleback Graphic:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBattleback.Wrap( -1 )
		sizer1.Add( self.labelBattleback, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxBattlebackChoices = []
		self.comboBoxBattleback = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, comboBoxBattlebackChoices, 0 )
		sizer1.Add( self.comboBoxBattleback, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		staticSizerTilesets.Add( sizer1, 0, wx.EXPAND, 5 )
		
		self.m_scrolledWindow4 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.SUNKEN_BORDER|wx.VSCROLL )
		self.m_scrolledWindow4.SetScrollRate( 5, 5 )
		self.m_scrolledWindow4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		sizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap36 = wx.StaticBitmap( self.m_scrolledWindow4, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/TilesetSample.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 256,-1 ), 0 )
		self.m_bitmap36.SetMinSize( wx.Size( 256,-1 ) )
		self.m_bitmap36.SetMaxSize( wx.Size( 256,-1 ) )
		
		sizer3.Add( self.m_bitmap36, 0, 0, 5 )
		
		self.m_scrolledWindow4.SetSizer( sizer3 )
		self.m_scrolledWindow4.Layout()
		sizer3.Fit( self.m_scrolledWindow4 )
		staticSizerTilesets.Add( self.m_scrolledWindow4, 1, wx.EXPAND|wx.ALL, 5 )
		
		sizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonPassage = wx.Button( self, wx.ID_ANY, u"Passage", wx.DefaultPosition, wx.Size( -1,46 ), 0 )
		sizer2.Add( self.buttonPassage, 0, wx.ALL, 5 )
		
		self.buttonPassage4Dir = wx.Button( self, wx.ID_ANY, u"Passage\n(4 Dir)", wx.DefaultPosition, wx.Size( -1,46 ), 0 )
		sizer2.Add( self.buttonPassage4Dir, 0, wx.ALL, 5 )
		
		self.buttonPriority = wx.Button( self, wx.ID_ANY, u"Priority", wx.DefaultPosition, wx.Size( -1,46 ), 0 )
		sizer2.Add( self.buttonPriority, 0, wx.ALL, 5 )
		
		self.buttonBushFlag = wx.Button( self, wx.ID_ANY, u"Bush\nFlag", wx.DefaultPosition, wx.Size( -1,46 ), 0 )
		sizer2.Add( self.buttonBushFlag, 0, wx.ALL, 5 )
		
		self.buttonCounter = wx.Button( self, wx.ID_ANY, u"Counter\nFlag", wx.DefaultPosition, wx.Size( -1,46 ), 0 )
		sizer2.Add( self.buttonCounter, 0, wx.ALL, 5 )
		
		self.buttonTerrainTag = wx.Button( self, wx.ID_ANY, u"Terrain\nTag", wx.DefaultPosition, wx.Size( -1,46 ), 0 )
		sizer2.Add( self.buttonTerrainTag, 0, wx.ALL, 5 )
		
		staticSizerTilesets.Add( sizer2, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( staticSizerTilesets, 75, wx.EXPAND|wx.ALL, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		# Connect Events
		self.listBoxTilesets.Bind( wx.EVT_LISTBOX, self.listBoxTilesets_SelectionChanged )
		self.buttonMaximum.Bind( wx.EVT_BUTTON, self.buttonMaximum_Clicked )
		self.textCtrlName.Bind( wx.EVT_TEXT, self.textCtrlName_ValueChanged )
		self.comboBoxTileset.Bind( wx.EVT_LEFT_DOWN, self.comboBoxTileset_Clicked )
		self.comboBoxAutotiles1.Bind( wx.EVT_LEFT_DOWN, self.comboBoxAutotiles1_Clicked )
		self.comboBoxAutotiles2.Bind( wx.EVT_LEFT_DOWN, self.comboBoxAutotiles2_Clicked )
		self.comboBoxAutotiles3.Bind( wx.EVT_LEFT_DOWN, self.comboBoxAutotiles3_Clicked )
		self.comboBoxAutotiles4.Bind( wx.EVT_LEFT_DOWN, self.comboBoxAutotiles4_Clicked )
		self.comboBoxAutotiles5.Bind( wx.EVT_LEFT_DOWN, self.comboBoxAutotiles5_Clicked )
		self.comboBoxAutotiles6.Bind( wx.EVT_LEFT_DOWN, self.comboBoxAutotiles6_Clicked )
		self.comboBoxAutotiles7.Bind( wx.EVT_LEFT_DOWN, self.comboBoxAutotiles7_Clicked )
		self.comboBoxPanorama.Bind( wx.EVT_LEFT_DOWN, self.comboBoxPanorama_Clicked )
		self.comboBoxFog.Bind( wx.EVT_LEFT_DOWN, self.comboBoxFog_Clicked )
		self.comboBoxBattleback.Bind( wx.EVT_LEFT_DOWN, self.comboBoxBattleback_Clicked )
		self.m_bitmap36.Bind( wx.EVT_LEFT_DCLICK, self.bitmapTileset_LeftClick )
		self.m_bitmap36.Bind( wx.EVT_LEFT_DOWN, self.bitmapTileset_LMouseDown )
		self.m_bitmap36.Bind( wx.EVT_LEFT_UP, self.bitmapTileset_LeftMouseUp )
		self.m_bitmap36.Bind( wx.EVT_RIGHT_DCLICK, self.bitmapTileset_RightClick )
		self.m_bitmap36.Bind( wx.EVT_RIGHT_DOWN, self.bitmapTileset_RightMouseDown )
		self.m_bitmap36.Bind( wx.EVT_RIGHT_UP, self.bitmapTileset_RightMouseUP )
		self.buttonPassage.Bind( wx.EVT_BUTTON, self.buttonPassage_Clicked )
		self.buttonPassage4Dir.Bind( wx.EVT_BUTTON, self.buttonPassage4Dir_Clicked )
		self.buttonPriority.Bind( wx.EVT_BUTTON, self.buttonPriority_Clicked )
		self.buttonBushFlag.Bind( wx.EVT_BUTTON, self.buttonBushFlag_Clicked )
		self.buttonCounter.Bind( wx.EVT_BUTTON, self.buttonCounter_Clicked )
		self.buttonTerrainTag.Bind( wx.EVT_BUTTON, self.buttonTerrainTag_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def listBoxTilesets_SelectionChanged( self, event ):
		event.Skip()
	
	def buttonMaximum_Clicked( self, event ):
		event.Skip()
	
	def textCtrlName_ValueChanged( self, event ):
		event.Skip()
	
	def comboBoxTileset_Clicked( self, event ):
		event.Skip()
	
	def comboBoxAutotiles1_Clicked( self, event ):
		event.Skip()
	
	def comboBoxAutotiles2_Clicked( self, event ):
		event.Skip()
	
	def comboBoxAutotiles3_Clicked( self, event ):
		event.Skip()
	
	def comboBoxAutotiles4_Clicked( self, event ):
		event.Skip()
	
	def comboBoxAutotiles5_Clicked( self, event ):
		event.Skip()
	
	def comboBoxAutotiles6_Clicked( self, event ):
		event.Skip()
	
	def comboBoxAutotiles7_Clicked( self, event ):
		event.Skip()
	
	def comboBoxPanorama_Clicked( self, event ):
		event.Skip()
	
	def comboBoxFog_Clicked( self, event ):
		event.Skip()
	
	def comboBoxBattleback_Clicked( self, event ):
		event.Skip()
	
	def bitmapTileset_LeftClick( self, event ):
		event.Skip()
	
	def bitmapTileset_LMouseDown( self, event ):
		event.Skip()
	
	def bitmapTileset_LeftMouseUp( self, event ):
		event.Skip()
	
	def bitmapTileset_RightClick( self, event ):
		event.Skip()
	
	def bitmapTileset_RightMouseDown( self, event ):
		event.Skip()
	
	def bitmapTileset_RightMouseUP( self, event ):
		event.Skip()
	
	def buttonPassage_Clicked( self, event ):
		event.Skip()
	
	def buttonPassage4Dir_Clicked( self, event ):
		event.Skip()
	
	def buttonPriority_Clicked( self, event ):
		event.Skip()
	
	def buttonBushFlag_Clicked( self, event ):
		event.Skip()
	
	def buttonCounter_Clicked( self, event ):
		event.Skip()
	
	def buttonTerrainTag_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class CommonEvents_Panel
###########################################################################

class CommonEvents_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		CommonEventsListSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapCommonEvents = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Database Panel Images/CommonEvents.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
		self.bitmapCommonEvents.SetMinSize( wx.Size( 150,26 ) )
		self.bitmapCommonEvents.SetMaxSize( wx.Size( 150,26 ) )
		
		CommonEventsListSizer.Add( self.bitmapCommonEvents, 0, wx.ALL|wx.EXPAND, 5 )
		
		listBoxCommonEventsChoices = []
		self.listBoxCommonEvents = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxCommonEventsChoices, wx.LB_SINGLE|wx.CLIP_CHILDREN )
		self.listBoxCommonEvents.SetToolTipString( u"Select the item to edit" )
		
		CommonEventsListSizer.Add( self.listBoxCommonEvents, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonMaximum = wx.Button( self, wx.ID_ANY, u"Change Maximum...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.buttonMaximum.SetToolTipString( u"Change the maximum of available items" )
		
		CommonEventsListSizer.Add( self.buttonMaximum, 0, wx.ALL|wx.EXPAND, 5 )
		
		MainSizer.Add( CommonEventsListSizer, 25, wx.EXPAND, 5 )
		
		staticSizerCommonEvents = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		sizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelName.Wrap( -1 )
		sizer1.Add( self.labelName, 35, wx.ALL, 5 )
		
		self.labelTrigger = wx.StaticText( self, wx.ID_ANY, u"Trigger:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTrigger.Wrap( -1 )
		sizer1.Add( self.labelTrigger, 30, wx.ALL, 5 )
		
		self.labelCondition = wx.StaticText( self, wx.ID_ANY, u"Condition Switch:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelCondition.Wrap( -1 )
		sizer1.Add( self.labelCondition, 35, wx.ALL, 5 )
		
		staticSizerCommonEvents.Add( sizer1, 0, wx.EXPAND, 5 )
		
		sizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textCtrlName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer2.Add( self.textCtrlName, 35, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		comboBoxTriggerChoices = [ u"None", u"Autorun", u"Parallel" ]
		self.comboBoxTrigger = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxTriggerChoices, 0 )
		self.comboBoxTrigger.SetSelection( 0 )
		sizer2.Add( self.comboBoxTrigger, 30, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		comboBoxConditionChoices = []
		self.comboBoxCondition = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxConditionChoices, 0 )
		sizer2.Add( self.comboBoxCondition, 35, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		staticSizerCommonEvents.Add( sizer2, 0, wx.EXPAND, 5 )
		
		listBoxPageChoices = [ u">@" ]
		self.listBoxPage = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxPageChoices, 0 )
		staticSizerCommonEvents.Add( self.listBoxPage, 1, wx.ALL|wx.EXPAND, 5 )
		
		MainSizer.Add( staticSizerCommonEvents, 75, wx.EXPAND|wx.ALL, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		# Connect Events
		self.listBoxCommonEvents.Bind( wx.EVT_LISTBOX, self.listBoxCommonEvents_SelectionChanged )
		self.buttonMaximum.Bind( wx.EVT_BUTTON, self.buttonMaximum_Clicked )
		self.textCtrlName.Bind( wx.EVT_TEXT, self.textCtrlName_ValueChanged )
		self.comboBoxTrigger.Bind( wx.EVT_CHOICE, self.comboBoxTrigger_SelectionChanged )
		self.comboBoxCondition.Bind( wx.EVT_LEFT_DOWN, self.comboBoxCondition_Clicked )
		self.listBoxPage.Bind( wx.EVT_LISTBOX, self.listBoxPage_SelectionChanged )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def listBoxCommonEvents_SelectionChanged( self, event ):
		event.Skip()
	
	def buttonMaximum_Clicked( self, event ):
		event.Skip()
	
	def textCtrlName_ValueChanged( self, event ):
		event.Skip()
	
	def comboBoxTrigger_SelectionChanged( self, event ):
		event.Skip()
	
	def comboBoxCondition_Clicked( self, event ):
		event.Skip()
	
	def listBoxPage_SelectionChanged( self, event ):
		event.Skip()
	

###########################################################################
## Class System_Panel
###########################################################################

class System_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelInitialParty = wx.StaticText( self, wx.ID_ANY, u"Initial Party:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelInitialParty.Wrap( -1 )
		sizer1.Add( self.labelInitialParty, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.listCtrlInitialParty = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		sizer1.Add( self.listCtrlInitialParty, 40, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelElements = wx.StaticText( self, wx.ID_ANY, u"Element Names:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelElements.Wrap( -1 )
		sizer1.Add( self.labelElements, 0, wx.ALL|wx.EXPAND, 5 )
		
		listBoxElementsChoices = []
		self.listBoxElements = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxElementsChoices, 0 )
		sizer1.Add( self.listBoxElements, 60, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.textControlElementName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer1.Add( self.textControlElementName, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonMaximum = wx.Button( self, wx.ID_ANY, u"Change Maximum...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer1.Add( self.buttonMaximum, 0, wx.ALL|wx.EXPAND, 5 )
		
		MainSizer.Add( sizer1, 25, wx.EXPAND, 5 )
		
		sizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"System Graphics / BGM / SE / ME" ), wx.HORIZONTAL )
		
		sizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelWindowskinGraphic = wx.StaticText( self, wx.ID_ANY, u"Windowskin Graphic:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelWindowskinGraphic.Wrap( -1 )
		sizer4.Add( self.labelWindowskinGraphic, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxWindowskinGraphicChoices = []
		self.comboBoxWindowskinGraphic = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxWindowskinGraphicChoices, 0 )
		sizer4.Add( self.comboBoxWindowskinGraphic, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelTitleGraphic = wx.StaticText( self, wx.ID_ANY, u"Title Graphic:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTitleGraphic.Wrap( -1 )
		sizer4.Add( self.labelTitleGraphic, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxTitleGraphicChoices = []
		self.comboBoxTitleGraphic = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxTitleGraphicChoices, 0 )
		sizer4.Add( self.comboBoxTitleGraphic, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelGameoverGraphic = wx.StaticText( self, wx.ID_ANY, u"Gameover Graphic:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelGameoverGraphic.Wrap( -1 )
		sizer4.Add( self.labelGameoverGraphic, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxGameoverGraphicChoices = []
		self.comboBoxGameoverGraphic = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxGameoverGraphicChoices, 0 )
		sizer4.Add( self.comboBoxGameoverGraphic, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelBattleTransitionGraphic = wx.StaticText( self, wx.ID_ANY, u"Battle Transition Graphic:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBattleTransitionGraphic.Wrap( -1 )
		sizer4.Add( self.labelBattleTransitionGraphic, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxBattleTransitionGraphicChoices = []
		self.comboBoxBattleTransitionGraphic = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxBattleTransitionGraphicChoices, 0 )
		sizer4.Add( self.comboBoxBattleTransitionGraphic, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelTitleBGM = wx.StaticText( self, wx.ID_ANY, u"Title BGM:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTitleBGM.Wrap( -1 )
		sizer4.Add( self.labelTitleBGM, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxTitleBGMChoices = []
		self.comboBoxTitleBGM = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxTitleBGMChoices, 0 )
		sizer4.Add( self.comboBoxTitleBGM, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelBattleBGM = wx.StaticText( self, wx.ID_ANY, u"Battle BGM:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBattleBGM.Wrap( -1 )
		sizer4.Add( self.labelBattleBGM, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxBattleBGMChoices = []
		self.comboBoxBattleBGM = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxBattleBGMChoices, 0 )
		sizer4.Add( self.comboBoxBattleBGM, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelBattleEndME = wx.StaticText( self, wx.ID_ANY, u"Battle End ME:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBattleEndME.Wrap( -1 )
		sizer4.Add( self.labelBattleEndME, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxBattleEndMEChoices = []
		self.comboBoxBattleEndME = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxBattleEndMEChoices, 0 )
		sizer4.Add( self.comboBoxBattleEndME, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelGameoverME = wx.StaticText( self, wx.ID_ANY, u"Gameover ME:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelGameoverME.Wrap( -1 )
		sizer4.Add( self.labelGameoverME, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxGameoverMEChoices = []
		self.comboBoxGameoverME = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxGameoverMEChoices, 0 )
		sizer4.Add( self.comboBoxGameoverME, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelCursorSE = wx.StaticText( self, wx.ID_ANY, u"Cursor SE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelCursorSE.Wrap( -1 )
		sizer4.Add( self.labelCursorSE, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxCursorSEChoices = []
		self.comboBoxCursorSE = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxCursorSEChoices, 0 )
		sizer4.Add( self.comboBoxCursorSE, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelDecisionSE = wx.StaticText( self, wx.ID_ANY, u"Decision SE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelDecisionSE.Wrap( -1 )
		sizer4.Add( self.labelDecisionSE, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxDecisionSEChoices = []
		self.comboBoxDecisionSE = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxDecisionSEChoices, 0 )
		sizer4.Add( self.comboBoxDecisionSE, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizer2.Add( sizer4, 1, wx.EXPAND, 5 )
		
		sizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelCancelSE = wx.StaticText( self, wx.ID_ANY, u"Cancel SE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelCancelSE.Wrap( -1 )
		sizer5.Add( self.labelCancelSE, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxCancelSEChoices = []
		self.comboBoxCancelSE = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxCancelSEChoices, 0 )
		sizer5.Add( self.comboBoxCancelSE, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelBuzzerSE = wx.StaticText( self, wx.ID_ANY, u"Buzzer SE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBuzzerSE.Wrap( -1 )
		sizer5.Add( self.labelBuzzerSE, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxBuzzerSEChoices = []
		self.comboBoxBuzzerSE = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxBuzzerSEChoices, 0 )
		sizer5.Add( self.comboBoxBuzzerSE, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelEquipSE = wx.StaticText( self, wx.ID_ANY, u"Equip SE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelEquipSE.Wrap( -1 )
		sizer5.Add( self.labelEquipSE, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxEquipSEChoices = []
		self.comboBoxEquipSE = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxEquipSEChoices, 0 )
		sizer5.Add( self.comboBoxEquipSE, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelShopSE = wx.StaticText( self, wx.ID_ANY, u"Shop SE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelShopSE.Wrap( -1 )
		sizer5.Add( self.labelShopSE, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxShopSEChoices = []
		self.comboBoxShopSE = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxShopSEChoices, 0 )
		sizer5.Add( self.comboBoxShopSE, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelSaveSE = wx.StaticText( self, wx.ID_ANY, u"Save SE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelSaveSE.Wrap( -1 )
		sizer5.Add( self.labelSaveSE, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxSaveSEChoices = []
		self.comboBoxSaveSE = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxSaveSEChoices, 0 )
		sizer5.Add( self.comboBoxSaveSE, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelLoadSE = wx.StaticText( self, wx.ID_ANY, u"Load SE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelLoadSE.Wrap( -1 )
		sizer5.Add( self.labelLoadSE, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxLoadSEChoices = []
		self.comboBoxLoadSE = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxLoadSEChoices, 0 )
		sizer5.Add( self.comboBoxLoadSE, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelBattleStartSE = wx.StaticText( self, wx.ID_ANY, u"Battle Start SE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBattleStartSE.Wrap( -1 )
		sizer5.Add( self.labelBattleStartSE, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxBattleStartSEChoices = []
		self.comboBoxBattleStartSE = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxBattleStartSEChoices, 0 )
		sizer5.Add( self.comboBoxBattleStartSE, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelEscapeSE = wx.StaticText( self, wx.ID_ANY, u"Escape SE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelEscapeSE.Wrap( -1 )
		sizer5.Add( self.labelEscapeSE, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxEscapeSEChoices = []
		self.comboBoxEscapeSE = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxEscapeSEChoices, 0 )
		sizer5.Add( self.comboBoxEscapeSE, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelActorCollapseSE = wx.StaticText( self, wx.ID_ANY, u"Actor Collapse SE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelActorCollapseSE.Wrap( -1 )
		sizer5.Add( self.labelActorCollapseSE, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxActorCollapseSEChoices = []
		self.comboBoxActorCollapseSE = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxActorCollapseSEChoices, 0 )
		sizer5.Add( self.comboBoxActorCollapseSE, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelEnemyCollapseSE = wx.StaticText( self, wx.ID_ANY, u"Enemy Collapse SE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelEnemyCollapseSE.Wrap( -1 )
		sizer5.Add( self.labelEnemyCollapseSE, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxEnemyCollapseSEChoices = []
		self.comboBoxEnemyCollapseSE = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxEnemyCollapseSEChoices, 0 )
		sizer5.Add( self.comboBoxEnemyCollapseSE, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizer2.Add( sizer5, 1, wx.EXPAND, 5 )
		
		MainSizer.Add( sizer2, 45, wx.EXPAND|wx.ALL, 5 )
		
		sizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Words" ), wx.HORIZONTAL )
		
		sizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelGold = wx.StaticText( self, wx.ID_ANY, u"G (currency):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelGold.Wrap( -1 )
		sizer6.Add( self.labelGold, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlGold = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer6.Add( self.textCtrlGold, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelHP = wx.StaticText( self, wx.ID_ANY, u"HP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelHP.Wrap( -1 )
		sizer6.Add( self.labelHP, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlHP = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer6.Add( self.textCtrlHP, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelSP = wx.StaticText( self, wx.ID_ANY, u"SP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelSP.Wrap( -1 )
		sizer6.Add( self.labelSP, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlSP = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer6.Add( self.textCtrlSP, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelStr = wx.StaticText( self, wx.ID_ANY, u"STR:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelStr.Wrap( -1 )
		sizer6.Add( self.labelStr, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlStr = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer6.Add( self.textCtrlStr, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelDex = wx.StaticText( self, wx.ID_ANY, u"DEX:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelDex.Wrap( -1 )
		sizer6.Add( self.labelDex, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlDex = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer6.Add( self.textCtrlDex, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelAgi = wx.StaticText( self, wx.ID_ANY, u"AGI:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAgi.Wrap( -1 )
		sizer6.Add( self.labelAgi, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlAgi = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer6.Add( self.textCtrlAgi, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelInt = wx.StaticText( self, wx.ID_ANY, u"INT:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelInt.Wrap( -1 )
		sizer6.Add( self.labelInt, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlInt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer6.Add( self.textCtrlInt, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelAtk = wx.StaticText( self, wx.ID_ANY, u"ATK:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAtk.Wrap( -1 )
		sizer6.Add( self.labelAtk, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlAtk = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer6.Add( self.textCtrlAtk, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelPdef = wx.StaticText( self, wx.ID_ANY, u"PDEF:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPdef.Wrap( -1 )
		sizer6.Add( self.labelPdef, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlPdef = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer6.Add( self.textCtrlPdef, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelMdef = wx.StaticText( self, wx.ID_ANY, u"MDEF:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMdef.Wrap( -1 )
		sizer6.Add( self.labelMdef, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlMdef = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer6.Add( self.textCtrlMdef, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer3.Add( sizer6, 1, wx.EXPAND, 5 )
		
		sizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelWeapon = wx.StaticText( self, wx.ID_ANY, u"Weapon:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelWeapon.Wrap( -1 )
		sizer7.Add( self.labelWeapon, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlWeapon = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer7.Add( self.textCtrlWeapon, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelShield = wx.StaticText( self, wx.ID_ANY, u"Shield:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelShield.Wrap( -1 )
		sizer7.Add( self.labelShield, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlShield = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer7.Add( self.textCtrlShield, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelHelmet = wx.StaticText( self, wx.ID_ANY, u"Helmet:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelHelmet.Wrap( -1 )
		sizer7.Add( self.labelHelmet, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlHelmet = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer7.Add( self.textCtrlHelmet, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelBodyArmor = wx.StaticText( self, wx.ID_ANY, u"Body Armor:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBodyArmor.Wrap( -1 )
		sizer7.Add( self.labelBodyArmor, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlBodyArmor = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer7.Add( self.textCtrlBodyArmor, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelAccessory = wx.StaticText( self, wx.ID_ANY, u"Accessory:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAccessory.Wrap( -1 )
		sizer7.Add( self.labelAccessory, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlAccessory = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer7.Add( self.textCtrlAccessory, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelAttack = wx.StaticText( self, wx.ID_ANY, u"Attack:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAttack.Wrap( -1 )
		sizer7.Add( self.labelAttack, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlAttack = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer7.Add( self.textCtrlAttack, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelSkill = wx.StaticText( self, wx.ID_ANY, u"Skill:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelSkill.Wrap( -1 )
		sizer7.Add( self.labelSkill, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlSkill = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer7.Add( self.textCtrlSkill, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelDefend = wx.StaticText( self, wx.ID_ANY, u"Defend:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelDefend.Wrap( -1 )
		sizer7.Add( self.labelDefend, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlDefend = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer7.Add( self.textCtrlDefend, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelItem = wx.StaticText( self, wx.ID_ANY, u"Item:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelItem.Wrap( -1 )
		sizer7.Add( self.labelItem, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlItem = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer7.Add( self.textCtrlItem, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelEquip = wx.StaticText( self, wx.ID_ANY, u"Equip:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelEquip.Wrap( -1 )
		sizer7.Add( self.labelEquip, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlEquip = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer7.Add( self.textCtrlEquip, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer3.Add( sizer7, 1, wx.EXPAND, 5 )
		
		MainSizer.Add( sizer3, 30, wx.EXPAND|wx.ALL, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		# Connect Events
		self.listCtrlInitialParty.Bind( wx.EVT_LEFT_DCLICK, self.listCtrlInitialParty_DoubleClicked )
		self.listCtrlInitialParty.Bind( wx.EVT_LIST_DELETE_ITEM, self.listCtrlInitialParty_ItemDeleted )
		self.listBoxElements.Bind( wx.EVT_LISTBOX, self.listBoxElements_SelectionChanged )
		self.textControlElementName.Bind( wx.EVT_TEXT, self.textCtrlElement_TextChanged )
		self.buttonMaximum.Bind( wx.EVT_BUTTON, self.buttonMaximum_Clicked )
		self.comboBoxWindowskinGraphic.Bind( wx.EVT_LEFT_DOWN, self.comboBoxWindowskinGraphic_Clicked )
		self.comboBoxTitleGraphic.Bind( wx.EVT_LEFT_DOWN, self.comboBoxTitleGraphic_Clicked )
		self.comboBoxGameoverGraphic.Bind( wx.EVT_LEFT_DOWN, self.comboBoxGameoverGraphic_Clciked )
		self.comboBoxBattleTransitionGraphic.Bind( wx.EVT_LEFT_DOWN, self.comboBoxBattleTransitionGraphic_Clicked )
		self.comboBoxTitleBGM.Bind( wx.EVT_LEFT_DOWN, self.comboBoxTitleBGM_Clicked )
		self.comboBoxBattleBGM.Bind( wx.EVT_LEFT_DOWN, self.comboBoxBattleBGM_Clicked )
		self.comboBoxBattleEndME.Bind( wx.EVT_LEFT_DOWN, self.comboBoxBattleEndME_Clicked )
		self.comboBoxGameoverME.Bind( wx.EVT_LEFT_DOWN, self.comboBoxGameoverME_Clicked )
		self.comboBoxCursorSE.Bind( wx.EVT_LEFT_DOWN, self.comboBoxCursorSE_Clicked )
		self.comboBoxDecisionSE.Bind( wx.EVT_LEFT_DOWN, self.comboBoxDecisionSE_Clicked )
		self.comboBoxCancelSE.Bind( wx.EVT_LEFT_DOWN, self.comboBoxCancelSE_Clicked )
		self.comboBoxBuzzerSE.Bind( wx.EVT_LEFT_DOWN, self.comboBoxBuzzerSE_Clicked )
		self.comboBoxEquipSE.Bind( wx.EVT_LEFT_DOWN, self.comboBoxEquipSE_Clicked )
		self.comboBoxShopSE.Bind( wx.EVT_LEFT_DOWN, self.comboBoxShopSE_Clicked )
		self.comboBoxSaveSE.Bind( wx.EVT_LEFT_DOWN, self.comboBoxSaveSE_Clicked )
		self.comboBoxLoadSE.Bind( wx.EVT_LEFT_DOWN, self.comboBoxLoadSE_Clicked )
		self.comboBoxBattleStartSE.Bind( wx.EVT_LEFT_DOWN, self.comboBoxBattleStartSE_Clicked )
		self.comboBoxEscapeSE.Bind( wx.EVT_LEFT_DOWN, self.comboBoxEscapeSE_Clicked )
		self.comboBoxActorCollapseSE.Bind( wx.EVT_LEFT_DOWN, self.comboBoxActorCollapseSE_Clicked )
		self.comboBoxEnemyCollapseSE.Bind( wx.EVT_LEFT_DOWN, self.comboBoxEnemyCollapseSE_Clicked )
		self.textCtrlGold.Bind( wx.EVT_TEXT, self.textCtrlGold_TextChanged )
		self.textCtrlHP.Bind( wx.EVT_TEXT, self.textCtrlHP_TextChanged )
		self.textCtrlSP.Bind( wx.EVT_TEXT, self.textCtrlSP_TextChanged )
		self.textCtrlStr.Bind( wx.EVT_TEXT, self.textCtrlStr_TextChanged )
		self.textCtrlDex.Bind( wx.EVT_TEXT, self.textCtrlDex_TextChanged )
		self.textCtrlAgi.Bind( wx.EVT_TEXT, self.textCtrlAgi_TextChanged )
		self.textCtrlInt.Bind( wx.EVT_TEXT, self.textCtrlInt_TextChanged )
		self.textCtrlAtk.Bind( wx.EVT_TEXT, self.textCtrlAtk_TextChanged )
		self.textCtrlPdef.Bind( wx.EVT_TEXT, self.textCtrlPdef_TextChanged )
		self.textCtrlMdef.Bind( wx.EVT_TEXT, self.textCtrlMdef_TextChanged )
		self.textCtrlWeapon.Bind( wx.EVT_TEXT, self.textCtrlWeapon_TextChanged )
		self.textCtrlShield.Bind( wx.EVT_TEXT, self.textCtrlShield_TextChanged )
		self.textCtrlHelmet.Bind( wx.EVT_TEXT, self.textCtrlHelmet_TextChanged )
		self.textCtrlBodyArmor.Bind( wx.EVT_TEXT, self.textCtrlBodyArmor_TextChanged )
		self.textCtrlAccessory.Bind( wx.EVT_TEXT, self.textCtrlAccessory_TextChanged )
		self.textCtrlAttack.Bind( wx.EVT_TEXT, self.textCtrlAttack_TextChanged )
		self.textCtrlSkill.Bind( wx.EVT_TEXT, self.textCtrlSkill_TextChanged )
		self.textCtrlDefend.Bind( wx.EVT_TEXT, self.textCtrlDefend_TextChanged )
		self.textCtrlItem.Bind( wx.EVT_TEXT, self.textCtrlItem_TextChanged )
		self.textCtrlEquip.Bind( wx.EVT_TEXT, self.textCtrlEquip_TextChanged )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def listCtrlInitialParty_DoubleClicked( self, event ):
		event.Skip()
	
	def listCtrlInitialParty_ItemDeleted( self, event ):
		event.Skip()
	
	def listBoxElements_SelectionChanged( self, event ):
		event.Skip()
	
	def textCtrlElement_TextChanged( self, event ):
		event.Skip()
	
	def buttonMaximum_Clicked( self, event ):
		event.Skip()
	
	def comboBoxWindowskinGraphic_Clicked( self, event ):
		event.Skip()
	
	def comboBoxTitleGraphic_Clicked( self, event ):
		event.Skip()
	
	def comboBoxGameoverGraphic_Clciked( self, event ):
		event.Skip()
	
	def comboBoxBattleTransitionGraphic_Clicked( self, event ):
		event.Skip()
	
	def comboBoxTitleBGM_Clicked( self, event ):
		event.Skip()
	
	def comboBoxBattleBGM_Clicked( self, event ):
		event.Skip()
	
	def comboBoxBattleEndME_Clicked( self, event ):
		event.Skip()
	
	def comboBoxGameoverME_Clicked( self, event ):
		event.Skip()
	
	def comboBoxCursorSE_Clicked( self, event ):
		event.Skip()
	
	def comboBoxDecisionSE_Clicked( self, event ):
		event.Skip()
	
	def comboBoxCancelSE_Clicked( self, event ):
		event.Skip()
	
	def comboBoxBuzzerSE_Clicked( self, event ):
		event.Skip()
	
	def comboBoxEquipSE_Clicked( self, event ):
		event.Skip()
	
	def comboBoxShopSE_Clicked( self, event ):
		event.Skip()
	
	def comboBoxSaveSE_Clicked( self, event ):
		event.Skip()
	
	def comboBoxLoadSE_Clicked( self, event ):
		event.Skip()
	
	def comboBoxBattleStartSE_Clicked( self, event ):
		event.Skip()
	
	def comboBoxEscapeSE_Clicked( self, event ):
		event.Skip()
	
	def comboBoxActorCollapseSE_Clicked( self, event ):
		event.Skip()
	
	def comboBoxEnemyCollapseSE_Clicked( self, event ):
		event.Skip()
	
	def textCtrlGold_TextChanged( self, event ):
		event.Skip()
	
	def textCtrlHP_TextChanged( self, event ):
		event.Skip()
	
	def textCtrlSP_TextChanged( self, event ):
		event.Skip()
	
	def textCtrlStr_TextChanged( self, event ):
		event.Skip()
	
	def textCtrlDex_TextChanged( self, event ):
		event.Skip()
	
	def textCtrlAgi_TextChanged( self, event ):
		event.Skip()
	
	def textCtrlInt_TextChanged( self, event ):
		event.Skip()
	
	def textCtrlAtk_TextChanged( self, event ):
		event.Skip()
	
	def textCtrlPdef_TextChanged( self, event ):
		event.Skip()
	
	def textCtrlMdef_TextChanged( self, event ):
		event.Skip()
	
	def textCtrlWeapon_TextChanged( self, event ):
		event.Skip()
	
	def textCtrlShield_TextChanged( self, event ):
		event.Skip()
	
	def textCtrlHelmet_TextChanged( self, event ):
		event.Skip()
	
	def textCtrlBodyArmor_TextChanged( self, event ):
		event.Skip()
	
	def textCtrlAccessory_TextChanged( self, event ):
		event.Skip()
	
	def textCtrlAttack_TextChanged( self, event ):
		event.Skip()
	
	def textCtrlSkill_TextChanged( self, event ):
		event.Skip()
	
	def textCtrlDefend_TextChanged( self, event ):
		event.Skip()
	
	def textCtrlItem_TextChanged( self, event ):
		event.Skip()
	
	def textCtrlEquip_TextChanged( self, event ):
		event.Skip()
	

###########################################################################
## Class ChangeMaximum_Dialog
###########################################################################

class ChangeMaximum_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Change Maximum...", pos = wx.DefaultPosition, size = wx.Size( 176,95 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.Size( -1,-1 ) )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.labelMaximum = wx.StaticText( self, wx.ID_ANY, u"Maximum:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMaximum.Wrap( -1 )
		MainSizer.Add( self.labelMaximum, 0, wx.ALL, 5 )
		
		self.spinCtrlMaximum = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SP_ARROW_KEYS|wx.SP_WRAP, 0, 65535, 0 )
		MainSizer.Add( self.spinCtrlMaximum, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer1.Add( self.buttonOK, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer1.Add( self.buttonCancel, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		MainSizer.Add( sizer1, 1, wx.ALIGN_BOTTOM|wx.FIXED_MINSIZE|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class Skill_Dialog
###########################################################################

class Skill_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Skill", pos = wx.DefaultPosition, size = wx.Size( 244,160 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.Size( -1,-1 ) )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.labelLevel = wx.StaticText( self, wx.ID_ANY, u"Level:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelLevel.Wrap( -1 )
		MainSizer.Add( self.labelLevel, 0, wx.ALL, 5 )
		
		self.spinCtrlLevel = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 65,-1 ), wx.SP_ARROW_KEYS|wx.SP_WRAP, 0, 65535, 1 )
		self.spinCtrlLevel.SetToolTipString( u"Level of the character when the skill is mastered" )
		
		MainSizer.Add( self.spinCtrlLevel, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelSkills = wx.StaticText( self, wx.ID_ANY, u"Skill to Learn:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelSkills.Wrap( -1 )
		MainSizer.Add( self.labelSkills, 0, wx.ALL, 5 )
		
		comboBoxSkillsChoices = []
		self.comboBoxSkills = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxSkillsChoices, 0 )
		self.comboBoxSkills.SetSelection( 0 )
		self.comboBoxSkills.SetToolTipString( u"The skill to learn" )
		
		MainSizer.Add( self.comboBoxSkills, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer1.SetMinSize( wx.Size( 1,1 ) ) 
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.buttonCancel.SetToolTipString( u"Cancel changes and return" )
		
		sizer1.Add( self.buttonCancel, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.buttonOK.SetToolTipString( u"Add skill to learn" )
		
		sizer1.Add( self.buttonOK, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		MainSizer.Add( sizer1, 1, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ExpCurve_Dialog
###########################################################################

class ExpCurve_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		MainSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ActorParameters_Dialog
###########################################################################

class ActorParameters_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		MainSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ChooseGraphic_Dialog
###########################################################################

class ChooseGraphic_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		MainSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class EnemyAction_Dialog
###########################################################################

class EnemyAction_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		MainSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class EventCommands_Dialog
###########################################################################

class EventCommands_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		MainSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class EventCondition_Dialog
###########################################################################

class EventCondition_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		MainSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class AnimationTiming_Dialog
###########################################################################

class AnimationTiming_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		MainSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class AnimationTweening_Dialog
###########################################################################

class AnimationTweening_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		MainSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class AnimationEntireSlide_Dialog
###########################################################################

class AnimationEntireSlide_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		MainSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class AnimationCellBatch_Dialog
###########################################################################

class AnimationCellBatch_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		MainSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ChooseFogGraphic_Dialog
###########################################################################

class ChooseFogGraphic_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		MainSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ChooseActor_Dialog
###########################################################################

class ChooseActor_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		MainSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ChooseAudio_Dialog
###########################################################################

class ChooseAudio_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		MainSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ChooseSwitch_Dialog
###########################################################################

class ChooseSwitch_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		MainSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ChooseVariable_Dialog
###########################################################################

class ChooseVariable_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		MainSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

