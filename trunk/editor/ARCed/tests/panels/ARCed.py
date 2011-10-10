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
#import Actors_Panel as poop

###########################################################################
## Class Actors_Panel
###########################################################################

class Actors_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		ActorListSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapActors = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Actors.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
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
		
		self.bitmapCharacterGraphic = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Character.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER )
		sizer3.Add( self.bitmapCharacterGraphic, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelBattlerGraphic = wx.StaticText( self, wx.ID_ANY, u"Battler Graphic:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBattlerGraphic.Wrap( -1 )
		sizer3.Add( self.labelBattlerGraphic, 0, wx.ALL, 5 )
		
		self.bitmapBattlerGraphic = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Battler.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER )
		sizer3.Add( self.bitmapBattlerGraphic, 0, wx.ALL, 5 )
		
		sizer1.Add( sizer3, 25, wx.EXPAND, 5 )
		
		staticSizerActors.Add( sizer1, 35, wx.EXPAND, 5 )
		
		sizer2 = wx.BoxSizer( wx.VERTICAL )
		
		sizerParameters = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Parameters" ), wx.HORIZONTAL )
		
		sizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapMaxHP = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/MaxHP.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER )
		sizer6.Add( self.bitmapMaxHP, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.bitmapSTR = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Str.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER )
		sizer6.Add( self.bitmapSTR, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.bitmapAGI = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Agi.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER )
		sizer6.Add( self.bitmapAGI, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizerParameters.Add( sizer6, 1, wx.EXPAND, 5 )
		
		sizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapMaxSP = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/MaxSP.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER )
		sizer7.Add( self.bitmapMaxSP, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.bitmapDEX = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Dex.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER )
		sizer7.Add( self.bitmapDEX, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.bitmapINT = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Int.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER )
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
		poop.buttonMaximum_Clicked(self, event)
	
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
		
		self.bitmapClasses = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Classes.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
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
		
		self.bitmapSkills = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Skills.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
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
		
		self.bitmapItems = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Items.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
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
## Class Armors_Panel
###########################################################################

class Armors_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		ArmorsListSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapArmors = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Armors.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
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
## Class Weapons_Panel
###########################################################################

class Weapons_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		WeaponsListSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapWeapons = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Weapons.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
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
## Class Enemies_Panel
###########################################################################

class Enemies_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		EnemiesListSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapEnemies = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Enemies.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
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
		
		self.bitmapBattlerGraphic = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Ghost.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER )
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
		
		self.bitmapTroops = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Troops.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
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
		
		self.bitmapTroopLayout = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Battleback.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER )
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
		self.listBoxEnemies.Bind( wx.EVT_LISTBOX, self.listBoxEnemies_SelectionChanged )
		self.buttonNewPage.Bind( wx.EVT_BUTTON, self.buttonNewEventPage_Click )
		self.buttonCopyPage.Bind( wx.EVT_BUTTON, self.buttonCopyEventPage_Click )
		self.buttonPastePage.Bind( wx.EVT_BUTTON, self.buttonPasteEventPage_Click )
		self.buttonDeletePage.Bind( wx.EVT_BUTTON, self.buttonDeleteEventPage_Click )
		self.buttonClearPage.Bind( wx.EVT_BUTTON, self.buttonClearEventPage_Click )
		self.comboBoxCondition.Bind( wx.EVT_LEFT_UP, self.comboBoxCondition_Clicked )
		self.comboBoxSpan.Bind( wx.EVT_CHOICE, self.comboBoxSpan_ValueChanged )
		self.listBoxEvents.Bind( wx.EVT_LEFT_DCLICK, self.listBoxEvents_DoubleClick )
	
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
	
	def listBoxEnemies_SelectionChanged( self, event ):
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
	
	def listBoxEvents_DoubleClick( self, event ):
		event.Skip()
	

###########################################################################
## Class States_Panel
###########################################################################

class States_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		StatesListSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapStates = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/States.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
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
		
		self.bitmapAnimations = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Animations.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
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
		
		self.bitmapPallette = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/AnimationSample1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER )
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
		
		self.bitmapAnimationFrames = wx.StaticBitmap( self.m_scrolledWindow3, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/AnimationSample2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
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
		
		self.bitmapTilesets = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Tilesets.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
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
		
		self.m_bitmap36 = wx.StaticBitmap( self.m_scrolledWindow4, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/TilesetSample.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 256,-1 ), 0 )
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
		
		self.bitmapCommonEvents = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/CommonEvents.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,26 ), wx.CLIP_CHILDREN|wx.FULL_REPAINT_ON_RESIZE )
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
## Class EventCommands1_Panel
###########################################################################

class EventCommands1_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 400,450 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerLeft = wx.BoxSizer( wx.VERTICAL )
		
		sizerMessages = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Message" ), wx.VERTICAL )
		
		self.buttonShowText = wx.Button( self, wx.ID_ANY, u"Show Text...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		sizerMessages.Add( self.buttonShowText, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonShowChoices = wx.Button( self, wx.ID_ANY, u"Show Choices...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		sizerMessages.Add( self.buttonShowChoices, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonInputNumber = wx.Button( self, wx.ID_ANY, u"Input Number...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		sizerMessages.Add( self.buttonInputNumber, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonChangeTextOptions = wx.Button( self, wx.ID_ANY, u"Change Text Options...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		sizerMessages.Add( self.buttonChangeTextOptions, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonChangeWindowskin = wx.Button( self, wx.ID_ANY, u"Change Windowskin...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerMessages.Add( self.buttonChangeWindowskin, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		sizerLeft.Add( sizerMessages, 0, wx.ALL|wx.EXPAND, 5 )
		
		sizerFlowControl = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Flow Control" ), wx.VERTICAL )
		
		self.buttonConditionalBranch = wx.Button( self, wx.ID_ANY, u"Conditional Branch...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerFlowControl.Add( self.buttonConditionalBranch, 0, wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.buttonWait = wx.Button( self, wx.ID_ANY, u"Wait...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerFlowControl.Add( self.buttonWait, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonLoop = wx.Button( self, wx.ID_ANY, u"Loop", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerFlowControl.Add( self.buttonLoop, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonBreakLoop = wx.Button( self, wx.ID_ANY, u"Break Loop", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerFlowControl.Add( self.buttonBreakLoop, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonExitEventProcessing = wx.Button( self, wx.ID_ANY, u"Exit Event Processing", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerFlowControl.Add( self.buttonExitEventProcessing, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonCallCommonEvent = wx.Button( self, wx.ID_ANY, u"Call Common Event...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerFlowControl.Add( self.buttonCallCommonEvent, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonLabel = wx.Button( self, wx.ID_ANY, u"Label...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerFlowControl.Add( self.buttonLabel, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonJumpToLabel = wx.Button( self, wx.ID_ANY, u"Jump To Label...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerFlowControl.Add( self.buttonJumpToLabel, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonComment = wx.Button( self, wx.ID_ANY, u"Comment...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerFlowControl.Add( self.buttonComment, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		sizerLeft.Add( sizerFlowControl, 0, wx.EXPAND|wx.ALL, 5 )
		
		sizerScript = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Advanced" ), wx.VERTICAL )
		
		self.buttonScript = wx.Button( self, wx.ID_ANY, u"Script...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerScript.Add( self.buttonScript, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizerLeft.Add( sizerScript, 0, wx.EXPAND|wx.ALL, 5 )
		
		MainSizer.Add( sizerLeft, 1, wx.EXPAND, 5 )
		
		sizerRight = wx.BoxSizer( wx.VERTICAL )
		
		sizerGameProgression = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Game Progression" ), wx.VERTICAL )
		
		self.buttonControlSwitches = wx.Button( self, wx.ID_ANY, u"Control Switches...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		sizerGameProgression.Add( self.buttonControlSwitches, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonControlVariables = wx.Button( self, wx.ID_ANY, u"Control Variables...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		sizerGameProgression.Add( self.buttonControlVariables, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonControlSelfSwitch = wx.Button( self, wx.ID_ANY, u"Control Self-Switch...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		sizerGameProgression.Add( self.buttonControlSelfSwitch, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonControlTimer = wx.Button( self, wx.ID_ANY, u"Control Timer...", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		sizerGameProgression.Add( self.buttonControlTimer, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		sizerRight.Add( sizerGameProgression, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sizerAudio = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Audio" ), wx.VERTICAL )
		
		self.buttonPlayBGM = wx.Button( self, wx.ID_ANY, u"Play BGM...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerAudio.Add( self.buttonPlayBGM, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonFadeOutBGM = wx.Button( self, wx.ID_ANY, u"Fade Out BGM...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerAudio.Add( self.buttonFadeOutBGM, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonPlayBGS = wx.Button( self, wx.ID_ANY, u"Play BGS...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerAudio.Add( self.buttonPlayBGS, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonFadeOutBGS = wx.Button( self, wx.ID_ANY, u"Fade Out BGS...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerAudio.Add( self.buttonFadeOutBGS, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonMemorizeBGMBGS = wx.Button( self, wx.ID_ANY, u"Memorize BGM/BGS", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerAudio.Add( self.buttonMemorizeBGMBGS, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.m_button158 = wx.Button( self, wx.ID_ANY, u"Restore BGS/BGM", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerAudio.Add( self.m_button158, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonPlayME = wx.Button( self, wx.ID_ANY, u"Play ME...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerAudio.Add( self.buttonPlayME, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonPlaySE = wx.Button( self, wx.ID_ANY, u"Play SE...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerAudio.Add( self.buttonPlaySE, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonStopSE = wx.Button( self, wx.ID_ANY, u"Stop SE...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerAudio.Add( self.buttonStopSE, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonChangeBattleBGM = wx.Button( self, wx.ID_ANY, u"Change Battle BGM...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerAudio.Add( self.buttonChangeBattleBGM, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangeBattleEndME = wx.Button( self, wx.ID_ANY, u"Change Battle End ME...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerAudio.Add( self.buttonChangeBattleEndME, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		sizerRight.Add( sizerAudio, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		MainSizer.Add( sizerRight, 1, wx.EXPAND, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		# Connect Events
		self.buttonShowText.Bind( wx.EVT_BUTTON, self.buttonShowText_Clicked )
		self.buttonShowChoices.Bind( wx.EVT_BUTTON, self.buttonShowChoices_Clicked )
		self.buttonInputNumber.Bind( wx.EVT_BUTTON, self.buttonInputNumber_Clicked )
		self.buttonChangeTextOptions.Bind( wx.EVT_BUTTON, self.buttonChangeTextOptions_Clicked )
		self.buttonChangeWindowskin.Bind( wx.EVT_BUTTON, self.buttonChangeWindowskin_Clicked )
		self.buttonConditionalBranch.Bind( wx.EVT_BUTTON, self.buttonConditionalBranch_Clicked )
		self.buttonWait.Bind( wx.EVT_BUTTON, self.buttonWait_Clicked )
		self.buttonLoop.Bind( wx.EVT_BUTTON, self.buttonLoop_Clicked )
		self.buttonBreakLoop.Bind( wx.EVT_BUTTON, self.buttonBreakLoop_Clicked )
		self.buttonExitEventProcessing.Bind( wx.EVT_BUTTON, self.buttonExitEventProcessing_Clicked )
		self.buttonCallCommonEvent.Bind( wx.EVT_BUTTON, self.buttonCallCommonEvent_Clicked )
		self.buttonLabel.Bind( wx.EVT_BUTTON, self.buttonLabel_Clicked )
		self.buttonJumpToLabel.Bind( wx.EVT_BUTTON, self.button_ClickedJumpToLabel )
		self.buttonComment.Bind( wx.EVT_BUTTON, self.buttonComment_Clicked )
		self.buttonScript.Bind( wx.EVT_BUTTON, self.buttonScript_Clicked )
		self.buttonControlSwitches.Bind( wx.EVT_BUTTON, self.buttonControlSwitches_Clicked )
		self.buttonControlVariables.Bind( wx.EVT_BUTTON, self.buttonControlVariables_Clicked )
		self.buttonControlSelfSwitch.Bind( wx.EVT_BUTTON, self.buttonControlSelfSwitch_Clicked )
		self.buttonControlTimer.Bind( wx.EVT_BUTTON, self.buttonControlTimer_Clicked )
		self.buttonPlayBGM.Bind( wx.EVT_BUTTON, self.buttonPlayBGM_Clicked )
		self.buttonFadeOutBGM.Bind( wx.EVT_BUTTON, self.buttonFadeOutBGM_Clicked )
		self.buttonPlayBGS.Bind( wx.EVT_BUTTON, self.buttonPlayBGS_Clicked )
		self.buttonFadeOutBGS.Bind( wx.EVT_BUTTON, self.buttonFadeOutBGS_Clicked )
		self.buttonMemorizeBGMBGS.Bind( wx.EVT_BUTTON, self.buttonMemorizeBGMBGS_Clicked )
		self.m_button158.Bind( wx.EVT_BUTTON, self.buttonRestoreBGMBGS_Clicked )
		self.buttonPlayME.Bind( wx.EVT_BUTTON, self.buttonPlayME_Clicked )
		self.buttonPlaySE.Bind( wx.EVT_BUTTON, self.buttonPlaySE_Clicked )
		self.buttonStopSE.Bind( wx.EVT_BUTTON, self.buttonStopSE_Clicked )
		self.buttonChangeBattleBGM.Bind( wx.EVT_BUTTON, self.buttonChangeBattleBGM_Clicked )
		self.buttonChangeBattleEndME.Bind( wx.EVT_BUTTON, self.buttonChangeBattleEndME_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonShowText_Clicked( self, event ):
		event.Skip()
	
	def buttonShowChoices_Clicked( self, event ):
		event.Skip()
	
	def buttonInputNumber_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeTextOptions_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeWindowskin_Clicked( self, event ):
		event.Skip()
	
	def buttonConditionalBranch_Clicked( self, event ):
		event.Skip()
	
	def buttonWait_Clicked( self, event ):
		event.Skip()
	
	def buttonLoop_Clicked( self, event ):
		event.Skip()
	
	def buttonBreakLoop_Clicked( self, event ):
		event.Skip()
	
	def buttonExitEventProcessing_Clicked( self, event ):
		event.Skip()
	
	def buttonCallCommonEvent_Clicked( self, event ):
		event.Skip()
	
	def buttonLabel_Clicked( self, event ):
		event.Skip()
	
	def button_ClickedJumpToLabel( self, event ):
		event.Skip()
	
	def buttonComment_Clicked( self, event ):
		event.Skip()
	
	def buttonScript_Clicked( self, event ):
		event.Skip()
	
	def buttonControlSwitches_Clicked( self, event ):
		event.Skip()
	
	def buttonControlVariables_Clicked( self, event ):
		event.Skip()
	
	def buttonControlSelfSwitch_Clicked( self, event ):
		event.Skip()
	
	def buttonControlTimer_Clicked( self, event ):
		event.Skip()
	
	def buttonPlayBGM_Clicked( self, event ):
		event.Skip()
	
	def buttonFadeOutBGM_Clicked( self, event ):
		event.Skip()
	
	def buttonPlayBGS_Clicked( self, event ):
		event.Skip()
	
	def buttonFadeOutBGS_Clicked( self, event ):
		event.Skip()
	
	def buttonMemorizeBGMBGS_Clicked( self, event ):
		event.Skip()
	
	def buttonRestoreBGMBGS_Clicked( self, event ):
		event.Skip()
	
	def buttonPlayME_Clicked( self, event ):
		event.Skip()
	
	def buttonPlaySE_Clicked( self, event ):
		event.Skip()
	
	def buttonStopSE_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeBattleBGM_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeBattleEndME_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class EventCommands2_Panel
###########################################################################

class EventCommands2_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 400,450 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerLeft = wx.BoxSizer( wx.VERTICAL )
		
		sizerMovement = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Movement" ), wx.VERTICAL )
		
		self.buttonTransferPlayer = wx.Button( self, wx.ID_ANY, u"Transfer Player...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerMovement.Add( self.buttonTransferPlayer, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonSetMoveRoute = wx.Button( self, wx.ID_ANY, u"Set Move Route...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerMovement.Add( self.buttonSetMoveRoute, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonSentEventLocation = wx.Button( self, wx.ID_ANY, u"Set Event Location...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerMovement.Add( self.buttonSentEventLocation, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonScrollMap = wx.Button( self, wx.ID_ANY, u"Scroll Map...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerMovement.Add( self.buttonScrollMap, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonWaitForMovesCompletion = wx.Button( self, wx.ID_ANY, u"Wait For Move's Completion", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerMovement.Add( self.buttonWaitForMovesCompletion, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		sizerLeft.Add( sizerMovement, 0, wx.ALL|wx.EXPAND, 5 )
		
		sizerScreen = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Screen" ), wx.VERTICAL )
		
		self.buttonPrepareForTransition = wx.Button( self, wx.ID_ANY, u"Prepare For Transition", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerScreen.Add( self.buttonPrepareForTransition, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonExecuteTransition = wx.Button( self, wx.ID_ANY, u"Execute Transition", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerScreen.Add( self.buttonExecuteTransition, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangeScreenTone = wx.Button( self, wx.ID_ANY, u"Change Screen Tone...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerScreen.Add( self.buttonChangeScreenTone, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonScreenFlash = wx.Button( self, wx.ID_ANY, u"Screen Flash...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerScreen.Add( self.buttonScreenFlash, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonScreenShake = wx.Button( self, wx.ID_ANY, u"Screen Shake...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerScreen.Add( self.buttonScreenShake, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		sizerLeft.Add( sizerScreen, 0, wx.EXPAND|wx.ALL, 5 )
		
		sizerParty = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Party" ), wx.VERTICAL )
		
		self.buttonChangePartyMember = wx.Button( self, wx.ID_ANY, u"Change Party Member...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerParty.Add( self.buttonChangePartyMember, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonChangeGold = wx.Button( self, wx.ID_ANY, u"Change Gold...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerParty.Add( self.buttonChangeGold, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangeItem = wx.Button( self, wx.ID_ANY, u"Change Item...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerParty.Add( self.buttonChangeItem, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangeWeapon = wx.Button( self, wx.ID_ANY, u"Change Weapon...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerParty.Add( self.buttonChangeWeapon, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangeArmor = wx.Button( self, wx.ID_ANY, u"Change Armor...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerParty.Add( self.buttonChangeArmor, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizerLeft.Add( sizerParty, 0, wx.EXPAND|wx.ALL, 5 )
		
		MainSizer.Add( sizerLeft, 1, wx.EXPAND, 5 )
		
		sizerRight = wx.BoxSizer( wx.VERTICAL )
		
		sizerMap = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Map" ), wx.VERTICAL )
		
		self.buttonChangeMapSettings = wx.Button( self, wx.ID_ANY, u"Change Map Settings...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerMap.Add( self.buttonChangeMapSettings, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonSetWeatherEffects = wx.Button( self, wx.ID_ANY, u"Set Weather Effects...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerMap.Add( self.buttonSetWeatherEffects, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangeFogColorTone = wx.Button( self, wx.ID_ANY, u"Change Fog Color Tone...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerMap.Add( self.buttonChangeFogColorTone, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangeFogOpacity = wx.Button( self, wx.ID_ANY, u"Change Fog Opacity...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerMap.Add( self.buttonChangeFogOpacity, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangeEncounter = wx.Button( self, wx.ID_ANY, u"Change Encounter...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerMap.Add( self.buttonChangeEncounter, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		sizerRight.Add( sizerMap, 0, wx.EXPAND|wx.ALL, 5 )
		
		sizerSceneControl = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Scene Control" ), wx.VERTICAL )
		
		self.buttonBattleProcessing = wx.Button( self, wx.ID_ANY, u"Battle Processing...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerSceneControl.Add( self.buttonBattleProcessing, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonShopProcessing = wx.Button( self, wx.ID_ANY, u"Shop Processing...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerSceneControl.Add( self.buttonShopProcessing, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonNameInputProcessing = wx.Button( self, wx.ID_ANY, u"Name Input Processing...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerSceneControl.Add( self.buttonNameInputProcessing, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonButtonInputProcessing = wx.Button( self, wx.ID_ANY, u"Button Input Processing...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerSceneControl.Add( self.buttonButtonInputProcessing, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonGameOver = wx.Button( self, wx.ID_ANY, u"Game Over", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerSceneControl.Add( self.buttonGameOver, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonReturnToTitleScreen = wx.Button( self, wx.ID_ANY, u"Return To Title Screen", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerSceneControl.Add( self.buttonReturnToTitleScreen, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangeMenuAccess = wx.Button( self, wx.ID_ANY, u"Change Menu Access...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerSceneControl.Add( self.buttonChangeMenuAccess, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonChangeSaveAccess = wx.Button( self, wx.ID_ANY, u"Change Save Access...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerSceneControl.Add( self.buttonChangeSaveAccess, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonCallMenuScreen = wx.Button( self, wx.ID_ANY, u"Call Menu Screen", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerSceneControl.Add( self.buttonCallMenuScreen, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonCallSaveScreen = wx.Button( self, wx.ID_ANY, u"Call Save Screen", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerSceneControl.Add( self.buttonCallSaveScreen, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		sizerRight.Add( sizerSceneControl, 0, wx.EXPAND|wx.ALL, 5 )
		
		MainSizer.Add( sizerRight, 1, wx.EXPAND, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		# Connect Events
		self.buttonTransferPlayer.Bind( wx.EVT_BUTTON, self.buttonTransferPlayer_Clicked )
		self.buttonSetMoveRoute.Bind( wx.EVT_BUTTON, self.buttonSetMoveRoute_Clicked )
		self.buttonSentEventLocation.Bind( wx.EVT_BUTTON, self.buttonSetEventLocation_Clicked )
		self.buttonScrollMap.Bind( wx.EVT_BUTTON, self.buttonScrollMap_Clicked )
		self.buttonWaitForMovesCompletion.Bind( wx.EVT_BUTTON, self.buttonWaitForMovesCompletion_Clicked )
		self.buttonPrepareForTransition.Bind( wx.EVT_BUTTON, self.buttonPrepareForTransition_Clicked )
		self.buttonExecuteTransition.Bind( wx.EVT_BUTTON, self.buttonExecuteTransition_Clicked )
		self.buttonChangeScreenTone.Bind( wx.EVT_BUTTON, self.buttonChangeScreenTone_Clicked )
		self.buttonScreenFlash.Bind( wx.EVT_BUTTON, self.buttonScreenFlash_Clicked )
		self.buttonScreenShake.Bind( wx.EVT_BUTTON, self.buttonScreenShake_Clicked )
		self.buttonChangePartyMember.Bind( wx.EVT_BUTTON, self.buttonChangePartyMember_Clicked )
		self.buttonChangeGold.Bind( wx.EVT_BUTTON, self.buttonChangeGold_Clicked )
		self.buttonChangeItem.Bind( wx.EVT_BUTTON, self.buttonChangeItem_Clicked )
		self.buttonChangeWeapon.Bind( wx.EVT_BUTTON, self.buttonChangeWeapon_Clicked )
		self.buttonChangeArmor.Bind( wx.EVT_BUTTON, self.buttonArmor_Clicked )
		self.buttonChangeMapSettings.Bind( wx.EVT_BUTTON, self.buttonChangeMapSettings_Clicked )
		self.buttonSetWeatherEffects.Bind( wx.EVT_BUTTON, self.buttonSetWeatherEffects_Clicked )
		self.buttonChangeFogColorTone.Bind( wx.EVT_BUTTON, self.buttonChangeFogColorTone_Clicked )
		self.buttonChangeFogOpacity.Bind( wx.EVT_BUTTON, self.buttonChangeFogOpacity_Clicked )
		self.buttonChangeEncounter.Bind( wx.EVT_BUTTON, self.buttonChangeEncounter_Clicked )
		self.buttonBattleProcessing.Bind( wx.EVT_BUTTON, self.buttonBattleProcessing_Clicked )
		self.buttonShopProcessing.Bind( wx.EVT_BUTTON, self.buttonShopProcessing_Clicked )
		self.buttonNameInputProcessing.Bind( wx.EVT_BUTTON, self.buttonNameInputProcessing_Clicked )
		self.buttonButtonInputProcessing.Bind( wx.EVT_BUTTON, self.buttonButtonInputProcessing_Clicked )
		self.buttonGameOver.Bind( wx.EVT_BUTTON, self.buttonGameOver_Clicked )
		self.buttonReturnToTitleScreen.Bind( wx.EVT_BUTTON, self.buttonReturnToTitleScreen_Clicked )
		self.buttonChangeMenuAccess.Bind( wx.EVT_BUTTON, self.buttonChangeMenuAccess_Clicked )
		self.buttonChangeSaveAccess.Bind( wx.EVT_BUTTON, self.buttonChangeSaveAccess_Clicked )
		self.buttonCallMenuScreen.Bind( wx.EVT_BUTTON, self.buttonCallMenuScreen_Clicked )
		self.buttonCallSaveScreen.Bind( wx.EVT_BUTTON, self.buttonCallSaveScreen_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonTransferPlayer_Clicked( self, event ):
		event.Skip()
	
	def buttonSetMoveRoute_Clicked( self, event ):
		event.Skip()
	
	def buttonSetEventLocation_Clicked( self, event ):
		event.Skip()
	
	def buttonScrollMap_Clicked( self, event ):
		event.Skip()
	
	def buttonWaitForMovesCompletion_Clicked( self, event ):
		event.Skip()
	
	def buttonPrepareForTransition_Clicked( self, event ):
		event.Skip()
	
	def buttonExecuteTransition_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeScreenTone_Clicked( self, event ):
		event.Skip()
	
	def buttonScreenFlash_Clicked( self, event ):
		event.Skip()
	
	def buttonScreenShake_Clicked( self, event ):
		event.Skip()
	
	def buttonChangePartyMember_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeGold_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeItem_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeWeapon_Clicked( self, event ):
		event.Skip()
	
	def buttonArmor_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeMapSettings_Clicked( self, event ):
		event.Skip()
	
	def buttonSetWeatherEffects_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeFogColorTone_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeFogOpacity_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeEncounter_Clicked( self, event ):
		event.Skip()
	
	def buttonBattleProcessing_Clicked( self, event ):
		event.Skip()
	
	def buttonShopProcessing_Clicked( self, event ):
		event.Skip()
	
	def buttonNameInputProcessing_Clicked( self, event ):
		event.Skip()
	
	def buttonButtonInputProcessing_Clicked( self, event ):
		event.Skip()
	
	def buttonGameOver_Clicked( self, event ):
		event.Skip()
	
	def buttonReturnToTitleScreen_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeMenuAccess_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeSaveAccess_Clicked( self, event ):
		event.Skip()
	
	def buttonCallMenuScreen_Clicked( self, event ):
		event.Skip()
	
	def buttonCallSaveScreen_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class EventCommands3_Panel
###########################################################################

class EventCommands3_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 400,450 ), style = wx.TAB_TRAVERSAL )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerLeft = wx.BoxSizer( wx.VERTICAL )
		
		sizerCharacter = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Character" ), wx.VERTICAL )
		
		self.buttonChangeTransparency = wx.Button( self, wx.ID_ANY, u"Change Transparency...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerCharacter.Add( self.buttonChangeTransparency, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonShowAnimation = wx.Button( self, wx.ID_ANY, u"Show Animation...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerCharacter.Add( self.buttonShowAnimation, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonEraseEvent = wx.Button( self, wx.ID_ANY, u"Erase Event", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerCharacter.Add( self.buttonEraseEvent, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		sizerLeft.Add( sizerCharacter, 0, wx.ALL|wx.EXPAND, 5 )
		
		sizerActor = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Actor" ), wx.VERTICAL )
		
		self.buttonChangeHP = wx.Button( self, wx.ID_ANY, u"Change HP...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerActor.Add( self.buttonChangeHP, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonChangeSP = wx.Button( self, wx.ID_ANY, u"Change SP...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerActor.Add( self.buttonChangeSP, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangeState = wx.Button( self, wx.ID_ANY, u"Change State...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerActor.Add( self.buttonChangeState, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonRecoverAll = wx.Button( self, wx.ID_ANY, u"Recover All", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerActor.Add( self.buttonRecoverAll, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangeExperience = wx.Button( self, wx.ID_ANY, u"Change Experience...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerActor.Add( self.buttonChangeExperience, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangeLevel = wx.Button( self, wx.ID_ANY, u"Change Level...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerActor.Add( self.buttonChangeLevel, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangeParamters = wx.Button( self, wx.ID_ANY, u"Change Parameters...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerActor.Add( self.buttonChangeParamters, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangeSkills = wx.Button( self, wx.ID_ANY, u"Change Skills...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerActor.Add( self.buttonChangeSkills, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangeEquipment = wx.Button( self, wx.ID_ANY, u"Change Equipment...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerActor.Add( self.buttonChangeEquipment, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangeActorName = wx.Button( self, wx.ID_ANY, u"Change Actor Name...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerActor.Add( self.buttonChangeActorName, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangeActorClass = wx.Button( self, wx.ID_ANY, u"Change Actor Class...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerActor.Add( self.buttonChangeActorClass, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangeActorGraphic = wx.Button( self, wx.ID_ANY, u"Change Actor Graphic...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerActor.Add( self.buttonChangeActorGraphic, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		sizerLeft.Add( sizerActor, 0, wx.EXPAND|wx.ALL, 5 )
		
		MainSizer.Add( sizerLeft, 1, wx.EXPAND, 5 )
		
		sizerRight = wx.BoxSizer( wx.VERTICAL )
		
		sizerPicture = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Picture" ), wx.VERTICAL )
		
		self.buttonShowPicture = wx.Button( self, wx.ID_ANY, u"Show Picture...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerPicture.Add( self.buttonShowPicture, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonMovePicture = wx.Button( self, wx.ID_ANY, u"Move Picture...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerPicture.Add( self.buttonMovePicture, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonRotatePicture = wx.Button( self, wx.ID_ANY, u"Rotate Picture...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerPicture.Add( self.buttonRotatePicture, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangePictureColorTone = wx.Button( self, wx.ID_ANY, u"Change Picture Color Tone...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerPicture.Add( self.buttonChangePictureColorTone, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonErasePicture = wx.Button( self, wx.ID_ANY, u"Erase Picture...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerPicture.Add( self.buttonErasePicture, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		sizerRight.Add( sizerPicture, 0, wx.EXPAND|wx.ALL, 5 )
		
		sizerBattle = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Battle" ), wx.VERTICAL )
		
		self.buttonChangeEnemyHP = wx.Button( self, wx.ID_ANY, u"Change Enemy HP...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerBattle.Add( self.buttonChangeEnemyHP, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonChangeEnemySP = wx.Button( self, wx.ID_ANY, u"Change Enemy SP...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerBattle.Add( self.buttonChangeEnemySP, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonChangeEnemyState = wx.Button( self, wx.ID_ANY, u"Change Enemy State...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerBattle.Add( self.buttonChangeEnemyState, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonEnemyRecoverAll = wx.Button( self, wx.ID_ANY, u"Enemy Recover All...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerBattle.Add( self.buttonEnemyRecoverAll, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonEnemyApperance = wx.Button( self, wx.ID_ANY, u"Enemy Appearance...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerBattle.Add( self.buttonEnemyApperance, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonEnemyTransform = wx.Button( self, wx.ID_ANY, u"Enemy Transform...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerBattle.Add( self.buttonEnemyTransform, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonShowBattleAnimation = wx.Button( self, wx.ID_ANY, u"Show Battle Animation...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerBattle.Add( self.buttonShowBattleAnimation, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonDealDamage = wx.Button( self, wx.ID_ANY, u"Deal Damage...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerBattle.Add( self.buttonDealDamage, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonForceAction = wx.Button( self, wx.ID_ANY, u"Force Action...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerBattle.Add( self.buttonForceAction, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.buttonAbortBattle = wx.Button( self, wx.ID_ANY, u"Abort Battle", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerBattle.Add( self.buttonAbortBattle, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		sizerRight.Add( sizerBattle, 0, wx.EXPAND|wx.ALL, 5 )
		
		MainSizer.Add( sizerRight, 1, wx.EXPAND, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		# Connect Events
		self.buttonChangeTransparency.Bind( wx.EVT_BUTTON, self.buttonChangeTransparency_Clicked )
		self.buttonShowAnimation.Bind( wx.EVT_BUTTON, self.buttonShowAnimation_Clicked )
		self.buttonEraseEvent.Bind( wx.EVT_BUTTON, self.buttonEraseEvent_Clicked )
		self.buttonChangeHP.Bind( wx.EVT_BUTTON, self.buttonChangeHP_Clicked )
		self.buttonChangeSP.Bind( wx.EVT_BUTTON, self.buttonChangeSP_Clicked )
		self.buttonChangeState.Bind( wx.EVT_BUTTON, self.buttonChangeState_Clicked )
		self.buttonRecoverAll.Bind( wx.EVT_BUTTON, self.buttonRecoverAll_Clicked )
		self.buttonChangeExperience.Bind( wx.EVT_BUTTON, self.buttonChangeExperience_Clicked )
		self.buttonChangeLevel.Bind( wx.EVT_BUTTON, self.buttonChangeLevel_Clicked )
		self.buttonChangeParamters.Bind( wx.EVT_BUTTON, self.buttonChangeParameters_Clicked )
		self.buttonChangeSkills.Bind( wx.EVT_BUTTON, self.buttonChangeSkills_Clicked )
		self.buttonChangeEquipment.Bind( wx.EVT_BUTTON, self.buttonChangeEquipment_Clicked )
		self.buttonChangeActorName.Bind( wx.EVT_BUTTON, self.buttonChangeActorName_Clicked )
		self.buttonChangeActorClass.Bind( wx.EVT_BUTTON, self.buttonChangeActorClass_Clicked )
		self.buttonChangeActorGraphic.Bind( wx.EVT_BUTTON, self.buttonChangeActorGraphic_Clicked )
		self.buttonShowPicture.Bind( wx.EVT_BUTTON, self.buttonShowPicture_Clicked )
		self.buttonMovePicture.Bind( wx.EVT_BUTTON, self.buttonMovePicture_Clicked )
		self.buttonRotatePicture.Bind( wx.EVT_BUTTON, self.buttonRotatePicture_Clicked )
		self.buttonChangePictureColorTone.Bind( wx.EVT_BUTTON, self.buttonChangePictureColorTone_Clicked )
		self.buttonErasePicture.Bind( wx.EVT_BUTTON, self.buttonErasePicture_Clicked )
		self.buttonChangeEnemyHP.Bind( wx.EVT_BUTTON, self.buttonChangeEnemyHP_Clicked )
		self.buttonChangeEnemySP.Bind( wx.EVT_BUTTON, self.buttonChangeEnemySP_Clicked )
		self.buttonChangeEnemyState.Bind( wx.EVT_BUTTON, self.buttonChangeEnemyState_Clicked )
		self.buttonEnemyRecoverAll.Bind( wx.EVT_BUTTON, self.buttonEnemyRecoverAll_Clicked )
		self.buttonEnemyApperance.Bind( wx.EVT_BUTTON, self.buttonEnemyAppearance_Clicked )
		self.buttonEnemyTransform.Bind( wx.EVT_BUTTON, self.buttonEnemyTransform_Clicked )
		self.buttonShowBattleAnimation.Bind( wx.EVT_BUTTON, self.buttonShowBattleAnimation_Clicked )
		self.buttonDealDamage.Bind( wx.EVT_BUTTON, self.buttonDealDamage_Clicked )
		self.buttonForceAction.Bind( wx.EVT_BUTTON, self.buttonForceAction_Clicked )
		self.buttonAbortBattle.Bind( wx.EVT_BUTTON, self.buttonAbortBattle_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonChangeTransparency_Clicked( self, event ):
		event.Skip()
	
	def buttonShowAnimation_Clicked( self, event ):
		event.Skip()
	
	def buttonEraseEvent_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeHP_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeSP_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeState_Clicked( self, event ):
		event.Skip()
	
	def buttonRecoverAll_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeExperience_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeLevel_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeParameters_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeSkills_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeEquipment_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeActorName_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeActorClass_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeActorGraphic_Clicked( self, event ):
		event.Skip()
	
	def buttonShowPicture_Clicked( self, event ):
		event.Skip()
	
	def buttonMovePicture_Clicked( self, event ):
		event.Skip()
	
	def buttonRotatePicture_Clicked( self, event ):
		event.Skip()
	
	def buttonChangePictureColorTone_Clicked( self, event ):
		event.Skip()
	
	def buttonErasePicture_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeEnemyHP_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeEnemySP_Clicked( self, event ):
		event.Skip()
	
	def buttonChangeEnemyState_Clicked( self, event ):
		event.Skip()
	
	def buttonEnemyRecoverAll_Clicked( self, event ):
		event.Skip()
	
	def buttonEnemyAppearance_Clicked( self, event ):
		event.Skip()
	
	def buttonEnemyTransform_Clicked( self, event ):
		event.Skip()
	
	def buttonShowBattleAnimation_Clicked( self, event ):
		event.Skip()
	
	def buttonDealDamage_Clicked( self, event ):
		event.Skip()
	
	def buttonForceAction_Clicked( self, event ):
		event.Skip()
	
	def buttonAbortBattle_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ChangeMaximum_Dialog
###########################################################################

class ChangeMaximum_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Change Maximum...", pos = wx.DefaultPosition, size = wx.Size( 181,115 ), style = wx.DEFAULT_DIALOG_STYLE )
		
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
## Class ExpCurve_Dialog
###########################################################################

class ExpCurve_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Experience Curve", pos = wx.DefaultPosition, size = wx.Size( 504,393 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.noteBookExpList = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panelNextLevel = wx.Panel( self.noteBookExpList, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		panelSizerNextLevel = wx.BoxSizer( wx.VERTICAL )
		
		self.textCtrlNextLevel = wx.TextCtrl( self.panelNextLevel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		panelSizerNextLevel.Add( self.textCtrlNextLevel, 1, wx.EXPAND, 5 )
		
		self.panelNextLevel.SetSizer( panelSizerNextLevel )
		self.panelNextLevel.Layout()
		panelSizerNextLevel.Fit( self.panelNextLevel )
		self.noteBookExpList.AddPage( self.panelNextLevel, u"To Next Level", True )
		self.panelTotal = wx.Panel( self.noteBookExpList, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		panelSizerTotal = wx.BoxSizer( wx.VERTICAL )
		
		self.textCtrlTotal = wx.TextCtrl( self.panelTotal, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		panelSizerTotal.Add( self.textCtrlTotal, 1, wx.EXPAND, 5 )
		
		self.panelTotal.SetSizer( panelSizerTotal )
		self.panelTotal.Layout()
		panelSizerTotal.Fit( self.panelTotal )
		self.noteBookExpList.AddPage( self.panelTotal, u"Total", False )
		
		MainSizer.Add( self.noteBookExpList, 1, wx.EXPAND |wx.ALL, 5 )
		
		sizerControls = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerBasis = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Basis" ), wx.HORIZONTAL )
		
		self.sliderBasis = wx.Slider( self, wx.ID_ANY, 35, 10, 50, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL )
		sizerBasis.Add( self.sliderBasis, 1, wx.ALL, 5 )
		
		self.spinCtrlBasis = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 10, 50, 35 )
		sizerBasis.Add( self.spinCtrlBasis, 0, wx.ALL, 5 )
		
		sizerControls.Add( sizerBasis, 1, wx.ALL, 5 )
		
		sizerInflation = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Inflation" ), wx.HORIZONTAL )
		
		self.sliderInflation = wx.Slider( self, wx.ID_ANY, 35, 10, 50, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL )
		sizerInflation.Add( self.sliderInflation, 1, wx.ALL, 5 )
		
		self.spinCtrlInflation = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 10, 50, 35 )
		sizerInflation.Add( self.spinCtrlInflation, 0, wx.ALL, 5 )
		
		sizerControls.Add( sizerInflation, 1, wx.ALL, 5 )
		
		MainSizer.Add( sizerControls, 0, wx.EXPAND, 5 )
		
		sizerButtons = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerButtons.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerButtons.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerButtons, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.sliderBasis.Bind( wx.EVT_SCROLL, self.sliderBasis_Scrolled )
		self.spinCtrlBasis.Bind( wx.EVT_SPINCTRL, self.spinCtrlBasis__ValueChanged )
		self.sliderInflation.Bind( wx.EVT_SCROLL, self.sliderInflation_Scrolled )
		self.spinCtrlInflation.Bind( wx.EVT_SPINCTRL, self.spinCtrlInflation_ValueChanged )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def sliderBasis_Scrolled( self, event ):
		event.Skip()
	
	def spinCtrlBasis__ValueChanged( self, event ):
		event.Skip()
	
	def sliderInflation_Scrolled( self, event ):
		event.Skip()
	
	def spinCtrlInflation_ValueChanged( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ActorParameters_Dialog
###########################################################################

class ActorParameters_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Parameters", pos = wx.DefaultPosition, size = wx.Size( 478,366 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.noteBookExperienceCurve = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panelMaxHP = wx.Panel( self.noteBookExperienceCurve, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		MainSizerMaxHP = wx.BoxSizer( wx.VERTICAL )
		
		sizerConrolsMaxHP = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerQuickSettingsMaxHP = wx.StaticBoxSizer( wx.StaticBox( self.panelMaxHP, wx.ID_ANY, u"Quick Settings" ), wx.HORIZONTAL )
		
		self.buttonQuickAMaxHP = wx.Button( self.panelMaxHP, wx.ID_ANY, u"A", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsMaxHP.Add( self.buttonQuickAMaxHP, 0, wx.ALL, 5 )
		
		self.buttonQuickBMaxHP = wx.Button( self.panelMaxHP, wx.ID_ANY, u"B", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsMaxHP.Add( self.buttonQuickBMaxHP, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.buttonQuickCMaxHP = wx.Button( self.panelMaxHP, wx.ID_ANY, u"C", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsMaxHP.Add( self.buttonQuickCMaxHP, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.buttonQuickDMaxHP = wx.Button( self.panelMaxHP, wx.ID_ANY, u"D", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsMaxHP.Add( self.buttonQuickDMaxHP, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.buttonQuickEMaxHP = wx.Button( self.panelMaxHP, wx.ID_ANY, u"E", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsMaxHP.Add( self.buttonQuickEMaxHP, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		sizerConrolsMaxHP.Add( sizerQuickSettingsMaxHP, 0, wx.ALL, 5 )
		
		sizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelLevelMaxHP = wx.StaticText( self.panelMaxHP, wx.ID_ANY, u"Level:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelLevelMaxHP.Wrap( -1 )
		sizer1.Add( self.labelLevelMaxHP, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlLevelMaxHP = wx.SpinCtrl( self.panelMaxHP, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 999, 1 )
		sizer1.Add( self.spinCtrlLevelMaxHP, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerConrolsMaxHP.Add( sizer1, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelValueMaxHP = wx.StaticText( self.panelMaxHP, wx.ID_ANY, u"Value:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelValueMaxHP.Wrap( -1 )
		sizer2.Add( self.labelValueMaxHP, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlValueMaxHP = wx.SpinCtrl( self.panelMaxHP, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer2.Add( self.spinCtrlValueMaxHP, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerConrolsMaxHP.Add( sizer2, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.buttonGenerateMaxHP = wx.Button( self.panelMaxHP, wx.ID_ANY, u"Generate Curve...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerConrolsMaxHP.Add( self.buttonGenerateMaxHP, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		MainSizerMaxHP.Add( sizerConrolsMaxHP, 0, wx.EXPAND, 5 )
		
		self.bitmapGraphMaxHP = wx.StaticBitmap( self.panelMaxHP, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/MaxHP.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 448,224 ), wx.SIMPLE_BORDER )
		MainSizerMaxHP.Add( self.bitmapGraphMaxHP, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.panelMaxHP.SetSizer( MainSizerMaxHP )
		self.panelMaxHP.Layout()
		MainSizerMaxHP.Fit( self.panelMaxHP )
		self.noteBookExperienceCurve.AddPage( self.panelMaxHP, u"MaxHP", True )
		self.panelMaxSP = wx.Panel( self.noteBookExperienceCurve, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		MainSizerMaxSP = wx.BoxSizer( wx.VERTICAL )
		
		sizerConrolsMaxSP = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerQuickSettingsMaxSP = wx.StaticBoxSizer( wx.StaticBox( self.panelMaxSP, wx.ID_ANY, u"Quick Settings" ), wx.HORIZONTAL )
		
		self.buttonQuickAMaxSP = wx.Button( self.panelMaxSP, wx.ID_ANY, u"A", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsMaxSP.Add( self.buttonQuickAMaxSP, 0, wx.ALL, 5 )
		
		self.buttonQuickBMaxSP = wx.Button( self.panelMaxSP, wx.ID_ANY, u"B", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsMaxSP.Add( self.buttonQuickBMaxSP, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.buttonQuickCMaxSP = wx.Button( self.panelMaxSP, wx.ID_ANY, u"C", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsMaxSP.Add( self.buttonQuickCMaxSP, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.buttonQuickDMaxSP = wx.Button( self.panelMaxSP, wx.ID_ANY, u"D", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsMaxSP.Add( self.buttonQuickDMaxSP, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.buttonQuickEMaxSP = wx.Button( self.panelMaxSP, wx.ID_ANY, u"E", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsMaxSP.Add( self.buttonQuickEMaxSP, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		sizerConrolsMaxSP.Add( sizerQuickSettingsMaxSP, 0, wx.ALL, 5 )
		
		sizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelLevelMaxSP = wx.StaticText( self.panelMaxSP, wx.ID_ANY, u"Level:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelLevelMaxSP.Wrap( -1 )
		sizer3.Add( self.labelLevelMaxSP, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlLevelMaxSP = wx.SpinCtrl( self.panelMaxSP, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 999, 1 )
		sizer3.Add( self.spinCtrlLevelMaxSP, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerConrolsMaxSP.Add( sizer3, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelValueMaxSP = wx.StaticText( self.panelMaxSP, wx.ID_ANY, u"Value:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelValueMaxSP.Wrap( -1 )
		sizer4.Add( self.labelValueMaxSP, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlValueMaxSP = wx.SpinCtrl( self.panelMaxSP, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer4.Add( self.spinCtrlValueMaxSP, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerConrolsMaxSP.Add( sizer4, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.buttonGenerateMaxSP = wx.Button( self.panelMaxSP, wx.ID_ANY, u"Generate Curve...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerConrolsMaxSP.Add( self.buttonGenerateMaxSP, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		MainSizerMaxSP.Add( sizerConrolsMaxSP, 0, wx.EXPAND, 5 )
		
		self.bitmapGraphMaxSP = wx.StaticBitmap( self.panelMaxSP, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/MaxSP.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 448,224 ), wx.SIMPLE_BORDER )
		MainSizerMaxSP.Add( self.bitmapGraphMaxSP, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.panelMaxSP.SetSizer( MainSizerMaxSP )
		self.panelMaxSP.Layout()
		MainSizerMaxSP.Fit( self.panelMaxSP )
		self.noteBookExperienceCurve.AddPage( self.panelMaxSP, u"MaxSP", False )
		self.panelStr = wx.Panel( self.noteBookExperienceCurve, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		MainSizerStr = wx.BoxSizer( wx.VERTICAL )
		
		sizerConrolsStr = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerQuickSettingsStr = wx.StaticBoxSizer( wx.StaticBox( self.panelStr, wx.ID_ANY, u"Quick Settings" ), wx.HORIZONTAL )
		
		self.buttonQuickAStr = wx.Button( self.panelStr, wx.ID_ANY, u"A", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsStr.Add( self.buttonQuickAStr, 0, wx.ALL, 5 )
		
		self.buttonQuickBStr = wx.Button( self.panelStr, wx.ID_ANY, u"B", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsStr.Add( self.buttonQuickBStr, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.buttonQuickCStr = wx.Button( self.panelStr, wx.ID_ANY, u"C", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsStr.Add( self.buttonQuickCStr, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.buttonQuickDStr = wx.Button( self.panelStr, wx.ID_ANY, u"D", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsStr.Add( self.buttonQuickDStr, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.buttonQuickEStr = wx.Button( self.panelStr, wx.ID_ANY, u"E", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsStr.Add( self.buttonQuickEStr, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		sizerConrolsStr.Add( sizerQuickSettingsStr, 0, wx.ALL, 5 )
		
		sizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelLevelStr = wx.StaticText( self.panelStr, wx.ID_ANY, u"Level:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelLevelStr.Wrap( -1 )
		sizer5.Add( self.labelLevelStr, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlLevelStr = wx.SpinCtrl( self.panelStr, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 999, 1 )
		sizer5.Add( self.spinCtrlLevelStr, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerConrolsStr.Add( sizer5, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelValueStr = wx.StaticText( self.panelStr, wx.ID_ANY, u"Value:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelValueStr.Wrap( -1 )
		sizer6.Add( self.labelValueStr, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlValueStr = wx.SpinCtrl( self.panelStr, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer6.Add( self.spinCtrlValueStr, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerConrolsStr.Add( sizer6, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.buttonGenerateStr = wx.Button( self.panelStr, wx.ID_ANY, u"Generate Curve...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerConrolsStr.Add( self.buttonGenerateStr, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		MainSizerStr.Add( sizerConrolsStr, 0, wx.EXPAND, 5 )
		
		self.bitmapGraphStr = wx.StaticBitmap( self.panelStr, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Str.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 448,224 ), wx.SIMPLE_BORDER )
		MainSizerStr.Add( self.bitmapGraphStr, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.panelStr.SetSizer( MainSizerStr )
		self.panelStr.Layout()
		MainSizerStr.Fit( self.panelStr )
		self.noteBookExperienceCurve.AddPage( self.panelStr, u"STR", False )
		self.panelDex = wx.Panel( self.noteBookExperienceCurve, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		MainSizerDex = wx.BoxSizer( wx.VERTICAL )
		
		sizerConrolsDex = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerQuickSettingsDex = wx.StaticBoxSizer( wx.StaticBox( self.panelDex, wx.ID_ANY, u"Quick Settings" ), wx.HORIZONTAL )
		
		self.buttonQuickADex = wx.Button( self.panelDex, wx.ID_ANY, u"A", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsDex.Add( self.buttonQuickADex, 0, wx.ALL, 5 )
		
		self.buttonQuickBDex = wx.Button( self.panelDex, wx.ID_ANY, u"B", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsDex.Add( self.buttonQuickBDex, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.buttonQuickCDex = wx.Button( self.panelDex, wx.ID_ANY, u"C", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsDex.Add( self.buttonQuickCDex, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.buttonQuickDDex = wx.Button( self.panelDex, wx.ID_ANY, u"D", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsDex.Add( self.buttonQuickDDex, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.buttonQuickEDex = wx.Button( self.panelDex, wx.ID_ANY, u"E", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsDex.Add( self.buttonQuickEDex, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		sizerConrolsDex.Add( sizerQuickSettingsDex, 0, wx.ALL, 5 )
		
		sizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelLevelDex = wx.StaticText( self.panelDex, wx.ID_ANY, u"Level:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelLevelDex.Wrap( -1 )
		sizer7.Add( self.labelLevelDex, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlLevelDex = wx.SpinCtrl( self.panelDex, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 999, 1 )
		sizer7.Add( self.spinCtrlLevelDex, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerConrolsDex.Add( sizer7, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelValueDex = wx.StaticText( self.panelDex, wx.ID_ANY, u"Value:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelValueDex.Wrap( -1 )
		sizer8.Add( self.labelValueDex, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlValueDex = wx.SpinCtrl( self.panelDex, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer8.Add( self.spinCtrlValueDex, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerConrolsDex.Add( sizer8, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.buttonGenerateDex = wx.Button( self.panelDex, wx.ID_ANY, u"Generate Curve...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerConrolsDex.Add( self.buttonGenerateDex, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		MainSizerDex.Add( sizerConrolsDex, 0, wx.EXPAND, 5 )
		
		self.bitmapGraphDex = wx.StaticBitmap( self.panelDex, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Dex.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 448,224 ), wx.SIMPLE_BORDER )
		MainSizerDex.Add( self.bitmapGraphDex, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.panelDex.SetSizer( MainSizerDex )
		self.panelDex.Layout()
		MainSizerDex.Fit( self.panelDex )
		self.noteBookExperienceCurve.AddPage( self.panelDex, u"DEX", False )
		self.panelAgi = wx.Panel( self.noteBookExperienceCurve, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		MainSizerAgi = wx.BoxSizer( wx.VERTICAL )
		
		sizerConrolsAgi = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerQuickSettingsAgi = wx.StaticBoxSizer( wx.StaticBox( self.panelAgi, wx.ID_ANY, u"Quick Settings" ), wx.HORIZONTAL )
		
		self.buttonQuickAAgi = wx.Button( self.panelAgi, wx.ID_ANY, u"A", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsAgi.Add( self.buttonQuickAAgi, 0, wx.ALL, 5 )
		
		self.buttonQuickBAgi = wx.Button( self.panelAgi, wx.ID_ANY, u"B", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsAgi.Add( self.buttonQuickBAgi, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.buttonQuickCAgi = wx.Button( self.panelAgi, wx.ID_ANY, u"C", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsAgi.Add( self.buttonQuickCAgi, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.buttonQuickDAgi = wx.Button( self.panelAgi, wx.ID_ANY, u"D", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsAgi.Add( self.buttonQuickDAgi, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.buttonQuickEAgi = wx.Button( self.panelAgi, wx.ID_ANY, u"E", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsAgi.Add( self.buttonQuickEAgi, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		sizerConrolsAgi.Add( sizerQuickSettingsAgi, 0, wx.ALL, 5 )
		
		sizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelLevelAgi = wx.StaticText( self.panelAgi, wx.ID_ANY, u"Level:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelLevelAgi.Wrap( -1 )
		sizer9.Add( self.labelLevelAgi, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlLevelAgi = wx.SpinCtrl( self.panelAgi, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 999, 1 )
		sizer9.Add( self.spinCtrlLevelAgi, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerConrolsAgi.Add( sizer9, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelValueAgi = wx.StaticText( self.panelAgi, wx.ID_ANY, u"Value:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelValueAgi.Wrap( -1 )
		sizer10.Add( self.labelValueAgi, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlValueAgi = wx.SpinCtrl( self.panelAgi, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer10.Add( self.spinCtrlValueAgi, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerConrolsAgi.Add( sizer10, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.buttonGenerateAgi = wx.Button( self.panelAgi, wx.ID_ANY, u"Generate Curve...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerConrolsAgi.Add( self.buttonGenerateAgi, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		MainSizerAgi.Add( sizerConrolsAgi, 0, wx.EXPAND, 5 )
		
		self.bitmapGraphAgi = wx.StaticBitmap( self.panelAgi, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Agi.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 448,224 ), wx.SIMPLE_BORDER )
		MainSizerAgi.Add( self.bitmapGraphAgi, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.panelAgi.SetSizer( MainSizerAgi )
		self.panelAgi.Layout()
		MainSizerAgi.Fit( self.panelAgi )
		self.noteBookExperienceCurve.AddPage( self.panelAgi, u"AGI", False )
		self.panelInt = wx.Panel( self.noteBookExperienceCurve, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		MainSizerInt = wx.BoxSizer( wx.VERTICAL )
		
		sizerConrolsInt = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerQuickSettingsInt = wx.StaticBoxSizer( wx.StaticBox( self.panelInt, wx.ID_ANY, u"Quick Settings" ), wx.HORIZONTAL )
		
		self.buttonQuickAInt = wx.Button( self.panelInt, wx.ID_ANY, u"A", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsInt.Add( self.buttonQuickAInt, 0, wx.ALL, 5 )
		
		self.buttonQuickBInt = wx.Button( self.panelInt, wx.ID_ANY, u"B", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsInt.Add( self.buttonQuickBInt, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.buttonQuickCInt = wx.Button( self.panelInt, wx.ID_ANY, u"C", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsInt.Add( self.buttonQuickCInt, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.buttonQuickDInt = wx.Button( self.panelInt, wx.ID_ANY, u"D", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsInt.Add( self.buttonQuickDInt, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.buttonQuickEInt = wx.Button( self.panelInt, wx.ID_ANY, u"E", wx.DefaultPosition, wx.Size( 23,23 ), 0 )
		sizerQuickSettingsInt.Add( self.buttonQuickEInt, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		sizerConrolsInt.Add( sizerQuickSettingsInt, 0, wx.ALL, 5 )
		
		sizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelLevelInt = wx.StaticText( self.panelInt, wx.ID_ANY, u"Level:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelLevelInt.Wrap( -1 )
		sizer11.Add( self.labelLevelInt, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlLevelInt = wx.SpinCtrl( self.panelInt, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 999, 1 )
		sizer11.Add( self.spinCtrlLevelInt, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerConrolsInt.Add( sizer11, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelValueInt = wx.StaticText( self.panelInt, wx.ID_ANY, u"Value:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelValueInt.Wrap( -1 )
		sizer12.Add( self.labelValueInt, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlValueInt = wx.SpinCtrl( self.panelInt, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer12.Add( self.spinCtrlValueInt, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerConrolsInt.Add( sizer12, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.buttonGenerateInt = wx.Button( self.panelInt, wx.ID_ANY, u"Generate Curve...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerConrolsInt.Add( self.buttonGenerateInt, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		MainSizerInt.Add( sizerConrolsInt, 0, wx.EXPAND, 5 )
		
		self.bitmapGraphInt = wx.StaticBitmap( self.panelInt, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Int.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 448,224 ), wx.SIMPLE_BORDER )
		MainSizerInt.Add( self.bitmapGraphInt, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.panelInt.SetSizer( MainSizerInt )
		self.panelInt.Layout()
		MainSizerInt.Fit( self.panelInt )
		self.noteBookExperienceCurve.AddPage( self.panelInt, u"INT", False )
		
		MainSizer.Add( self.noteBookExperienceCurve, 1, wx.EXPAND |wx.ALL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonQuickAMaxHP.Bind( wx.EVT_BUTTON, self.buttonQuickAMaxHP_Clicked )
		self.buttonQuickBMaxHP.Bind( wx.EVT_BUTTON, self.buttonQuickBMaxHP_Clicked )
		self.buttonQuickCMaxHP.Bind( wx.EVT_BUTTON, self.buttonQuickCMaxHP_Clicked )
		self.buttonQuickDMaxHP.Bind( wx.EVT_BUTTON, self.buttonQuickDMaxHP_Clicked )
		self.buttonQuickEMaxHP.Bind( wx.EVT_BUTTON, self.buttonQuickEMaxHP_Clicked )
		self.spinCtrlLevelMaxHP.Bind( wx.EVT_SPINCTRL, self.spinCtrlLevelMaxHP_ValueChanged )
		self.spinCtrlValueMaxHP.Bind( wx.EVT_SPINCTRL, self.spinCtrlValueMaxHP_ValueChanged )
		self.buttonGenerateMaxHP.Bind( wx.EVT_BUTTON, self.buttonGenerateMaxHP_Clicked )
		self.bitmapGraphMaxHP.Bind( wx.EVT_LEFT_DCLICK, self.bitmapGraphMaxHP_LeftClick )
		self.bitmapGraphMaxHP.Bind( wx.EVT_LEFT_DOWN, self.bitmapGraphMaxHP_LeftDown )
		self.bitmapGraphMaxHP.Bind( wx.EVT_LEFT_UP, self.bitmapGraphMaxHP_LeftUp )
		self.buttonQuickAMaxSP.Bind( wx.EVT_BUTTON, self.buttonQuickAMaxSP_Clicked )
		self.buttonQuickBMaxSP.Bind( wx.EVT_BUTTON, self.buttonQuickBMaxSP_Clicked )
		self.buttonQuickCMaxSP.Bind( wx.EVT_BUTTON, self.buttonQuickCMaxSP_Clicked )
		self.buttonQuickDMaxSP.Bind( wx.EVT_BUTTON, self.buttonQuickDMaxSP_Clicked )
		self.buttonQuickEMaxSP.Bind( wx.EVT_BUTTON, self.buttonQuickEMaxSP_Clicked )
		self.spinCtrlLevelMaxSP.Bind( wx.EVT_SPINCTRL, self.spinCtrlLevelMaxSP_ValueChanged )
		self.spinCtrlValueMaxSP.Bind( wx.EVT_SPINCTRL, self.spinCtrlValueMaxSP_ValueChanged )
		self.buttonGenerateMaxSP.Bind( wx.EVT_BUTTON, self.buttonGenerateMaxSP_Clicked )
		self.bitmapGraphMaxSP.Bind( wx.EVT_LEFT_DCLICK, self.bitmapGraphMaxSP_LeftClick )
		self.bitmapGraphMaxSP.Bind( wx.EVT_LEFT_DOWN, self.bitmapGraphMaxSP_LeftDown )
		self.bitmapGraphMaxSP.Bind( wx.EVT_LEFT_UP, self.bitmapGraphMaxSP_LeftUp )
		self.buttonQuickAStr.Bind( wx.EVT_BUTTON, self.buttonQuickAStr_Clicked )
		self.buttonQuickBStr.Bind( wx.EVT_BUTTON, self.buttonQuickBStr_Clicked )
		self.buttonQuickCStr.Bind( wx.EVT_BUTTON, self.buttonQuickCStr_Clicked )
		self.buttonQuickDStr.Bind( wx.EVT_BUTTON, self.buttonQuickDStr_Clicked )
		self.buttonQuickEStr.Bind( wx.EVT_BUTTON, self.buttonQuickEStr_Clicked )
		self.spinCtrlLevelStr.Bind( wx.EVT_SPINCTRL, self.spinCtrlLevelStr_ValueChanged )
		self.spinCtrlValueStr.Bind( wx.EVT_SPINCTRL, self.spinCtrlValueStr_ValueChanged )
		self.buttonGenerateStr.Bind( wx.EVT_BUTTON, self.buttonGenerateStr_Clicked )
		self.bitmapGraphStr.Bind( wx.EVT_LEFT_DCLICK, self.bitmapGraphStr_LeftClick )
		self.bitmapGraphStr.Bind( wx.EVT_LEFT_DOWN, self.bitmapGraphStr_LeftDown )
		self.bitmapGraphStr.Bind( wx.EVT_LEFT_UP, self.bitmapGraphStr_LeftUp )
		self.buttonQuickADex.Bind( wx.EVT_BUTTON, self.buttonQuickADex_Clicked )
		self.buttonQuickBDex.Bind( wx.EVT_BUTTON, self.buttonQuickBDex_Clicked )
		self.buttonQuickCDex.Bind( wx.EVT_BUTTON, self.buttonQuickCDex_Clicked )
		self.buttonQuickDDex.Bind( wx.EVT_BUTTON, self.buttonQuickDDex_Clicked )
		self.buttonQuickEDex.Bind( wx.EVT_BUTTON, self.buttonQuickEDex_Clicked )
		self.spinCtrlLevelDex.Bind( wx.EVT_SPINCTRL, self.spinCtrlLevelDex_ValueChanged )
		self.spinCtrlValueDex.Bind( wx.EVT_SPINCTRL, self.spinCtrlValueDex_ValueChanged )
		self.buttonGenerateDex.Bind( wx.EVT_BUTTON, self.buttonGenerateDex_Clicked )
		self.bitmapGraphDex.Bind( wx.EVT_LEFT_DCLICK, self.bitmapGraphDex_LeftClick )
		self.bitmapGraphDex.Bind( wx.EVT_LEFT_DOWN, self.bitmapGraphDex_LeftDown )
		self.bitmapGraphDex.Bind( wx.EVT_LEFT_UP, self.bitmapGraphDex_LeftUp )
		self.buttonQuickAAgi.Bind( wx.EVT_BUTTON, self.buttonQuickAAgi_Clicked )
		self.buttonQuickBAgi.Bind( wx.EVT_BUTTON, self.buttonQuickBAgi_Clicked )
		self.buttonQuickCAgi.Bind( wx.EVT_BUTTON, self.buttonQuickCAgi_Clicked )
		self.buttonQuickDAgi.Bind( wx.EVT_BUTTON, self.buttonQuickDAgi_Clicked )
		self.buttonQuickEAgi.Bind( wx.EVT_BUTTON, self.buttonQuickEAgi_Clicked )
		self.spinCtrlLevelAgi.Bind( wx.EVT_SPINCTRL, self.spinCtrlLevelAgi_ValueChanged )
		self.spinCtrlValueAgi.Bind( wx.EVT_SPINCTRL, self.spinCtrlValueAgi_ValueChanged )
		self.buttonGenerateAgi.Bind( wx.EVT_BUTTON, self.buttonGenerateAgi_Clicked )
		self.bitmapGraphAgi.Bind( wx.EVT_LEFT_DCLICK, self.bitmapGraphAgi_LeftClick )
		self.bitmapGraphAgi.Bind( wx.EVT_LEFT_DOWN, self.bitmapGraphAgi_LeftDown )
		self.bitmapGraphAgi.Bind( wx.EVT_LEFT_UP, self.bitmapGraphAgi_LeftUp )
		self.buttonQuickAInt.Bind( wx.EVT_BUTTON, self.buttonQuickAInt_Clicked )
		self.buttonQuickBInt.Bind( wx.EVT_BUTTON, self.buttonQuickBMaxHP_Clicked )
		self.buttonQuickCInt.Bind( wx.EVT_BUTTON, self.buttonQuickCInt_Clicked )
		self.buttonQuickDInt.Bind( wx.EVT_BUTTON, self.buttonQuickDInt_Clicked )
		self.buttonQuickEInt.Bind( wx.EVT_BUTTON, self.buttonQuickEInt_Clicked )
		self.spinCtrlLevelInt.Bind( wx.EVT_SPINCTRL, self.spinCtrlLevelInt_ValueChanged )
		self.spinCtrlValueInt.Bind( wx.EVT_SPINCTRL, self.spinCtrlValueInt_ValueChanged )
		self.buttonGenerateInt.Bind( wx.EVT_BUTTON, self.buttonGenerateInt_Clicked )
		self.bitmapGraphInt.Bind( wx.EVT_LEFT_DCLICK, self.bitmapGraphInt_LeftClick )
		self.bitmapGraphInt.Bind( wx.EVT_LEFT_DOWN, self.bitmapGraphInt_LeftDown )
		self.bitmapGraphInt.Bind( wx.EVT_LEFT_UP, self.bitmapGraphInt_LeftUp )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonQuickAMaxHP_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickBMaxHP_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickCMaxHP_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickDMaxHP_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickEMaxHP_Clicked( self, event ):
		event.Skip()
	
	def spinCtrlLevelMaxHP_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlValueMaxHP_ValueChanged( self, event ):
		event.Skip()
	
	def buttonGenerateMaxHP_Clicked( self, event ):
		event.Skip()
	
	def bitmapGraphMaxHP_LeftClick( self, event ):
		event.Skip()
	
	def bitmapGraphMaxHP_LeftDown( self, event ):
		event.Skip()
	
	def bitmapGraphMaxHP_LeftUp( self, event ):
		event.Skip()
	
	def buttonQuickAMaxSP_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickBMaxSP_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickCMaxSP_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickDMaxSP_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickEMaxSP_Clicked( self, event ):
		event.Skip()
	
	def spinCtrlLevelMaxSP_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlValueMaxSP_ValueChanged( self, event ):
		event.Skip()
	
	def buttonGenerateMaxSP_Clicked( self, event ):
		event.Skip()
	
	def bitmapGraphMaxSP_LeftClick( self, event ):
		event.Skip()
	
	def bitmapGraphMaxSP_LeftDown( self, event ):
		event.Skip()
	
	def bitmapGraphMaxSP_LeftUp( self, event ):
		event.Skip()
	
	def buttonQuickAStr_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickBStr_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickCStr_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickDStr_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickEStr_Clicked( self, event ):
		event.Skip()
	
	def spinCtrlLevelStr_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlValueStr_ValueChanged( self, event ):
		event.Skip()
	
	def buttonGenerateStr_Clicked( self, event ):
		event.Skip()
	
	def bitmapGraphStr_LeftClick( self, event ):
		event.Skip()
	
	def bitmapGraphStr_LeftDown( self, event ):
		event.Skip()
	
	def bitmapGraphStr_LeftUp( self, event ):
		event.Skip()
	
	def buttonQuickADex_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickBDex_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickCDex_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickDDex_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickEDex_Clicked( self, event ):
		event.Skip()
	
	def spinCtrlLevelDex_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlValueDex_ValueChanged( self, event ):
		event.Skip()
	
	def buttonGenerateDex_Clicked( self, event ):
		event.Skip()
	
	def bitmapGraphDex_LeftClick( self, event ):
		event.Skip()
	
	def bitmapGraphDex_LeftDown( self, event ):
		event.Skip()
	
	def bitmapGraphDex_LeftUp( self, event ):
		event.Skip()
	
	def buttonQuickAAgi_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickBAgi_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickCAgi_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickDAgi_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickEAgi_Clicked( self, event ):
		event.Skip()
	
	def spinCtrlLevelAgi_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlValueAgi_ValueChanged( self, event ):
		event.Skip()
	
	def buttonGenerateAgi_Clicked( self, event ):
		event.Skip()
	
	def bitmapGraphAgi_LeftClick( self, event ):
		event.Skip()
	
	def bitmapGraphAgi_LeftDown( self, event ):
		event.Skip()
	
	def bitmapGraphAgi_LeftUp( self, event ):
		event.Skip()
	
	def buttonQuickAInt_Clicked( self, event ):
		event.Skip()
	
	
	def buttonQuickCInt_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickDInt_Clicked( self, event ):
		event.Skip()
	
	def buttonQuickEInt_Clicked( self, event ):
		event.Skip()
	
	def spinCtrlLevelInt_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlValueInt_ValueChanged( self, event ):
		event.Skip()
	
	def buttonGenerateInt_Clicked( self, event ):
		event.Skip()
	
	def bitmapGraphInt_LeftClick( self, event ):
		event.Skip()
	
	def bitmapGraphInt_LeftDown( self, event ):
		event.Skip()
	
	def bitmapGraphInt_LeftUp( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class GenerateCurve_Dialog
###########################################################################

class GenerateCurve_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Generate Curve", pos = wx.DefaultPosition, size = wx.Size( 275,149 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		sizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelLevel1 = wx.StaticText( self, wx.ID_ANY, u"Level 1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelLevel1.Wrap( -1 )
		sizer2.Add( self.labelLevel1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_spinCtrl101 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer2.Add( self.m_spinCtrl101, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer1.Add( sizer2, 1, 0, 5 )
		
		sizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelMaxLevel = wx.StaticText( self, wx.ID_ANY, u"Max Level:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMaxLevel.Wrap( -1 )
		sizer3.Add( self.labelMaxLevel, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_spinCtrl102 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer3.Add( self.m_spinCtrl102, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizer1.Add( sizer3, 1, 0, 5 )
		
		sizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer4.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer4.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		sizer1.Add( sizer4, 0, 0, 5 )
		
		MainSizer.Add( sizer1, 0, wx.EXPAND, 5 )
		
		self.sliderCurve = wx.Slider( self, wx.ID_ANY, 0, -25, 25, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_LABELS|wx.SL_TOP )
		MainSizer.Add( self.sliderCurve, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
		self.sliderCurve.Bind( wx.EVT_SCROLL, self.sliderCurve_Scrolled )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	
	def sliderCurve_Scrolled( self, event ):
		event.Skip()
	

###########################################################################
## Class ChooseGraphic_Dialog
###########################################################################

class ChooseGraphic_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Choose Graphic", pos = wx.DefaultPosition, size = wx.Size( 640,480 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		bSizer250 = wx.BoxSizer( wx.HORIZONTAL )
		
		listBoxGraphicsChoices = []
		self.listBoxGraphics = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,-1 ), listBoxGraphicsChoices, 0 )
		bSizer250.Add( self.listBoxGraphics, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer253 = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapGraphic = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER )
		bSizer253.Add( self.bitmapGraphic, 1, wx.EXPAND|wx.ALL, 5 )
		
		sizerHue = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Hue" ), wx.VERTICAL )
		
		self.sliderHue = wx.Slider( self, wx.ID_ANY, 0, 0, 359, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		sizerHue.Add( self.sliderHue, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer253.Add( sizerHue, 0, wx.EXPAND|wx.ALL, 5 )
		
		bSizer250.Add( bSizer253, 1, wx.EXPAND, 5 )
		
		MainSizer.Add( bSizer250, 1, wx.EXPAND, 5 )
		
		bSizer252 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer252.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer252.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( bSizer252, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.listBoxGraphics.Bind( wx.EVT_LISTBOX, self.listBoxGraphics_SelectionChanged )
		self.sliderHue.Bind( wx.EVT_SCROLL, self.sliderHue_Scrolled )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def listBoxGraphics_SelectionChanged( self, event ):
		event.Skip()
	
	def sliderHue_Scrolled( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

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
## Class ChooseAudio_Dialog
###########################################################################

class ChooseAudio_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Choose Audio", pos = wx.DefaultPosition, size = wx.Size( 270,436 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		sizerMainControls = wx.BoxSizer( wx.HORIZONTAL )
		
		listBoxAudioChoices = []
		self.listBoxAudio = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxAudioChoices, 0 )
		sizerMainControls.Add( self.listBoxAudio, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizerControls = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonPlay = wx.Button( self, wx.ID_ANY, u"Play", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerControls.Add( self.buttonPlay, 0, wx.ALL, 5 )
		
		self.buttonStop = wx.Button( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerControls.Add( self.buttonStop, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerVolume = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Volume" ), wx.VERTICAL )
		
		self.sliderVolume = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_INVERSE|wx.SL_LABELS|wx.SL_LEFT|wx.SL_VERTICAL )
		sizerVolume.Add( self.sliderVolume, 1, 0, 5 )
		
		sizerControls.Add( sizerVolume, 1, wx.EXPAND|wx.ALL, 5 )
		
		sizerPitch = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Pitch" ), wx.VERTICAL )
		
		self.sliderPitch = wx.Slider( self, wx.ID_ANY, 100, 50, 150, wx.DefaultPosition, wx.DefaultSize, wx.SL_INVERSE|wx.SL_LABELS|wx.SL_LEFT|wx.SL_VERTICAL )
		sizerPitch.Add( self.sliderPitch, 0, wx.ALL, 5 )
		
		sizerControls.Add( sizerPitch, 1, wx.EXPAND|wx.ALL, 5 )
		
		sizerMainControls.Add( sizerControls, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerMainControls, 1, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonPlay.Bind( wx.EVT_BUTTON, self.buttonPlay_Clicked )
		self.buttonStop.Bind( wx.EVT_BUTTON, self.buttonStop_Clicked )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonPlay_Clicked( self, event ):
		event.Skip()
	
	def buttonStop_Clicked( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class EnemyAction_Dialog
###########################################################################

class EnemyAction_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Action", pos = wx.DefaultPosition, size = wx.Size( 309,387 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		sizerCondition = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Condition" ), wx.VERTICAL )
		
		sizerTurm = wx.BoxSizer( wx.HORIZONTAL )
		
		self.checkBoxTurn = wx.CheckBox( self, wx.ID_ANY, u"Turn", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		sizerTurm.Add( self.checkBoxTurn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlTurn1 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 10, 1 )
		sizerTurm.Add( self.spinCtrlTurn1, 0, wx.ALL, 5 )
		
		self.labelPlus = wx.StaticText( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPlus.Wrap( -1 )
		sizerTurm.Add( self.labelPlus, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlTurn2 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerTurm.Add( self.spinCtrlTurn2, 0, wx.ALL, 5 )
		
		self.labelX = wx.StaticText( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelX.Wrap( -1 )
		sizerTurm.Add( self.labelX, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerCondition.Add( sizerTurm, 0, wx.EXPAND, 5 )
		
		sizerHP = wx.BoxSizer( wx.HORIZONTAL )
		
		self.checkBoxTurn = wx.CheckBox( self, wx.ID_ANY, u"HP", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		sizerHP.Add( self.checkBoxTurn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlHP = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerHP.Add( self.spinCtrlHP, 0, wx.ALL, 5 )
		
		self.labelBelow = wx.StaticText( self, wx.ID_ANY, u"% or below", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBelow.Wrap( -1 )
		sizerHP.Add( self.labelBelow, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		sizerCondition.Add( sizerHP, 0, wx.EXPAND, 5 )
		
		sizerLevel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.checkBoxLevel = wx.CheckBox( self, wx.ID_ANY, u"Level", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		sizerLevel.Add( self.checkBoxLevel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlLevel = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerLevel.Add( self.spinCtrlLevel, 0, wx.ALL, 5 )
		
		self.labelAbove = wx.StaticText( self, wx.ID_ANY, u"or above", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAbove.Wrap( -1 )
		sizerLevel.Add( self.labelAbove, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		sizerCondition.Add( sizerLevel, 0, wx.EXPAND, 5 )
		
		sizerSwitch = wx.BoxSizer( wx.HORIZONTAL )
		
		self.checkBoxSwitch = wx.CheckBox( self, wx.ID_ANY, u"Switch", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		sizerSwitch.Add( self.checkBoxSwitch, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxSwitchChoices = []
		self.comboBoxSwitch = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxSwitchChoices, 0 )
		self.comboBoxSwitch.SetSelection( 0 )
		sizerSwitch.Add( self.comboBoxSwitch, 1, wx.ALL, 5 )
		
		self.labelON = wx.StaticText( self, wx.ID_ANY, u"is ON", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelON.Wrap( -1 )
		sizerSwitch.Add( self.labelON, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		sizerCondition.Add( sizerSwitch, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerCondition, 0, wx.ALL|wx.EXPAND, 5 )
		
		sizerAction = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Action" ), wx.VERTICAL )
		
		sizerBasic = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioBtnBasic = wx.RadioButton( self, wx.ID_ANY, u"Basic", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		sizerBasic.Add( self.radioBtnBasic, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxBasicChoices = []
		self.comboBoxBasic = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxBasicChoices, 0 )
		self.comboBoxBasic.SetSelection( 0 )
		sizerBasic.Add( self.comboBoxBasic, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerAction.Add( sizerBasic, 0, wx.EXPAND, 5 )
		
		sizerSkill = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioBtnSkill = wx.RadioButton( self, wx.ID_ANY, u"Skill", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		sizerSkill.Add( self.radioBtnSkill, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxSkillChoices = []
		self.comboBoxSkill = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxSkillChoices, 0 )
		self.comboBoxSkill.SetSelection( 0 )
		sizerSkill.Add( self.comboBoxSkill, 1, wx.ALL, 5 )
		
		sizerAction.Add( sizerSkill, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerAction, 0, wx.EXPAND|wx.ALL, 5 )
		
		sizerRating = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Rating" ), wx.HORIZONTAL )
		
		self.sliderRating = wx.Slider( self, wx.ID_ANY, 5, 0, 10, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL )
		sizerRating.Add( self.sliderRating, 1, wx.ALL, 5 )
		
		self.spinCtrlRating = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 5 )
		sizerRating.Add( self.spinCtrlRating, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerRating, 0, wx.ALL|wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.checkBoxTurn.Bind( wx.EVT_CHECKBOX, self.checkBoxTurn_CheckChanged )
		self.checkBoxTurn.Bind( wx.EVT_CHECKBOX, self.checkBoxHP_CheckChanged )
		self.checkBoxLevel.Bind( wx.EVT_CHECKBOX, self.checkBoxLevel_CheckChanged )
		self.checkBoxSwitch.Bind( wx.EVT_CHECKBOX, self.checkBoxSwitch_CheckChanged )
		self.radioBtnBasic.Bind( wx.EVT_RADIOBUTTON, self.radioBtnBasic_CheckChanged )
		self.radioBtnSkill.Bind( wx.EVT_RADIOBUTTON, self.radioBtnSkill_CheckChanged )
		self.sliderRating.Bind( wx.EVT_SCROLL, self.sliderRating_ValueChanged )
		self.spinCtrlRating.Bind( wx.EVT_SPINCTRL, self.spinCtrlRating_ValueChanged )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def checkBoxTurn_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxHP_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxLevel_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxSwitch_CheckChanged( self, event ):
		event.Skip()
	
	def radioBtnBasic_CheckChanged( self, event ):
		event.Skip()
	
	def radioBtnSkill_CheckChanged( self, event ):
		event.Skip()
	
	def sliderRating_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlRating_ValueChanged( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ChooseTreasure_Dialog
###########################################################################

class ChooseTreasure_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Treasure", pos = wx.DefaultPosition, size = wx.Size( 269,229 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.radioBtn_None = wx.RadioButton( self, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		MainSizer.Add( self.radioBtn_None, 0, wx.ALL|wx.EXPAND, 5 )
		
		sizerItem = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioBtn_Item = wx.RadioButton( self, wx.ID_ANY, u"Item", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		sizerItem.Add( self.radioBtn_Item, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxItemChoices = []
		self.comboBoxItem = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxItemChoices, 0 )
		self.comboBoxItem.SetSelection( 0 )
		sizerItem.Add( self.comboBoxItem, 1, wx.ALL, 5 )
		
		MainSizer.Add( sizerItem, 0, wx.EXPAND, 5 )
		
		sizerWeapon = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioBtn_Weapon = wx.RadioButton( self, wx.ID_ANY, u"Weapon", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		sizerWeapon.Add( self.radioBtn_Weapon, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		comboBoxWeaponChoices = []
		self.comboBoxWeapon = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxWeaponChoices, 0 )
		self.comboBoxWeapon.SetSelection( 0 )
		sizerWeapon.Add( self.comboBoxWeapon, 1, wx.ALL, 5 )
		
		MainSizer.Add( sizerWeapon, 0, wx.EXPAND, 5 )
		
		sizerArmor = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioBtn_Armor = wx.RadioButton( self, wx.ID_ANY, u"Armor", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		sizerArmor.Add( self.radioBtn_Armor, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		comboBoxArmorChoices = []
		self.comboBoxArmor = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxArmorChoices, 0 )
		self.comboBoxArmor.SetSelection( 0 )
		sizerArmor.Add( self.comboBoxArmor, 1, wx.ALL, 5 )
		
		MainSizer.Add( sizerArmor, 0, wx.EXPAND, 5 )
		
		self.labelProbability = wx.StaticText( self, wx.ID_ANY, u"Probability:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelProbability.Wrap( -1 )
		MainSizer.Add( self.labelProbability, 0, wx.ALL, 5 )
		
		self.spinCtrlProbability = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		MainSizer.Add( self.spinCtrlProbability, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class EventCondition_Dialog
###########################################################################

class EventCondition_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Condition", pos = wx.DefaultPosition, size = wx.Size( 310,259 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		sizerConditions = wx.BoxSizer( wx.VERTICAL )
		
		sizerTurn = wx.BoxSizer( wx.HORIZONTAL )
		
		self.checkBoxTurn = wx.CheckBox( self, wx.ID_ANY, u"Turn", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerTurn.Add( self.checkBoxTurn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlTurn1 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerTurn.Add( self.spinCtrlTurn1, 0, wx.ALL, 5 )
		
		self.labelPlus = wx.StaticText( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPlus.Wrap( -1 )
		sizerTurn.Add( self.labelPlus, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlTurn2 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerTurn.Add( self.spinCtrlTurn2, 0, wx.ALL, 5 )
		
		self.labelX = wx.StaticText( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelX.Wrap( -1 )
		sizerTurn.Add( self.labelX, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerConditions.Add( sizerTurn, 0, wx.EXPAND, 5 )
		
		sizerEnemy1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.checkBoxEnemy = wx.CheckBox( self, wx.ID_ANY, u"Enemy", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerEnemy1.Add( self.checkBoxEnemy, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxEnemyChoices = []
		self.comboBoxEnemy = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,-1 ), comboBoxEnemyChoices, 0 )
		self.comboBoxEnemy.SetSelection( 0 )
		sizerEnemy1.Add( self.comboBoxEnemy, 0, wx.ALL, 5 )
		
		self.labelHP1 = wx.StaticText( self, wx.ID_ANY, u"'s HP is", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelHP1.Wrap( -1 )
		sizerEnemy1.Add( self.labelHP1, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		sizerConditions.Add( sizerEnemy1, 0, wx.EXPAND, 5 )
		
		sizerEnemy2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelFiller1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		self.labelFiller1.Wrap( -1 )
		sizerEnemy2.Add( self.labelFiller1, 0, wx.ALL, 5 )
		
		self.spinCtrlEnemyHPPercent = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerEnemy2.Add( self.spinCtrlEnemyHPPercent, 0, wx.ALL, 5 )
		
		self.labelBelow1 = wx.StaticText( self, wx.ID_ANY, u"% or below", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBelow1.Wrap( -1 )
		sizerEnemy2.Add( self.labelBelow1, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		sizerConditions.Add( sizerEnemy2, 0, wx.EXPAND, 5 )
		
		sizerActor1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.checkBoxActor = wx.CheckBox( self, wx.ID_ANY, u"Actor", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerActor1.Add( self.checkBoxActor, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxActorChoices = []
		self.comboBoxActor = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,-1 ), comboBoxActorChoices, 0 )
		self.comboBoxActor.SetSelection( 0 )
		sizerActor1.Add( self.comboBoxActor, 0, wx.ALL, 5 )
		
		self.labelHP2 = wx.StaticText( self, wx.ID_ANY, u"'s HP is", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelHP2.Wrap( -1 )
		sizerActor1.Add( self.labelHP2, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		sizerConditions.Add( sizerActor1, 0, wx.EXPAND, 5 )
		
		sizerActor2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelFiller2 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		self.labelFiller2.Wrap( -1 )
		sizerActor2.Add( self.labelFiller2, 0, wx.ALL, 5 )
		
		self.spinCtrlActorHPPercent = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerActor2.Add( self.spinCtrlActorHPPercent, 0, wx.ALL, 5 )
		
		self.labelBelow2 = wx.StaticText( self, wx.ID_ANY, u"% or below", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBelow2.Wrap( -1 )
		sizerActor2.Add( self.labelBelow2, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		sizerConditions.Add( sizerActor2, 0, wx.EXPAND, 5 )
		
		sizerSwitch = wx.BoxSizer( wx.HORIZONTAL )
		
		self.checkBoxSwitch = wx.CheckBox( self, wx.ID_ANY, u"Switch", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerSwitch.Add( self.checkBoxSwitch, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxSwitchChoices = []
		self.comboBoxSwitch = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,-1 ), comboBoxSwitchChoices, 0 )
		self.comboBoxSwitch.SetSelection( 0 )
		sizerSwitch.Add( self.comboBoxSwitch, 0, wx.ALL, 5 )
		
		self.labelON = wx.StaticText( self, wx.ID_ANY, u"is ON", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelON.Wrap( -1 )
		sizerSwitch.Add( self.labelON, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		sizerConditions.Add( sizerSwitch, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerConditions, 1, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.checkBoxTurn.Bind( wx.EVT_CHECKBOX, self.checkBoxTurn_CheckChanged )
		self.checkBoxEnemy.Bind( wx.EVT_CHECKBOX, self.checkBoxEnemy_CheckChanged )
		self.checkBoxActor.Bind( wx.EVT_CHECKBOX, self.checkBoxActor_CheckChanged )
		self.checkBoxSwitch.Bind( wx.EVT_CHECKBOX, self.checkBoxSwitch_CheckChanged )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def checkBoxTurn_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxEnemy_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxActor_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxSwitch_CheckChanged( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class AnimationTiming_Dialog
###########################################################################

class AnimationTiming_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"SE and Flash Timing", pos = wx.DefaultPosition, size = wx.Size( 418,335 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		sizerFrame = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelFrame = wx.StaticText( self, wx.ID_ANY, u"Frame:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelFrame.Wrap( -1 )
		sizer1.Add( self.labelFrame, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlFrames = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer1.Add( self.spinCtrlFrames, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerFrame.Add( sizer1, 20, 0, 5 )
		
		sizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelSE = wx.StaticText( self, wx.ID_ANY, u"SE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelSE.Wrap( -1 )
		sizer2.Add( self.labelSE, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxSEChoices = []
		self.comboBoxSE = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxSEChoices, 0 )
		sizer2.Add( self.comboBoxSE, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerFrame.Add( sizer2, 45, 0, 5 )
		
		sizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelCondition = wx.StaticText( self, wx.ID_ANY, u"Condition:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelCondition.Wrap( -1 )
		sizer3.Add( self.labelCondition, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxConditionChoices = []
		self.comboBoxCondition = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxConditionChoices, 0 )
		self.comboBoxCondition.SetSelection( 0 )
		sizer3.Add( self.comboBoxCondition, 35, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerFrame.Add( sizer3, 35, 0, 5 )
		
		MainSizer.Add( sizerFrame, 0, wx.EXPAND, 5 )
		
		sizerFlash = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Flash" ), wx.VERTICAL )
		
		sizerFlashArea = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonNone = wx.RadioButton( self, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerFlashArea.Add( self.radioButtonNone, 0, wx.ALL, 5 )
		
		self.radioButtonTarget = wx.RadioButton( self, wx.ID_ANY, u"Target", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerFlashArea.Add( self.radioButtonTarget, 0, wx.ALL, 5 )
		
		self.radioButtonScreen = wx.RadioButton( self, wx.ID_ANY, u"Screen", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerFlashArea.Add( self.radioButtonScreen, 0, wx.ALL, 5 )
		
		self.radioButtonHideTarget = wx.RadioButton( self, wx.ID_ANY, u"Hide Target", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerFlashArea.Add( self.radioButtonHideTarget, 0, wx.ALL, 5 )
		
		sizerFlash.Add( sizerFlashArea, 0, wx.EXPAND, 5 )
		
		sizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		sizer7 = wx.BoxSizer( wx.VERTICAL )
		
		sizerRed = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelRed = wx.StaticText( self, wx.ID_ANY, u"Red:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelRed.Wrap( -1 )
		sizerRed.Add( self.labelRed, 20, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.sliderRed = wx.Slider( self, wx.ID_ANY, 255, 0, 255, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		sizerRed.Add( self.sliderRed, 55, wx.ALL, 5 )
		
		self.spinCtrlRed = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 255, 255 )
		sizerRed.Add( self.spinCtrlRed, 25, wx.ALL, 5 )
		
		sizer7.Add( sizerRed, 0, wx.EXPAND, 5 )
		
		sizerGreen = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelGreen = wx.StaticText( self, wx.ID_ANY, u"Green:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelGreen.Wrap( -1 )
		sizerGreen.Add( self.labelGreen, 20, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.sliderGreen = wx.Slider( self, wx.ID_ANY, 255, 0, 255, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		sizerGreen.Add( self.sliderGreen, 55, wx.ALL, 5 )
		
		self.spinCtrlGreen = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 255, 255 )
		sizerGreen.Add( self.spinCtrlGreen, 25, wx.ALL, 5 )
		
		sizer7.Add( sizerGreen, 0, wx.EXPAND, 5 )
		
		sizerBlue = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelBlue = wx.StaticText( self, wx.ID_ANY, u"Blue:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBlue.Wrap( -1 )
		sizerBlue.Add( self.labelBlue, 20, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.sliderBlue = wx.Slider( self, wx.ID_ANY, 255, 0, 255, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		sizerBlue.Add( self.sliderBlue, 55, wx.ALL, 5 )
		
		self.spinCtrlBlue = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 255, 255 )
		sizerBlue.Add( self.spinCtrlBlue, 25, wx.ALL, 5 )
		
		sizer7.Add( sizerBlue, 0, wx.EXPAND, 5 )
		
		sizerStrength = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelStrength = wx.StaticText( self, wx.ID_ANY, u"Strength:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelStrength.Wrap( -1 )
		sizerStrength.Add( self.labelStrength, 20, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.sliderStrength = wx.Slider( self, wx.ID_ANY, 255, 0, 255, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		sizerStrength.Add( self.sliderStrength, 55, wx.ALL, 5 )
		
		self.spinCtrlStrength = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 255, 255 )
		sizerStrength.Add( self.spinCtrlStrength, 25, wx.ALL, 5 )
		
		sizer7.Add( sizerStrength, 0, wx.EXPAND, 5 )
		
		sizer6.Add( sizer7, 75, wx.EXPAND, 5 )
		
		self.m_bitmap33 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		sizer6.Add( self.m_bitmap33, 25, wx.ALL|wx.EXPAND, 5 )
		
		sizer4.Add( sizer6, 1, wx.EXPAND, 5 )
		
		sizerFlash.Add( sizer4, 1, wx.EXPAND, 5 )
		
		sizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDuration = wx.StaticText( self, wx.ID_ANY, u"Duration:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelDuration.Wrap( -1 )
		sizer5.Add( self.labelDuration, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlDurationFrames = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizer5.Add( self.spinCtrlDurationFrames, 0, wx.ALL, 5 )
		
		self.labelFrames = wx.StaticText( self, wx.ID_ANY, u"Frames", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelFrames.Wrap( -1 )
		sizer5.Add( self.labelFrames, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerFlash.Add( sizer5, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerFlash, 1, wx.EXPAND|wx.ALL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.spinCtrlFrames.Bind( wx.EVT_SPINCTRL, self.spinCtrlFrame_ValueChanged )
		self.comboBoxSE.Bind( wx.EVT_LEFT_DOWN, self.comboBoxSE_LeftClicked )
		self.comboBoxCondition.Bind( wx.EVT_CHOICE, self.comboBoxCondition_SelectionChanged )
		self.radioButtonNone.Bind( wx.EVT_RADIOBUTTON, self.radioButtonNone_Checked )
		self.radioButtonTarget.Bind( wx.EVT_RADIOBUTTON, self.radioButtonTarget_Checked )
		self.radioButtonScreen.Bind( wx.EVT_RADIOBUTTON, self.radioButtonScreen_Checked )
		self.radioButtonHideTarget.Bind( wx.EVT_RADIOBUTTON, self.radioButtonHideTarget_Checked )
		self.sliderRed.Bind( wx.EVT_SCROLL, self.slideCtrlRed_ValueChanged )
		self.spinCtrlRed.Bind( wx.EVT_SPINCTRL, self.spinCtrlRed_ValueChanged )
		self.sliderGreen.Bind( wx.EVT_SCROLL, self.slideCtrlGreen_ValueChanged )
		self.spinCtrlGreen.Bind( wx.EVT_SPINCTRL, self.spinCtrlGreen_ValueChanged )
		self.sliderBlue.Bind( wx.EVT_SCROLL, self.slideCtrlBlue_ValueChanged )
		self.spinCtrlBlue.Bind( wx.EVT_SPINCTRL, self.spinCtrlBlue_ValueChanged )
		self.sliderStrength.Bind( wx.EVT_SCROLL, self.slideCtrlStrength_ValueChanged )
		self.spinCtrlStrength.Bind( wx.EVT_SPINCTRL, self.spinCtrlStrength_ValueChanged )
		self.spinCtrlDurationFrames.Bind( wx.EVT_SPINCTRL, self.spinCtrlDurationFrames_ValueChanged )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def spinCtrlFrame_ValueChanged( self, event ):
		event.Skip()
	
	def comboBoxSE_LeftClicked( self, event ):
		event.Skip()
	
	def comboBoxCondition_SelectionChanged( self, event ):
		event.Skip()
	
	def radioButtonNone_Checked( self, event ):
		event.Skip()
	
	def radioButtonTarget_Checked( self, event ):
		event.Skip()
	
	def radioButtonScreen_Checked( self, event ):
		event.Skip()
	
	def radioButtonHideTarget_Checked( self, event ):
		event.Skip()
	
	def slideCtrlRed_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlRed_ValueChanged( self, event ):
		event.Skip()
	
	def slideCtrlGreen_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlGreen_ValueChanged( self, event ):
		event.Skip()
	
	def slideCtrlBlue_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlBlue_ValueChanged( self, event ):
		event.Skip()
	
	def slideCtrlStrength_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlStrength_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlDurationFrames_ValueChanged( self, event ):
		event.Skip()
	

###########################################################################
## Class AnimationTweening_Dialog
###########################################################################

class AnimationTweening_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tweening", pos = wx.DefaultPosition, size = wx.Size( 179,263 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.labelFrames = wx.StaticText( self, wx.ID_ANY, u"Frames:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelFrames.Wrap( -1 )
		MainSizer.Add( self.labelFrames, 0, wx.ALL, 5 )
		
		sizerFrames = wx.BoxSizer( wx.HORIZONTAL )
		
		self.spinCtrlFramesStart = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerFrames.Add( self.spinCtrlFramesStart, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelTilde1 = wx.StaticText( self, wx.ID_ANY, u"~", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTilde1.Wrap( -1 )
		sizerFrames.Add( self.labelTilde1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlFramesEnd = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerFrames.Add( self.spinCtrlFramesEnd, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerFrames, 0, wx.EXPAND, 5 )
		
		self.labelCells = wx.StaticText( self, wx.ID_ANY, u"Cells:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelCells.Wrap( -1 )
		MainSizer.Add( self.labelCells, 0, wx.ALL, 5 )
		
		sizerCells = wx.BoxSizer( wx.HORIZONTAL )
		
		self.spinCtrlCellsStart = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerCells.Add( self.spinCtrlCellsStart, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelTilde2 = wx.StaticText( self, wx.ID_ANY, u"~", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTilde2.Wrap( -1 )
		sizerCells.Add( self.labelTilde2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlCellsEnd = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerCells.Add( self.spinCtrlCellsEnd, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerCells, 0, wx.EXPAND, 5 )
		
		sizerTweeningItems = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tweening Items" ), wx.VERTICAL )
		
		self.checkBoxPattern = wx.CheckBox( self, wx.ID_ANY, u"Pattern", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerTweeningItems.Add( self.checkBoxPattern, 0, wx.ALL, 5 )
		
		self.checkBoxPosition = wx.CheckBox( self, wx.ID_ANY, u"Position / Zoom / Angle", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerTweeningItems.Add( self.checkBoxPosition, 0, wx.ALL, 5 )
		
		self.checkBoxOpacity = wx.CheckBox( self, wx.ID_ANY, u"Opacity / Blending", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerTweeningItems.Add( self.checkBoxOpacity, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerTweeningItems, 0, wx.EXPAND|wx.ALL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class AnimationEntireSlide_Dialog
###########################################################################

class AnimationEntireSlide_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Entire Slide", pos = wx.DefaultPosition, size = wx.Size( 179,200 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.labelFrames = wx.StaticText( self, wx.ID_ANY, u"Frames:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelFrames.Wrap( -1 )
		MainSizer.Add( self.labelFrames, 0, wx.ALL, 5 )
		
		sizerFrames = wx.BoxSizer( wx.HORIZONTAL )
		
		self.sinCtrlFramesStart = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerFrames.Add( self.sinCtrlFramesStart, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelTilde = wx.StaticText( self, wx.ID_ANY, u"~", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTilde.Wrap( -1 )
		sizerFrames.Add( self.labelTilde, 0, wx.ALL, 5 )
		
		self.spinCtrlFramesEnd = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerFrames.Add( self.spinCtrlFramesEnd, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerFrames, 0, wx.EXPAND, 5 )
		
		sizerMovement = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Movement Amount" ), wx.HORIZONTAL )
		
		bSizer258 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelMoveX = wx.StaticText( self, wx.ID_ANY, u"X:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMoveX.Wrap( -1 )
		bSizer258.Add( self.labelMoveX, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlMoveX = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer258.Add( self.spinCtrlMoveX, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerMovement.Add( bSizer258, 1, wx.EXPAND, 5 )
		
		bSizer259 = wx.BoxSizer( wx.VERTICAL )
		
		self.labelMoveY = wx.StaticText( self, wx.ID_ANY, u"Y:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMoveY.Wrap( -1 )
		bSizer259.Add( self.labelMoveY, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlMoveY = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer259.Add( self.spinCtrlMoveY, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizerMovement.Add( bSizer259, 1, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerMovement, 0, wx.EXPAND|wx.ALL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Click )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Click( self, event ):
		event.Skip()
	
	def buttonCancel_Click( self, event ):
		event.Skip()
	

###########################################################################
## Class AnimationCellBatch_Dialog
###########################################################################

class AnimationCellBatch_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cell Batch", pos = wx.DefaultPosition, size = wx.Size( 335,284 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.labelFrames = wx.StaticText( self, wx.ID_ANY, u"Frames:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelFrames.Wrap( -1 )
		MainSizer.Add( self.labelFrames, 0, wx.ALL, 5 )
		
		sizerFrames = wx.BoxSizer( wx.HORIZONTAL )
		
		self.spinCtrlFramesStart = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerFrames.Add( self.spinCtrlFramesStart, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelTilde1 = wx.StaticText( self, wx.ID_ANY, u"~", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTilde1.Wrap( -1 )
		sizerFrames.Add( self.labelTilde1, 0, wx.ALL, 5 )
		
		self.spinCtrlFramesEnd = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerFrames.Add( self.spinCtrlFramesEnd, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerFrames, 0, wx.EXPAND, 5 )
		
		self.labelCells = wx.StaticText( self, wx.ID_ANY, u"Cells:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelCells.Wrap( -1 )
		MainSizer.Add( self.labelCells, 0, wx.ALL, 5 )
		
		sizerCells = wx.BoxSizer( wx.HORIZONTAL )
		
		self.spinCtrlCellsStart = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerCells.Add( self.spinCtrlCellsStart, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelTilde2 = wx.StaticText( self, wx.ID_ANY, u"~", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTilde2.Wrap( -1 )
		sizerCells.Add( self.labelTilde2, 0, wx.ALL, 5 )
		
		self.spinCtrlCellsEnd = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerCells.Add( self.spinCtrlCellsEnd, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerCells, 0, wx.EXPAND, 5 )
		
		sizerSettings = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		bSizer268 = wx.BoxSizer( wx.VERTICAL )
		
		self.checkBoxPattern = wx.CheckBox( self, wx.ID_ANY, u"Pattern", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer268.Add( self.checkBoxPattern, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlPattern = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer268.Add( self.spinCtrlPattern, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.checkBoxAngle = wx.CheckBox( self, wx.ID_ANY, u"Angle", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer268.Add( self.checkBoxAngle, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlAngle = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer268.Add( self.spinCtrlAngle, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerSettings.Add( bSizer268, 1, wx.EXPAND, 5 )
		
		bSizer2681 = wx.BoxSizer( wx.VERTICAL )
		
		self.checkBoxX = wx.CheckBox( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2681.Add( self.checkBoxX, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlX = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer2681.Add( self.spinCtrlX, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.checkBoxFlip = wx.CheckBox( self, wx.ID_ANY, u"Flip", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2681.Add( self.checkBoxFlip, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlFlip = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer2681.Add( self.spinCtrlFlip, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerSettings.Add( bSizer2681, 1, wx.EXPAND, 5 )
		
		bSizer2682 = wx.BoxSizer( wx.VERTICAL )
		
		self.checkBoxY = wx.CheckBox( self, wx.ID_ANY, u"Y", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2682.Add( self.checkBoxY, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlY = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer2682.Add( self.spinCtrlY, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.checkBoxOpacity = wx.CheckBox( self, wx.ID_ANY, u"Opacity", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2682.Add( self.checkBoxOpacity, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlOpacity = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer2682.Add( self.spinCtrlOpacity, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerSettings.Add( bSizer2682, 1, wx.EXPAND, 5 )
		
		bSizer2683 = wx.BoxSizer( wx.VERTICAL )
		
		self.checkBoxZoom = wx.CheckBox( self, wx.ID_ANY, u"Zoom", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2683.Add( self.checkBoxZoom, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlZoom = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer2683.Add( self.spinCtrlZoom, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.checkBoxBlending = wx.CheckBox( self, wx.ID_ANY, u"Blending", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2683.Add( self.checkBoxBlending, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlBlending = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer2683.Add( self.spinCtrlBlending, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerSettings.Add( bSizer2683, 1, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerSettings, 0, wx.EXPAND|wx.ALL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.checkBoxPattern.Bind( wx.EVT_CHECKBOX, self.checkBoxPattern_CheckChanged )
		self.checkBoxAngle.Bind( wx.EVT_CHECKBOX, self.checkBoxAngle_CheckChanged )
		self.checkBoxX.Bind( wx.EVT_CHECKBOX, self.checkBoxX_CheckChanged )
		self.checkBoxFlip.Bind( wx.EVT_CHECKBOX, self.checkBoxFlip_CheckChanged )
		self.checkBoxY.Bind( wx.EVT_CHECKBOX, self.checkBoxY_CheckChanged )
		self.checkBoxOpacity.Bind( wx.EVT_CHECKBOX, self.checkBoxOpacity_CheckChanged )
		self.checkBoxZoom.Bind( wx.EVT_CHECKBOX, self.checkBoxZoom_CheckChanged )
		self.checkBoxBlending.Bind( wx.EVT_CHECKBOX, self.checkBoxBlending_CheckChanged )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def checkBoxPattern_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxAngle_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxX_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxFlip_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxY_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxOpacity_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxZoom_CheckChanged( self, event ):
		event.Skip()
	
	def checkBoxBlending_CheckChanged( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class AnimationCellProperties_Dialog
###########################################################################

class AnimationCellProperties_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cell Properties", pos = wx.DefaultPosition, size = wx.Size( 321,160 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		sizerLabels1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelPattern = wx.StaticText( self, wx.ID_ANY, u"Pattern:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPattern.Wrap( -1 )
		sizerLabels1.Add( self.labelPattern, 1, wx.ALL, 5 )
		
		self.labelX = wx.StaticText( self, wx.ID_ANY, u"X:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelX.Wrap( -1 )
		sizerLabels1.Add( self.labelX, 1, wx.ALL, 5 )
		
		self.labelY = wx.StaticText( self, wx.ID_ANY, u"Y:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelY.Wrap( -1 )
		sizerLabels1.Add( self.labelY, 1, wx.ALL, 5 )
		
		self.labelZoom = wx.StaticText( self, wx.ID_ANY, u"Zoom:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelZoom.Wrap( -1 )
		sizerLabels1.Add( self.labelZoom, 1, wx.ALL, 5 )
		
		MainSizer.Add( sizerLabels1, 0, wx.EXPAND, 5 )
		
		sizerControls1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.spinCtrlPattern = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerControls1.Add( self.spinCtrlPattern, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.spinCtrlX = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerControls1.Add( self.spinCtrlX, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.spinCtrlY = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerControls1.Add( self.spinCtrlY, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.spinCtrlZoom = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerControls1.Add( self.spinCtrlZoom, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerControls1, 0, wx.EXPAND, 5 )
		
		sizerLabels2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelAngle = wx.StaticText( self, wx.ID_ANY, u"Angle:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAngle.Wrap( -1 )
		sizerLabels2.Add( self.labelAngle, 1, wx.ALL, 5 )
		
		self.labelFlip = wx.StaticText( self, wx.ID_ANY, u"Flip:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelFlip.Wrap( -1 )
		sizerLabels2.Add( self.labelFlip, 1, wx.ALL, 5 )
		
		self.labelOpacity = wx.StaticText( self, wx.ID_ANY, u"Opacity:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelOpacity.Wrap( -1 )
		sizerLabels2.Add( self.labelOpacity, 1, wx.ALL, 5 )
		
		self.labelBlending = wx.StaticText( self, wx.ID_ANY, u"Blending:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBlending.Wrap( -1 )
		sizerLabels2.Add( self.labelBlending, 1, wx.ALL, 5 )
		
		MainSizer.Add( sizerLabels2, 0, wx.EXPAND, 5 )
		
		sizerControls2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.spinCtrlAngle = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerControls2.Add( self.spinCtrlAngle, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.spinCtrlFlip = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerControls2.Add( self.spinCtrlFlip, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.spinCtrlOpacity = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerControls2.Add( self.spinCtrlOpacity, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.spinCtrlBlending = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerControls2.Add( self.spinCtrlBlending, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerControls2, 0, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ChooseFogGraphic_Dialog
###########################################################################

class ChooseFogGraphic_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Fog Graphic", pos = wx.DefaultPosition, size = wx.Size( 714,468 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		sizerControls = wx.BoxSizer( wx.HORIZONTAL )
		
		listBoxGraphicsChoices = []
		self.listBoxGraphics = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,-1 ), listBoxGraphicsChoices, 0 )
		sizerControls.Add( self.listBoxGraphics, 0, wx.ALL|wx.EXPAND, 5 )
		
		sizerPreview = wx.BoxSizer( wx.VERTICAL )
		
		sizerGraphic = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bitmapGraphic = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER )
		sizerGraphic.Add( self.bitmapGraphic, 1, wx.EXPAND|wx.ALL, 5 )
		
		sizerOptions = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Options" ), wx.VERTICAL )
		
		self.labelOpacity = wx.StaticText( self, wx.ID_ANY, u"Opacity:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelOpacity.Wrap( -1 )
		sizerOptions.Add( self.labelOpacity, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlOpacity = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 255, 255 )
		sizerOptions.Add( self.spinCtrlOpacity, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelBlending = wx.StaticText( self, wx.ID_ANY, u"Blending:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBlending.Wrap( -1 )
		sizerOptions.Add( self.labelBlending, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxBlendingChoices = [ u"Normal", u"Addition", u"Subtraction" ]
		self.comboBoxBlending = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 64,-1 ), comboBoxBlendingChoices, 0 )
		self.comboBoxBlending.SetSelection( 0 )
		sizerOptions.Add( self.comboBoxBlending, 0, wx.ALL, 5 )
		
		self.labelZoom = wx.StaticText( self, wx.ID_ANY, u"Zoom:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelZoom.Wrap( -1 )
		sizerOptions.Add( self.labelZoom, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlZoom = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerOptions.Add( self.spinCtrlZoom, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelSX = wx.StaticText( self, wx.ID_ANY, u"SX:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelSX.Wrap( -1 )
		sizerOptions.Add( self.labelSX, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlSX = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerOptions.Add( self.spinCtrlSX, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelSY = wx.StaticText( self, wx.ID_ANY, u"SY:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelSY.Wrap( -1 )
		sizerOptions.Add( self.labelSY, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.spinCtrlSY = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerOptions.Add( self.spinCtrlSY, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerGraphic.Add( sizerOptions, 0, wx.EXPAND|wx.ALL, 5 )
		
		sizerPreview.Add( sizerGraphic, 1, wx.EXPAND, 5 )
		
		sizerHue = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Hue" ), wx.VERTICAL )
		
		self.sliderHue = wx.Slider( self, wx.ID_ANY, 0, 0, 359, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		sizerHue.Add( self.sliderHue, 0, wx.ALL|wx.EXPAND, 5 )
		
		sizerPreview.Add( sizerHue, 0, wx.EXPAND|wx.ALL, 5 )
		
		sizerControls.Add( sizerPreview, 1, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerControls, 1, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.listBoxGraphics.Bind( wx.EVT_LISTBOX, self.listBoxGraphics_SelectionChanged )
		self.spinCtrlOpacity.Bind( wx.EVT_SPINCTRL, self.spinCtrOpacityl_ValueChanged )
		self.comboBoxBlending.Bind( wx.EVT_CHOICE, self.comboBoxBlending_SelectionChanged )
		self.spinCtrlZoom.Bind( wx.EVT_SPINCTRL, self.spinCtrlZoom_ValueChanged )
		self.spinCtrlSX.Bind( wx.EVT_SPINCTRL, self.spinCtrlSX_ValueChanged )
		self.spinCtrlSY.Bind( wx.EVT_SPINCTRL, self.spinCtrlSY_ValueChanged )
		self.sliderHue.Bind( wx.EVT_SCROLL, self.sliderHue_Scrolled )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def listBoxGraphics_SelectionChanged( self, event ):
		event.Skip()
	
	def spinCtrOpacityl_ValueChanged( self, event ):
		event.Skip()
	
	def comboBoxBlending_SelectionChanged( self, event ):
		event.Skip()
	
	def spinCtrlZoom_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlSX_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlSY_ValueChanged( self, event ):
		event.Skip()
	
	def sliderHue_Scrolled( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ChooseActor_Dialog
###########################################################################

class ChooseActor_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Initial Party", pos = wx.DefaultPosition, size = wx.Size( 290,104 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerActor = wx.BoxSizer( wx.VERTICAL )
		
		self.labelActor = wx.StaticText( self, wx.ID_ANY, u"Actor:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelActor.Wrap( -1 )
		sizerActor.Add( self.labelActor, 0, wx.ALL, 5 )
		
		comboBoxActorsChoices = []
		self.comboBoxActors = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxActorsChoices, 0 )
		self.comboBoxActors.SetSelection( 0 )
		sizerActor.Add( self.comboBoxActors, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerActor, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ChooseSwitchVariable_Dialog
###########################################################################

class ChooseSwitchVariable_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Switch", pos = wx.DefaultPosition, size = wx.Size( 317,398 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		sizerControls = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerGroup = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapHeader = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../Database Panel Images/Switch.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerGroup.Add( self.bitmapHeader, 0, wx.ALL|wx.EXPAND, 5 )
		
		listBoxGroupChoices = []
		self.listBoxGroup = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxGroupChoices, 0 )
		sizerGroup.Add( self.listBoxGroup, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.buttonChangeMax = wx.Button( self, wx.ID_ANY, u"Change Max...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerGroup.Add( self.buttonChangeMax, 0, wx.ALL|wx.EXPAND, 5 )
		
		sizerControls.Add( sizerGroup, 40, wx.EXPAND, 5 )
		
		sizerItemList = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		listBoxItemsChoices = []
		self.listBoxItems = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBoxItemsChoices, 0 )
		sizerItemList.Add( self.listBoxItems, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizerName = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelName.Wrap( -1 )
		sizerName.Add( self.labelName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.textCtrlName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerName.Add( self.textCtrlName, 1, wx.ALL, 5 )
		
		sizerItemList.Add( sizerName, 0, wx.EXPAND, 5 )
		
		sizerControls.Add( sizerItemList, 60, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerControls, 1, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		self.buttonApply = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonApply, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.listBoxGroup.Bind( wx.EVT_LISTBOX, self.listBoxGroup_SelectionChanged )
		self.buttonChangeMax.Bind( wx.EVT_BUTTON, self.buttonMax_Clicked )
		self.listBoxItems.Bind( wx.EVT_LISTBOX, self.listBoxItems_SelectionChanged )
		self.textCtrlName.Bind( wx.EVT_TEXT, self.textCtrlName_TextChanged )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
		self.buttonApply.Bind( wx.EVT_BUTTON, self.buttonApply_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def listBoxGroup_SelectionChanged( self, event ):
		event.Skip()
	
	def buttonMax_Clicked( self, event ):
		event.Skip()
	
	def listBoxItems_SelectionChanged( self, event ):
		event.Skip()
	
	def textCtrlName_TextChanged( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	
	def buttonApply_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ShowText_Dialog
###########################################################################

class ShowText_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Show Text", pos = wx.DefaultPosition, size = wx.Size( 322,160 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.textCtrlMessageText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_WORDWRAP )
		MainSizer.Add( self.textCtrlMessageText, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ShowChoices_Dialog
###########################################################################

class ShowChoices_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Show Choices", pos = wx.DefaultPosition, size = wx.Size( 315,268 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		sizerControls = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerChoices = wx.BoxSizer( wx.VERTICAL )
		
		self.labelChoice1 = wx.StaticText( self, wx.ID_ANY, u"Choice 1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelChoice1.Wrap( -1 )
		sizerChoices.Add( self.labelChoice1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlChoice1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerChoices.Add( self.textCtrlChoice1, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelChoice2 = wx.StaticText( self, wx.ID_ANY, u"Choice 2:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelChoice2.Wrap( -1 )
		sizerChoices.Add( self.labelChoice2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlChoice2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerChoices.Add( self.textCtrlChoice2, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelChoice3 = wx.StaticText( self, wx.ID_ANY, u"Choice 3:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelChoice3.Wrap( -1 )
		sizerChoices.Add( self.labelChoice3, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlChoice3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerChoices.Add( self.textCtrlChoice3, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelChoice4 = wx.StaticText( self, wx.ID_ANY, u"Choice 4:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelChoice4.Wrap( -1 )
		sizerChoices.Add( self.labelChoice4, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrlChoice4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerChoices.Add( self.textCtrlChoice4, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizerControls.Add( sizerChoices, 1, wx.EXPAND, 5 )
		
		sizerCancel = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"When Cancel" ), wx.VERTICAL )
		
		self.radioButtonDisallow = wx.RadioButton( self, wx.ID_ANY, u"Disallow", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerCancel.Add( self.radioButtonDisallow, 0, wx.ALL, 5 )
		
		self.radioButtonChoice1 = wx.RadioButton( self, wx.ID_ANY, u"Choice 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerCancel.Add( self.radioButtonChoice1, 0, wx.ALL, 5 )
		
		self.radioButtonChoice2 = wx.RadioButton( self, wx.ID_ANY, u"Choice 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerCancel.Add( self.radioButtonChoice2, 0, wx.ALL, 5 )
		
		self.radioButtonChoice3 = wx.RadioButton( self, wx.ID_ANY, u"Choice 3", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerCancel.Add( self.radioButtonChoice3, 0, wx.ALL, 5 )
		
		self.radioButtonChoice4 = wx.RadioButton( self, wx.ID_ANY, u"Choice 4", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerCancel.Add( self.radioButtonChoice4, 0, wx.ALL, 5 )
		
		self.radioButtonBranch = wx.RadioButton( self, wx.ID_ANY, u"Branch", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerCancel.Add( self.radioButtonBranch, 0, wx.ALL, 5 )
		
		sizerControls.Add( sizerCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerControls, 1, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class InputNumber_Dialog
###########################################################################

class InputNumber_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Input Number", pos = wx.DefaultPosition, size = wx.Size( 284,130 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerVariable = wx.BoxSizer( wx.VERTICAL )
		
		self.labelVariable = wx.StaticText( self, wx.ID_ANY, u"Variable for Number:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelVariable.Wrap( -1 )
		sizerVariable.Add( self.labelVariable, 0, wx.ALL, 5 )
		
		comboBoxVariableChoices = []
		self.comboBoxVariable = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxVariableChoices, 0 )
		sizerVariable.Add( self.comboBoxVariable, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelDigits = wx.StaticText( self, wx.ID_ANY, u"Digits:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelDigits.Wrap( -1 )
		sizerVariable.Add( self.labelDigits, 0, wx.ALL, 5 )
		
		self.spinCtrlDigits = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerVariable.Add( self.spinCtrlDigits, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerVariable, 1, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.comboBoxVariable.Bind( wx.EVT_LEFT_DOWN, self.comboBoxVariable_Clicked )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def comboBoxVariable_Clicked( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ChangeTextOptions_Dialog
###########################################################################

class ChangeTextOptions_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Change Text Options", pos = wx.DefaultPosition, size = wx.Size( 238,119 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		radioBoxPositionChoices = [ u"Top", u"Middle", u"Bottom" ]
		self.radioBoxPosition = wx.RadioBox( self, wx.ID_ANY, u"Position", wx.DefaultPosition, wx.DefaultSize, radioBoxPositionChoices, 1, wx.RA_SPECIFY_COLS )
		self.radioBoxPosition.SetSelection( 0 )
		MainSizer.Add( self.radioBoxPosition, 0, wx.ALL, 5 )
		
		radioBoxWindowChoices = [ u"Show", u"Hide" ]
		self.radioBoxWindow = wx.RadioBox( self, wx.ID_ANY, u"Window", wx.DefaultPosition, wx.DefaultSize, radioBoxWindowChoices, 1, wx.RA_SPECIFY_COLS )
		self.radioBoxWindow.SetSelection( 0 )
		MainSizer.Add( self.radioBoxWindow, 0, wx.ALL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.EXPAND, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ButonProcessing_Dialog
###########################################################################

class ButonProcessing_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Button Input Processing", pos = wx.DefaultPosition, size = wx.Size( 274,97 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerVariable = wx.BoxSizer( wx.VERTICAL )
		
		self.labelVariable = wx.StaticText( self, wx.ID_ANY, u"Variable for Button Code:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelVariable.Wrap( -1 )
		sizerVariable.Add( self.labelVariable, 0, wx.ALL, 5 )
		
		comboBoxVariableChoices = []
		self.comboBoxVariable = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxVariableChoices, 0 )
		sizerVariable.Add( self.comboBoxVariable, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerVariable, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.EXPAND, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.comboBoxVariable.Bind( wx.EVT_LEFT_DOWN, self.comboBoxVariable_Clicked )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def comboBoxVariable_Clicked( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class Wait_Dialog
###########################################################################

class Wait_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Wait", pos = wx.DefaultPosition, size = wx.Size( 242,94 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerControls = wx.BoxSizer( wx.VERTICAL )
		
		self.labelTime = wx.StaticText( self, wx.ID_ANY, u"Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTime.Wrap( -1 )
		sizerControls.Add( self.labelTime, 0, wx.ALL, 5 )
		
		sizerWait = wx.BoxSizer( wx.HORIZONTAL )
		
		self.spinCtrlFrames = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerWait.Add( self.spinCtrlFrames, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelFrames = wx.StaticText( self, wx.ID_ANY, u"Frames", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelFrames.Wrap( -1 )
		sizerWait.Add( self.labelFrames, 0, wx.ALL, 5 )
		
		sizerControls.Add( sizerWait, 0, 0, 5 )
		
		MainSizer.Add( sizerControls, 1, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class Comment_Dialog
###########################################################################

class Comment_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Comment", pos = wx.DefaultPosition, size = wx.Size( 256,177 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.textCtrlComment = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_WORDWRAP )
		MainSizer.Add( self.textCtrlComment, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ConditionalBranch_Dialog
###########################################################################

class ConditionalBranch_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Conditional Branch", pos = wx.DefaultPosition, size = wx.Size( 375,340 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.noteBookConditions = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panelConditions1 = wx.Panel( self.noteBookConditions, wx.ID_ANY, wx.DefaultPosition, wx.Size( 9,-1 ), wx.TAB_TRAVERSAL )
		sizerTab1 = wx.BoxSizer( wx.VERTICAL )
		
		sizerLineSwitch = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonSwitch = wx.RadioButton( self.panelConditions1, wx.ID_ANY, u"Switch", wx.DefaultPosition, wx.Size( 72,-1 ), wx.RB_SINGLE )
		sizerLineSwitch.Add( self.radioButtonSwitch, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxSwitchChoices = []
		self.comboBoxSwitch = wx.ComboBox( self.panelConditions1, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.Size( 160,-1 ), comboBoxSwitchChoices, 0 )
		sizerLineSwitch.Add( self.comboBoxSwitch, 0, wx.ALL, 5 )
		
		self.labelIsONOFF = wx.StaticText( self.panelConditions1, wx.ID_ANY, u"is", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelIsONOFF.Wrap( -1 )
		sizerLineSwitch.Add( self.labelIsONOFF, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxSwitchValueChoices = [ u"ON", u"OFF" ]
		self.comboBoxSwitchValue = wx.Choice( self.panelConditions1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 64,-1 ), comboBoxSwitchValueChoices, 0 )
		self.comboBoxSwitchValue.SetSelection( 0 )
		sizerLineSwitch.Add( self.comboBoxSwitchValue, 0, wx.ALL, 5 )
		
		sizerTab1.Add( sizerLineSwitch, 0, wx.EXPAND, 5 )
		
		sizerLineVariable1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonVariable = wx.RadioButton( self.panelConditions1, wx.ID_ANY, u"Variable", wx.DefaultPosition, wx.Size( 72,-1 ), wx.RB_SINGLE )
		sizerLineVariable1.Add( self.radioButtonVariable, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxVariableChoices = []
		self.comboBoxVariable = wx.ComboBox( self.panelConditions1, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.Size( 160,-1 ), comboBoxVariableChoices, 0 )
		sizerLineVariable1.Add( self.comboBoxVariable, 0, wx.ALL, 5 )
		
		self.labelIsValue = wx.StaticText( self.panelConditions1, wx.ID_ANY, u"is", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelIsValue.Wrap( -1 )
		sizerLineVariable1.Add( self.labelIsValue, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerTab1.Add( sizerLineVariable1, 0, wx.EXPAND, 5 )
		
		sizerLineVariable2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDummy1 = wx.StaticText( self.panelConditions1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		self.labelDummy1.Wrap( -1 )
		sizerLineVariable2.Add( self.labelDummy1, 0, wx.ALL, 5 )
		
		comboBoxVariableModifierChoices = []
		self.comboBoxVariableModifier = wx.ComboBox( self.panelConditions1, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.Size( 192,-1 ), comboBoxVariableModifierChoices, 0 )
		sizerLineVariable2.Add( self.comboBoxVariableModifier, 0, wx.ALL, 5 )
		
		sizerTab1.Add( sizerLineVariable2, 0, wx.EXPAND, 5 )
		
		sizerLineVariable3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDummy2 = wx.StaticText( self.panelConditions1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		self.labelDummy2.Wrap( -1 )
		sizerLineVariable3.Add( self.labelDummy2, 0, wx.ALL, 5 )
		
		self.radioButtonConstant = wx.RadioButton( self.panelConditions1, wx.ID_ANY, u"Constant", wx.DefaultPosition, wx.Size( 72,-1 ), wx.RB_GROUP )
		sizerLineVariable3.Add( self.radioButtonConstant, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlConstantValue = wx.SpinCtrl( self.panelConditions1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerLineVariable3.Add( self.spinCtrlConstantValue, 0, wx.ALL, 5 )
		
		sizerTab1.Add( sizerLineVariable3, 0, wx.EXPAND, 5 )
		
		sizerLineVariable4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDummy3 = wx.StaticText( self.panelConditions1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		self.labelDummy3.Wrap( -1 )
		sizerLineVariable4.Add( self.labelDummy3, 0, wx.ALL, 5 )
		
		self.radioButtonVariableValue = wx.RadioButton( self.panelConditions1, wx.ID_ANY, u"Variable", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerLineVariable4.Add( self.radioButtonVariableValue, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxVariableValueChoices = []
		self.comboBoxVariableValue = wx.ComboBox( self.panelConditions1, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, comboBoxVariableValueChoices, 0 )
		sizerLineVariable4.Add( self.comboBoxVariableValue, 1, wx.ALL, 5 )
		
		sizerTab1.Add( sizerLineVariable4, 0, wx.EXPAND, 5 )
		
		sizerSelfSwitch = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonSelfSwitch = wx.RadioButton( self.panelConditions1, wx.ID_ANY, u"Self-Switch", wx.DefaultPosition, wx.Size( 72,-1 ), wx.RB_GROUP|wx.RB_SINGLE )
		sizerSelfSwitch.Add( self.radioButtonSelfSwitch, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxLettersChoices = [ u"A", u"B", u"C", u"D", u"E", u"F", u"G", u"H", u"I", u"J", u"K", u"L", u"M", u"N", u"O", u"P", u"Q", u"R", u"S", u"T", u"U", u"V", u"W", u"X", u"Y", u"Z" ]
		self.comboBoxLetters = wx.Choice( self.panelConditions1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 64,-1 ), comboBoxLettersChoices, 0 )
		self.comboBoxLetters.SetSelection( 0 )
		sizerSelfSwitch.Add( self.comboBoxLetters, 0, wx.ALL, 5 )
		
		self.labelIsSelfSwitch = wx.StaticText( self.panelConditions1, wx.ID_ANY, u"is", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelIsSelfSwitch.Wrap( -1 )
		sizerSelfSwitch.Add( self.labelIsSelfSwitch, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxSelfSwitchValueChoices = [ u"ON", u"OFF" ]
		self.comboBoxSelfSwitchValue = wx.Choice( self.panelConditions1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 64,-1 ), comboBoxSelfSwitchValueChoices, 0 )
		self.comboBoxSelfSwitchValue.SetSelection( 0 )
		sizerSelfSwitch.Add( self.comboBoxSelfSwitchValue, 0, wx.ALL, 5 )
		
		sizerTab1.Add( sizerSelfSwitch, 0, wx.EXPAND, 5 )
		
		sizerTimer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonTimer = wx.RadioButton( self.panelConditions1, wx.ID_ANY, u"Timer", wx.DefaultPosition, wx.Size( 72,-1 ), wx.RB_SINGLE )
		sizerTimer.Add( self.radioButtonTimer, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlMinutes = wx.SpinCtrl( self.panelConditions1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerTimer.Add( self.spinCtrlMinutes, 0, wx.ALL, 5 )
		
		self.labelMinutes = wx.StaticText( self.panelConditions1, wx.ID_ANY, u"Min", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMinutes.Wrap( -1 )
		sizerTimer.Add( self.labelMinutes, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )
		
		self.spinCtrlSeconds = wx.SpinCtrl( self.panelConditions1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerTimer.Add( self.spinCtrlSeconds, 0, wx.ALL, 5 )
		
		self.labelSeconds = wx.StaticText( self.panelConditions1, wx.ID_ANY, u"Sec", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelSeconds.Wrap( -1 )
		sizerTimer.Add( self.labelSeconds, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )
		
		spinCtrlTimerValueChoices = [ u"or More", u"or Less" ]
		self.spinCtrlTimerValue = wx.Choice( self.panelConditions1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, spinCtrlTimerValueChoices, 0 )
		self.spinCtrlTimerValue.SetSelection( 0 )
		sizerTimer.Add( self.spinCtrlTimerValue, 1, wx.ALL, 5 )
		
		sizerTab1.Add( sizerTimer, 0, wx.EXPAND, 5 )
		
		self.panelConditions1.SetSizer( sizerTab1 )
		self.panelConditions1.Layout()
		self.noteBookConditions.AddPage( self.panelConditions1, u"1", False )
		self.panelConditions2 = wx.Panel( self.noteBookConditions, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerTab2 = wx.BoxSizer( wx.VERTICAL )
		
		sizerActor = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonActor = wx.RadioButton( self.panelConditions2, wx.ID_ANY, u"Actor", wx.DefaultPosition, wx.DefaultSize, wx.RB_USE_CHECKBOX )
		sizerActor.Add( self.radioButtonActor, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxActorsChoices = []
		self.comboBoxActors = wx.Choice( self.panelConditions2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,-1 ), comboBoxActorsChoices, 0 )
		self.comboBoxActors.SetSelection( 0 )
		sizerActor.Add( self.comboBoxActors, 0, wx.ALL, 5 )
		
		self.labelIsActor = wx.StaticText( self.panelConditions2, wx.ID_ANY, u"is", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelIsActor.Wrap( -1 )
		sizerActor.Add( self.labelIsActor, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerTab2.Add( sizerActor, 0, wx.EXPAND, 5 )
		
		sizerInParty = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDummy4 = wx.StaticText( self.panelConditions2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 32,-1 ), 0 )
		self.labelDummy4.Wrap( -1 )
		sizerInParty.Add( self.labelDummy4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.radioButtonInParty = wx.RadioButton( self.panelConditions2, wx.ID_ANY, u"In the Party", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		sizerInParty.Add( self.radioButtonInParty, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerTab2.Add( sizerInParty, 0, wx.EXPAND, 5 )
		
		sizerActorName = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDummy5 = wx.StaticText( self.panelConditions2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 32,-1 ), 0 )
		self.labelDummy5.Wrap( -1 )
		sizerActorName.Add( self.labelDummy5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.radioButtonActorName = wx.RadioButton( self.panelConditions2, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		sizerActorName.Add( self.radioButtonActorName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxActorNameChoices = []
		self.comboBoxActorName = wx.Choice( self.panelConditions2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxActorNameChoices, 0 )
		self.comboBoxActorName.SetSelection( 0 )
		sizerActorName.Add( self.comboBoxActorName, 1, wx.ALL, 5 )
		
		self.labelNameApplied = wx.StaticText( self.panelConditions2, wx.ID_ANY, u"Applied", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		self.labelNameApplied.Wrap( -1 )
		sizerActorName.Add( self.labelNameApplied, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerTab2.Add( sizerActorName, 0, wx.EXPAND, 5 )
		
		sizerActorSkill = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDummy6 = wx.StaticText( self.panelConditions2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 32,-1 ), 0 )
		self.labelDummy6.Wrap( -1 )
		sizerActorSkill.Add( self.labelDummy6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.radioButtonActorSkill = wx.RadioButton( self.panelConditions2, wx.ID_ANY, u"Skill", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		sizerActorSkill.Add( self.radioButtonActorSkill, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxActorSkillChoices = []
		self.comboBoxActorSkill = wx.Choice( self.panelConditions2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxActorSkillChoices, 0 )
		self.comboBoxActorSkill.SetSelection( 0 )
		sizerActorSkill.Add( self.comboBoxActorSkill, 1, wx.ALL, 5 )
		
		self.labelSkillLearned = wx.StaticText( self.panelConditions2, wx.ID_ANY, u"Learned", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		self.labelSkillLearned.Wrap( -1 )
		sizerActorSkill.Add( self.labelSkillLearned, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerTab2.Add( sizerActorSkill, 0, wx.EXPAND, 5 )
		
		SizerActorWeapon = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDummy7 = wx.StaticText( self.panelConditions2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 32,-1 ), 0 )
		self.labelDummy7.Wrap( -1 )
		SizerActorWeapon.Add( self.labelDummy7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.radioButtonActorWeapon = wx.RadioButton( self.panelConditions2, wx.ID_ANY, u"Weapons", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		SizerActorWeapon.Add( self.radioButtonActorWeapon, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxActorWeaponChoices = []
		self.comboBoxActorWeapon = wx.Choice( self.panelConditions2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxActorWeaponChoices, 0 )
		self.comboBoxActorWeapon.SetSelection( 0 )
		SizerActorWeapon.Add( self.comboBoxActorWeapon, 1, wx.ALL, 5 )
		
		self.labelActorEquipped1 = wx.StaticText( self.panelConditions2, wx.ID_ANY, u"Equipped", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		self.labelActorEquipped1.Wrap( -1 )
		SizerActorWeapon.Add( self.labelActorEquipped1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerTab2.Add( SizerActorWeapon, 0, wx.EXPAND, 5 )
		
		sizerActorArmor = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDummy8 = wx.StaticText( self.panelConditions2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 32,-1 ), 0 )
		self.labelDummy8.Wrap( -1 )
		sizerActorArmor.Add( self.labelDummy8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.radioButtonActorArmor = wx.RadioButton( self.panelConditions2, wx.ID_ANY, u"Armor", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		sizerActorArmor.Add( self.radioButtonActorArmor, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxActorArmorChoices = []
		self.comboBoxActorArmor = wx.Choice( self.panelConditions2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxActorArmorChoices, 0 )
		self.comboBoxActorArmor.SetSelection( 0 )
		sizerActorArmor.Add( self.comboBoxActorArmor, 1, wx.ALL, 5 )
		
		self.labelActorEquipped2 = wx.StaticText( self.panelConditions2, wx.ID_ANY, u"Equipped", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		self.labelActorEquipped2.Wrap( -1 )
		sizerActorArmor.Add( self.labelActorEquipped2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerTab2.Add( sizerActorArmor, 0, wx.EXPAND, 5 )
		
		sizerActorState = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDummy9 = wx.StaticText( self.panelConditions2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 32,-1 ), 0 )
		self.labelDummy9.Wrap( -1 )
		sizerActorState.Add( self.labelDummy9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.radioButtonActorState = wx.RadioButton( self.panelConditions2, wx.ID_ANY, u"State", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		sizerActorState.Add( self.radioButtonActorState, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxActorStateChoices = []
		self.comboBoxActorState = wx.Choice( self.panelConditions2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxActorStateChoices, 0 )
		self.comboBoxActorState.SetSelection( 0 )
		sizerActorState.Add( self.comboBoxActorState, 1, wx.ALL, 5 )
		
		self.labelStateInflicted = wx.StaticText( self.panelConditions2, wx.ID_ANY, u"Inflicted", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		self.labelStateInflicted.Wrap( -1 )
		sizerActorState.Add( self.labelStateInflicted, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerTab2.Add( sizerActorState, 0, wx.EXPAND, 5 )
		
		self.panelConditions2.SetSizer( sizerTab2 )
		self.panelConditions2.Layout()
		sizerTab2.Fit( self.panelConditions2 )
		self.noteBookConditions.AddPage( self.panelConditions2, u"2", False )
		self.panelConditions3 = wx.Panel( self.noteBookConditions, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerTab3 = wx.BoxSizer( wx.VERTICAL )
		
		sizerEnemy = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelEnemy = wx.RadioButton( self.panelConditions3, wx.ID_ANY, u"Enemy", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerEnemy.Add( self.labelEnemy, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboBoxEnemyChoices = []
		self.comboBoxEnemy = wx.Choice( self.panelConditions3, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,-1 ), comboBoxEnemyChoices, 0 )
		self.comboBoxEnemy.SetSelection( 0 )
		sizerEnemy.Add( self.comboBoxEnemy, 0, wx.ALL, 5 )
		
		self.labelIsEnemy = wx.StaticText( self.panelConditions3, wx.ID_ANY, u"is", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelIsEnemy.Wrap( -1 )
		sizerEnemy.Add( self.labelIsEnemy, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerTab3.Add( sizerEnemy, 0, wx.EXPAND, 5 )
		
		sizerEnemyAppeared = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDummy10 = wx.StaticText( self.panelConditions3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		self.labelDummy10.Wrap( -1 )
		sizerEnemyAppeared.Add( self.labelDummy10, 0, wx.ALL, 5 )
		
		self.radioButtonEnemyAppeared = wx.RadioButton( self.panelConditions3, wx.ID_ANY, u"Appeared", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		sizerEnemyAppeared.Add( self.radioButtonEnemyAppeared, 0, wx.ALL, 5 )
		
		sizerTab3.Add( sizerEnemyAppeared, 0, wx.EXPAND, 5 )
		
		sizerEnemyState = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDummy11 = wx.StaticText( self.panelConditions3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		self.labelDummy11.Wrap( -1 )
		sizerEnemyState.Add( self.labelDummy11, 0, wx.ALL, 5 )
		
		self.radioButtonEnemyState = wx.RadioButton( self.panelConditions3, wx.ID_ANY, u"State", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerEnemyState.Add( self.radioButtonEnemyState, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxEnemyStateChoices = []
		self.comboBoxEnemyState = wx.Choice( self.panelConditions3, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,-1 ), comboBoxEnemyStateChoices, 0 )
		self.comboBoxEnemyState.SetSelection( 0 )
		sizerEnemyState.Add( self.comboBoxEnemyState, 1, wx.ALL, 5 )
		
		self.labelEnemyStateInflicted = wx.StaticText( self.panelConditions3, wx.ID_ANY, u"Inflicted", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelEnemyStateInflicted.Wrap( -1 )
		sizerEnemyState.Add( self.labelEnemyStateInflicted, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		sizerTab3.Add( sizerEnemyState, 0, wx.EXPAND, 5 )
		
		sizerCharacter = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelCharacter = wx.RadioButton( self.panelConditions3, wx.ID_ANY, u"Character", wx.DefaultPosition, wx.Size( 72,-1 ), wx.RB_GROUP|wx.RB_SINGLE )
		sizerCharacter.Add( self.labelCharacter, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxCharacterChoices = []
		self.comboBoxCharacter = wx.Choice( self.panelConditions3, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,-1 ), comboBoxCharacterChoices, 0 )
		self.comboBoxCharacter.SetSelection( -1 )
		sizerCharacter.Add( self.comboBoxCharacter, 0, wx.ALL, 5 )
		
		self.labelIsCharacter = wx.StaticText( self.panelConditions3, wx.ID_ANY, u"is", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelIsCharacter.Wrap( -1 )
		sizerCharacter.Add( self.labelIsCharacter, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerTab3.Add( sizerCharacter, 0, wx.EXPAND, 5 )
		
		sizerCharacterFacing = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDummy12 = wx.StaticText( self.panelConditions3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		self.labelDummy12.Wrap( -1 )
		sizerCharacterFacing.Add( self.labelDummy12, 0, wx.ALL, 5 )
		
		self.labelFacing = wx.StaticText( self.panelConditions3, wx.ID_ANY, u"Facing", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelFacing.Wrap( -1 )
		sizerCharacterFacing.Add( self.labelFacing, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxFacingChoices = [ u"LEFT", u"RIGHT", u"UP", u"DOWN" ]
		self.comboBoxFacing = wx.Choice( self.panelConditions3, wx.ID_ANY, wx.DefaultPosition, wx.Size( 64,-1 ), comboBoxFacingChoices, 0 )
		self.comboBoxFacing.SetSelection( 0 )
		sizerCharacterFacing.Add( self.comboBoxFacing, 0, wx.ALL, 5 )
		
		sizerTab3.Add( sizerCharacterFacing, 0, wx.EXPAND, 5 )
		
		self.panelConditions3.SetSizer( sizerTab3 )
		self.panelConditions3.Layout()
		sizerTab3.Fit( self.panelConditions3 )
		self.noteBookConditions.AddPage( self.panelConditions3, u"3", False )
		self.panelConditions4 = wx.Panel( self.noteBookConditions, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerTab4 = wx.BoxSizer( wx.VERTICAL )
		
		sizerInventoryGold = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonGold = wx.RadioButton( self.panelConditions4, wx.ID_ANY, u"Gold", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerInventoryGold.Add( self.radioButtonGold, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlGold = wx.SpinCtrl( self.panelConditions4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerInventoryGold.Add( self.spinCtrlGold, 0, wx.ALL, 5 )
		
		comboBoxGoldModifierChoices = [ u"or More", u"or Less" ]
		self.comboBoxGoldModifier = wx.Choice( self.panelConditions4, wx.ID_ANY, wx.DefaultPosition, wx.Size( 72,-1 ), comboBoxGoldModifierChoices, 0 )
		self.comboBoxGoldModifier.SetSelection( 0 )
		sizerInventoryGold.Add( self.comboBoxGoldModifier, 0, wx.ALL, 5 )
		
		sizerTab4.Add( sizerInventoryGold, 0, wx.EXPAND, 5 )
		
		sizerInventoryItem = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonItem = wx.RadioButton( self.panelConditions4, wx.ID_ANY, u"Item", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerInventoryItem.Add( self.radioButtonItem, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxInventoryItemChoices = []
		self.comboBoxInventoryItem = wx.Choice( self.panelConditions4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxInventoryItemChoices, 0 )
		self.comboBoxInventoryItem.SetSelection( 0 )
		sizerInventoryItem.Add( self.comboBoxInventoryItem, 1, wx.ALL, 5 )
		
		self.labelInventoryItem = wx.StaticText( self.panelConditions4, wx.ID_ANY, u"In Inventory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelInventoryItem.Wrap( -1 )
		sizerInventoryItem.Add( self.labelInventoryItem, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerTab4.Add( sizerInventoryItem, 0, wx.EXPAND, 5 )
		
		sizerInventoryWeapon = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonWeapon = wx.RadioButton( self.panelConditions4, wx.ID_ANY, u"Weapon", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerInventoryWeapon.Add( self.radioButtonWeapon, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxInventoryWeaponChoices = []
		self.comboBoxInventoryWeapon = wx.Choice( self.panelConditions4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxInventoryWeaponChoices, 0 )
		self.comboBoxInventoryWeapon.SetSelection( 0 )
		sizerInventoryWeapon.Add( self.comboBoxInventoryWeapon, 1, wx.ALL, 5 )
		
		self.labelInventoryWeapon = wx.StaticText( self.panelConditions4, wx.ID_ANY, u"In Inventory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelInventoryWeapon.Wrap( -1 )
		sizerInventoryWeapon.Add( self.labelInventoryWeapon, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerTab4.Add( sizerInventoryWeapon, 0, wx.EXPAND, 5 )
		
		sizerInventoryArmor = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonArmor = wx.RadioButton( self.panelConditions4, wx.ID_ANY, u"Armor", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerInventoryArmor.Add( self.radioButtonArmor, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxInventoryArmorChoices = []
		self.comboBoxInventoryArmor = wx.Choice( self.panelConditions4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxInventoryArmorChoices, 0 )
		self.comboBoxInventoryArmor.SetSelection( 0 )
		sizerInventoryArmor.Add( self.comboBoxInventoryArmor, 1, wx.ALL, 5 )
		
		self.labelInventoryArmor = wx.StaticText( self.panelConditions4, wx.ID_ANY, u"In Inventory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelInventoryArmor.Wrap( -1 )
		sizerInventoryArmor.Add( self.labelInventoryArmor, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerTab4.Add( sizerInventoryArmor, 0, wx.EXPAND, 5 )
		
		sizerButtonPress = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonButton = wx.RadioButton( self.panelConditions4, wx.ID_ANY, u"Button", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerButtonPress.Add( self.radioButtonButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxButtonPressChoices = []
		self.comboBoxButtonPress = wx.Choice( self.panelConditions4, wx.ID_ANY, wx.DefaultPosition, wx.Size( 72,-1 ), comboBoxButtonPressChoices, 0 )
		self.comboBoxButtonPress.SetSelection( -1 )
		sizerButtonPress.Add( self.comboBoxButtonPress, 0, wx.ALL, 5 )
		
		self.labelButtonPressed = wx.StaticText( self.panelConditions4, wx.ID_ANY, u"Is Being Pressed", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelButtonPressed.Wrap( -1 )
		sizerButtonPress.Add( self.labelButtonPressed, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerTab4.Add( sizerButtonPress, 0, wx.EXPAND, 5 )
		
		sizerScriptCondition = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonScript = wx.RadioButton( self.panelConditions4, wx.ID_ANY, u"Script", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerScriptCondition.Add( self.radioButtonScript, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.textCtrlScriptCondition = wx.TextCtrl( self.panelConditions4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerScriptCondition.Add( self.textCtrlScriptCondition, 1, wx.ALL, 5 )
		
		sizerTab4.Add( sizerScriptCondition, 0, wx.EXPAND, 5 )
		
		self.panelConditions4.SetSizer( sizerTab4 )
		self.panelConditions4.Layout()
		sizerTab4.Fit( self.panelConditions4 )
		self.noteBookConditions.AddPage( self.panelConditions4, u"4", True )
		
		MainSizer.Add( self.noteBookConditions, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.labelElseCondition = wx.CheckBox( self, wx.ID_ANY, u"Set handling when conditions do not apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelElseCondition.SetValue(True) 
		MainSizer.Add( self.labelElseCondition, 0, wx.ALL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.radioButtonActor.Bind( wx.EVT_RADIOBUTTON, self.radioButtonActor_CheckChanged )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def radioButtonActor_CheckChanged( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class CallCommonEvent_Dialog
###########################################################################

class CallCommonEvent_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Call Common Event", pos = wx.DefaultPosition, size = wx.Size( 290,94 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerCommonEvent = wx.BoxSizer( wx.VERTICAL )
		
		self.labelCommonEvent = wx.StaticText( self, wx.ID_ANY, u"Common Event:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelCommonEvent.Wrap( -1 )
		sizerCommonEvent.Add( self.labelCommonEvent, 0, wx.ALL, 5 )
		
		comboBoxCommonEventChoices = []
		self.comboBoxCommonEvent = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxCommonEventChoices, 0 )
		self.comboBoxCommonEvent.SetSelection( 0 )
		sizerCommonEvent.Add( self.comboBoxCommonEvent, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		MainSizer.Add( sizerCommonEvent, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class Label_Dialog
###########################################################################

class Label_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 290,94 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerLabel = wx.BoxSizer( wx.VERTICAL )
		
		self.labelLabel = wx.StaticText( self, wx.ID_ANY, u"Label Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelLabel.Wrap( -1 )
		sizerLabel.Add( self.labelLabel, 0, wx.ALL, 5 )
		
		self.textCtrlLabel = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerLabel.Add( self.textCtrlLabel, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerLabel, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ControlSwitches_Dialog
###########################################################################

class ControlSwitches_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Control Switches", pos = wx.DefaultPosition, size = wx.Size( 310,213 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		sizerSwitch = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Switch" ), wx.VERTICAL )
		
		sizerSingleSwitch = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonSingleSwitch = wx.RadioButton( self, wx.ID_ANY, u"Single", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		sizerSingleSwitch.Add( self.radioButtonSingleSwitch, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxSingleSwitchChoices = []
		self.comboBoxSingleSwitch = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxSingleSwitchChoices, 0 )
		self.comboBoxSingleSwitch.SetSelection( 0 )
		sizerSingleSwitch.Add( self.comboBoxSingleSwitch, 1, wx.ALL, 5 )
		
		sizerSwitch.Add( sizerSingleSwitch, 0, wx.EXPAND, 5 )
		
		sizerBatchSwitch = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonBatchSwitch = wx.RadioButton( self, wx.ID_ANY, u"Batch", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		sizerBatchSwitch.Add( self.radioButtonBatchSwitch, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlBatchStart = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerBatchSwitch.Add( self.spinCtrlBatchStart, 1, wx.ALL, 5 )
		
		self.labelTilde = wx.StaticText( self, wx.ID_ANY, u"~", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTilde.Wrap( -1 )
		sizerBatchSwitch.Add( self.labelTilde, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlBatchEnd = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerBatchSwitch.Add( self.spinCtrlBatchEnd, 1, wx.ALL, 5 )
		
		sizerSwitch.Add( sizerBatchSwitch, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerSwitch, 1, wx.EXPAND|wx.ALL, 5 )
		
		radioBoxOperationChoices = [ u"ON", u"OFF" ]
		self.radioBoxOperation = wx.RadioBox( self, wx.ID_ANY, u"Operation", wx.DefaultPosition, wx.DefaultSize, radioBoxOperationChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioBoxOperation.SetSelection( 0 )
		MainSizer.Add( self.radioBoxOperation, 0, wx.ALL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.spinCtrlBatchStart.Bind( wx.EVT_SPINCTRL, self.spinCtrlBatchStart_ValueChanged )
		self.spinCtrlBatchEnd.Bind( wx.EVT_SPINCTRL, self.spinCtrlBatchEnd_ValueChanged )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def spinCtrlBatchStart_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlBatchEnd_ValueChanged( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ControlVariables_Dialog
###########################################################################

class ControlVariables_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Control Variables", pos = wx.DefaultPosition, size = wx.Size( 359,490 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		sizerVariableSelect = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Variable" ), wx.VERTICAL )
		
		sizerSingleSwitch = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonSingleVariable = wx.RadioButton( self, wx.ID_ANY, u"Single", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		sizerSingleSwitch.Add( self.radioButtonSingleVariable, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxSingleVariableChoices = []
		self.comboBoxSingleVariable = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxSingleVariableChoices, 0 )
		self.comboBoxSingleVariable.SetSelection( 0 )
		sizerSingleSwitch.Add( self.comboBoxSingleVariable, 1, wx.ALL, 5 )
		
		sizerVariableSelect.Add( sizerSingleSwitch, 0, wx.EXPAND, 5 )
		
		sizerBatchVariable = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonBatchVariable = wx.RadioButton( self, wx.ID_ANY, u"Batch", wx.DefaultPosition, wx.Size( 64,-1 ), 0 )
		sizerBatchVariable.Add( self.radioButtonBatchVariable, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlBatchStart = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerBatchVariable.Add( self.spinCtrlBatchStart, 1, wx.ALL, 5 )
		
		self.labelTilde1 = wx.StaticText( self, wx.ID_ANY, u"~", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTilde1.Wrap( -1 )
		sizerBatchVariable.Add( self.labelTilde1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlBatchEnd = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerBatchVariable.Add( self.spinCtrlBatchEnd, 1, wx.ALL, 5 )
		
		sizerVariableSelect.Add( sizerBatchVariable, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerVariableSelect, 0, wx.ALL|wx.EXPAND, 5 )
		
		radioBoxOperationChoices = [ u"Set", u"Add", u"Sub", u"Mul", u"Div", u"Mod" ]
		self.radioBoxOperation = wx.RadioBox( self, wx.ID_ANY, u"Operation", wx.DefaultPosition, wx.DefaultSize, radioBoxOperationChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioBoxOperation.SetSelection( 0 )
		MainSizer.Add( self.radioBoxOperation, 0, wx.ALL|wx.EXPAND, 5 )
		
		sizerOperand = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Operand" ), wx.VERTICAL )
		
		sizerConstant = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonConstant = wx.RadioButton( self, wx.ID_ANY, u"Constant", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerConstant.Add( self.radioButtonConstant, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlConstant = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 96,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerConstant.Add( self.spinCtrlConstant, 0, wx.ALL, 5 )
		
		sizerOperand.Add( sizerConstant, 1, wx.EXPAND, 5 )
		
		sizerVariable = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonVariable = wx.RadioButton( self, wx.ID_ANY, u"Variable", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerVariable.Add( self.radioButtonVariable, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxVariableChoices = []
		self.comboBoxVariable = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,-1 ), comboBoxVariableChoices, 0 )
		self.comboBoxVariable.SetSelection( -1 )
		sizerVariable.Add( self.comboBoxVariable, 1, wx.ALL, 5 )
		
		sizerOperand.Add( sizerVariable, 1, wx.EXPAND, 5 )
		
		sizerRandom = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonRandom = wx.RadioButton( self, wx.ID_ANY, u"Random", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerRandom.Add( self.radioButtonRandom, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlRandomStart = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerRandom.Add( self.spinCtrlRandomStart, 1, wx.ALL, 5 )
		
		self.labelTilde2 = wx.StaticText( self, wx.ID_ANY, u"~", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTilde2.Wrap( -1 )
		sizerRandom.Add( self.labelTilde2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlRandomEnd = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerRandom.Add( self.spinCtrlRandomEnd, 1, wx.ALL, 5 )
		
		sizerOperand.Add( sizerRandom, 1, wx.EXPAND, 5 )
		
		sizerItem = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonItem = wx.RadioButton( self, wx.ID_ANY, u"Item", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerItem.Add( self.radioButtonItem, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxItemChoices = []
		self.comboBoxItem = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxItemChoices, 0 )
		self.comboBoxItem.SetSelection( 0 )
		sizerItem.Add( self.comboBoxItem, 1, wx.ALL, 5 )
		
		self.labelItemInInventory = wx.StaticText( self, wx.ID_ANY, u"In Inventory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelItemInInventory.Wrap( -1 )
		sizerItem.Add( self.labelItemInInventory, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerOperand.Add( sizerItem, 1, wx.EXPAND, 5 )
		
		sizerActor = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonActor = wx.RadioButton( self, wx.ID_ANY, u"Actor", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerActor.Add( self.radioButtonActor, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxActorChoices = []
		self.comboBoxActor = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxActorChoices, 0 )
		self.comboBoxActor.SetSelection( 0 )
		sizerActor.Add( self.comboBoxActor, 0, wx.ALL, 5 )
		
		self.labelPossessive1 = wx.StaticText( self, wx.ID_ANY, u"'s", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPossessive1.Wrap( -1 )
		sizerActor.Add( self.labelPossessive1, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		comboBoxActorParametersChoices = [ u"Level", u"EXP", u"HP", u"SP", u"MaxHP", u"MaxSP", u"STR", u"DEX", u"AGI", u"INT", u"PDEF", u"MDEF" ]
		self.comboBoxActorParameters = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxActorParametersChoices, 0 )
		self.comboBoxActorParameters.SetSelection( 0 )
		sizerActor.Add( self.comboBoxActorParameters, 1, wx.ALL, 5 )
		
		sizerOperand.Add( sizerActor, 1, wx.EXPAND, 5 )
		
		sizerEnemy = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonEnemy = wx.RadioButton( self, wx.ID_ANY, u"Enemy", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerEnemy.Add( self.radioButtonEnemy, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxEnemyChoices = []
		self.comboBoxEnemy = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxEnemyChoices, 0 )
		self.comboBoxEnemy.SetSelection( 0 )
		sizerEnemy.Add( self.comboBoxEnemy, 0, wx.ALL, 5 )
		
		self.labelPossessive2 = wx.StaticText( self, wx.ID_ANY, u"'s", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPossessive2.Wrap( -1 )
		sizerEnemy.Add( self.labelPossessive2, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		comboBoxEnemyParametersChoices = [ u"HP", u"SP", u"MaxHP", u"MaxSP", u"STR", u"DEX", u"AGI", u"INT", u"PDEF", u"MDEF" ]
		self.comboBoxEnemyParameters = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxEnemyParametersChoices, 0 )
		self.comboBoxEnemyParameters.SetSelection( 0 )
		sizerEnemy.Add( self.comboBoxEnemyParameters, 1, wx.ALL, 5 )
		
		sizerOperand.Add( sizerEnemy, 1, wx.EXPAND, 5 )
		
		sizerCharacter = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonCharacter = wx.RadioButton( self, wx.ID_ANY, u"Character", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerCharacter.Add( self.radioButtonCharacter, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxCharacterChoices = []
		self.comboBoxCharacter = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxCharacterChoices, 0 )
		self.comboBoxCharacter.SetSelection( 0 )
		sizerCharacter.Add( self.comboBoxCharacter, 0, wx.ALL, 5 )
		
		self.labelPossessive3 = wx.StaticText( self, wx.ID_ANY, u"'s", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPossessive3.Wrap( -1 )
		sizerCharacter.Add( self.labelPossessive3, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		comboBoxCharacterParametersChoices = [ u"Map X", u"Map Y", u"Direction", u"Screen X", u"Screen Y", u"Terrain Tag" ]
		self.comboBoxCharacterParameters = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxCharacterParametersChoices, 0 )
		self.comboBoxCharacterParameters.SetSelection( 5 )
		sizerCharacter.Add( self.comboBoxCharacterParameters, 1, wx.ALL, 5 )
		
		sizerOperand.Add( sizerCharacter, 1, wx.EXPAND, 5 )
		
		sizerOther = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonOther = wx.RadioButton( self, wx.ID_ANY, u"Other", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerOther.Add( self.radioButtonOther, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxOtherChoices = [ u"Map ID", u"Party Members", u"Gold", u"Steps", u"Play Time", u"Timer", u"Save Count" ]
		self.comboBoxOther = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxOtherChoices, 0 )
		self.comboBoxOther.SetSelection( 0 )
		sizerOther.Add( self.comboBoxOther, 0, wx.ALL, 5 )
		
		sizerOperand.Add( sizerOther, 1, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerOperand, 0, wx.EXPAND|wx.ALL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.spinCtrlBatchStart.Bind( wx.EVT_SPINCTRL, self.spinCtrlBatchStart_ValueChanged )
		self.spinCtrlBatchEnd.Bind( wx.EVT_SPINCTRL, self.spinCtrlBatchEnd_ValueChanged )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def spinCtrlBatchStart_ValueChanged( self, event ):
		event.Skip()
	
	def spinCtrlBatchEnd_ValueChanged( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ControlSelfSwitches_Dialog
###########################################################################

class ControlSelfSwitches_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Control Self Switch", pos = wx.DefaultPosition, size = wx.Size( 208,139 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerSelfSwitch = wx.BoxSizer( wx.VERTICAL )
		
		self.labelSelfSwicth = wx.StaticText( self, wx.ID_ANY, u"Self Switch:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelSelfSwicth.Wrap( -1 )
		sizerSelfSwitch.Add( self.labelSelfSwicth, 0, wx.ALL, 5 )
		
		comboBoxLettersChoices = [ u"A", u"B", u"C", u"D", u"E", u"F", u"G", u"H", u"I", u"J", u"K", u"L", u"M", u"N", u"O", u"P", u"Q", u"R", u"S", u"T", u"U", u"V", u"W", u"X", u"Y", u"Z" ]
		self.comboBoxLetters = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 64,-1 ), comboBoxLettersChoices, 0 )
		self.comboBoxLetters.SetSelection( 0 )
		sizerSelfSwitch.Add( self.comboBoxLetters, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		radioBoxOperationChoices = [ u"ON", u"OFF" ]
		self.radioBoxOperation = wx.RadioBox( self, wx.ID_ANY, u"Operation", wx.DefaultPosition, wx.DefaultSize, radioBoxOperationChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioBoxOperation.SetSelection( 0 )
		sizerSelfSwitch.Add( self.radioBoxOperation, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerSelfSwitch, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ControlTimer_Dialog
###########################################################################

class ControlTimer_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Control Timer", pos = wx.DefaultPosition, size = wx.Size( 296,116 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerControls = wx.BoxSizer( wx.VERTICAL )
		
		radioBoxOperationChoices = [ u"Start", u"Stop" ]
		self.radioBoxOperation = wx.RadioBox( self, wx.ID_ANY, u"Operation", wx.DefaultPosition, wx.DefaultSize, radioBoxOperationChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioBoxOperation.SetSelection( 0 )
		sizerControls.Add( self.radioBoxOperation, 0, wx.ALL, 5 )
		
		sizerTimer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.spinCtrlTimerMin = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerTimer.Add( self.spinCtrlTimerMin, 1, wx.ALL, 5 )
		
		self.labelMinutes = wx.StaticText( self, wx.ID_ANY, u"Min", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMinutes.Wrap( -1 )
		sizerTimer.Add( self.labelMinutes, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.spinCtrlTimerSec = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerTimer.Add( self.spinCtrlTimerSec, 1, wx.ALL, 5 )
		
		self.labelSeconds = wx.StaticText( self, wx.ID_ANY, u"Sec", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelSeconds.Wrap( -1 )
		sizerTimer.Add( self.labelSeconds, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		sizerControls.Add( sizerTimer, 1, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerControls, 1, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ChangelGold_Dialog
###########################################################################

class ChangelGold_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Change Gold", pos = wx.DefaultPosition, size = wx.Size( 287,211 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		radioBoxOperationChoices = [ u"Increase", u"Decrease" ]
		self.radioBoxOperation = wx.RadioBox( self, wx.ID_ANY, u"Operation", wx.DefaultPosition, wx.DefaultSize, radioBoxOperationChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioBoxOperation.SetSelection( 0 )
		MainSizer.Add( self.radioBoxOperation, 0, wx.ALL, 5 )
		
		sizerOperand = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Operand" ), wx.VERTICAL )
		
		sizerConstant = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonConstant = wx.RadioButton( self, wx.ID_ANY, u"Constant", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerConstant.Add( self.radioButtonConstant, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlConstant = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerConstant.Add( self.spinCtrlConstant, 0, wx.ALL, 5 )
		
		sizerOperand.Add( sizerConstant, 0, wx.EXPAND, 5 )
		
		sizerVariable = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonVariable = wx.RadioButton( self, wx.ID_ANY, u"Variable", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerVariable.Add( self.radioButtonVariable, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxVariableChoices = []
		self.comboBoxVariable = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxVariableChoices, 0 )
		self.comboBoxVariable.SetSelection( 0 )
		sizerVariable.Add( self.comboBoxVariable, 1, wx.ALL, 5 )
		
		sizerOperand.Add( sizerVariable, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerOperand, 1, wx.EXPAND|wx.ALL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ChangelPartyEquipment_Dialog
###########################################################################

class ChangelPartyEquipment_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Change (Equipment Type)", pos = wx.DefaultPosition, size = wx.Size( 287,261 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.labelEquipmentType = wx.StaticText( self, wx.ID_ANY, u"(Equipment Type):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelEquipmentType.Wrap( -1 )
		MainSizer.Add( self.labelEquipmentType, 0, wx.ALL, 5 )
		
		comboBoxEquipmentChoices = []
		self.comboBoxEquipment = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxEquipmentChoices, 0 )
		self.comboBoxEquipment.SetSelection( 0 )
		MainSizer.Add( self.comboBoxEquipment, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		radioBoxOperationChoices = [ u"Increase", u"Decrease" ]
		self.radioBoxOperation = wx.RadioBox( self, wx.ID_ANY, u"Operation", wx.DefaultPosition, wx.DefaultSize, radioBoxOperationChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioBoxOperation.SetSelection( 0 )
		MainSizer.Add( self.radioBoxOperation, 0, wx.ALL, 5 )
		
		sizerOperand = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Operand" ), wx.VERTICAL )
		
		sizerConstant = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonConstant = wx.RadioButton( self, wx.ID_ANY, u"Constant", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerConstant.Add( self.radioButtonConstant, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlConstant = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerConstant.Add( self.spinCtrlConstant, 0, wx.ALL, 5 )
		
		sizerOperand.Add( sizerConstant, 0, wx.EXPAND, 5 )
		
		sizerVariable = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonVariable = wx.RadioButton( self, wx.ID_ANY, u"Variable", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerVariable.Add( self.radioButtonVariable, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxVariableChoices = []
		self.comboBoxVariable = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxVariableChoices, 0 )
		self.comboBoxVariable.SetSelection( 0 )
		sizerVariable.Add( self.comboBoxVariable, 1, wx.ALL, 5 )
		
		sizerOperand.Add( sizerVariable, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerOperand, 1, wx.EXPAND|wx.ALL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ChangePartyMember_Dialog
###########################################################################

class ChangePartyMember_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Change Party Member", pos = wx.DefaultPosition, size = wx.Size( 283,157 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerActor = wx.BoxSizer( wx.VERTICAL )
		
		self.labelActor = wx.StaticText( self, wx.ID_ANY, u"Actor:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelActor.Wrap( -1 )
		sizerActor.Add( self.labelActor, 0, wx.ALL, 5 )
		
		comboBoxActorChoices = []
		self.comboBoxActor = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxActorChoices, 0 )
		self.comboBoxActor.SetSelection( 0 )
		sizerActor.Add( self.comboBoxActor, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		radioBoxOperationChoices = [ u"Add", u"Remove" ]
		self.radioBoxOperation = wx.RadioBox( self, wx.ID_ANY, u"Operation", wx.DefaultPosition, wx.DefaultSize, radioBoxOperationChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioBoxOperation.SetSelection( 0 )
		sizerActor.Add( self.radioBoxOperation, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.checkBoxInitialize = wx.CheckBox( self, wx.ID_ANY, u"Initialize", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.checkBoxInitialize.SetValue(True) 
		sizerActor.Add( self.checkBoxInitialize, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerActor, 1, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ChangeAccess_Dialog
###########################################################################

class ChangeAccess_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Change (Menu/Save/Encounter)", pos = wx.DefaultPosition, size = wx.Size( 241,93 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		radioBoxOperationChoices = [ u"Enable", u"Disable" ]
		self.radioBoxOperation = wx.RadioBox( self, wx.ID_ANY, u"Operation", wx.DefaultPosition, wx.DefaultSize, radioBoxOperationChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioBoxOperation.SetSelection( 0 )
		MainSizer.Add( self.radioBoxOperation, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class TransferPlayer_Dialog
###########################################################################

class TransferPlayer_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Transfer Player", pos = wx.DefaultPosition, size = wx.Size( 251,280 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.labelDirect = wx.RadioButton( self, wx.ID_ANY, u"Direct Appointment", wx.DefaultPosition, wx.DefaultSize, 0 )
		MainSizer.Add( self.labelDirect, 0, wx.ALL, 5 )
		
		bSizer510 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDummy1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 16,-1 ), 0 )
		self.labelDummy1.Wrap( -1 )
		bSizer510.Add( self.labelDummy1, 0, wx.ALL, 5 )
		
		comboBoxDirectAppointmentChoices = []
		self.comboBoxDirectAppointment = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxDirectAppointmentChoices, 0 )
		bSizer510.Add( self.comboBoxDirectAppointment, 1, wx.ALL, 5 )
		
		MainSizer.Add( bSizer510, 0, wx.EXPAND, 5 )
		
		self.comboBoxVaribleAppointment = wx.RadioButton( self, wx.ID_ANY, u"Appoint with Variables", wx.DefaultPosition, wx.DefaultSize, 0 )
		MainSizer.Add( self.comboBoxVaribleAppointment, 0, wx.ALL, 5 )
		
		bSizer511 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDummy2 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 16,-1 ), 0 )
		self.labelDummy2.Wrap( -1 )
		bSizer511.Add( self.labelDummy2, 0, wx.ALL, 5 )
		
		self.labelMapID = wx.StaticText( self, wx.ID_ANY, u"Map ID:", wx.DefaultPosition, wx.Size( 48,-1 ), 0 )
		self.labelMapID.Wrap( -1 )
		bSizer511.Add( self.labelMapID, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox50Choices = []
		self.m_comboBox50 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox50Choices, 0 )
		bSizer511.Add( self.m_comboBox50, 1, wx.ALL, 5 )
		
		MainSizer.Add( bSizer511, 0, wx.EXPAND, 5 )
		
		bSizer5111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDummy3 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 16,-1 ), 0 )
		self.labelDummy3.Wrap( -1 )
		bSizer5111.Add( self.labelDummy3, 0, wx.ALL, 5 )
		
		self.labelMapX = wx.StaticText( self, wx.ID_ANY, u"Map X:", wx.DefaultPosition, wx.Size( 48,-1 ), 0 )
		self.labelMapX.Wrap( -1 )
		bSizer5111.Add( self.labelMapX, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox501Choices = []
		self.m_comboBox501 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox501Choices, 0 )
		bSizer5111.Add( self.m_comboBox501, 1, wx.ALL, 5 )
		
		MainSizer.Add( bSizer5111, 0, wx.EXPAND, 5 )
		
		bSizer5112 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDummy4 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 16,-1 ), 0 )
		self.labelDummy4.Wrap( -1 )
		bSizer5112.Add( self.labelDummy4, 0, wx.ALL, 5 )
		
		self.labelMapY = wx.StaticText( self, wx.ID_ANY, u"Map Y:", wx.DefaultPosition, wx.Size( 48,-1 ), 0 )
		self.labelMapY.Wrap( -1 )
		bSizer5112.Add( self.labelMapY, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox502Choices = []
		self.m_comboBox502 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox502Choices, 0 )
		bSizer5112.Add( self.m_comboBox502, 1, wx.ALL, 5 )
		
		MainSizer.Add( bSizer5112, 0, wx.EXPAND, 5 )
		
		bSizer519 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDirection = wx.StaticText( self, wx.ID_ANY, u"Direction:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelDirection.Wrap( -1 )
		bSizer519.Add( self.labelDirection, 1, wx.ALL, 5 )
		
		self.labelFading = wx.StaticText( self, wx.ID_ANY, u"Fading:", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		self.labelFading.Wrap( -1 )
		bSizer519.Add( self.labelFading, 0, wx.ALL, 5 )
		
		MainSizer.Add( bSizer519, 0, wx.EXPAND, 5 )
		
		bSizer520 = wx.BoxSizer( wx.HORIZONTAL )
		
		comboBoxDirectionChoices = [ u"Retain", u"Left", u"Right", u"Up", u"Down" ]
		self.comboBoxDirection = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxDirectionChoices, 0 )
		self.comboBoxDirection.SetSelection( 0 )
		bSizer520.Add( self.comboBoxDirection, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		comboBoxFadingChoices = [ u"Yes", u"No" ]
		self.comboBoxFading = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 72,-1 ), comboBoxFadingChoices, 0 )
		self.comboBoxFading.SetSelection( 0 )
		bSizer520.Add( self.comboBoxFading, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( bSizer520, 0, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.comboBoxDirectAppointment.Bind( wx.EVT_LEFT_DOWN, self.comboBoxDirectAppointment_Clicked )
		self.comboBoxVaribleAppointment.Bind( wx.EVT_LEFT_DOWN, self.comboBoxVaribleAppointment_Clicked )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def comboBoxDirectAppointment_Clicked( self, event ):
		event.Skip()
	
	def comboBoxVaribleAppointment_Clicked( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class TransferTilemap_Dialog
###########################################################################

class TransferTilemap_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 241,159 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class SetEventLocation_Dialog
###########################################################################

class SetEventLocation_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 241,159 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class EventLocationTilemap_Dialog
###########################################################################

class EventLocationTilemap_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 241,159 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ScrollMap_Dialog
###########################################################################

class ScrollMap_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 241,159 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ChangeMapSettings_Dialog
###########################################################################

class ChangeMapSettings_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 241,159 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ChangeTone_Dialog
###########################################################################

class ChangeTone_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 241,159 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ChangeOpacity_Dialog
###########################################################################

class ChangeOpacity_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 241,159 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ShowAnimation_Dialog
###########################################################################

class ShowAnimation_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 241,159 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class TransparentFlag_Dialog
###########################################################################

class TransparentFlag_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 241,159 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MoveRoute_Dialog
###########################################################################

class MoveRoute_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 241,159 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class Jump_Dialog
###########################################################################

class Jump_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 241,159 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ChangeSpeed_Dialog
###########################################################################

class ChangeSpeed_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 241,159 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ChangeBlending_Dialog
###########################################################################

class ChangeBlending_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 241,159 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ScreenShake_Dialog
###########################################################################

class ScreenShake_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Screen Shake", pos = wx.DefaultPosition, size = wx.Size( 338,179 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		sizerPower = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelPower = wx.StaticText( self, wx.ID_ANY, u"Power:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPower.Wrap( -1 )
		sizerPower.Add( self.labelPower, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.sliderPower = wx.Slider( self, wx.ID_ANY, 5, 0, 10, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL )
		sizerPower.Add( self.sliderPower, 1, wx.ALL, 5 )
		
		self.spinCtrlPower = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 5 )
		sizerPower.Add( self.spinCtrlPower, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		MainSizer.Add( sizerPower, 0, wx.EXPAND, 5 )
		
		sizerSpeed = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelSpeed = wx.StaticText( self, wx.ID_ANY, u"Speed:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelSpeed.Wrap( -1 )
		sizerSpeed.Add( self.labelSpeed, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.sliderSpeed = wx.Slider( self, wx.ID_ANY, 5, 0, 10, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL )
		sizerSpeed.Add( self.sliderSpeed, 1, wx.ALL, 5 )
		
		self.spinCtrlSpeed = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 5 )
		sizerSpeed.Add( self.spinCtrlSpeed, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		MainSizer.Add( sizerSpeed, 0, wx.EXPAND, 5 )
		
		sizerDuration = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelTime = wx.StaticText( self, wx.ID_ANY, u"Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTime.Wrap( -1 )
		sizerDuration.Add( self.labelTime, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlFrames = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 2000, 200 )
		sizerDuration.Add( self.spinCtrlFrames, 0, wx.ALL, 5 )
		
		self.labelFrames = wx.StaticText( self, wx.ID_ANY, u"Frames", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelFrames.Wrap( -1 )
		sizerDuration.Add( self.labelFrames, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		MainSizer.Add( sizerDuration, 0, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.sliderPower.Bind( wx.EVT_SCROLL, self.sliderPower_ScrollChanged )
		self.spinCtrlPower.Bind( wx.EVT_SPINCTRL, self.spinCtrlPower_ValueChanged )
		self.sliderSpeed.Bind( wx.EVT_SCROLL, self.sliderSpeed_ScrollChanged )
		self.spinCtrlSpeed.Bind( wx.EVT_SPINCTRL, self.spinCtrlSpeed_ValueChanged )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def sliderPower_ScrollChanged( self, event ):
		event.Skip()
	
	def spinCtrlPower_ValueChanged( self, event ):
		event.Skip()
	
	def sliderSpeed_ScrollChanged( self, event ):
		event.Skip()
	
	def spinCtrlSpeed_ValueChanged( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ShowPicture_Dialog
###########################################################################

class ShowPicture_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Show Picture", pos = wx.DefaultPosition, size = wx.Size( 288,418 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		sizerPicture = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerNumber = wx.BoxSizer( wx.VERTICAL )
		
		self.labelNumber = wx.StaticText( self, wx.ID_ANY, u"Number:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelNumber.Wrap( -1 )
		sizerNumber.Add( self.labelNumber, 0, wx.ALL, 5 )
		
		self.m_spinCtrl162 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerNumber.Add( self.m_spinCtrl162, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerPicture.Add( sizerNumber, 0, 0, 5 )
		
		sizerGraphic = wx.BoxSizer( wx.VERTICAL )
		
		self.labelGraphic = wx.StaticText( self, wx.ID_ANY, u"Picture Graphic:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelGraphic.Wrap( -1 )
		sizerGraphic.Add( self.labelGraphic, 0, wx.ALL, 5 )
		
		comboBoxGraphicChoices = []
		self.comboBoxGraphic = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxGraphicChoices, 0 )
		sizerGraphic.Add( self.comboBoxGraphic, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		sizerPicture.Add( sizerGraphic, 1, 0, 5 )
		
		MainSizer.Add( sizerPicture, 0, wx.EXPAND, 5 )
		
		sizerDisplayOrigin = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Display Origin" ), wx.VERTICAL )
		
		radioBoxOriginChoices = [ u"Upper-Left Corner", u"Center" ]
		self.radioBoxOrigin = wx.RadioBox( self, wx.ID_ANY, u"Origin Point", wx.DefaultPosition, wx.DefaultSize, radioBoxOriginChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioBoxOrigin.SetSelection( 0 )
		sizerDisplayOrigin.Add( self.radioBoxOrigin, 0, wx.ALL, 5 )
		
		sizerConstantX = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonConstant = wx.RadioButton( self, wx.ID_ANY, u"Constant", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerConstantX.Add( self.radioButtonConstant, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.labelConstantX = wx.StaticText( self, wx.ID_ANY, u"X:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelConstantX.Wrap( -1 )
		sizerConstantX.Add( self.labelConstantX, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlConstantX = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 72,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerConstantX.Add( self.spinCtrlConstantX, 0, wx.ALL, 5 )
		
		sizerDisplayOrigin.Add( sizerConstantX, 0, wx.EXPAND, 5 )
		
		sizerConstantY = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDummy1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		self.labelDummy1.Wrap( -1 )
		sizerConstantY.Add( self.labelDummy1, 0, wx.ALL, 5 )
		
		self.labelConstantY = wx.StaticText( self, wx.ID_ANY, u"Y:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelConstantY.Wrap( -1 )
		sizerConstantY.Add( self.labelConstantY, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlConstantY = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 72,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerConstantY.Add( self.spinCtrlConstantY, 0, wx.ALL, 5 )
		
		sizerDisplayOrigin.Add( sizerConstantY, 0, wx.EXPAND, 5 )
		
		sizerVariableX = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonVariable = wx.RadioButton( self, wx.ID_ANY, u"Variable", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerVariableX.Add( self.radioButtonVariable, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.labelVariableX = wx.StaticText( self, wx.ID_ANY, u"X:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelVariableX.Wrap( -1 )
		sizerVariableX.Add( self.labelVariableX, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxVariableXChoices = []
		self.comboBoxVariableX = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxVariableXChoices, 0 )
		sizerVariableX.Add( self.comboBoxVariableX, 1, wx.ALL, 5 )
		
		sizerDisplayOrigin.Add( sizerVariableX, 0, wx.EXPAND, 5 )
		
		sizerVariableY = wx.BoxSizer( wx.HORIZONTAL )
		
		self.abelDummy2 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		self.abelDummy2.Wrap( -1 )
		sizerVariableY.Add( self.abelDummy2, 0, wx.ALL, 5 )
		
		self.labelVariableY = wx.StaticText( self, wx.ID_ANY, u"Y:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelVariableY.Wrap( -1 )
		sizerVariableY.Add( self.labelVariableY, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxVariableYChoices = []
		self.comboBoxVariableY = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxVariableYChoices, 0 )
		sizerVariableY.Add( self.comboBoxVariableY, 1, wx.ALL, 5 )
		
		sizerDisplayOrigin.Add( sizerVariableY, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerDisplayOrigin, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizerSettings = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerZoom = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Zoom" ), wx.VERTICAL )
		
		sizerZoomX = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelZoomX = wx.StaticText( self, wx.ID_ANY, u"X:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelZoomX.Wrap( -1 )
		sizerZoomX.Add( self.labelZoomX, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlZoomX = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerZoomX.Add( self.spinCtrlZoomX, 1, wx.ALL, 5 )
		
		sizerZoom.Add( sizerZoomX, 0, wx.EXPAND, 5 )
		
		sizerZoomY = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelZoomY = wx.StaticText( self, wx.ID_ANY, u"Y:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelZoomY.Wrap( -1 )
		sizerZoomY.Add( self.labelZoomY, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlZoomY = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerZoomY.Add( self.spinCtrlZoomY, 1, wx.ALL, 5 )
		
		sizerZoom.Add( sizerZoomY, 0, wx.EXPAND, 5 )
		
		sizerSettings.Add( sizerZoom, 1, wx.ALL, 5 )
		
		sizerOpacity = wx.BoxSizer( wx.VERTICAL )
		
		self.labelOpacity = wx.StaticText( self, wx.ID_ANY, u"Opacity:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelOpacity.Wrap( -1 )
		sizerOpacity.Add( self.labelOpacity, 0, wx.ALL, 5 )
		
		self.spinCtrlOpacity = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 255, 255 )
		sizerOpacity.Add( self.spinCtrlOpacity, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerSettings.Add( sizerOpacity, 0, 0, 5 )
		
		sizerBlending = wx.BoxSizer( wx.VERTICAL )
		
		self.labelBlending = wx.StaticText( self, wx.ID_ANY, u"Blending:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBlending.Wrap( -1 )
		sizerBlending.Add( self.labelBlending, 0, wx.ALL, 5 )
		
		comboBoxBlendingChoices = [ u"Normal", u"Add", u"Subtract" ]
		self.comboBoxBlending = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), comboBoxBlendingChoices, 0 )
		self.comboBoxBlending.SetSelection( 0 )
		sizerBlending.Add( self.comboBoxBlending, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerSettings.Add( sizerBlending, 0, 0, 5 )
		
		MainSizer.Add( sizerSettings, 0, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.comboBoxGraphic.Bind( wx.EVT_LEFT_DOWN, self.comboBoxPictureGraphic_Clicked )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def comboBoxPictureGraphic_Clicked( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class MovePicture_Dialog
###########################################################################

class MovePicture_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Move Picture", pos = wx.DefaultPosition, size = wx.Size( 288,418 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		sizerPicture = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerNumber = wx.BoxSizer( wx.VERTICAL )
		
		self.labelNumber = wx.StaticText( self, wx.ID_ANY, u"Number:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelNumber.Wrap( -1 )
		sizerNumber.Add( self.labelNumber, 0, wx.ALL, 5 )
		
		self.m_spinCtrl162 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerNumber.Add( self.m_spinCtrl162, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerPicture.Add( sizerNumber, 1, wx.EXPAND, 5 )
		
		sizerTime = wx.BoxSizer( wx.VERTICAL )
		
		self.labelTime = wx.StaticText( self, wx.ID_ANY, u"Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTime.Wrap( -1 )
		sizerTime.Add( self.labelTime, 0, wx.ALL, 5 )
		
		sizerFrames = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_spinCtrl163 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerFrames.Add( self.m_spinCtrl163, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelFrames = wx.StaticText( self, wx.ID_ANY, u"Frames", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelFrames.Wrap( -1 )
		sizerFrames.Add( self.labelFrames, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		sizerTime.Add( sizerFrames, 1, wx.EXPAND, 5 )
		
		sizerPicture.Add( sizerTime, 1, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerPicture, 0, 0, 5 )
		
		sizerDisplayOrigin = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Display Origin" ), wx.VERTICAL )
		
		radioBoxOriginChoices = [ u"Upper-Left Corner", u"Center" ]
		self.radioBoxOrigin = wx.RadioBox( self, wx.ID_ANY, u"Origin Point", wx.DefaultPosition, wx.DefaultSize, radioBoxOriginChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioBoxOrigin.SetSelection( 0 )
		sizerDisplayOrigin.Add( self.radioBoxOrigin, 0, wx.ALL, 5 )
		
		sizerConstantX = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonConstant = wx.RadioButton( self, wx.ID_ANY, u"Constant", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerConstantX.Add( self.radioButtonConstant, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.labelConstantX = wx.StaticText( self, wx.ID_ANY, u"X:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelConstantX.Wrap( -1 )
		sizerConstantX.Add( self.labelConstantX, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlConstantX = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 72,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerConstantX.Add( self.spinCtrlConstantX, 0, wx.ALL, 5 )
		
		sizerDisplayOrigin.Add( sizerConstantX, 0, wx.EXPAND, 5 )
		
		sizerConstantY = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDummy1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		self.labelDummy1.Wrap( -1 )
		sizerConstantY.Add( self.labelDummy1, 0, wx.ALL, 5 )
		
		self.labelConstantY = wx.StaticText( self, wx.ID_ANY, u"Y:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelConstantY.Wrap( -1 )
		sizerConstantY.Add( self.labelConstantY, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlConstantY = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 72,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerConstantY.Add( self.spinCtrlConstantY, 0, wx.ALL, 5 )
		
		sizerDisplayOrigin.Add( sizerConstantY, 0, wx.EXPAND, 5 )
		
		sizerVariableX = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonVariable = wx.RadioButton( self, wx.ID_ANY, u"Variable", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerVariableX.Add( self.radioButtonVariable, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.labelVariableX = wx.StaticText( self, wx.ID_ANY, u"X:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelVariableX.Wrap( -1 )
		sizerVariableX.Add( self.labelVariableX, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxVariableXChoices = []
		self.comboBoxVariableX = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxVariableXChoices, 0 )
		sizerVariableX.Add( self.comboBoxVariableX, 1, wx.ALL, 5 )
		
		sizerDisplayOrigin.Add( sizerVariableX, 0, wx.EXPAND, 5 )
		
		sizerVariableY = wx.BoxSizer( wx.HORIZONTAL )
		
		self.abelDummy2 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		self.abelDummy2.Wrap( -1 )
		sizerVariableY.Add( self.abelDummy2, 0, wx.ALL, 5 )
		
		self.labelVariableY = wx.StaticText( self, wx.ID_ANY, u"Y:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelVariableY.Wrap( -1 )
		sizerVariableY.Add( self.labelVariableY, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxVariableYChoices = []
		self.comboBoxVariableY = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxVariableYChoices, 0 )
		sizerVariableY.Add( self.comboBoxVariableY, 1, wx.ALL, 5 )
		
		sizerDisplayOrigin.Add( sizerVariableY, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerDisplayOrigin, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizerSettings = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerZoom = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Zoom" ), wx.VERTICAL )
		
		sizerZoomX = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelZoomX = wx.StaticText( self, wx.ID_ANY, u"X:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelZoomX.Wrap( -1 )
		sizerZoomX.Add( self.labelZoomX, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlZoomX = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerZoomX.Add( self.spinCtrlZoomX, 1, wx.ALL, 5 )
		
		sizerZoom.Add( sizerZoomX, 0, wx.EXPAND, 5 )
		
		sizerZoomY = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelZoomY = wx.StaticText( self, wx.ID_ANY, u"Y:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelZoomY.Wrap( -1 )
		sizerZoomY.Add( self.labelZoomY, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlZoomY = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerZoomY.Add( self.spinCtrlZoomY, 1, wx.ALL, 5 )
		
		sizerZoom.Add( sizerZoomY, 0, wx.EXPAND, 5 )
		
		sizerSettings.Add( sizerZoom, 1, wx.ALL, 5 )
		
		sizerOpacity = wx.BoxSizer( wx.VERTICAL )
		
		self.labelOpacity = wx.StaticText( self, wx.ID_ANY, u"Opacity:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelOpacity.Wrap( -1 )
		sizerOpacity.Add( self.labelOpacity, 0, wx.ALL, 5 )
		
		self.spinCtrlOpacity = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 255, 255 )
		sizerOpacity.Add( self.spinCtrlOpacity, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerSettings.Add( sizerOpacity, 0, 0, 5 )
		
		sizerBlending = wx.BoxSizer( wx.VERTICAL )
		
		self.labelBlending = wx.StaticText( self, wx.ID_ANY, u"Blending:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBlending.Wrap( -1 )
		sizerBlending.Add( self.labelBlending, 0, wx.ALL, 5 )
		
		comboBoxBlendingChoices = [ u"Normal", u"Add", u"Subtract" ]
		self.comboBoxBlending = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), comboBoxBlendingChoices, 0 )
		self.comboBoxBlending.SetSelection( 0 )
		sizerBlending.Add( self.comboBoxBlending, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerSettings.Add( sizerBlending, 0, 0, 5 )
		
		MainSizer.Add( sizerSettings, 0, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class RotatePicture_Dialog
###########################################################################

class RotatePicture_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Rotate Picture", pos = wx.DefaultPosition, size = wx.Size( 277,91 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerNumber = wx.BoxSizer( wx.VERTICAL )
		
		self.labelNumber = wx.StaticText( self, wx.ID_ANY, u"Number:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelNumber.Wrap( -1 )
		sizerNumber.Add( self.labelNumber, 0, wx.ALL, 5 )
		
		self.spinCtrlSpeed = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerNumber.Add( self.spinCtrlSpeed, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerNumber, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerSpeed = wx.BoxSizer( wx.VERTICAL )
		
		self.labelSpeed = wx.StaticText( self, wx.ID_ANY, u"Speed:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelSpeed.Wrap( -1 )
		sizerSpeed.Add( self.labelSpeed, 0, wx.ALL, 5 )
		
		self.spinCtrlSpeed = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerSpeed.Add( self.spinCtrlSpeed, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		MainSizer.Add( sizerSpeed, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ErasePicture_Dialog
###########################################################################

class ErasePicture_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Erase Picture", pos = wx.DefaultPosition, size = wx.Size( 200,93 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerNumber = wx.BoxSizer( wx.VERTICAL )
		
		self.labelNumber = wx.StaticText( self, wx.ID_ANY, u"Number:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelNumber.Wrap( -1 )
		sizerNumber.Add( self.labelNumber, 0, wx.ALL, 5 )
		
		self.spinCtrlNumber = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerNumber.Add( self.spinCtrlNumber, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerNumber, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class WeatherEffects_Dialog
###########################################################################

class WeatherEffects_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Set Weather Effects", pos = wx.DefaultPosition, size = wx.Size( 305,273 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		listCtrlEffectsChoices = [ u"None", u"Rain", u"Storm", u"Snow", u"Blizzard", u"Hail", u"Green Leaves", u"Autumn Leaves", u"Rose Petals", u"Sakura Petals" ]
		self.listCtrlEffects = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listCtrlEffectsChoices, wx.LB_NEEDED_SB|wx.LB_SINGLE )
		MainSizer.Add( self.listCtrlEffects, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizerPower = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelPower = wx.StaticText( self, wx.ID_ANY, u"Power:", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.labelPower.Wrap( -1 )
		sizerPower.Add( self.labelPower, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.sliderPower = wx.Slider( self, wx.ID_ANY, 25, 0, 50, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS|wx.SL_TOP )
		sizerPower.Add( self.sliderPower, 1, wx.ALL, 5 )
		
		self.m_spinCtrl157 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 50, 25 )
		sizerPower.Add( self.m_spinCtrl157, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		MainSizer.Add( sizerPower, 0, wx.EXPAND, 5 )
		
		sizerTime = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelTime = wx.StaticText( self, wx.ID_ANY, u"Time:  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTime.Wrap( -1 )
		sizerTime.Add( self.labelTime, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlFrames = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 2000, 200 )
		sizerTime.Add( self.spinCtrlFrames, 0, wx.ALL, 5 )
		
		self.labelFrames = wx.StaticText( self, wx.ID_ANY, u"Frames", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelFrames.Wrap( -1 )
		sizerTime.Add( self.labelFrames, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		MainSizer.Add( sizerTime, 0, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.sliderPower.Bind( wx.EVT_SCROLL, self.sliderPower_ScrollChanged )
		self.m_spinCtrl157.Bind( wx.EVT_SPINCTRL, self.spinCtrlPower_ValueChanged )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def sliderPower_ScrollChanged( self, event ):
		event.Skip()
	
	def spinCtrlPower_ValueChanged( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class FadeOutAudio_Dialog
###########################################################################

class FadeOutAudio_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Fade Out (BGM/BGS)", pos = wx.DefaultPosition, size = wx.Size( 241,91 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerFade = wx.BoxSizer( wx.VERTICAL )
		
		self.labelTime = wx.StaticText( self, wx.ID_ANY, u"Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTime.Wrap( -1 )
		sizerFade.Add( self.labelTime, 0, wx.ALL, 5 )
		
		sizerSeconds = wx.BoxSizer( wx.HORIZONTAL )
		
		self.spinCtrlSeconds = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerSeconds.Add( self.spinCtrlSeconds, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelSeconds = wx.StaticText( self, wx.ID_ANY, u"Sec", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelSeconds.Wrap( -1 )
		sizerSeconds.Add( self.labelSeconds, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerFade.Add( sizerSeconds, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerFade, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class BattleProcessing_Dialog
###########################################################################

class BattleProcessing_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Battle Processing", pos = wx.DefaultPosition, size = wx.Size( 301,128 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerTroop = wx.BoxSizer( wx.VERTICAL )
		
		self.labelTroop = wx.StaticText( self, wx.ID_ANY, u"Troop:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTroop.Wrap( -1 )
		sizerTroop.Add( self.labelTroop, 0, wx.ALL, 5 )
		
		comboBoxTroopChoices = []
		self.comboBoxTroop = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxTroopChoices, 0 )
		self.comboBoxTroop.SetSelection( 0 )
		sizerTroop.Add( self.comboBoxTroop, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.checkBoxCanEscape = wx.CheckBox( self, wx.ID_ANY, u"Can Escape", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.checkBoxCanEscape.SetValue(True) 
		sizerTroop.Add( self.checkBoxCanEscape, 0, wx.ALL, 5 )
		
		self.checkBoxContinueLost = wx.CheckBox( self, wx.ID_ANY, u"Continue After Loss", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerTroop.Add( self.checkBoxContinueLost, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerTroop, 1, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ShopProcessing_Dialog
###########################################################################

class ShopProcessing_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Shop Processing", pos = wx.DefaultPosition, size = wx.Size( 276,316 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.listCtrlShopGoods = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON|wx.LC_REPORT )
		MainSizer.Add( self.listCtrlShopGoods, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.listCtrlShopGoods.Bind( wx.EVT_LEFT_DCLICK, self.listCtrlShopGoods_DoubleClick )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def listCtrlShopGoods_DoubleClick( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ShopGoods_Dialog
###########################################################################

class ShopGoods_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Goods", pos = wx.DefaultPosition, size = wx.Size( 281,157 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		sizerItem = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonItem = wx.RadioButton( self, wx.ID_ANY, u"Item", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerItem.Add( self.radioButtonItem, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxItemChoices = []
		self.comboBoxItem = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxItemChoices, 0 )
		self.comboBoxItem.SetSelection( 0 )
		sizerItem.Add( self.comboBoxItem, 1, wx.ALL, 5 )
		
		MainSizer.Add( sizerItem, 0, wx.EXPAND, 5 )
		
		sizerWeapons = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonWeapon = wx.RadioButton( self, wx.ID_ANY, u"Weapon", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerWeapons.Add( self.radioButtonWeapon, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxWeaponChoices = []
		self.comboBoxWeapon = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxWeaponChoices, 0 )
		self.comboBoxWeapon.SetSelection( 0 )
		sizerWeapons.Add( self.comboBoxWeapon, 1, wx.ALL, 5 )
		
		MainSizer.Add( sizerWeapons, 0, wx.EXPAND, 5 )
		
		sizerArmor = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonArmor = wx.RadioButton( self, wx.ID_ANY, u"Armor", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerArmor.Add( self.radioButtonArmor, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxArmorChoices = []
		self.comboBoxArmor = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxArmorChoices, 0 )
		self.comboBoxArmor.SetSelection( 0 )
		sizerArmor.Add( self.comboBoxArmor, 1, wx.ALL, 5 )
		
		MainSizer.Add( sizerArmor, 0, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class NameProcessing_Dialog
###########################################################################

class NameProcessing_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Name Input Processing", pos = wx.DefaultPosition, size = wx.Size( 276,136 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerName = wx.BoxSizer( wx.VERTICAL )
		
		self.labelActor = wx.StaticText( self, wx.ID_ANY, u"Actor:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelActor.Wrap( -1 )
		sizerName.Add( self.labelActor, 0, wx.ALL, 5 )
		
		comboBoxActorChoices = []
		self.comboBoxActor = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxActorChoices, 0 )
		self.comboBoxActor.SetSelection( 0 )
		sizerName.Add( self.comboBoxActor, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelMaxCharacters = wx.StaticText( self, wx.ID_ANY, u"Max Characters:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMaxCharacters.Wrap( -1 )
		sizerName.Add( self.labelMaxCharacters, 0, wx.ALL, 5 )
		
		self.spinCtrlMaxCharacters = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerName.Add( self.spinCtrlMaxCharacters, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerName, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.EXPAND|wx.ALIGN_BOTTOM, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ChangeHP_Dialog
###########################################################################

class ChangeHP_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Change HP", pos = wx.DefaultPosition, size = wx.Size( 241,283 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.labelActor = wx.StaticText( self, wx.ID_ANY, u"Actor:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelActor.Wrap( -1 )
		MainSizer.Add( self.labelActor, 0, wx.ALL, 5 )
		
		comboBoxActorChoices = []
		self.comboBoxActor = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,-1 ), comboBoxActorChoices, 0 )
		self.comboBoxActor.SetSelection( 0 )
		MainSizer.Add( self.comboBoxActor, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		radioBoxOperationChoices = [ u"Increase", u"Decrease" ]
		self.radioBoxOperation = wx.RadioBox( self, wx.ID_ANY, u"Operation", wx.DefaultPosition, wx.DefaultSize, radioBoxOperationChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioBoxOperation.SetSelection( 0 )
		MainSizer.Add( self.radioBoxOperation, 0, wx.ALL, 5 )
		
		sizerOperand = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Operand" ), wx.VERTICAL )
		
		sizerConstant = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonConstant = wx.RadioButton( self, wx.ID_ANY, u"Constant", wx.DefaultPosition, wx.Size( 72,-1 ), wx.RB_GROUP )
		sizerConstant.Add( self.radioButtonConstant, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlConstant = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerConstant.Add( self.spinCtrlConstant, 0, wx.ALL, 5 )
		
		sizerOperand.Add( sizerConstant, 0, wx.EXPAND, 5 )
		
		sizerVariable = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonVariable = wx.RadioButton( self, wx.ID_ANY, u"Variable", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerVariable.Add( self.radioButtonVariable, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxVariableChoices = []
		self.comboBoxVariable = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxVariableChoices, 0 )
		sizerVariable.Add( self.comboBoxVariable, 1, wx.ALL, 5 )
		
		sizerOperand.Add( sizerVariable, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerOperand, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.checkBoxKnockout = wx.CheckBox( self, wx.ID_ANY, u"Allow Knockout in Battle", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.checkBoxKnockout.SetValue(True) 
		MainSizer.Add( self.checkBoxKnockout, 0, wx.ALL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.comboBoxVariable.Bind( wx.EVT_LEFT_DOWN, self.comboBoxVariable_Clicked )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def comboBoxVariable_Clicked( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ChangeStat_Dialog
###########################################################################

class ChangeStat_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Change (SP/Exp/Level)", pos = wx.DefaultPosition, size = wx.Size( 241,260 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.labelActor = wx.StaticText( self, wx.ID_ANY, u"Actor:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelActor.Wrap( -1 )
		MainSizer.Add( self.labelActor, 0, wx.ALL, 5 )
		
		comboBoxActorChoices = []
		self.comboBoxActor = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,-1 ), comboBoxActorChoices, 0 )
		self.comboBoxActor.SetSelection( 0 )
		MainSizer.Add( self.comboBoxActor, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		radioBoxOperationChoices = [ u"Increase", u"Decrease" ]
		self.radioBoxOperation = wx.RadioBox( self, wx.ID_ANY, u"Operation", wx.DefaultPosition, wx.DefaultSize, radioBoxOperationChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioBoxOperation.SetSelection( 0 )
		MainSizer.Add( self.radioBoxOperation, 0, wx.ALL, 5 )
		
		sizerOperand = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Operand" ), wx.VERTICAL )
		
		sizerConstant = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonConstant = wx.RadioButton( self, wx.ID_ANY, u"Constant", wx.DefaultPosition, wx.Size( 72,-1 ), wx.RB_GROUP )
		sizerConstant.Add( self.radioButtonConstant, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlConstant = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerConstant.Add( self.spinCtrlConstant, 0, wx.ALL, 5 )
		
		sizerOperand.Add( sizerConstant, 0, wx.EXPAND, 5 )
		
		sizerVariable = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonVariable = wx.RadioButton( self, wx.ID_ANY, u"Variable", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerVariable.Add( self.radioButtonVariable, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxVariableChoices = []
		self.comboBoxVariable = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxVariableChoices, 0 )
		sizerVariable.Add( self.comboBoxVariable, 1, wx.ALL, 5 )
		
		sizerOperand.Add( sizerVariable, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerOperand, 0, wx.EXPAND|wx.ALL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.comboBoxVariable.Bind( wx.EVT_LEFT_DOWN, self.comboBoxVariable_Clicked )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def comboBoxVariable_Clicked( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ChangeParameters_Dialog
###########################################################################

class ChangeParameters_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Change Parameters", pos = wx.DefaultPosition, size = wx.Size( 248,309 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.labelActor = wx.StaticText( self, wx.ID_ANY, u"Actor:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelActor.Wrap( -1 )
		MainSizer.Add( self.labelActor, 0, wx.ALL, 5 )
		
		comboBoxActorChoices = []
		self.comboBoxActor = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,-1 ), comboBoxActorChoices, 0 )
		self.comboBoxActor.SetSelection( 0 )
		MainSizer.Add( self.comboBoxActor, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelParameter = wx.StaticText( self, wx.ID_ANY, u"Parameter:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelParameter.Wrap( -1 )
		MainSizer.Add( self.labelParameter, 0, wx.ALL, 5 )
		
		comboBoxParameterChoices = [ u"MaxHP", u"MaxSP", u"STR", u"DEX", u"AGI", u"INT" ]
		self.comboBoxParameter = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 72,-1 ), comboBoxParameterChoices, 0 )
		self.comboBoxParameter.SetSelection( 0 )
		MainSizer.Add( self.comboBoxParameter, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		radioBoxOperationChoices = [ u"Increase", u"Decrease" ]
		self.radioBoxOperation = wx.RadioBox( self, wx.ID_ANY, u"Operation", wx.DefaultPosition, wx.DefaultSize, radioBoxOperationChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioBoxOperation.SetSelection( 0 )
		MainSizer.Add( self.radioBoxOperation, 0, wx.ALL, 5 )
		
		sizerOperand = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Operand" ), wx.VERTICAL )
		
		sizerConstant = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonConstant = wx.RadioButton( self, wx.ID_ANY, u"Constant", wx.DefaultPosition, wx.Size( 72,-1 ), wx.RB_GROUP )
		sizerConstant.Add( self.radioButtonConstant, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlConstant = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerConstant.Add( self.spinCtrlConstant, 0, wx.ALL, 5 )
		
		sizerOperand.Add( sizerConstant, 0, wx.EXPAND, 5 )
		
		sizerVariable = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonVariable = wx.RadioButton( self, wx.ID_ANY, u"Variable", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerVariable.Add( self.radioButtonVariable, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxVariableChoices = []
		self.comboBoxVariable = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxVariableChoices, 0 )
		sizerVariable.Add( self.comboBoxVariable, 1, wx.ALL, 5 )
		
		sizerOperand.Add( sizerVariable, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerOperand, 0, wx.EXPAND|wx.ALL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.comboBoxVariable.Bind( wx.EVT_LEFT_DOWN, self.comboBoxVariable_Clicked )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def comboBoxVariable_Clicked( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ChangeState_Dialog
###########################################################################

class ChangeState_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Change State", pos = wx.DefaultPosition, size = wx.Size( 249,186 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerState = wx.BoxSizer( wx.VERTICAL )
		
		self.labelActor = wx.StaticText( self, wx.ID_ANY, u"Actor:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelActor.Wrap( -1 )
		sizerState.Add( self.labelActor, 0, wx.ALL, 5 )
		
		comboBoxActorChoices = []
		self.comboBoxActor = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxActorChoices, 0 )
		self.comboBoxActor.SetSelection( 0 )
		sizerState.Add( self.comboBoxActor, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		radioBoxOperationChoices = [ u"Add", u"Remove" ]
		self.radioBoxOperation = wx.RadioBox( self, wx.ID_ANY, u"Operation", wx.DefaultPosition, wx.DefaultSize, radioBoxOperationChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioBoxOperation.SetSelection( 0 )
		sizerState.Add( self.radioBoxOperation, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.labelState = wx.StaticText( self, wx.ID_ANY, u"State:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelState.Wrap( -1 )
		sizerState.Add( self.labelState, 0, wx.ALL, 5 )
		
		comboBoxStateChoices = []
		self.comboBoxState = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxStateChoices, 0 )
		self.comboBoxState.SetSelection( 0 )
		sizerState.Add( self.comboBoxState, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerState, 1, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ChangeSkills_Dialog
###########################################################################

class ChangeSkills_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Change Skills", pos = wx.DefaultPosition, size = wx.Size( 275,183 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerSkill = wx.BoxSizer( wx.VERTICAL )
		
		self.labelActor = wx.StaticText( self, wx.ID_ANY, u"Actor:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelActor.Wrap( -1 )
		sizerSkill.Add( self.labelActor, 0, wx.ALL, 5 )
		
		comboBoxActorChoices = []
		self.comboBoxActor = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxActorChoices, 0 )
		self.comboBoxActor.SetSelection( 0 )
		sizerSkill.Add( self.comboBoxActor, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		radioBoxOperationChoices = [ u"Learn", u"Forget" ]
		self.radioBoxOperation = wx.RadioBox( self, wx.ID_ANY, u"Operation", wx.DefaultPosition, wx.DefaultSize, radioBoxOperationChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioBoxOperation.SetSelection( 0 )
		sizerSkill.Add( self.radioBoxOperation, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.labelSkill = wx.StaticText( self, wx.ID_ANY, u"Skill:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelSkill.Wrap( -1 )
		sizerSkill.Add( self.labelSkill, 0, wx.ALL, 5 )
		
		comboBoxSkillChoices = []
		self.comboBoxSkill = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxSkillChoices, 0 )
		self.comboBoxSkill.SetSelection( 0 )
		sizerSkill.Add( self.comboBoxSkill, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerSkill, 1, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ChangeEquipment_Dialog
###########################################################################

class ChangeEquipment_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Change Equipment", pos = wx.DefaultPosition, size = wx.Size( 283,299 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.labelActor = wx.StaticText( self, wx.ID_ANY, u"Actor:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelActor.Wrap( -1 )
		MainSizer.Add( self.labelActor, 0, wx.ALL, 5 )
		
		comboBoxActorChoices = []
		self.comboBoxActor = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,-1 ), comboBoxActorChoices, 0 )
		self.comboBoxActor.SetSelection( 0 )
		MainSizer.Add( self.comboBoxActor, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerEquipment = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Equipment" ), wx.VERTICAL )
		
		sizerWeapon = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonWeapon = wx.RadioButton( self, wx.ID_ANY, u"Weapon", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerWeapon.Add( self.radioButtonWeapon, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxWeaponChoices = []
		self.comboBoxWeapon = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxWeaponChoices, 0 )
		self.comboBoxWeapon.SetSelection( 0 )
		sizerWeapon.Add( self.comboBoxWeapon, 1, wx.ALL, 5 )
		
		sizerEquipment.Add( sizerWeapon, 0, wx.EXPAND, 5 )
		
		sizerShield = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonShield = wx.RadioButton( self, wx.ID_ANY, u"Shield", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerShield.Add( self.radioButtonShield, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxShieldChoices = []
		self.comboBoxShield = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxShieldChoices, 0 )
		self.comboBoxShield.SetSelection( 0 )
		sizerShield.Add( self.comboBoxShield, 1, wx.ALL, 5 )
		
		sizerEquipment.Add( sizerShield, 0, wx.EXPAND, 5 )
		
		sizerHelmet = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonHelmet = wx.RadioButton( self, wx.ID_ANY, u"Helmet", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerHelmet.Add( self.radioButtonHelmet, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxHelmetChoices = []
		self.comboBoxHelmet = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxHelmetChoices, 0 )
		self.comboBoxHelmet.SetSelection( 0 )
		sizerHelmet.Add( self.comboBoxHelmet, 1, wx.ALL, 5 )
		
		sizerEquipment.Add( sizerHelmet, 0, wx.EXPAND, 5 )
		
		sizerBodyArmor = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonBodyArmor = wx.RadioButton( self, wx.ID_ANY, u"Body Armor", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerBodyArmor.Add( self.radioButtonBodyArmor, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxBodyArmorChoices = []
		self.comboBoxBodyArmor = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxBodyArmorChoices, 0 )
		self.comboBoxBodyArmor.SetSelection( 0 )
		sizerBodyArmor.Add( self.comboBoxBodyArmor, 1, wx.ALL, 5 )
		
		sizerEquipment.Add( sizerBodyArmor, 0, wx.EXPAND, 5 )
		
		sizerAccessory = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonAccessory = wx.RadioButton( self, wx.ID_ANY, u"Accessory", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerAccessory.Add( self.radioButtonAccessory, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxAccessoryChoices = []
		self.comboBoxAccessory = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxAccessoryChoices, 0 )
		self.comboBoxAccessory.SetSelection( 0 )
		sizerAccessory.Add( self.comboBoxAccessory, 1, wx.ALL, 5 )
		
		sizerEquipment.Add( sizerAccessory, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerEquipment, 1, wx.EXPAND|wx.ALL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ChangeActorName_Dialog
###########################################################################

class ChangeActorName_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Change Actor Name:", pos = wx.DefaultPosition, size = wx.Size( 261,128 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerName = wx.BoxSizer( wx.VERTICAL )
		
		self.labelActor = wx.StaticText( self, wx.ID_ANY, u"Actor:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelActor.Wrap( -1 )
		sizerName.Add( self.labelActor, 0, wx.ALL, 5 )
		
		comboBoxActorChoices = []
		self.comboBoxActor = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxActorChoices, 0 )
		self.comboBoxActor.SetSelection( 0 )
		sizerName.Add( self.comboBoxActor, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelName.Wrap( -1 )
		sizerName.Add( self.labelName, 0, wx.ALL, 5 )
		
		self.textCtrlName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerName.Add( self.textCtrlName, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		MainSizer.Add( sizerName, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ChangeActorClass_Dialog
###########################################################################

class ChangeActorClass_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Change Actor Class", pos = wx.DefaultPosition, size = wx.Size( 258,129 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerClass = wx.BoxSizer( wx.VERTICAL )
		
		self.labelActor = wx.StaticText( self, wx.ID_ANY, u"Actor:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelActor.Wrap( -1 )
		sizerClass.Add( self.labelActor, 0, wx.ALL, 5 )
		
		comboBoxActorChoices = []
		self.comboBoxActor = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxActorChoices, 0 )
		self.comboBoxActor.SetSelection( 0 )
		sizerClass.Add( self.comboBoxActor, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelClass = wx.StaticText( self, wx.ID_ANY, u"Class:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelClass.Wrap( -1 )
		sizerClass.Add( self.labelClass, 0, wx.ALL, 5 )
		
		comboBoxClassChoices = []
		self.comboBoxClass = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxClassChoices, 0 )
		self.comboBoxClass.SetSelection( 0 )
		sizerClass.Add( self.comboBoxClass, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerClass, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ChangeActorGraphic_Dialog
###########################################################################

class ChangeActorGraphic_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Change Actor Graphic", pos = wx.DefaultPosition, size = wx.Size( 254,179 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerGraphic = wx.BoxSizer( wx.VERTICAL )
		
		self.labelActor = wx.StaticText( self, wx.ID_ANY, u"Actor:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelActor.Wrap( -1 )
		sizerGraphic.Add( self.labelActor, 0, wx.ALL, 5 )
		
		m_choice90Choices = []
		self.m_choice90 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice90Choices, 0 )
		self.m_choice90.SetSelection( 0 )
		sizerGraphic.Add( self.m_choice90, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelCharacterGraphic = wx.StaticText( self, wx.ID_ANY, u"Character Graphic:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelCharacterGraphic.Wrap( -1 )
		sizerGraphic.Add( self.labelCharacterGraphic, 0, wx.ALL, 5 )
		
		comboBoxCharacterChoices = []
		self.comboBoxCharacter = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxCharacterChoices, 0 )
		sizerGraphic.Add( self.comboBoxCharacter, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.labelBattlerGraphic = wx.StaticText( self, wx.ID_ANY, u"Battler Graphic:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBattlerGraphic.Wrap( -1 )
		sizerGraphic.Add( self.labelBattlerGraphic, 0, wx.ALL, 5 )
		
		comboBoxBattlerChoices = []
		self.comboBoxBattler = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxBattlerChoices, 0 )
		sizerGraphic.Add( self.comboBoxBattler, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerGraphic, 1, wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.comboBoxCharacter.Bind( wx.EVT_LEFT_UP, self.comboBoxCharacter_Clicked )
		self.comboBoxBattler.Bind( wx.EVT_LEFT_DOWN, self.comboBoxBattler_Clicked )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def comboBoxCharacter_Clicked( self, event ):
		event.Skip()
	
	def comboBoxBattler_Clicked( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class RecoverAll_Dialog
###########################################################################

class RecoverAll_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Recover All", pos = wx.DefaultPosition, size = wx.Size( 275,90 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerControls = wx.BoxSizer( wx.VERTICAL )
		
		self.labelBattler = wx.StaticText( self, wx.ID_ANY, u"(Actor/Enemy)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelBattler.Wrap( -1 )
		sizerControls.Add( self.labelBattler, 0, wx.ALL, 5 )
		
		comboBoxBattlerChoices = []
		self.comboBoxBattler = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxBattlerChoices, 0 )
		self.comboBoxBattler.SetSelection( -1 )
		sizerControls.Add( self.comboBoxBattler, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerControls, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class EnemyAppearance_Dialog
###########################################################################

class EnemyAppearance_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Enemy Appearance", pos = wx.DefaultPosition, size = wx.Size( 275,90 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerControls = wx.BoxSizer( wx.VERTICAL )
		
		self.labelEnemy = wx.StaticText( self, wx.ID_ANY, u"Enemy:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelEnemy.Wrap( -1 )
		sizerControls.Add( self.labelEnemy, 0, wx.ALL, 5 )
		
		comboBoxEnemyChoices = []
		self.comboBoxEnemy = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxEnemyChoices, 0 )
		self.comboBoxEnemy.SetSelection( 0 )
		sizerControls.Add( self.comboBoxEnemy, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerControls, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class EnemyTransform_Dialog
###########################################################################

class EnemyTransform_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Enemy Transformation", pos = wx.DefaultPosition, size = wx.Size( 305,129 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerControls = wx.BoxSizer( wx.VERTICAL )
		
		self.labelEnemy = wx.StaticText( self, wx.ID_ANY, u"Enemy:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelEnemy.Wrap( -1 )
		sizerControls.Add( self.labelEnemy, 0, wx.ALL, 5 )
		
		comboBoxEnemyChoices = []
		self.comboBoxEnemy = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxEnemyChoices, 0 )
		sizerControls.Add( self.comboBoxEnemy, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.labelTransform = wx.StaticText( self, wx.ID_ANY, u"Transform to:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTransform.Wrap( -1 )
		sizerControls.Add( self.labelTransform, 0, wx.ALL, 5 )
		
		comboBoxTransformChoices = []
		self.comboBoxTransform = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxTransformChoices, 0 )
		self.comboBoxTransform.SetSelection( 0 )
		sizerControls.Add( self.comboBoxTransform, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		MainSizer.Add( sizerControls, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.VERTICAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, 0, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.comboBoxEnemy.Bind( wx.EVT_LEFT_DOWN, self.comboBoxEnemy_Clicked )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def comboBoxEnemy_Clicked( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class BattleAnimation_Dialog
###########################################################################

class BattleAnimation_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Show Battle Animation", pos = wx.DefaultPosition, size = wx.Size( 267,205 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		sizerTarget = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Target" ), wx.VERTICAL )
		
		sizerEnemy = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonEnemy = wx.RadioButton( self, wx.ID_ANY, u"Enemy", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerEnemy.Add( self.radioButtonEnemy, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxEnemyChoices = [ u"Entire Troop" ]
		self.comboBoxEnemy = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxEnemyChoices, 0 )
		self.comboBoxEnemy.SetSelection( 0 )
		sizerEnemy.Add( self.comboBoxEnemy, 1, wx.ALL, 5 )
		
		sizerTarget.Add( sizerEnemy, 0, wx.EXPAND, 5 )
		
		sizerActor = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonActor = wx.RadioButton( self, wx.ID_ANY, u"Actor", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerActor.Add( self.radioButtonActor, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxActorChoices = [ u"Entire Party", u"Actor 1", u"Actor 2", u"Actor 3", u"Actor 4", u"Actor 5", u"Actor 6", u"Actor 7", u"Actor 8", u"Actor 9", u"Actor 10" ]
		self.comboBoxActor = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxActorChoices, 0 )
		self.comboBoxActor.SetSelection( 0 )
		sizerActor.Add( self.comboBoxActor, 1, wx.ALL, 5 )
		
		sizerTarget.Add( sizerActor, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerTarget, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.labelAnimation = wx.StaticText( self, wx.ID_ANY, u"Animation:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAnimation.Wrap( -1 )
		MainSizer.Add( self.labelAnimation, 0, wx.ALL, 5 )
		
		comboBoxAnimationChoices = []
		self.comboBoxAnimation = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxAnimationChoices, 0 )
		self.comboBoxAnimation.SetSelection( 0 )
		MainSizer.Add( self.comboBoxAnimation, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class DealDamage_Dialog
###########################################################################

class DealDamage_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Deal Damage", pos = wx.DefaultPosition, size = wx.Size( 284,252 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		sizerTarget = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Target" ), wx.VERTICAL )
		
		sizerEnemy = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonEnemy = wx.RadioButton( self, wx.ID_ANY, u"Enemy", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerEnemy.Add( self.radioButtonEnemy, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxEnemyChoices = [ u"Entire Troop" ]
		self.comboBoxEnemy = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxEnemyChoices, 0 )
		self.comboBoxEnemy.SetSelection( 0 )
		sizerEnemy.Add( self.comboBoxEnemy, 1, wx.ALL, 5 )
		
		sizerTarget.Add( sizerEnemy, 0, wx.EXPAND, 5 )
		
		sizerActor = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonActor = wx.RadioButton( self, wx.ID_ANY, u"Actor", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerActor.Add( self.radioButtonActor, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxActorChoices = [ u"Entire Party", u"Actor 1", u"Actor 2", u"Actor 3", u"Actor 4", u"Actor 5", u"Actor 6", u"Actor 7", u"Actor 8", u"Actor 9", u"Actor 10" ]
		self.comboBoxActor = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxActorChoices, 0 )
		self.comboBoxActor.SetSelection( 0 )
		sizerActor.Add( self.comboBoxActor, 1, wx.ALL, 5 )
		
		sizerTarget.Add( sizerActor, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerTarget, 0, wx.EXPAND|wx.ALL, 5 )
		
		sizerOperand = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Operand" ), wx.VERTICAL )
		
		sizerConstant = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonConstant = wx.RadioButton( self, wx.ID_ANY, u"Constant", wx.DefaultPosition, wx.Size( 72,-1 ), wx.RB_GROUP )
		sizerConstant.Add( self.radioButtonConstant, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrlConstant = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sizerConstant.Add( self.spinCtrlConstant, 0, wx.ALL, 5 )
		
		sizerOperand.Add( sizerConstant, 0, wx.EXPAND, 5 )
		
		sizerVariable = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonVariable = wx.RadioButton( self, wx.ID_ANY, u"Variable", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerVariable.Add( self.radioButtonVariable, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxVariableChoices = []
		self.comboBoxVariable = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxVariableChoices, 0 )
		sizerVariable.Add( self.comboBoxVariable, 1, wx.ALL, 5 )
		
		sizerOperand.Add( sizerVariable, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerOperand, 0, wx.EXPAND|wx.ALL, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.comboBoxVariable.Bind( wx.EVT_LEFT_DOWN, self.comboBoxVariable_Clicked )
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def comboBoxVariable_Clicked( self, event ):
		event.Skip()
	
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ForceAction_Dialog
###########################################################################

class ForceAction_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Force Action", pos = wx.DefaultPosition, size = wx.Size( 307,367 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		sizerBattler = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Battler" ), wx.VERTICAL )
		
		sizerEnemy = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonEnemy = wx.RadioButton( self, wx.ID_ANY, u"Enemy", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerEnemy.Add( self.radioButtonEnemy, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxEnemiesChoices = [ u"Entire Troop" ]
		self.comboBoxEnemies = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxEnemiesChoices, 0 )
		self.comboBoxEnemies.SetSelection( 0 )
		sizerEnemy.Add( self.comboBoxEnemies, 1, wx.ALL, 5 )
		
		sizerBattler.Add( sizerEnemy, 0, wx.EXPAND, 5 )
		
		sizerActor = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonActor = wx.RadioButton( self, wx.ID_ANY, u"Actor", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerActor.Add( self.radioButtonActor, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxActorsChoices = [ u"Entire Party", u"Actor 1", u"Actor 2", u"Actor 3", u"Actor 4", u"Actor 5", u"Actor 6", u"Actor 7", u"Actor 8", u"Actor 9", u"Actor 10" ]
		self.comboBoxActors = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxActorsChoices, 0 )
		self.comboBoxActors.SetSelection( 0 )
		sizerActor.Add( self.comboBoxActors, 1, wx.ALL, 5 )
		
		sizerBattler.Add( sizerActor, 1, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerBattler, 0, wx.EXPAND|wx.ALL, 5 )
		
		sizerAction = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Action" ), wx.VERTICAL )
		
		sizerBasic = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonBasic = wx.RadioButton( self, wx.ID_ANY, u"Basic", wx.DefaultPosition, wx.Size( 72,-1 ), wx.RB_GROUP )
		sizerBasic.Add( self.radioButtonBasic, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxBasicChoices = [ u"Attack", u"Defend", u"Escape", u"Do Nothing" ]
		self.comboBoxBasic = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxBasicChoices, 0 )
		self.comboBoxBasic.SetSelection( 0 )
		sizerBasic.Add( self.comboBoxBasic, 1, wx.ALL, 5 )
		
		sizerAction.Add( sizerBasic, 0, wx.EXPAND, 5 )
		
		sizerSkill = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioButtonSkill = wx.RadioButton( self, wx.ID_ANY, u"Skill", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		sizerSkill.Add( self.radioButtonSkill, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxSkillChoices = []
		self.comboBoxSkill = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxSkillChoices, 0 )
		self.comboBoxSkill.SetSelection( 0 )
		sizerSkill.Add( self.comboBoxSkill, 1, wx.ALL, 5 )
		
		sizerAction.Add( sizerSkill, 0, wx.EXPAND, 5 )
		
		self.staticLine = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sizerAction.Add( self.staticLine, 0, wx.EXPAND |wx.ALL, 5 )
		
		sizerTarget = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelTarget = wx.StaticText( self, wx.ID_ANY, u"Action Target:", wx.DefaultPosition, wx.Size( 72,-1 ), 0 )
		self.labelTarget.Wrap( -1 )
		sizerTarget.Add( self.labelTarget, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		comboBoxTargetChoices = [ u"Last Target", u"Random", u"Index 1", u"Index 2", u"Index 3", u"Index 4", u"Index 5", u"Index 6", u"Index 7", u"Index 8", u"Index 9", u"Index 10" ]
		self.comboBoxTarget = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxTargetChoices, 0 )
		self.comboBoxTarget.SetSelection( 0 )
		sizerTarget.Add( self.comboBoxTarget, 1, wx.ALL, 5 )
		
		sizerAction.Add( sizerTarget, 0, wx.EXPAND, 5 )
		
		MainSizer.Add( sizerAction, 0, wx.EXPAND|wx.ALL, 5 )
		
		radioBoxTimingChoices = [ u"Execute in Normal Sequence", u"Execute Now" ]
		self.radioBoxTiming = wx.RadioBox( self, wx.ID_ANY, u"Timing", wx.DefaultPosition, wx.DefaultSize, radioBoxTimingChoices, 1, wx.RA_SPECIFY_COLS )
		self.radioBoxTiming.SetSelection( 0 )
		MainSizer.Add( self.radioBoxTiming, 0, wx.ALL|wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

###########################################################################
## Class ScriptCall_Dialog
###########################################################################

class ScriptCall_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Script", pos = wx.DefaultPosition, size = wx.Size( 338,253 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		MainSizer.SetMinSize( wx.Size( 320,196 ) ) 
		self.textCtrlScript = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_WORDWRAP )
		MainSizer.Add( self.textCtrlScript, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizerOKCancel = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonOK, 0, wx.ALL, 5 )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerOKCancel.Add( self.buttonCancel, 0, wx.ALL, 5 )
		
		MainSizer.Add( sizerOKCancel, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonOK.Bind( wx.EVT_BUTTON, self.buttonOK_Clicked )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.buttonCancel_Clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonOK_Clicked( self, event ):
		event.Skip()
	
	def buttonCancel_Clicked( self, event ):
		event.Skip()
	

