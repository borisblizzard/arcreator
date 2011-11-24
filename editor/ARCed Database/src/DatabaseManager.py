import wx
from Core.Cache import PILCache as Cache
from Core.RMXP import RGSS1_RPG as RPG
from math import ceil
import PIL
import os
import Kernel
from Kernel import Manager as KM

class DatabaseManager(object):

	ARC_FORMAT = False
	
	TEXT_COLOR = wx.Color(241, 243, 248)
	GRADIENT_LEFT = wx.Color(100, 100, 100)
	GRADIENT_RIGHT = wx.Color(60, 60, 60)

	#----------------------------------------------------------------------------------
	@staticmethod
	def RenderImage( glCanvas, filename, hue=0, type='battler'):
		"""Draws the character/battler graphic to the static bitmap.
		
		Arguments:
		glCanvas -- The wxStaticBitmap that will be drawn on
		filename -- The string path to the image to use as the source
		hue -- An integer that represents the degree of color displacement to use
		type -- A string to denote the type of graphic to draw ('character' or 'battler')

		Returns:
		None
		
		"""
		#if type == 'character': folder = '/Graphics/Characters/'
		#elif type == 'battler': folder = '/Graphics/Battlers/'

		try:
			if type == 'character': img = Cache.Character(filename, hue)
			elif type == 'battler': img = Cache.Battler(filename, hue)
		except:
			img = None
		glCanvas.ChangeImage(img)

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
		#wxContainer.SetDoubleBuffered(True)

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
		from ChangeMaximum_Dialog import ChangeMaximum_Dialog
		currentMax = wxList.GetCount()
		digits = len(str(maxAllowed))
		dialog = ChangeMaximum_Dialog(parent, currentMax, 1, maxAllowed)
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
	def ChooseAudio(parent, folder, audio, loops=None):
		"""Creates the Choose Audio dialog
		
		Arguments:
		folder -- The root folder that contains audio files to populate the list
		audio -- The RPG.AudioFile instance that is currently defined
		
		Returns:
		Returns the chosen RPG.AudioFile

		"""
		from ChooseAudio_Dialog import ChooseAudio_Dialog
		dialog = ChooseAudio_Dialog(parent, folder, loops, audio)
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
	def DrawButtonIcon( button, filename, from_resource ):
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
			pilImage = Cache.Icon(filename)
			if pilImage is not None:
				image = wx.EmptyImage(pilImage.size[0], pilImage.size[1])
				image.SetData(pilImage.convert("RGB").tostring())
				image.SetAlphaData(pilImage.convert("RGBA").tostring()[3::4])
				bitmap = wx.BitmapFromImage(image)
			else:
				bitmap = wx.EmptyBitmap(1, 1)
		button.SetBitmapLabel(bitmap)

	#----------------------------------------------------------------------------------
	@staticmethod
	def CreateParameterControls(parent, event, suffix, rowcount=4, defaults=[]):
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
		threshold = len(defaults)
		count = 0
		parameters = defaults
		if DatabaseManager.ARC_FORMAT:
			config = Kernel.GlobalObjects.get_value('ARCed_config')
			parameters.extend(config.getlist('GameSetup', 'Parameters'))
		else:
			parameters.extend(['STR', 'DEX', 'AGI', 'INT'])
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
					if count < threshold:
						label = wx.StaticText( parent, wx.ID_ANY, param)
					else:
						label = wx.StaticText( parent, wx.ID_ANY, param + suffix)
					count += 1
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
		#parent.Layout()
		#parent.SetVirtualSizeHints(-1, -1, parent.GetClientSize().GetWidth() - 32)
		#parent.SetSizer ( mainsizer )
		return objectList

	#----------------------------------------------------------------------------------
	@staticmethod 
	def gcd(num1, num2):
		""" Calculates the greatest common denominator of two numbers"""
		if num1 > num2:
			for i in range(1, num2 + 1):
				if num2 % i == 0 and num1 % i == 0:
					result = i
			return result
		elif num2 > num1:
			for i in range(1, num1 + 1):
				if num1 % i == 0 and num2 % i == 0:
					result = i
			return result
		else:
			result = num1 * num2 / num1
			return result

	#----------------------------------------------------------------------------------
	@staticmethod
	def lcm(num1, num2):
		"""Returns the lowest common multiple of two numbers"""
		result = num1 * num2 / DatabaseManager.gcd(num1, num2)
		return result

	#----------------------------------------------------------------------------------
	@staticmethod
	def CalculateParameter(min, max, speed, level, initLvl, fnlLvl):
		"""Calculates the parameter value of a curve at the passed level"""
		p_range, l_range = max - min, float(fnlLvl - initLvl)
		linear = ceil(min + p_range * ((level - initLvl) / l_range))
		if speed == 0: return linear
		if speed < 0:
		  curve = ceil(min + p_range * (((level - initLvl) / l_range) ** 2))
		else:
		  curve = ceil(max - p_range * (((fnlLvl - level) / l_range) ** 2))
		return ((curve * abs(speed) + linear * (10 - abs(speed))) / 10)
