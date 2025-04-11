from engine.require import *

from .menu import *





__all__ = ("Window_SystemTray",)





class Window_SystemTray(RFT_Object, QSystemTrayIcon):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setIcon(Icons.core.icon)

		self.setToolTip("Desktop Display")
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~~ Menu ~~~~~~~~~~~~~
		self.trayMenu = Window_SystemTray_Menu(self)
		self.setContextMenu(self.trayMenu)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.activated.connect(self._activated)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _activated(self, event):
		if (event == QSystemTrayIcon.ActivationReason.Trigger):
			self.trayMenu.actionEdit.trigger()

		elif (event == QSystemTrayIcon.ActivationReason.MiddleClick):
			self.trayMenu.actionSettings.trigger()




