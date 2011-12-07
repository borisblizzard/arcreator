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
		self._modified_name = None

	def IsModified( self ):
		"""Returns True/False if text has been modified from original"""
		if self._modified_text is None:
			return False
		return self._text != self._modified_text

	def ApplyChanges( self ):
		"""Sets the original text to that of the modified text"""
		if self._modified_text is not None:
			self._text = self._modified_text
			self._modified_text = None
		if self._modified_name is not None:
			self._name = self._modified_name 
			self._modified_name = None

	def GetName( self ):
		"""Returns the name of the script"""
		if self._modified_name is not None:
			return self._modified_name
		return self._name

	def GetFileName( self ):
		"""Returns the name of the script including the leading indexing numbers"""
		return os.path.basename(self.GetPath())

	def ChangeName( self, name ):
		if name != self._name:
			self._modified_name = name

	def GetText( self ):
		"""Returns the text of the script as a string"""
		if self._modified_text is not None:
			return self._modified_text
		return self._text

	def SetText( self, text ):
		"""Sets the new string value of the text, but does not apply it permanently"""
		if self._readonly:
			return
		if text != self.GetText():
			self._modified_text = text

	def GetLines( self ):
		"""Returns a string list of the scripts text broken into lines"""
		if self._modified_text is not None:
			return self._modified_text.splitlines()
		return self._text.splitlines()

	def GetPath( self ):
		"""Returns the full path to the script file"""
		return self._path

	def SetPath( self, path ):
		"""Sets a new path for the script to save/load from"""
		self._path = path

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

	def LoadScript( self, path ):
		"""Loads the script from path and returns True if successful"""
		try:
			self._path = path
			self._name = os.path.splitext(os.path.basename(path))[0][5:]
			file = open(path, 'rb')
			self._text = file.read()
			file.close()
			return True
		except:
			Kernel.Log(str.format('Failed to load script at {}', path),
			  '[ScriptEditor]', True, True)
		return False

	def SaveScript( self, id ):
		import codecs
		filename = ''.join([str(id).zfill(4), '-', self.GetName(), '.rb'])
		if filename != self.GetFileName():
			os.remove(self.GetPath())
			self.SetPath(os.path.join(self.GetDirectory(), filename))
		self.ApplyChanges()
		file = open(self.GetPath(), 'wb')
		file.write(codecs.BOM_UTF8)
		file.write(self.GetText().encode('utf-8'))
		file.close()