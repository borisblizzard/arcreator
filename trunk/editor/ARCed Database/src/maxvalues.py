import ConfigParser
import RPGutil as util

class DatabaseLimits():

	def __init__(self, iniPath):
		""" 
		Parses an .ini file creating, dictionary attributes for each section 
		whose keys are the options and values are the corresponding integers
		"""
		config = ConfigParser.SafeConfigParser()
		config.read(util.opj(iniPath))
		for section in config.sections():
			data = {}
			for option in config.options(section):
				data[option] = config.getint(section, option)
			setattr(self.__class__, section, data)