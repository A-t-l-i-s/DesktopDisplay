from engine.require import *
from engine.scripts import *

from .enable import *
from .title import *
from .icon import *
from .remove import *
from .duplicate import *





__all__ = ("Window_Tabs_Scripts_Item",)





class Window_Tabs_Scripts_Item(RFT_Object, QFrame):
	def __init__(self, parent, key, scope):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.key = key
		self.scope = scope
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setObjectName("main")

		self.setStyleSheet(Styles.core.window.tabs.scripts)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QHBoxLayout(self)
		self.layout.setSpacing(3)
		self.layout.setContentsMargins(3, 3, 3, 3)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Widgets ~~~~~~~~~~~
		self.enableToggle = Window_Tabs_Scripts_Item_Enable(self)
		self.layout.addWidget(self.enableToggle)


		self.iconLabel = Window_Tabs_Scripts_Item_Icon(self)
		self.layout.addWidget(self.iconLabel)


		self.titleLabel = Window_Tabs_Scripts_Item_Title(self)
		self.layout.addWidget(self.titleLabel)


		self.duplicateButton = Window_Tabs_Scripts_Item_Duplicate(self)
		self.layout.addWidget(self.duplicateButton)
		
		if (self.scope.duplicate or not self.scope.duplicateAllow):
			self.duplicateButton.hide()


		self.removeButton = Window_Tabs_Scripts_Item_Remove(self)
		self.layout.addWidget(self.removeButton)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



