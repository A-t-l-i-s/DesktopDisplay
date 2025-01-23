from RFTLib.Require import *
from RFTLib.Core.Structure import *





__all__ = ("Entry",)





class Entry:
	def init(self):
		# Import module
		import yaml

		self.yaml = yaml



	def load(self, file):
		try:
			# Read file
			data_ = self.yaml.load(
				file,
				Loader = self.yaml.FullLoader
			)

			if (data_ == None):
				data_ = {}
		
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


