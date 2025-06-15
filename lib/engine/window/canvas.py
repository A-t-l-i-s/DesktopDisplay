from engine.require import *

from .tabs import *
from .buttons import *





__all__ = ("Window_Canvas",)





class Window_Canvas(RFT_Object, QWidget):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setStyleSheet(Styles.core.window.main)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QVBoxLayout(self)
		self.layout.setSpacing(0)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Widgets ~~~~~~~~~~~
		self.tabsWidget = Window_Tabs(self)
		self.layout.addWidget(self.tabsWidget)

		self.buttonsWidget = Window_Buttons(self)
		self.layout.addWidget(self.buttonsWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


