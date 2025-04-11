from engine.require import *





__all__ = ("Scripts_Window_Canvas",)





class Scripts_Window_Canvas(RFT_Object, QWidget):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.scope = self.parent.scope
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setMouseTracking(False)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QVBoxLayout(self)

		self.layout.setSpacing(0)
		self.layout.setContentsMargins(0, 0, 0, 0)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def paintEvent(self, event):
		if (self.scope.getEnabled()):
			# Create painter instance
			painter = QPainter()

			# Size
			w = self.width()
			h = self.height()


			# Start paint
			painter.begin(self)


			# Erase background
			if (not self.scope.window.transparent):
				painter.fillRect(0, 0, w, h, QColor(0, 0, 0))


			# ~~~~ Draw Function ~~~~~
			if (not self.scope.window.hidden):
				if ((func := self.scope.drawEvent) is not None):
					try:
						func(self.scope, painter)

					except:
						win = self.scope.gui.parent
						
						if (win.alert_disable_ignore(f"{self.scope.id} : drawEvent()").wait() != win.alertWindow.ALERT_IGNORE):
							self.scope.drawEvent = None
			# ~~~~~~~~~~~~~~~~~~~~~~~~


			# Reset Pen/Brush
			painter.setPen(QColor(0, 0, 0, 0))
			painter.setBrush(QColor(0, 0, 0, 0))


			# ~~~~~ Editing Mode ~~~~~
			if (self.scope.inst.editing):
				# Make Window Clickable
				painter.fillRect(
					0, 0,
					w, h,
					QColor(0, 0, 0, 1)
				)

				# Border color
				c = QColor(10, 10, 10, 200)


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
					1, 20,
					w - 3, h - 3 - 18
				)


				# Title Color/Font
				painter.setPen(QColor(255, 255, 255))
				painter.setFont(QFont("Dosis", 11, 600, False))

				# Fetch window title
				if ((t := self.scope.locs.get("title")) is not None):
					title = t

				else:
					title = self.scope.id

				# Draw Text		
				painter.drawText(
					22, 0,
					w - 26, 20,
					Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
					title
				)
			# ~~~~~~~~~~~~~~~~~~~~~~~~


			# End paint
			painter.end()


