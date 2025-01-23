from engine.require import *

from .item import *
from .reset import *





__all__ = ("Scripts_Window_Menu_Settings",)





class Scripts_Window_Menu_Settings(RFT_Object, QMenu):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.actions = []
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setTitle("Settings")

		self.setIcon(Icons.settings)

		self.setStyleSheet(Styles.settings)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Actions ~~~~~~~~~~~
		for k, v in self.parent.parent.script.settings.items():
			action = Scripts_Window_Menu_Settings_Item(self, k, v)			
			self.addAction(action)

			if (v.get("seperator")):
				self.addSeparator()

			self.actions.append(action)
			

		if (len(self.actions) > 0):
			self.addSeparator()

			self.actionReset = Scripts_Window_Menu_Settings_Reset(self)
			self.addAction(self.actionReset)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def mouseReleaseEvent(self, event):
		action = self.activeAction()

		if (action):
			if (action.isCheckable()):
				action.setChecked(not action.isChecked())
			
			action.triggered.emit()
			event.accept()
		else:
			QMenu.mouseReleaseEvent(self, event)


