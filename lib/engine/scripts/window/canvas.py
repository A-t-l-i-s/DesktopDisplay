from engine.require import *





__all__ = ("Scripts_Window_Canvas",)





class Scripts_Window_Canvas(RFT_Object, QWidget):
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


		# ~~~~ Draw Function ~~~~~
		if ((func := self.parent.script.draw) != None):
			try:
				func(self.parent, painter)

			except:
				if (RFT_Exception.Traceback().alert(f"{self.parent.script.path} : draw()") == RFT_Exception.ALERT_ABORT):
					self.script.draw = None
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~ Editing Mode ~~~~~
		if (self.parent.script.editing):
			w = self.width()
			h = self.height()

			c = QColor(10, 10, 10)


			# Top Bar
			painter.fillRect(
				0, 0,
				w, 20,
				c
			)

			# Border Pen
			painter.setPen(
				QPen(
					c,
					3
				)
			)

			# Draw Border
			painter.drawRect(
				1, 1,
				w - 3, h - 3
			)


			# Title Color/Font
			painter.setPen(QColor(255, 255, 255))
			painter.setFont(QFont("Dosis", 11, 600, False))

			# Draw Text			
			painter.drawText(
				58, 0,
				w - 65, 20,
				Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter,
				self.parent.script.window.title
			)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# End paint
		painter.end()


