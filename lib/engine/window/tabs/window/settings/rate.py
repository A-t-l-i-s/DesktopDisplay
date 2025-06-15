from engine.require import *





__all__ = ("Window_Settings_Tabs_Window_Settings_Rate",)





class Window_Settings_Tabs_Window_Settings_Rate(RFT_Object, QFrame):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QHBoxLayout(self)

		self.layout.setSpacing(0)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Label Widget ~~~~~~~~~
		self.labelWidget = QLabel()
		self.labelWidget.setText("Framerate:")
		self.labelWidget.setFixedSize(120, 25)

		self.labelWidget.setFont(
			QFont("JetBrains Mono", 10, 600, False)
		)

		self.labelWidget.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)

		self.layout.addWidget(self.labelWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Input Widget ~~~~~~~~~
		self.inputWidget = QLineEdit()
		self.inputWidget.setFixedSize(100, 23)
		self.inputWidget.setStyleSheet(Styles.core.input)

		self.inputWidget.setPlaceholderText(f"{Tables.window.rate}")

		self.inputWidget.editingFinished.connect(self._triggered)

		self.layout.addWidget(self.inputWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		t = self.inputWidget.text()

		try:
			v = int(t)

		except:
			...

		else:
			if (v > 0):
				Tables.window.rate = v

		finally:
			self.inputWidget.setText(None)
			self.inputWidget.setPlaceholderText(str(Tables.window.rate))

			self.parent.parent.parent.parent.parent.timer.restart()



