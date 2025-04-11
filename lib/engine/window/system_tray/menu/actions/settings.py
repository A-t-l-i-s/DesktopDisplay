from engine.require import *
from engine.scripts import *





__all__ = ("Window_SystemTray_Menu_Settings",)





class Window_SystemTray_Menu_Settings(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Settings")

		self.setIcon(Icons.core.settings)

		self.setCheckable(True)
		self.setChecked(False)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.triggered.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		win = self.parent.parent.parent.settingsWindow

		if (self.isChecked()):
			win.show()

		else:
			win.hide()

