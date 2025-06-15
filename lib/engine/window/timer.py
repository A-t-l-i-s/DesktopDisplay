from engine.require import *
from engine.scripts import *





__all__ = ("Window_Timer",)





class Window_Timer(RFT_Object, QTimer):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent

		self.rate = 0
		self.timestampsLen = 100
		self.timestamps = [time.time()] * self.timestampsLen
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setTimerType(Qt.TimerType.PreciseTimer)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.timeout.connect(self._timeout)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def restart(self):
		self.stop()
		self.start(1000 // Tables.window.rate)



	def _timeout(self):
		# ~~~~~~~ Framerate ~~~~~~
		# Append current time to timestamps
		self.timestamps.append(time.time())

		# Get difference between first and last timestamp
		dif = self.timestamps[-1] - self.timestamps.pop(0)

		if (dif):
			# Get difference between timestamps
			self.rate = self.timestampsLen / dif
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~ Repaint Windows ~~~
		Scripts.update()
		# ~~~~~~~~~~~~~~~~~~~~~~~~



