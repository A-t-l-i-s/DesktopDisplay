from engine.require import *
from engine.scripts import *





__all__ = ("Window_Tabs_Installer_Item",)





class Window_Tabs_Installer_Item(RFT_Object, QFrame):
	def __init__(self, parent, package):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.package = package
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setObjectName("main")

		self.setStyleSheet(Styles.core.window.tabs.installer)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QHBoxLayout(self)
		self.layout.setSpacing(3)
		self.layout.setContentsMargins(3, 3, 3, 3)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Widgets ~~~~~~~~~~~
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



