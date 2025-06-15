from engine.require import *

from .move import *
from .resize import *
from .properties import *
from .settings import *

from .disable import *
from .duplicate import *





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
		# ~~~~~~~~~ Move ~~~~~~~~~
		self.menuMove = Scripts_Window_Menu_Move(self)
		self.addMenu(self.menuMove)
		# ~~~~~~~~~~~~~~~~~~~~~~~~

		# ~~~~~~~~ Resize ~~~~~~~~
		self.menuResize = Scripts_Window_Menu_Resize(self)
		self.addMenu(self.menuResize)
		# ~~~~~~~~~~~~~~~~~~~~~~~~

		self.addSeparator()

		# ~~~~~~ Properties ~~~~~~
		self.menuProperties = Scripts_Window_Menu_Properties(self)
		self.addMenu(self.menuProperties)
		# ~~~~~~~~~~~~~~~~~~~~~~~~
		
		self.addSeparator()

		# ~~~~~~~ Settings ~~~~~~~
		self.menuSettings = Scripts_Window_Menu_Settings(self)
		
		if (self.parent.scope.settingsDefault):
			self.addMenu(self.menuSettings)
		# ~~~~~~~~~~~~~~~~~~~~~~~~

		self.addSeparator()

		# ~~~~~~~ Duplicate ~~~~~~
		self.actionDuplicate = Scripts_Window_Menu_Duplicate(self)
		
		if (not self.parent.scope.duplicate and self.parent.scope.duplicateAllow):
			self.addAction(self.actionDuplicate)
		# ~~~~~~~~~~~~~~~~~~~~~~~~

		self.addSeparator()

		# ~~~~~~~~ Disable ~~~~~~~
		self.actionDisable = Scripts_Window_Menu_Disable(self)
		self.addAction(self.actionDisable)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

