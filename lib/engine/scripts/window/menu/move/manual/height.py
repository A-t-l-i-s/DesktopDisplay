from engine.require import *





__all__ = ("Scripts_Window_Menu_Move_Manual_Height",)





class Scripts_Window_Menu_Move_Manual_Height(RFT_Object, QWidgetAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent

		self.window = self.parent.parent.parent.parent.window
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QHBoxLayout()
		self.layout.setSpacing(0)
		self.layout.setContentsMargins(5, 2, 2, 2)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Container ~~~~~~~~~~
		self.container = QWidget()
		self.container.setLayout(self.layout)

		self.setDefaultWidget(self.container)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Key Widget ~~~~~~~~~~
		self.keyWidget = QLabel()
		self.keyWidget.setFixedSize(100, 25)

		self.keyWidget.setText("Height")

		self.keyWidget.setFont(
			QFont("Dosis", 11, 600, False)
		)

		self.layout.addWidget(self.keyWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Value Widget ~~~~~~~~~
		self.valueWidget = QLineEdit()
		self.valueWidget.setStyleSheet(Styles.core.input)

		self.layout.addWidget(self.valueWidget)
		
		self.reload()

		self.valueWidget.editingFinished.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def reload(self):
		self.valueWidget.setPlaceholderText(str(self.window.height))



	def _triggered(self):
		text = self.valueWidget.text()
		text = text.strip()

		if (text):
			try:
				value = ast.literal_eval(text)
			
			except:
				...

			else:
				if (isinstance(value, int)):
					self.window.height = value
					self.valueWidget.setPlaceholderText(str(value))

					win = self.parent.parent.parent
					win.resize(win.width(), value)

					self.reload()


		self.valueWidget.setText(None)






