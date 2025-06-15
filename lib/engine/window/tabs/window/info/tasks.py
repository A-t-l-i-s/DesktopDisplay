from engine.require import *





__all__ = ("Window_Settings_Tabs_Window_Info_Tasks",)





class Window_Settings_Tabs_Window_Info_Tasks(RFT_Object, QFrame):
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
		self.labelWidget.setText("Tasks:")
		self.labelWidget.setFixedSize(120, 25)

		self.labelWidget.setFont(
			QFont("JetBrains Mono", 10, 600, False)
		)

		self.labelWidget.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)

		self.layout.addWidget(self.labelWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Input Widget ~~~~~~~~~
		self.inputWidget = QLabel()
		self.inputWidget.setText("")
		self.inputWidget.setFixedSize(100, 23)

		self.inputWidget.setFont(
			QFont("JetBrains Mono", 10, 700, False)
		)

		self.inputWidget.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)

		self.layout.addWidget(self.inputWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




	def reload(self):
		self.inputWidget.setText(f"{len(self.parent.parent.parent.tasksWidget.tasks)}")

