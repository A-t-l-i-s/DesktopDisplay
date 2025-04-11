from engine.require import *





__all__ = ("Window_Settings_Tabs_Window_Rate",)





class Window_Settings_Tabs_Window_Rate(RFT_Object, QFrame):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent

		self.timerMain = self.parent.parent.parent.parent.timer
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QHBoxLayout(self)

		self.layout.setSpacing(0)
		self.layout.setContentsMargins(5, 2, 2, 2)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ FPS Widget ~~~~~~~~~~
		self.fpsWidget = QLabel()
		self.fpsWidget.setFixedSize(100, 25)

		self.fpsWidget.setFont(
			QFont("JetBrains Mono", 10, 600, False)
		)

		self.fpsWidget.setAlignment(Qt.AlignmentFlag.AlignCenter)

		self.layout.addWidget(self.fpsWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Input Widget ~~~~~~~~~
		self.widget = QLineEdit()
		self.widget.setFixedSize(90, 20)
		self.widget.setStyleSheet(Styles.core.input)

		self.widget.setPlaceholderText(f"{Tables.window.rate}")

		self.widget.editingFinished.connect(self._triggered)

		self.layout.addWidget(self.widget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Timer ~~~~~~~~
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.reload)
		self.timer.start(100)
		# ~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		t = self.widget.text()

		try:
			v = int(t)

		except:
			...

		else:
			if (v > 0):
				Tables.window.rate = v

		finally:
			self.widget.setText(None)
			self.widget.setPlaceholderText(str(Tables.window.rate))

			self.timerMain.stop()
			self.timerMain.start(960 // Tables.window.rate)




	def reload(self):
		if (self.parent.parent.currentWidget() == self.parent and self.parent.parent.isVisible()):
			self.fpsWidget.setText(
				f"{self.timerMain.rate:.2f} fps"
			)



