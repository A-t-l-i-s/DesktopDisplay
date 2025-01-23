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
		self.setIcon(Icons.icon)

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
		if (event == QSystemTrayIcon.ActivationReason.Trigger or event == QSystemTrayIcon.ActivationReason.DoubleClick):
			w = self.trayMenu.actionEdit

			w.setChecked(not w.isChecked())
			w._triggered()


