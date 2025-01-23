from engine.require import *

from .done import *
from .restart import *





__all__ = ("Window_ButtonsList",)





class Window_ButtonsList(RFT_Object, QFrame):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setStyleSheet(Styles.options_list)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QHBoxLayout()

		self.layout.setSpacing(10)
		self.layout.setContentsMargins(5, 5, 5, 5)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

		self.setLayout(self.layout)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Widgets ~~~~~~~~~~~
		self.doneButton = Window_ButtonsList_Done(self)
		self.layout.addWidget(self.doneButton)

		# self.restartButton = Window_ButtonsList_Restart(self)
		# self.layout.addWidget(self.restartButton)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



