from engine.require import *
from engine.scripts import *

from .menu import *





__all__ = ("Window_SystemTray",)





class Window_SystemTray(RFT_Object, QSystemTrayIcon):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent

		self.notif = Scripts.consoleNotif
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


		# ~~~~~~~~~ Timer ~~~~~~~~
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.reload)
		self.timer.start(1000 // 10)
		# ~~~~~~~~~~~~~~~~~~~~~~~~



	def reload(self):
		tabs = self.parent.canvas.tabsWidget
		tabsC = tabs.consoleWidget

		if (Scripts.consoleNotif):
			if (tabs.currentWidget() != tabsC or not tabs.parent.isVisible()):
				if (not self.notif):
					self.setIcon(Icons.core.icon_notif)
					tabs.setTabIcon(tabsC.index, Icons.core.console_notif)
					self.notif = True

		else:
			if (self.notif):
				self.setIcon(Icons.core.icon)
				tabs.setTabIcon(tabsC.index, Icons.core.console)
				self.notif = False



	def _activated(self, event):
		if (event == QSystemTrayIcon.ActivationReason.Trigger):
			self.trayMenu.actionEdit.trigger()

		elif (event == QSystemTrayIcon.ActivationReason.MiddleClick):
			self.trayMenu.actionSettings.trigger()




