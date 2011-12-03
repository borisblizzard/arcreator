
import os
import fnmatch
from Database.ScriptEditor.Script import Script
import Kernel

class Manager(object):

	@staticmethod
	def LoadScripts(dir):
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


	@staticmethod
	def SaveScripts():
		if not Kernel.GlobalObjects.has_key('Scripts'):
			Kernel.Log('Attempted saving of scripts before initialization.', 
				'[ScriptEditor]', False, False)
		else:
			result = True
			scripts = Kernel.GlobalObjects.get_value('Scripts')
			for script in scripts:
				if not script.SaveScript():
					result = False
			return result

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
			count = 0
			total_lines = 0
			total_words = 0
			total_characters = 0
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
