from engine.require import *
from engine.scripts import *

from .pid import *
from .icon import *
from .time import *
from .title import *
from .terminate import *





__all__ = ("Window_Settings_Tabs_Tasks_Item",)





class Window_Settings_Tabs_Tasks_Item(RFT_Object, QFrame):
	def __init__(self, parent, data):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.data = data
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setObjectName("main")

		self.setStyleSheet(Styles.core.window.tabs.tasks)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QHBoxLayout(self)
		self.layout.setSpacing(3)
		self.layout.setContentsMargins(3, 3, 3, 3)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Widgets ~~~~~~~~~~~
		self.iconLabel = Window_Settings_Tabs_Tasks_Item_Icon(self)
		self.layout.addWidget(self.iconLabel)

		self.titleLabel = Window_Settings_Tabs_Tasks_Item_Title(self)
		self.layout.addWidget(self.titleLabel)

		self.pidLabel = Window_Settings_Tabs_Tasks_Item_PID(self)
		self.layout.addWidget(self.pidLabel)

		self.timeLabel = Window_Settings_Tabs_Tasks_Item_Time(self)
		self.layout.addWidget(self.timeLabel)

		self.terminateButton = Window_Settings_Tabs_Tasks_Item_Terminate(self)
		self.layout.addWidget(self.terminateButton)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



