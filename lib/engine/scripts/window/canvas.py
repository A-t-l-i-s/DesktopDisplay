from engine.require import *





__all__ = ("Scripts_Window_Canvas",)





class Scripts_Window_Canvas(RFT_Object, QWidget):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.black = QColor(0, 0, 0, 255)
		self.transparent = QColor(0, 0, 0, 0)

		self.borderColor = QColor(10, 10, 10, 200)
		self.backgroundColor = QColor(0, 0, 0, 1)

		self.textColor = QColor(255, 255, 255)
		self.textFont = QFont("Dosis", 11, 600, False)

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


			if (not self.scope.window.hidden):
				# Erase background
				if (not self.scope.window.transparent):
					painter.fillRect(0, 0, w, h, self.black)


				# ~~~~ Draw Function ~~~~~
				if ((func := self.scope.drawEvent) is not None):
					try:
						func(self.scope, painter)

					except:
						self.scope.printErr(
							RFT_Exception.Traceback(),
							uidEnd = " : drawEvent()"
						)
				# ~~~~~~~~~~~~~~~~~~~~~~~~




			# ~~~~~ Editing Mode ~~~~~
			if (self.scope.inst.editing):
				# Reset Pen/Brush
				painter.setPen(self.transparent)
				painter.setBrush(self.transparent)

				painter.setRenderHint(QPainter.RenderHint.Antialiasing | QPainter.RenderHint.TextAntialiasing)
				painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)


				# Make Window Clickable
				painter.fillRect(
					0, 0,
					w, h,
					self.backgroundColor
				)

				# Top Bar
				painter.fillRect(
					0, 0,
					w, 20,
					self.borderColor
				)


				# Border Pen
				painter.setPen(
					QPen(
						self.borderColor,
						3
					)
				)

				# Draw Border
				painter.drawRect(
					1, 20,
					w - 3, h - 3 - 18
				)


				# Title Color/Font
				painter.setPen(self.textColor)
				painter.setFont(self.textFont)

				# Fetch window title
				if ((t := self.scope.locs.get("title")) is not None):
					title = t

				else:
					title = self.scope.id

				# Edit title
				if (self.scope.duplicate):
					title += " (Duplicate)"

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


