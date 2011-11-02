import wx
import Kernel
from Kernel import Manager as KM

class Configuration_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		''' Basic constructor for the Configurator Panel '''
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 517,364 ), style = wx.TAB_TRAVERSAL )
		global Config
		Config = Kernel.GlobalObjects.get_value('ARCed_config')
		self.Dictionary = {}
		# Create the fonts
		headerFont = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		optionFont = wx.Font(8, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		if not optionFont.SetFaceName('Consolas'):
			 optionFont.SetFaceName('Courier')
		# Create the main container controls
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		self.scrolledWindowEquipment = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CLIP_CHILDREN|wx.HSCROLL|wx.SIMPLE_BORDER|wx.VSCROLL )
		self.scrolledWindowEquipment.SetScrollRate( 5, 5 )
		sizerConfig = wx.BoxSizer( wx.VERTICAL )
		text = wx.StaticText( self.scrolledWindowEquipment, wx.ID_ANY, 
					'* Some settings may not have effect until after restart')
		font = text.GetFont()
		font.SetWeight(wx.BOLD)
		text.SetFont(font)
		sizerConfig.Add( text, 0, wx.EXPAND |wx.ALL, 5 )
		self.staticSectionLine = wx.StaticLine( self.scrolledWindowEquipment, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sizerConfig.Add( self.staticSectionLine, 0, wx.EXPAND |wx.ALL, 5 )
		# Iterate through each section
		for section in Config.itersections():
			sectionheader = wx.StaticText( self.scrolledWindowEquipment, wx.ID_ANY, 
				section[0].capitalize(), wx.DefaultPosition, wx.DefaultSize, 0 )
			sectionheader.Wrap( -1 )
			sectionheader.SetFont(headerFont)
			sizerConfig.Add( sectionheader, 0, wx.ALL, 5 )
			# Iterate through each section's items
			for option in section[1].iteritems():
				# Create label
				optionSizer = wx.BoxSizer( wx.HORIZONTAL )
				optionlabel = wx.StaticText( self.scrolledWindowEquipment, wx.ID_ANY, 
					option[0], wx.DefaultPosition, wx.Size( 96,-1 ), 0 )
				optionlabel.Wrap( -1 )
				optionSizer.Add( optionlabel, 0, wx.ALL, 5 )
				# Create text control
				value = Config.get(section[0], option[0])
				textCtrl = wx.TextCtrl( self.scrolledWindowEquipment, wx.ID_ANY, 
					value, wx.DefaultPosition, wx.DefaultSize, 0 )
				textCtrl.SetFont(optionFont)
				optionSizer.Add( textCtrl, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
				textCtrl.Bind( wx.EVT_TEXT, self.textBox_DataChanged )
				# Create the "changed" label, initialized as empty string
				labelChanged = wx.StaticText( self.scrolledWindowEquipment, wx.ID_ANY, 
					wx.EmptyString, wx.DefaultPosition, wx.Size( 8,-1 ), wx.ALIGN_CENTRE )
				labelChanged.Wrap( -1 )
				self.Dictionary[textCtrl] = [section[0], option[0], labelChanged]
				optionSizer.Add( labelChanged, 0, wx.ALL, 5 )
				sizerConfig.Add( optionSizer, 0, wx.EXPAND, 5 )
			endLine = wx.StaticLine( self.scrolledWindowEquipment, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
			sizerConfig.Add( endLine, 0, wx.EXPAND |wx.ALL, 5 )
		# Set the sizer and add the scrolled window to the panel
		self.scrolledWindowEquipment.SetSizer( sizerConfig )
		self.scrolledWindowEquipment.Layout()
		sizerConfig.Fit( self.scrolledWindowEquipment )
		MainSizer.Add( self.scrolledWindowEquipment, 1, wx.EXPAND |wx.ALL, 5 )
		'''
		# Create buttons
		sizerButtons = wx.BoxSizer( wx.HORIZONTAL )
		self.buttonSave = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerButtons.Add( self.buttonSave, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerButtons.Add( self.buttonCancel, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		MainSizer.Add( sizerButtons, 0, wx.ALIGN_RIGHT, 5 )
		'''
		# Layout panel
		self.SetSizer( MainSizer )
		self.Layout()
		# Connect Events
		textCtrl.Bind( wx.EVT_TEXT, self.textBox_DataChanged )
		#self.buttonSave.Bind( wx.EVT_BUTTON, Kernel.Protect(self.buttonSave_Clicked) )
		#self.buttonCancel.Bind( wx.EVT_BUTTON, Kernel.Protect(self.buttonCancel_Clicked) )
	
	def __del__( self ):
		pass
	
	def textBox_DataChanged( self, event ):
		''' Sets the value in the configuration '''
		data = self.Dictionary[event.GetEventObject()]
		data[2].SetLabel('*')
		Config.set(data[0], data[1], event.GetString())
'''
	def buttonSave_Clicked( self, event ):
		
		msg = wx.MessageBox(u"Settings have been saved, but will not take effect until the editor has been restarted.\n\r\nWould you like to restart now?",
			'Restart Required', wx.YES_NO|wx.ICON_QUESTION)
		if msg == wx.YES:
			# TODO: Implement restart
			pass
		self.Destroy()

	def buttonCancel_Clicked( self, event ):
		self.Destroy()


app = wx.PySimpleApp( 0 )
frame = wx.Frame( None, wx.ID_ANY, 'Configuration Manager', size=(400,300) )
panel = Configuration_Panel( frame, 'C:/Users/Eric/Desktop/ARC/editor/ARCed/src/ARCed.cfg' )
frame.CenterOnScreen()
frame.Show()
app.MainLoop()
'''