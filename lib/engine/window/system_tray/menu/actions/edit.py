from engine.require import *
from engine.scripts import *





__all__ = ("Window_SystemTray_Menu_Edit",)





class Window_SystemTray_Menu_Edit(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Edit")

		self.setIcon(Icons.core.edit)

		self.setCheckable(True)
		self.setChecked(Scripts.editing)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.triggered.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		if (self.isChecked()):
			# Start editing all windows
			Scripts.startEditing()

		else:
			# Show all windows
			Scripts.stopEditing()

