from engine.require import *

from .done import *





__all__ = ("Window_Buttons",)





class Window_Buttons(RFT_Object, QFrame):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setStyleSheet(Styles.core.window.buttons)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QHBoxLayout(self)

		self.layout.setSpacing(10)
		self.layout.setContentsMargins(5, 5, 5, 5)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Widgets ~~~~~~~~~~~
		self.doneButton = Window_Buttons_Done(self)
		self.layout.addWidget(self.doneButton)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



