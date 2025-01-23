from RFTLib.Require import *

from .Object import *
from .Buffer import *
from .Exception import *
from .Structure import *





__all__ = ("RFT_Server",)





class RFT_Server(RFT_Object):
	def __init__(self, ip:str, port:int, client:bool = False):
		self.ip = ip
		self.port = port
		self.client = client
		self.chunkSize = 8192

		self.data = RFT_Structure()

		self.running = True
		self.thread = None

		self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


		if (not self.client):
			try:
				self.server.bind((self.ip, self.port))
		
			except:
				raise RFT_Exception.Traceback()
				self.running = False



	# ~~~~~~~ Attach Structures ~~~~~~
	def attach(self, struct:RFT_Structure, name:str):
		self.data[name] = struct


	def dettach(self, name:str) -> RFT_Structure:
		if (self.data.contains(name)):
			return self.data.pop(name)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~ Refresh Structures ~~~~~~
	def refresh(self, name:str):
		if (self.client):
			if (struct := self.data.get(name)):
				structP = RFT_Structure({
					name: struct
				})

				buf = RFT_Buffer(structP)

				try:
					self.server.sendto(
						buf.data,
						(
							self.ip,
							self.port
						)
					)
				except:
					raise RFT_Exception.Traceback()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~ Run Server ~~~~~~~~~~
	def start(self):
		if (not self.client):
			self.running = True

			if (self.thread is not None):
				self.running = False
				self.thread.join()

			self.thread = threading.Thread(
				target = self.start_,
				args = (),
				kwargs = {},
				daemon = True
			)

			self.thread.start()



	def start_(self):
		if (not self.client):
			while (self.running):
				data, addr = self.server.recvfrom(self.chunkSize)
			
				buf = RFT_Buffer(data)

				try:
					struct = buf.toStruct()
				
				except:
					...
				
				else:
					for k, v in struct.items():
						if (self.data.contains(k)):
							if (isinstance(v, RFT_Structure | dict)):
								for k_, v_ in v.items():
									self.data[k][k_] = v_
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




