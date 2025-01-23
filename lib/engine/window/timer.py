from engine.require import *
from engine.scripts import *





__all__ = ("Window_Timer",)





class Window_Timer(RFT_Object, QTimer):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent

		self.screen = None

		self.rate = 30
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.timeout.connect(self._timeout)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		

		# ~~~~~~~~~ Start ~~~~~~~~
		self.start(900 // self.rate)



	def _timeout(self):
		# ~~~~ Repaint Windows ~~~
		# Main window
		self.parent.canvas.update()

		# Script windows
		for s in Scripts.scripts:
			s.canvas.update()
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~ Update Window ~~~~
		cur = QCursor()
		screen = QtApp.screenAt(cur.pos())

		if (screen != self.screen):
			self.screen = screen

			size = self.screen.availableGeometry()

			w = size.width()
			h = size.height()
			x = (size.width() - w) + size.x()
			y = (size.height() - h) + size.y()

			self.parent.move(x, y)
			self.parent.setFixedSize(w, h)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~ Script Exit ~~~~~
		if (self.parent.scriptExit):
			self.parent.exit()

		if (self.parent.scriptRestart):
			self.parent.restart()
		# ~~~~~~~~~~~~~~~~~~~~~~~~

