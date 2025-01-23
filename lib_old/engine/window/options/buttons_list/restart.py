from engine.require import *





__all__ = ("Window_ButtonsList_Restart",)





class Window_ButtonsList_Restart(RFT_Object, QPushButton):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Restart")
		self.setCursor(Qt.CursorShape.PointingHandCursor)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.clicked.connect(self._clicked)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _clicked(self):
		self.parent.parent.parent.restart()

