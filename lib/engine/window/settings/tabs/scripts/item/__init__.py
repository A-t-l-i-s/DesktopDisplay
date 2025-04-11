from engine.require import *
from engine.scripts import *

from .enable import *
from .title import *
from .icon import *
from .remove import *
from .console import *





__all__ = ("Window_Settings_Scripts_Item",)





class Window_Settings_Scripts_Item(RFT_Object, QFrame):
	def __init__(self, parent, key, scope):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.key = key
		self.scope = scope
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setObjectName("main")

		self.setStyleSheet(Styles.core.settings.tabs.scripts)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QHBoxLayout(self)
		self.layout.setSpacing(3)
		self.layout.setContentsMargins(3, 3, 3, 3)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Widgets ~~~~~~~~~~~
		self.enableToggle = Window_Settings_Scripts_Item_Enable(self)
		self.layout.addWidget(self.enableToggle)


		self.iconLabel = Window_Settings_Scripts_Item_Icon(self)
		self.layout.addWidget(self.iconLabel)


		self.titleLabel = Window_Settings_Scripts_Item_Title(self)
		self.layout.addWidget(self.titleLabel)


		self.consoleButton = Window_Settings_Scripts_Item_Console(self)
		self.layout.addWidget(self.consoleButton)

		self.removeButton = Window_Settings_Scripts_Item_Remove(self)
		self.layout.addWidget(self.removeButton)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



