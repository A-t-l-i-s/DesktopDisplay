from engine.require import *

from .widgets.input import *
from .widgets.color import *
from .widgets.toggle import *
from .widgets.range import *
from .widgets.list import *





__all__ = ("Scripts_Window_Menu_Settings_Item",)





class Scripts_Window_Menu_Settings_Item(RFT_Object, QWidgetAction):
	def __init__(self, parent, key, value):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent

		self.size = (120, 23)

		self.scope = self.parent.parent.parent.scope
		self.locs = self.scope.locs
		self.table = self.scope.settings

		self.setting = value

		self.key = key
		self.name = self.locs.settings.get(key, key)
		self.type = self.setting.get("type", None)
		self.callback = self.setting.get("callback", None)

		self.defaultValue = self.setting.get("value", None)
		self.value = self.table.get(key, self.defaultValue)
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
		self.keyWidget.setFixedSize(120, 25)

		self.keyWidget.setText(self.name)

		self.keyWidget.setFont(
			QFont("Dosis", 11, 600, False)
		)

		self.layout.addWidget(self.keyWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		if (self.type == self.scope.SETTINGS.COLOR):
			# ~~~~~~~~~ Color Widget ~~~~~~~~~
			self.widget = Scripts_Window_Menu_Settings_Color(self)
			self.layout.addWidget(self.widget)
			# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		elif (self.type == self.scope.SETTINGS.TOGGLE):
			# ~~~~~~~~~ Toggle Widget ~~~~~~~~
			self.widget = Scripts_Window_Menu_Settings_Toggle(self)
			self.layout.addWidget(self.widget)
			# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		elif (self.type == self.scope.SETTINGS.INPUT):
			# ~~~~~~~~~ Input Widget ~~~~~~~~~
			self.widget = Scripts_Window_Menu_Settings_Input(self)
			self.layout.addWidget(self.widget)
			# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		elif (self.type == self.scope.SETTINGS.RANGE):
			# ~~~~~~~~~ Range Widget ~~~~~~~~~
			self.widget = Scripts_Window_Menu_Settings_Range(self)
			self.layout.addWidget(self.widget)
			# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		elif (self.type == self.scope.SETTINGS.LIST):
			# ~~~~~~~~ Options Widget ~~~~~~~~
			self.widget = Scripts_Window_Menu_Settings_List(self)
			self.layout.addWidget(self.widget)
			# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		else:
			# ~~~~~~~~~ Title Widget ~~~~~~~~~
			f = QFont("Dosis ExtraBold", 13)
			f.setUnderline(True)

			self.keyWidget.setFont(f)

			self.type = None
			# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


