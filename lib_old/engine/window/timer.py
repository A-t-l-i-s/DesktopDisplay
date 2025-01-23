from engine.require import *





__all__ = ("Window_Timer",)





class Window_Timer(RFT_Object, QTimer):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent

		self.rate = Tables.window.rate

		self.fps = 0
		self.timestamps = collections.deque([], 50)

		self.paused = False
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.timeout.connect(self._timeout)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		

		# ~~~~~~~~~ Start ~~~~~~~~
		self.start(900 // self.rate)



	@pyqtSlot()
	def _timeout(self):
		# Append current time to timestamps
		self.timestamps.append(time.time())

		# Get amount of timestamps
		l = len(self.timestamps)

		if (l > 1):
			# Get first and last timestamp
			last = self.timestamps[-1]
			first = self.timestamps[0]

			# Get difference between timestamps
			self.fps = l / (last - first)


		if (not self.paused):
			# Repaint window
			self.parent.canvas.repaint()	



