from RFTLib.Require import *
from RFTLib.Core.Structure import *





__all__ = ("Entry",)





class Entry:
	def init(self):
		# Import module
		import json

		self.json = json



	def load(self, file):
		try:
			# Read file
			data_ = self.json.load(file)
		
		except:
			RFT_Exception.Traceback().print()
			
			# Default
			data_ = {}

		finally:
			if (isinstance(data_, dict)):
				# Convert to struct
				data = RFT_Structure(data_)

			else:
				data = data_


		# Return data
		return data


