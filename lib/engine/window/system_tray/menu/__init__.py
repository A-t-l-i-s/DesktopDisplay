from engine.require import *

from .actions.exit import *
from .actions.edit import *
from .actions.restart import *
from .actions.settings import *





__all__ = ("Window_SystemTray_Menu",)





class Window_SystemTray_Menu(RFT_Object, QMenu):
	def __init__(self, parent):
		super().__init__(parent.parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setStyleSheet(Styles.core.menu)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Actions ~~~~~~~~~~~
		self.actionEdit = Window_SystemTray_Menu_Edit(self)
		self.addAction(self.actionEdit)

		self.addSeparator()
		
		self.actionSettings = Window_SystemTray_Menu_Settings(self)
		self.addAction(self.actionSettings)

		self.addSeparator()

		self.actionRestart = Window_SystemTray_Menu_Restart(self)
		self.addAction(self.actionRestart)

		self.actionExit = Window_SystemTray_Menu_Exit(self)
		self.addAction(self.actionExit)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

