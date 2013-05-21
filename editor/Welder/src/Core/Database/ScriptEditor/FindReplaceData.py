#--------------------------------------------------------------------------------------
# FindReplaceData
#--------------------------------------------------------------------------------------

class FindReplaceData(object):
	
	def __init__(self):
		"""Basic constructor for FindReplaceData"""
		self.SearchString = ['', '']
		self.ReplaceString = ''
		self.Scope = 0
		self.MatchCase = False
		self.WholeWord = False
		self.SearchUp = False
		self.RegExSearch = False
		self.RegExMode = 0