from engine.require import *
from engine.scripts import *

from .item import *





__all__ = ("Window_Tabs_Scripts",)





class Window_Tabs_Scripts(RFT_Object, QScrollArea):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.index = -1

		self.widget = QWidget(self)

		self.found = RFT_Structure()
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~ Settings ~~~~~~~
		self.setWidgetResizable(True)
		
		self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
		self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

		self.setStyleSheet(Styles.core.scrollbar)

		self.setWidget(self.widget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Layout ~~~~~~~~
		self.layout = QVBoxLayout(self.widget)

		self.layout.setSpacing(3)
		self.layout.setContentsMargins(5, 5, 5, 5)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Timer ~~~~~~~~
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.reload)
		self.timer.start(100)
		# ~~~~~~~~~~~~~~~~~~~~~~~~



	def reload(self):
		if (self.parent.currentWidget() == self and self.parent.parent.isVisible()):
			for k, v in Scripts.scopes.items():
				if (not self.found.contains(k)):
					# Create new item
					widget = Window_Tabs_Scripts_Item(self, k, v)
					self.layout.addWidget(widget)

					self.found[k] = widget

				else:
					# Check if mismatched enable checkbox
					w = self.found[k]

					if (w is not None):
						if (w.enableToggle.isChecked() != (x := v.getEnabled())):
							w.enableToggle.setChecked(x)



