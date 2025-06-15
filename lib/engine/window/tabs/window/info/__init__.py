from engine.require import *

from .fps import *
from .tasks import *
from .threads import *
from .version import *
from .version_internal import *





__all__ = ("Window_Settings_Tabs_Window_Info",)





class Window_Settings_Tabs_Window_Info(RFT_Object, QFrame):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setObjectName("info")

		self.setFixedWidth(280)

		self.setStyleSheet(Styles.core.window.tabs.window)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QVBoxLayout(self)
		self.layout.setSpacing(3)
		self.layout.setContentsMargins(3, 3, 3, 3)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Widgets ~~~~~~~~~~~
		self.fpsWidget = Window_Settings_Tabs_Window_Info_FPS(self)
		self.layout.addWidget(self.fpsWidget)


		self.threadsWidget = Window_Settings_Tabs_Window_Info_Threads(self)
		self.layout.addWidget(self.threadsWidget)

		self.tasksWidget = Window_Settings_Tabs_Window_Info_Tasks(self)
		self.layout.addWidget(self.tasksWidget)


		self.versionWidget = Window_Settings_Tabs_Window_Info_Version(self)
		self.layout.addWidget(self.versionWidget)

		self.versionInternalWidget = Window_Settings_Tabs_Window_Info_Version_Internal(self)
		self.layout.addWidget(self.versionInternalWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



