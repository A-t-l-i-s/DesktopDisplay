from engine.require import *





__all__ = ("Window_Canvas",)





class Window_Canvas(RFT_Object, QWidget):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setMouseTracking(False)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def paintEvent(self, event):
		# Create painter instance
		painter = QPainter()

		# Start paint
		painter.begin(self)


		# painter.fillRect(0, 0, self.width(), self.height(), QColor(255, 255, 255))


		# End paint
		painter.end()


