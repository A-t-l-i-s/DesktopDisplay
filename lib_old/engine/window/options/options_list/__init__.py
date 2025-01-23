from engine.require import *

from .item import *





__all__ = ("Window_OptionsList",)





class Window_OptionsList(RFT_Object, QScrollArea):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.touched = False

		self.widget = QWidget()
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
		self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
		self.setWidgetResizable(True)

		self.setWidget(self.widget)

		self.setStyleSheet(Styles.options_list)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QVBoxLayout()

		self.layout.setSpacing(10)
		self.layout.setContentsMargins(5, 5, 5, 5)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

		self.widget.setLayout(self.layout)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




	def clear(self):
		self.touched = False

		while (self.layout.count()):
			c = self.layout.takeAt(0)
			w = c.widget()

			if (w):
				w.deleteLater()



	def reload(self):
		# Clear widgets
		self.clear()


		# ~~~~~~~~ Window Settings ~~~~~~~
		locs = Locs.window
		table = Tables.window
		default = Data.window

		# Create new item
		widget = Window_OptionsList_Item(self, locs, table, default)
		self.layout.addWidget(widget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Script Settings ~~~~~~~
		for k, v in Tables.scripts.items():
			locs = Locs.scripts.allocate(k)
			table = Tables.scripts.allocate(k)
			default = Data.defaults.allocate(k)

			# Create new item
			widget = Window_OptionsList_Item(self, locs, table, default)
			self.layout.addWidget(widget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



