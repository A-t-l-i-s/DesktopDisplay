from engine.require import *





__all__ = ("Window_Settings_Tabs_Window_Settings_Autorun",)





class Window_Settings_Tabs_Window_Settings_Autorun(RFT_Object, QFrame):
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
		self.labelWidget.setText("Run at Startup:")
		self.labelWidget.setFixedSize(130, 25)

		self.labelWidget.setFont(
			QFont("JetBrains Mono", 10, 600, False)
		)

		self.labelWidget.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)

		self.layout.addWidget(self.labelWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Input Widget ~~~~~~~~~
		self.inputWidget = QCheckBox()

		self.inputWidget.setFixedSize(14, 14)
		self.inputWidget.setStyleSheet(Styles.core.toggle)
		self.inputWidget.setCursor(Qt.CursorShape.PointingHandCursor)

		self.inputWidget.setChecked(Internal.isStartup())
		
		self.inputWidget.checkStateChanged.connect(self._triggered)

		self.layout.addWidget(self.inputWidget)

		if (Internal.isDebug() or not Internal.isProduction()):
			self.labelWidget.setEnabled(False)
			self.inputWidget.setEnabled(False)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		Internal.isStartup(
			self.inputWidget.isChecked()
		)



