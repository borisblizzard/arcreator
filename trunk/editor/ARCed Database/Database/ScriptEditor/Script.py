import os
import Kernel
#--------------------------------------------------------------------------------------
# Script
#--------------------------------------------------------------------------------------
class Script(object):

	def __init__(self, path, readonly=False):
		"""Basic constructor for a Script object"""
		self._readonly = readonly
		self.LoadScript(path)

	def GetName( self ):
		"""Returns the name of the script"""
		return self._name[3:]

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
		return self._text

	def GetLines( self ):
		"""Returns a string list of the scripts text broken into lines"""
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
			self._name = os.path.split(os.path.basename)[0]
			file = open(path, 'rb')
			self._text = file.read()
			file.close()
			return True
		except:
			Kernel.Log(str.format('Failed to load script at {}', path),
			  '[ScriptEditor]', True, True)
		return False