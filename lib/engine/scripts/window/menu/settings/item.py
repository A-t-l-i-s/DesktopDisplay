from engine.require import *

from .widgets.input import *
from .widgets.color import *
from .widgets.toggle import *





__all__ = ("Scripts_Window_Menu_Settings_Item",)





class Scripts_Window_Menu_Settings_Item(RFT_Object, QWidgetAction):
	def __init__(self, parent, key, setting):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent

		self.key = key
		self.name = setting.get("name", key)
		self.type = setting.get("type", None)

		self.script = self.parent.parent.parent.script
		self.settings = self.script.table.settings

		self.defaultValue = setting.get("value", None)
		self.value = self.settings.get(key, self.defaultValue)
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
		self.keyWidget.setFixedSize(140, 25)

		self.keyWidget.setText(self.name)

		self.keyWidget.setFont(
			QFont("Dosis", 11, 600, False)
		)

		self.layout.addWidget(self.keyWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		if (self.type == "color"):
			if (isinstance(self.value, list | tuple)):
				if (len(self.value) == 3):
					self.value += [255]

				if (len(self.value) == 4):
					self.widget = Scripts_Window_Menu_Settings_Color(self)
					self.layout.addWidget(self.widget)

		elif (self.type == "toggle"):
			self.widget = Scripts_Window_Menu_Settings_Toggle(self)
			self.layout.addWidget(self.widget)

		elif (self.type == "input"):
			self.widget = Scripts_Window_Menu_Settings_Input(self)
			self.layout.addWidget(self.widget)

		else:
			f = QFont("Dosis ExtraBold", 13)
			f.setUnderline(True)

			self.keyWidget.setFont(f)

			self.type = None


