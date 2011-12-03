import os
import Kernel
#--------------------------------------------------------------------------------------
# Script
#--------------------------------------------------------------------------------------

class Script(object):

	def __init__(self, id, path, readonly=False):
		"""Basic constructor for a Script object"""
		self._readonly = readonly
		self.Id = id
		self.LoadScript(path)
		self.CursorPosition = 0
		self._modified_text = None

	def IsModified( self ):
		"""Returns True/False if text has been modified from original"""
		return self._modified_text != None

	def ApplyChanges( self, save=False ):
		"""Sets the original text to that of the modified text"""
		if self._modified_text is not None:
			self._text = self._modified_text
			self._modified = None
			if save:
				self.SaveScript()

	def GetName( self ):
		"""Returns the name of the script"""
		return self._name[5:]

	def ChangeName(self, name ):
		"""Changes the name of the script, and updates the path as well"""
		self._name = str.join([self._name[:3], name])
		dir = os.path.dirname(self._path)
		self._path = str.join(dir, self._name, '.rb')

	def GetRealName( self ):
		"""Returns the name of the script including the leading indexing numbers"""
		return self._name

	def GetText( self ):
		"""Returns the text of the script as a string"""
		if self._modified_text is not None:
			return self._modified_text
		return self._text

	def SetText( self, text ):
		"""Sets the new string value of the text, but does not apply it permanently"""
		if self._readonly:
			return
		self._modified_text = text

	def GetLines( self ):
		"""Returns a string list of the scripts text broken into lines"""
		if self._modified_text is not None:
			return self._modified_text.splitlines()
		return self._text.splitlines()

	def GetPath( self ):
		"""Returns the full path to the script file"""
		return self._path

	def GetDirectory( self ):
		"""Returns the directory where the script resides"""
		return os.path.dirname(self._path)

	def IsReadOnly( self ):
		"""Returns read-only flag"""
		return self._readonly

	def iterlines( self ):
		"""Iterates over the lines of the script, yielding the index and text of each line"""
		for i, text in enumerate(self._text.splitlines()):
			yield i, text

	def SaveScript( self ):
		"""Saves the script to the path it was loaded from. Returns True if successful"""
		self.ApplyChanges()
		try:
			file = open(self._path, 'wb')
			file.write(self._text)
			file.close()
			return True
		except:
			Kernel.Log(str.format('Failed to save script at {}', path),
			  '[ScriptEditor]', True, True)
		return False

	def LoadScript( self, path ):
		"""Loads the script from path and returns True if successful"""
		try:
			self._path = path
			self._name = os.path.splitext(os.path.basename(path))[0]
			file = open(path, 'rb')
			self._text = file.read()
			file.close()
			return True
		except:
			Kernel.Log(str.format('Failed to load script at {}', path),
			  '[ScriptEditor]', True, True)
		return False