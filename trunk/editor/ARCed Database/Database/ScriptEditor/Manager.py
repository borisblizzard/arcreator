import os
import wx 
import codecs
import Kernel
#--------------------------------------------------------------------------------------
# Manager
#--------------------------------------------------------------------------------------

class Manager(object):

	#----------------------------------------------------------------------------------
	@staticmethod
	def LoadScripts(dir):
		"""Loads all scripts and stores them in memory

		Arguments:
		dir -- The directory where the scripts are located

		Returns:
		None

		"""
		import fnmatch
		from Database.ScriptEditor.Script import Script
		# TODO: Include internal scripts as read-only entries?
		paths = []
		for file in os.listdir(dir):
			if fnmatch.fnmatch(file, '*.rb'):
				paths.append(os.path.join(dir, file))
		scripts = [Script(i, path, False) for i, path in enumerate(sorted(paths))]
		if Kernel.GlobalObjects.has_key('Scripts'):
			Kernel.GlobalObjects.set_value('Scripts', scripts)
		else:
			Kernel.GlobalObjects.request_new_key('Scripts', 'CORE', scripts)

	#----------------------------------------------------------------------------------
	@staticmethod
	def SaveScripts():
		"""Iterates over each script and saves the it to disk

		Arguments:
		None

		Returns:
		Bool value if all scripts were saved successfully

		"""
		# If scripts are not loaded into memory, do not bother saving.
		if not Kernel.GlobalObjects.has_key('Scripts'):
			return False

		try:
			pass
			# TODO: Apply deleting scripts marked for deletion here
		except:
			Kernel.Log('Failed to delete all scripts marked for deletion', 
			  ['Script Editor'], True, False)
		result = True
		scripts = Kernel.GlobalObjects.get_value('Scripts')
		for i, script in enumerate(scripts):
			# TODO: Apply escape sequences for invalid characters in the filename
			filename = str.format('{0}-{1}.rb', str(i).zfill(4), script.GetName())
			original_path = script.GetPath()
			isChanged = filename != script.GetFileName()
			# If script text has not changed...
			if not script.IsModified():
				# If filename has changed, simply rename
				if isChanged:
					new_path = os.path.join(script.GetDirectory(), filename)
					try:
						os.rename(original_path, new_path)
						os.path.join(script.GetDirectory(), filename)
						script.SetPath(new_path)
					except:
						Kernel.Log(str.format('Failed to rename \"{0}\" to \"{1}\"', 
							 os.path.basename(original_path), filename),
							'[Script Editor]', True, False)
						result = False
				# Do nothing if no modifications or renaming took place
				continue
			# Apply modifications of script text and overwrite original text
			script.ApplyChanges()
			if isChanged:
				# If path has changed, remove old path
				try:
					os.remove(original_path)
				except:
					Kernel.Log(str.format('Failed to remove {}.', original_path),
						'[Script Editor]', True, False)
				# Set the scripts new path
				path = os.path.join(script.GetDirectory(), filename)
				script.SetPath(path)
			try:
				file = open(script.GetPath(), 'wb')
				file.write(codecs.BOM_UTF8)
				file.write(script.GetText().encode('utf-8'))
				file.close()
			except:
				message = str.format('Script at path {} failed to save.\nPlease ensure there are sufficient privileges to write data to the location', script.GetPath()) 
				Kernel.Log(message, '[Script Editor]', True, False)
				result = False
		return result

	#----------------------------------------------------------------------------------
	@staticmethod
	def GetScriptStatistics(whitespace=True):
		"""Returns statistics of the combined scripts

		Arguments:
		whitespace -- True or False if whitespace will be included in count

		Returns:
		A four element tuple whose values are as follows:
			(Number of Scripts, Total Lines, Total Words, Total Characters)

		"""
		if not Kernel.GlobalObjects.has_key('Scripts'):
			return (0, 0, 0, 0)
		else:
			scripts = Kernel.GlobalObjects.get_value('Scripts')
			count = total_lines = total_words = total_characters = 0
			for script in scripts:
				count += 1
				lines = script.GetLines()
				if not whitespace:
					lines = []
					for line in script.GetLines():
						stripped = line.strip()
						if stripped == '' or stripped.startswith('#'):
							continue
						lines.append(line)
				else:
					lines = script.GetLines()
				total_lines += len(lines)
				for line in lines:
					total_characters += len(line)
					total_words += len(line.split())
			return (count, total_lines, total_words, total_characters)

	#----------------------------------------------------------------------------------
	@staticmethod 
	def GetUserSettings():
		"""Returns the settings defined in the configuration
		
		Arguments:
		None
		
		Returns:
		A list of format strings for the respective styles
		
		"""
		styles = Manager.GetStyles()
		cfg = Kernel.GlobalObjects.get_value('ARCed_config').get_section('ScriptEditor')
		settings = [cfg.get(styles[1]) for style in styles]
		return settings

	#----------------------------------------------------------------------------------
	@staticmethod
	def GetDefaultSettings ():
		"""Returns the internal default settings
		
		Arguments:
		None
		
		Returns:
		A list of format strings for the respective styles
		
		"""
		# Get the default font faces for font families
		mono = wx.Font(10, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		roman = wx.Font(10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL)

		# TODO: Remove
		mono.SetFaceName('Consolas')

		faces = { 'mono' : mono.GetFaceName(),
				  'roman' : roman.GetFaceName(),
			      'size' : 10,
			      'size2' : 8
				}
		settings = [
					"face:%(mono)s,size:%(size)d" % faces, # Default
					"back:#C0C0C0,face:%(mono)s,size:%(size2)d" % faces, # Line Numbers
					"face:%(mono)s" % faces, # Control Character
					"fore:#FFFFFF,back:#0000FF,bold", # Brace Light
					"fore:#000000,back:#FF0000,bold", # Brace Bad
					"fore:#008000,face:%(mono)s,size:%(size)d" % faces, # Comment Block
					"fore:#008000,face:%(mono)s,size:%(size)d" % faces, # Comment
					"fore:#800000,face:%(mono)s,size:%(size)d" % faces, # Numbers
					"fore:#800080,italic,face:%(roman)s,size:%(size)d" % faces, # Double-Quoted Strings
					"fore:#C80080,italic,face:%(roman)s,size:%(size)d" % faces, # Single-Quoted Strings
					"fore:#0000FF,bold,size:%(size)d" % faces, # Keywords
					"fore:#000000,bold,size:%(size)d" % faces, # Class Name
					"fore:#000000,bold,size:%(size)d" % faces, # Module Name
					"fore:#000000,bold,size:%(size)d" % faces, # Method Name
					"fore:#2B91AF,bold,size:%(size)d" % faces, # Operators
					"fore:#000000,face:%(mono)s,size:%(size)d" % faces, # Normal 
					"fore:#000000,face:%(mono)s,size:%(size)d" % faces, # Global Variable
					"fore:#000000,face:%(mono)s,size:%(size)d" % faces, # Instance Variable
					"fore:#000000,face:%(mono)s,size:%(size)d" % faces, # Class Variable
					"fore:#9370DB,face:%(mono)s,size:%(size)d" % faces, # Regular Expressions
					"fore:#000000,face:%(mono)s,size:%(size)d" % faces, # Symbol
					"fore:#808080,face:%(mono)s,size:%(size)d" % faces, # Backticks
					"fore:#000000,face:%(mono)s,size:%(size)d" % faces, # Data Section
					"fore:#FF0000,face:%(mono)s,bold,size:%(size)d" % faces # Error
				]
		return settings

	#----------------------------------------------------------------------------------
	@staticmethod
	def GetStyles():
		"""Returns a list of styles for the Scintilla control
		
		Arguments:
		None
		
		Returns:
		A list of 2 element tuples, the first element is the constant for the setting,
		and the second element is the string name of the key in the configuration
		
		"""
		import wx.stc as stc
		styles = [
					(stc.STC_STYLE_DEFAULT, 'global_default'),		
					(stc.STC_STYLE_LINENUMBER, 'line_number'),
					(stc.STC_STYLE_CONTROLCHAR, 'control_char'),	
					(stc.STC_STYLE_BRACELIGHT, 'brace_light'),
					(stc.STC_STYLE_BRACEBAD, 'brace_bad'),		
					(stc.STC_ST_COMMENT, 'comment_block'),			
					(stc.STC_RB_COMMENTLINE, 'comment_line'),
					(stc.STC_RB_NUMBER, 'numbers'),			
					(stc.STC_RB_STRING, 'double_quote_string'),
					(stc.STC_RB_CHARACTER, 'single_quote_string'),			
					(stc.STC_RB_WORD, 'keywords'),
					(stc.STC_RB_CLASSNAME, 'class_name'),			
					(stc.STC_RB_MODULE_NAME, 'module_name'),
					(stc.STC_RB_DEFNAME, 'method_name'),			
					(stc.STC_RB_OPERATOR, 'operators'),
					(stc.STC_RB_IDENTIFIER, 'normal_text'),		
					(stc.STC_RB_GLOBAL, 'global_variables'),
					(stc.STC_RB_INSTANCE_VAR, 'instance_variables'),		
					(stc.STC_RB_CLASS_VAR, 'class_variables'),
					(stc.STC_RB_REGEX, 'regex'),				
					(stc.STC_RB_SYMBOL, 'symbols'),
					(stc.STC_RB_BACKTICKS, 'backticks'),			
					(stc.STC_RB_DATASECTION, 'data_sections'),
					(stc.STC_RB_ERROR, 'errors')
				]
		return styles

	#----------------------------------------------------------------------------------
	@staticmethod 
	def ApplyUserSettings( scriptcontrol ):
		"""Applies user-defined settings to the control
		
		Arguments:
		scriptcontrol -- A wx.stc.StyledTextCtrl instance
		
		Returns:
		None
		
		"""
		default = Manager.GetDefaultSettings()
		styles = Manager.GetStyles()
		cfg = Kernel.GlobalObjects.get_value('ARCed_config').get_section('ScriptEditor')
		for style in styles:
			try:
				setting = cfg.get(style[1])
				scriptcontrol.StyleSetSpec(style[0], setting)
			except:
				scriptcontrol.StyleSetSpec(style[0], default[i])
				Kernel.Log(str.format('Style setting \"{}\" is malformed/missing and the default value will be used', styles[i][1]), 
					'[Script Editor]', True, False)
		scriptcontrol.SetTabWidth(int(cfg.get('tab_width')))
		scriptcontrol.SetEdgeColumn(int(cfg.get('edge_column')))
		scriptcontrol.SetCaretLineVisible(cfg.get('show_caret').lower() == 'true')
		scriptcontrol.SetCaretForeground(Manager.ParseColor(cfg.get('caret_fore')))
		scriptcontrol.SetCaretLineBack(Manager.ParseColor(cfg.get('caret_back')))
		scriptcontrol.SetCaretLineBackAlpha(int(cfg.get('caret_alpha')))
		scriptcontrol.SetIndentationGuides(cfg.get('indent_guides').lower() == 'true')

	#----------------------------------------------------------------------------------
	@staticmethod 
	def ParseColor(string):
		"""Parses the color string and returns the wx.Colour instance"""
		if string.startswith('#'):
			string = string[1:]
		if len(string) < 6:
			string = string.zfill(6)
		return wx.Colour(int(string[:2], 16), int(string[2:4], 16), int(string[4:6], 16))

	#----------------------------------------------------------------------------------
	@staticmethod 
	def ApplyDefaultSettings( scriptcontrol ):
		"""Applies default settings to the control
		
		Arguments:
		scriptcontrol -- A wx.stc.StyledTextCtrl instance
		
		Returns:
		None
		
		"""
		default = Manager.GetDefaultSettings()
		styles = Manager.GetStyles()
		cfg = Kernel.GlobalObjects.get_value('ARCed_config').get_section('ScriptEditor')
		for i in xrange(len(default)):
			scriptcontrol.StyleSetSpec(styles[i][0], default[i])
			cfg.set(styles[i][1], default[i])
		scriptcontrol.SetTabWidth(2)
		scriptcontrol.SetCaretLineVisible(True)
		scriptcontrol.SetCaretLineBack(wx.Colour(0, 0, 0))
		scriptcontrol.SetCaretForeground(wx.Colour(40, 40, 40))
		scriptcontrol.SetCaretLineBackAlpha(CARET_ALPHA)
		scriptcontrol.SetIndentationGuides(40)
		scriptcontrol.SetEdgeColumn(80)