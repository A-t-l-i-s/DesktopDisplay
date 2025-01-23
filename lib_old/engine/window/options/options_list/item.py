from engine.require import *

from .key import *
from .reset import *





__all__ = ("Window_OptionsList_Item",)





class Window_OptionsList_Item(RFT_Object, QFrame):
	def __init__(self, parent, locs, table, default):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.locs = locs
		self.table = table
		self.default = default
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setStyleSheet(Styles.options_item)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QVBoxLayout()
		self.layout.setSpacing(3)
		self.layout.setContentsMargins(5, 3, 5, 3)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)

		self.setLayout(self.layout)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Title ~~~~~~~~
		self.titleLabel = QLabel()
		self.titleLabel.setText(self.locs.get("name"))

		self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
		self.titleLabel.setStyleSheet(Styles.options_list_title)

		self.layout.addWidget(self.titleLabel)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Keys ~~~~~~~~~
		for k in self.table.keys():
			key = Window_OptionsList_Item_Key(self, k, self.locs, self.table, self.default)
			self.layout.addWidget(key)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~ Reset Button ~~~~~
		self.resetButton = Window_OptionsList_Item_Reset(self)
		self.layout.addWidget(self.resetButton)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


