from engine.require import *

from .move import *
from .resize import *
from .properties import *
from .settings import *





__all__ = ("Scripts_Window_Menu",)





class Scripts_Window_Menu(RFT_Object, QMenu):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setStyleSheet(Styles.core.menu)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Actions ~~~~~~~~~~~
		self.menuMove = Scripts_Window_Menu_Move(self)
		self.addMenu(self.menuMove)

		self.menuResize = Scripts_Window_Menu_Resize(self)
		self.addMenu(self.menuResize)

		self.addSeparator()

		self.menuProperties = Scripts_Window_Menu_Properties(self)
		self.addMenu(self.menuProperties)
		
		self.addSeparator()

		self.menuSettings = Scripts_Window_Menu_Settings(self)
		self.addMenu(self.menuSettings)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

