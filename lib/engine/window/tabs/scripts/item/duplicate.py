from engine.require import *
from engine.scripts import *





__all__ = ("Window_Tabs_Scripts_Item_Duplicate",)





class Window_Tabs_Scripts_Item_Duplicate(RFT_Object, QPushButton):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.scope = self.parent.scope
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setObjectName("duplicate")

		self.setToolTip("Duplicate")

		self.setIcon(Icons.core.duplicate)
		self.setCursor(Qt.CursorShape.PointingHandCursor)

		self.setFixedSize(30, 30)

		self.setStyleSheet(Styles.core.button + Styles.core.window.tabs.scripts)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.clicked.connect(self._clicked)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _clicked(self):
		win = self.parent.parent.parent.parent.parent
		idS = self.scope.id

		# Create new id and table
		id_ = f"{idS}_{Scripts.newId()}"
		if ((dup := Tables.duplicates.get(idS)) is not None):
			# Add id to duplicates
			dup.append(id_)

			# Reload scripts and windows
			Scripts.load(win, idS)
			Scripts.loadWindows(win, id_)
