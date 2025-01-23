from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Structure import *
from RFTLib.Core.Exception import *





__all__ = ("RFT_Rypple_Process",)





class RFT_Rypple_Process(RFT_Object):
	popout_:bool = False
	processes_:list = []


	@classmethod
	def run(self, *args: tuple | list):
		if (len(args) == 1):
			args = shlex.split(args[0])

		try:
			# Create new subprocess attached to main process
			process = subprocess.Popen(
				args,
				creationflags = subprocess.CREATE_NEW_CONSOLE if self.popout_ else 0x00
			)
		except:
			RFT_Exception("Failed to start.", RFT_Exception.ERROR).print()

		else:
			self.processes_.append(
				process
			)

		return self


	@classmethod
	def wait(self):
		for p in self.processes_:
			p.wait()

		self.processes_.clear()
		return self


	@classmethod
	def popout(self, value:bool = True):
		self.popout_ = value
		return self


