from engine.require import *





__all__ = ("Window_Canvas",)





class Window_Canvas(RFT_Object, QWidget):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.events = []
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setMouseTracking(False)



		if (Tables.window.dropShadow):
			self.shadow = QGraphicsDropShadowEffect()
			
			self.shadow.setBlurRadius(100)
			self.shadow.setOffset(5, 5)
			self.shadow.setColor(QColor(*Tables.window.dropShadowColor))
		
			self.setGraphicsEffect(self.shadow)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def paintEvent(self, event):
		# Create painter instance
		painter = QPainter()
		painter.parent = self

		# Start paint
		painter.begin(self)

		if (Tables.window.antialiasing):
			painter.setRenderHint(QPainter.RenderHint.Antialiasing)




		# ~~~~~~~~~~~~~ Debug ~~~~~~~~~~~~
		if (Tables.window.showFps):
			painter.setFont(
				QFont("Dosis Bold", 16)
			)

			painter.drawText(
				5, 5,
				100, 30,
				Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignLeft,
				f"{round(self.parent.timer.fps, 2)} FPS"
			)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# Call all paint events
		for i, event in enumerate(self.events):
			try:
				# Call function
				event.__call__(painter)
			
			except:
				self.parent.timer.stop()

				# Print traceback exception
				if (RFT_Exception.Traceback().alert() == RFT_Exception.ALERT_ABORT):
					self.parent.exit()

				else:
					self.parent.restart()


		# End paint
		painter.end()


