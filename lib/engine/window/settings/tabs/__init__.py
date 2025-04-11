from engine.require import *

from .window import *
from .scripts import *
from .installer import *
from .console import *
from .tasks import *





__all__ = ("Window_Settings_Tabs",)





class Window_Settings_Tabs(RFT_Object, QTabWidget):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~ Settings ~~~~~~~
		self.setStyleSheet(Styles.core.settings.tabs.main)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Tabs ~~~~~~~~~
		self.windowWidget = Window_Settings_Tabs_Window(self)
		i = self.addTab(self.windowWidget, "Window")
		self.setTabIcon(i, Icons.core.icon)

		self.scriptsWidget = Window_Settings_Tabs_Scripts(self)
		i = self.addTab(self.scriptsWidget, "Scripts")
		self.setTabIcon(i, Icons.core.window)

		# self.installerWidget = Window_Settings_Tabs_Installer(self)
		# self.addTab(self.installerWidget, "Installer")

		self.consoleWidget = Window_Settings_Tabs_Console(self)
		i = self.addTab(self.consoleWidget, "Console")
		self.setTabIcon(i, Icons.core.terminal)

		self.tasksWidget = Window_Settings_Tabs_Tasks(self)
		i = self.addTab(self.tasksWidget, "Tasks")
		self.setTabIcon(i, Icons.core.icon_task)
		# ~~~~~~~~~~~~~~~~~~~~~~~~



