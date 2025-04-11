from engine.require import *
from engine.scripts import *





__all__ = ("Window_Timer",)





class Window_Timer(RFT_Object, QTimer):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent

		self.rate = 0
		self.timestampsLen = 50
		self.timestamps = [time.time()] * self.timestampsLen
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.timeout.connect(self._timeout)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _timeout(self):
		# ~~~~~~~ Framerate ~~~~~~
		# Append current time to timestamps
		self.timestamps.append(time.time())

		# Get difference between timestamps
		self.rate = self.timestampsLen / (self.timestamps[-1] - self.timestamps.pop(0))
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~ Repaint Windows ~~~
		Scripts.update()
		# ~~~~~~~~~~~~~~~~~~~~~~~~

