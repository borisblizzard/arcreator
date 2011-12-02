#--------------------------------------------------------------------------------------
# Script
#--------------------------------------------------------------------------------------
class Script(object):

	def __init__(self, name, text, path, readonly=False):
		self.Name = name
		self.Text = text
		self.Path = path
		self.ReadOnly = readonly