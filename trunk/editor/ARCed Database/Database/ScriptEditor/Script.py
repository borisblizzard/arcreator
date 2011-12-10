import os
import Kernel
from codecs import open as utf8_open
#--------------------------------------------------------------------------------------
# Script
#--------------------------------------------------------------------------------------

class Script(object):

	def __init__(self, id, path, readonly=False):
		"""Basic constructor for a Script object"""
		self._readonly = readonly
		self.Id = id
		Kernel.Protect(self.LoadScript)(path)
		self.CursorPosition = 0
		self._modified_text = None
		self._modified_name = None

	def CompareStrings(self, str1, str2):
		"""Ensures both strings are unicode strings in UTF-8 format and compares them"""
		if not type(str1) == unicode:
			str1 = str1.decode('utf-8')
		if not type(str2) == unicode:
			str2 = str2.decode('utf-8')
		return str1 == str2

	def IsModified( self ):
		"""Returns True/False if text has been modified from original"""
		if self._modified_text is not None:
			same = self.CompareStrings(self._text, self._modified_text)
			return not same
		return False

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
		"""Sets the new name of the script"""
		if name != self._name:
			self._modified_name = name

	def GetPath( self ):
		"""Returns the full path to the script file"""
		return self._path

	def SetPath( self, path ):
		"""Sets a new path for the script to save/load from"""
		self._path = path

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
		return self.GetLines().splitlines()

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
		"""Loads the script from path"""
		self._path = path
		self._name = os.path.splitext(os.path.basename(path))[0][5:]
		file = utf8_open(path, 'rb', 'utf-8')
		self._text = file.read()
		file.close()

	def _WriteToDisk(self, path):
		"""Writes the file to disk using UTF-8 encoding"""
		try:
			file = open(path, 'wb')
			file.write('\xef\xbb\xbf')
			file.write(self.GetText().encode('utf-8'))
			file.close()
			return True
		except Exception:
			return False

	def SaveScript( self, id ):
		"""Performs required IO action depending on text and name modification"""
		new_filename = ''.join([str(id).zfill(4), '-', self.GetName(), '.rb'])
		old_filename = self.GetFileName()
		name_changed = new_filename != old_filename
		result = True
		# If text has not been modified
		if not self.IsModified():
			# If name has been changed
			if name_changed:
				path = os.path.join(self.GetDirectory(), new_filename)
				# If old file is still present, rename to new name
				if os.path.exists(self.GetPath()):
					os.rename(self.GetPath(), path)
				else:
					# Create new file if old one was not found
					result = self._WriteToDisk(path)
				self.SetPath(path)
				self.ApplyChanges()
		# If text has been modified
		else:
			# Remove old file if exists
			if name_changed and os.path.exists(self.GetPath()):
				os.remove(self.GetPath())
				self.SetPath(os.path.join(self.GetDirectory(), new_filename))
			# Set the new text and name
			self.ApplyChanges()
			result = self._WriteToDisk(self.GetPath())
		return result