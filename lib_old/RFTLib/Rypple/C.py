from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Structure import *





__all__ = ("RFT_Rypple_C",)





class RFT_Rypple_C(RFT_Object):
	inFile_:str = None
	outFile_:str = None

	static_:bool = False
	shared_:bool = False
	ui_:bool = False

	includePath_:list = []
	libraryPath_:list = []

	library_:list = []
	version_:str = None

	bit_:int = None
	compression_:int = None

	define_:dict = {}

	args_:list = []
	exe_:str = "gcc"


	@classmethod
	def inFile(self, file:str):
		self.inFile_ = file
		return self

	@classmethod
	def outFile(self, file:str):
		self.outFile_ = file
		return self


	@classmethod
	def static(self, value:bool = True):
		self.static_ = value
		return self

	@classmethod
	def shared(self, value:bool = True):
		self.shared_ = value
		return self

	@classmethod
	def ui(self, value:bool = True):
		self.ui_ = value
		return self


	@classmethod
	def includePath(self, path:str | Path):
		self.includePath_.append(path)
		return self

	@classmethod
	def libraryPath(self, path:str | Path):
		self.libraryPath_.append(path)
		return self

	@classmethod
	def library(self, name:str):
		self.library_.append(name)
		return self


	@classmethod
	def version(self, name:str):
		self.version_ = name
		return self


	@classmethod
	def bit(self, value:int):
		self.bit_ = value
		return self

	@classmethod
	def compression(self, value:int):
		self.compression_ = value
		return self


	@classmethod
	def define(self, key:str, value:str):
		self.define_[key] = value


	@classmethod
	def add(self, name:str):
		self.args_.append(name)
		return self



	@classmethod
	def done(self):
		args = [self.exe_]

		if (self.inFile_):
			args.append(self.inFile_)

		if (self.outFile_):
			args.append(f"-o{self.outFile_}")


		if (self.static_):
			args.append("-static")

		if (self.shared_):
			args.append("-shared")

		if (self.ui_):
			args.append("-mwindows")


		for v in self.includePath_:
			args.append(f"-I{v}")

		for v in self.libraryPath_:
			args.append(f"-L{v}")

		for v in self.library_:
			args.append(f"-l{v}")


		if (self.version_):
			args.append(f"--std={self.version_}")

		if (self.bit_):
			args.append(f"-m{self.bit_}")

		if (self.compression_):
			args.append(f"-O{self.compression_}")


		for k, v in self.define_.items():
			args.append(f"-D {k}={v}")


		args += self.args_

		return self.scope.run(*args)



