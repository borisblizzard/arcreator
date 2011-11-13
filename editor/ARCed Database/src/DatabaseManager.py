import wx
from Core.Cache import PILCache as Cache
from Core.RMXP import RGSS1_RPG as RPG
import os
import Kernel
from Kernel import Manager as KM

class DatabaseManager(object):

	ARC_FORMAT = False
	
	TEXT_COLOR = wx.Color(241, 243, 248)
	GRADIENT_LEFT = wx.Color(100, 100, 100)
	GRADIENT_RIGHT = wx.Color(60, 60, 60)

	_ALPHA_BRUSH = None

	# TODO: Remove this. Use RTP path from Kernel via the Cache
	xp_rtp = "%COMMONPROGRAMFILES%/Enterbrain/RGSS/Standard"
	RTPDir = os.path.normpath(os.path.expandvars(xp_rtp))

	#----------------------------------------------------------------------------------
	@staticmethod
	def DrawBitmap( staticBitmap, filename, hue=0, type='battler', rows=1, columns=1, tile=(0,0)):
		"""Draws the character/battler graphic to the static bitmap.
		
		Arguments:
		staticBitmap -- The wxStaticBitmap that will be drawn on
		filename -- The string path to the image to use as the source
		hue -- An integer that represents the degree of color displacement to use
		type -- A string to denote the type of graphic to draw ('character' or 'battler')
		rows -- The number of rows that the image uses
		columns -- The number of columns the image uses
		tile -- A two element tuple that defines the displayed tile that will be drawn

		Returns:
		None
		
		"""
		if DatabaseManager._ALPHA_BRUSH is None:
			DatabaseManager._ALPHA_BRUSH = wx.Brush(wx.Color(228, 228, 228), wx.SOLID)
		if type == 'character':
			# TODO: Load data from cache
			srcBmp = wx.Bitmap(DatabaseManager.RTPDir + '/Graphics/Characters/' + filename + '.png')
			#srcBmp = Cache.Character(filename, hue)
		elif type == 'battler':
			# TODO: Load data from cache
			srcBmp = wx.Bitmap(DatabaseManager.RTPDir + '/Graphics/Battlers/' + filename + '.png')
			#srcBmp = Cache.Battler(filename, hue)
		tile_width = srcBmp.GetWidth() / columns
		tile_height = srcBmp.GetHeight() / rows
		srcDC = wx.MemoryDC()
		srcDC.Clear()
		srcDC.SelectObjectAsSource(srcBmp)
		cSize = [48, 64]
		if tile_width > cSize[0]: cSize[0] = tile_width + 8
		if tile_height > cSize[1]: cSize[1] = tile_height + 8
		destBmp = wx.EmptyBitmap(cSize[0], cSize[1])
		destDC = wx.MemoryDC()
		destDC.SelectObject(destBmp)
		destDC.SetBackground(DatabaseManager._ALPHA_BRUSH)
		destDC.Clear()
		x = tile_width * tile[0]
		y = tile_height * tile[1]
		destX = (cSize[0] - tile_width) / 2
		destY = (cSize[1] - tile_height) / 2
		destDC.Blit(destX, destY, tile_width, tile_height, srcDC, x, y, wx.COPY, True)
		destDC.SelectObject(wx.NullBitmap)
		staticBitmap.SetSize(destBmp.GetSize())
		staticBitmap.SetBitmap(destBmp)
		del (destDC)
		del (srcDC)
		del (destBmp)

	#----------------------------------------------------------------------------------
	@staticmethod
	def DrawHeaderBitmap( staticBitmap, text, font=None, textcolor=None, 
			gradient1=None, gradient2=None ):
		"""Draws text on a static bitmap control and applies a gradient color fill
		
		Arguments:
		staticBitmap -- The wxStaticBitmap that will be drawn on
		text -- The string of text to draw
		font -- The wxFont to use for the text
		textcolor -- The wxColor that will be used to draw the text
		gradient1 -- A wxColor that will be the gradient color on the left
		gradient2 -- A wxColor that will be the gradient color on the right
		
		Returns:
		None

		"""
		memDC = wx.MemoryDC()
		bmpsize = staticBitmap.GetClientSize()
		bmp = wx.EmptyBitmap(bmpsize[0], bmpsize[1])
		memDC.SelectObject(bmp)
		memDC.Clear()	
		if textcolor == None: textcolor = DatabaseManager.TEXT_COLOR
		if gradient1 == None: gradient1 = DatabaseManager.GRADIENT_LEFT
		if gradient2 == None: gradient2 = DatabaseManager.GRADIENT_RIGHT
		if font == None: font = wx.Font(10, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, 
					wx.FONTWEIGHT_NORMAL, faceName='Ethnocentric') # TODO: Change this?
		memDC.SetFont(font)	
		memDC.SetTextForeground(textcolor)
		textsize = memDC.GetTextExtent(text)
		x = (bmpsize[0] - textsize[0]) / 2
		y = (bmpsize[1] - textsize[1]) / 2
		rect = wx.Rect(0, 0, bmpsize[0], bmpsize[1])
		memDC.GradientFillLinear(rect, gradient1, gradient2)
		memDC.DrawText(text, x, y)
		staticBitmap.SetBitmap(bmp)
		del (memDC)
		del (bmp)

	#----------------------------------------------------------------------------------
	@staticmethod
	def GetAddSubImageList():
		""" Creates a wxImageList for a plus/minus/empty check box and returns it.
		
		Returns:
		A wxImageList of plus/minus/empty check bitmaps
		
		"""
		icons = KM.get_component('IconManager').object
		imageList = wx.ImageList(14, 12)
		imageList.Add(icons.getBitmap('check_empty'))
		imageList.Add(icons.getBitmap('check_plus'))
		imageList.Add(icons.getBitmap('check_minus'))
		return imageList

	#----------------------------------------------------------------------------------
	@staticmethod
	def GetNormalCheckImageList():
		icons = KM.get_component('IconManager').object
		imageList = wx.ImageList(14, 12)
		imageList.Add(icons.getBitmap('check_empty'))
		imageList.Add(icons.getBitmap('check_green'))
		return imageList

	#----------------------------------------------------------------------------------
	@staticmethod
	def FixedIndex( index ):
		"""Returns the correct starting index for game data structure depending on the current format

		Arguments:
		index -- An integer to format
		
		Returns:
		An integer formatted to to be compatible with current game data structure
		
		"""
		if DatabaseManager.ARC_FORMAT: return index
		else: return index + 1

	#----------------------------------------------------------------------------------
	@staticmethod
	def FillControl(wxContainer, dataSource=[], digits=3, defaults=[], 
			start=0, fixed=True, clear=True):
		"""Fills the control with items from the data source and numbers them.

		Arguments:
		wxContainer -- An instance of control derived from wxControlWithItems
		dataSource -- A list of items that responds to ".name"
		digits -- he number of digits that will be filled with 0's for numbering
		defaults -- A list of items that will be in the control by default
		start -- The beginning index that is read from the data source
		fixed -- Bool that determines of the index will be adjusted'
		clear -- Bool to determine if the control's items will be cleared before adding

		Returns:
		None

		"""
		if clear:
			wxContainer.Clear()
		if fixed:
			start = DatabaseManager.FixedIndex(start)
		defaults.extend([
			''.join([str(i).zfill(digits), ': ',
		    dataSource[i].name]) for i in xrange(start, len(dataSource))])
		wxContainer.AppendItems(defaults)
	
	#----------------------------------------------------------------------------------
	@staticmethod
	def FillWithoutNumber(wxContainer, dataSource=[], defaults=[],
			start=0, fixed=True, clear=True):
		"""Fills the control with items from the data source without numbering.

		Arguments:
		wxContainer -- An instance of control derived from wxControlWithItems
		dataSource -- A list of items that responds to ".name"
		defaults -- A list of items that will be in the control by default
		start -- The beginning index that is read from the data source
		fixed -- Bool that determines of the index will be adjusted'
		clear -- Bool to determine if the control's items will be cleared before adding

		Returns:
		None

		"""
		if clear:
			wxContainer.Clear()
		if fixed:
			start = DatabaseManager.FixedIndex(start)
		defaults.extend([dataSource[i].name for i in xrange(start, len(dataSource))])
		wxContainer.AppendItems(defaults)

	#----------------------------------------------------------------------------------
	@staticmethod
	def ChangeDataCapacity(parent, wxList, data, maxAllowed ):
		"""Creates the Change Maximum dialog and changes the capacity of data
		
		Arguments:
		parent -- The parent that will be assigned to the dialog
		wxList -- The wxList that is associated with the data
		data -- A list of RPG data classes
		maxAllowed -- The maximum capacity allowed
		
		Returns:
		None
		
		"""
		from ARCedChangeMaximum_Dialog import ARCedChangeMaximum_Dialog
		currentMax = wxList.GetCount()
		digits = len(str(maxAllowed))
		dialog = ARCedChangeMaximum_Dialog(parent, currentMax, 1, maxAllowed)
		if dialog.ShowModal() == wx.ID_OK:
			newMax = dialog.spinCtrlMaximum.GetValue()
			if newMax != currentMax: 
				if newMax > currentMax:
					data.extend([None for i in xrange(newMax - currentMax)])
					start = currentMax + 1
					labels = [
						''.join([str(start + i).zfill(digits), ':'])
						for i in xrange(newMax - currentMax)]
					wxList.AppendItems(labels)
				else:
					index = wxList.GetSelection()
					del data[newMax + 1:currentMax]
					wxList.SetItems(wxList.GetItems()[0:newMax])
					if DatabaseManager.FixedIndex(index) >= newMax:
						index = newMax - 1
					wxList.SetSelection(index)
		dialog.Destroy()

	#----------------------------------------------------------------------------------
	@staticmethod
	def ChooseGraphic(folder, current, hue, huechange=True):
		"""Creates the dialog for selecting a graphic
		
		Arguments:
		folder -- The root directory that contains image files to populate the list.
		current -- The string name of the currently chosen graphic
		hue -- The hue of the current graphic (0...360)
		huechange -- Bool to determine if changing the hue is permitted
		
		Returns:
		Returns a three element tuple. The first and second element are the filename
		and hue of the selected graphic, and the third is a bool flag denoting if
		the values have been changed.
		
		"""
		pass

	#----------------------------------------------------------------------------------
	@staticmethod
	def ChooseAudio(parent, folder, audio, loops=None):
		"""Creates the Choose Audio dialog
		
		Arguments:
		folder -- The root folder that contains audio files to populate the list
		audio -- The RPG.AudioFile instance that is currently defined
		
		Returns:
		Returns the chosen RPG.AudioFile

		"""
		from ARCedChooseAudio_Dialog import ARCedChooseAudio_Dialog
		dialog = ARCedChooseAudio_Dialog(parent, folder, loops, audio)
		if dialog.ShowModal() == wx.ID_OK:
			audio = dialog.GetAudio()
		dialog.Destroy()
		return audio

	#----------------------------------------------------------------------------------
	@staticmethod
	def UpdateObjectName(object, name, listbox, digits):
		"""Updates the selected object's name and updates the associated wxListBox

		Arguments:
		object -- Then object. Must respond to ".name".
		name -- The string name of the object
		listbox -- The associated listbox for this object
		digits -- The number of digits used for the numbering

		Returns:
		None

		"""
		index = listbox.GetSelection()
		object.name = name
		listbox.SetString(index, 
			''.join([str(DatabaseManager.FixedIndex(index)).zfill(digits), ': ', name]))

	#----------------------------------------------------------------------------------
	@staticmethod
	def ChangeSkillStates( object, index, value ):
		"""Changes the skill's add/remove state, and updates the custom check list

		Arguments:
		object -- The RPG game object to change. Must respond to "minus_state_set" and "plus_state_set".
		index -- The index of the state
		value -- The values of the custom check list state

		Returns:
		None

		"""
		if index is None:
			return
		state_id = DatabaseManager.FixedIndex(index)
		if value == 0:
			if state_id in object.minus_state_set: 
				object.minus_state_set.remove(state_id)
			elif state_id in object.plus_state_set: 
				object.plus_state_set.remove(state_id)
		if value == 1:
			if state_id in object.minus_state_set: 
				object.minus_state_set.remove(state_id)
			object.plus_state_set.append(state_id)
		if value == -1:
			if state_id in object.plus_state_set: 
				object.plus_state_set.remove(state_id)
			object.minus_state_set.append(state_id)

	#----------------------------------------------------------------------------------
	@staticmethod
	def DrawButtonIcon(button, filename, from_resource):
		"""Draws a bitmap on a button from an embedded resource or file

		Arguments:
		button -- A wxBitmapButton instance to draw on
		filename -- Either the filename if a game icon or the embedded resource name
		from_resource -- Bool flag to denote if bitmap loads from embedded resource

		Returns:
		None

		"""
		if from_resource:
			icons = KM.get_component('IconManager').object
			bitmap = icons.getBitmap(filename)
		else:
			# TODO: Use Cache instead
			path = ''.join([DatabaseManager.RTPDir, '/Graphics/Icons/', filename, '.png'])
			bitmap = wx.Bitmap(path)
			#bitmap = Cache.Icon(filename)
		button.SetBitmapLabel(bitmap)

	#----------------------------------------------------------------------------------
	@staticmethod
	def TestSFX( audioFile ):
		# TEMP METHOD
		from pygame import mixer as Mixer
		Mixer.init()
		path = ''.join([DatabaseManager.RTPDir, '/Audio/SE/', audioFile.name, '.ogg'])
		player = Mixer.Sound(path)
		player.set_volume(audioFile.volume / 100.0)
		player.play()

	#----------------------------------------------------------------------------------
	@staticmethod
	def AddParameterSpinCtrls(parent, event, suffix, rowcount=4):
		"""Creates spin controls for the passed parameters, adds them to the parent
		control, and returns an array of the created wxSpinCtrl objects.

		Arguments:
		parent -- The parent control to add the spin controls to
		event -- A function to bind to each control
		suffix -- A string suffix to append to the names of each parameter
		rowcount -- The number of controls to add to each row

		Returns:
		A list of wxSpinCtrl objects

		"""
		if DatabaseManager.ARC_FORMAT:
			config = Kernel.GlobalObjects.get_value('ARCed_config')
			parameters = config.getlist('Misc', 'Parameters')
		else:
			parameters = ['STR', 'DEX', 'AGI', 'INT']
		objectList = []
		mainsizer = parent.GetSizer()
		rows = [parameters[i:i+rowcount] for i in xrange(0, len(parameters), rowcount)]
		percent = 100 / rowcount
		# Iterate through each of the rows and create the controls
		for row in rows:
			labelsizer = wx.BoxSizer(wx.HORIZONTAL)
			spinsizer = wx.BoxSizer(wx.HORIZONTAL)
			n = len(row)
			if n < rowcount:
				row.append(None)
				proportion = percent * (rowcount - n)
			for param in row:
				if param != None:
					label = wx.StaticText( parent, wx.ID_ANY, param + suffix)
					label.Wrap( -1 )
					labelsizer.Add( label, percent, wx.ALL, 5 )
					spinctrl = wx.SpinCtrl( parent, wx.ID_ANY, wx.EmptyString, style=wx.SP_ARROW_KEYS|wx.SP_WRAP)
					spinctrl.Bind(wx.EVT_SPINCTRL, Kernel.Protect(event))
					objectList.append(spinctrl)
					spinsizer.Add( spinctrl, percent, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
				else:
					# Create a dummy filler
					dummy = wx.StaticText( parent, wx.ID_ANY, '')
					dummy.Wrap(-1)
					labelsizer.Add(dummy, proportion, wx.ALL, 5)
					spinsizer.Add(dummy, proportion, wx.ALL, 5)
			mainsizer.Add( labelsizer, 0, wx.EXPAND, 5 )
			mainsizer.Add( spinsizer, 0, wx.EXPAND, 5 )
		return objectList
