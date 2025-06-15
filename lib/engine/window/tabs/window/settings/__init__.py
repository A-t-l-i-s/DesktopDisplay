from engine.require import *

from .rate import *
from .autorun import *





__all__ = ("Window_Settings_Tabs_Window_Settings",)





class Window_Settings_Tabs_Window_Settings(RFT_Object, QFrame):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setObjectName("settings")

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
		self.rateWidget = Window_Settings_Tabs_Window_Settings_Rate(self)
		self.layout.addWidget(self.rateWidget)

		self.autorunWidget = Window_Settings_Tabs_Window_Settings_Autorun(self)
		self.layout.addWidget(self.autorunWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



