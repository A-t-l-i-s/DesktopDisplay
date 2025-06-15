from engine.require import *
from engine.scripts import *

from .window import *
from .scripts import *
from .installer import *
from .console import *
from .tasks import *





__all__ = ("Window_Tabs",)





class Window_Tabs(RFT_Object, QTabWidget):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~ Settings ~~~~~~~
		self.setStyleSheet(Styles.core.window.tabs.main)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Tabs ~~~~~~~~~
		self.windowWidget = Window_Settings_Tabs_Window(self)
		i = self.addTab(self.windowWidget, "Window")
		self.windowWidget.index = i
		self.setTabIcon(i, Icons.core.icon)

		self.scriptsWidget = Window_Tabs_Scripts(self)
		i = self.addTab(self.scriptsWidget, "Scripts")
		self.scriptsWidget.index = i
		self.setTabIcon(i, Icons.core.window)

		self.installerWidget = Window_Tabs_Installer(self)
		i = self.addTab(self.installerWidget, "Installer")
		self.installerWidget.index = i
		self.setTabIcon(i, Icons.core.download)

		self.consoleWidget = Window_Tabs_Console(self)
		i = self.addTab(self.consoleWidget, "Console")
		self.consoleWidget.index = i
		self.setTabIcon(i, Icons.core.console)

		self.tasksWidget = Window_Settings_Tabs_Tasks(self)
		i = self.addTab(self.tasksWidget, "Tasks")
		self.tasksWidget.index = i
		self.setTabIcon(i, Icons.core.icon_task)
		# ~~~~~~~~~~~~~~~~~~~~~~~~



