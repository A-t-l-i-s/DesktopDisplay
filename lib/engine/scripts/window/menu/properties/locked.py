from engine.require import *





__all__ = ("Scripts_Window_Menu_Properties_Locked",)





class Scripts_Window_Menu_Properties_Locked(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.scope = self.parent.parent.parent.scope
		self.gui = self.parent.parent.parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Locked")

		self.setCheckable(True)
		self.setChecked(self.scope.window.locked)

		self.updateIcon()
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.triggered.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	def updateIcon(self):
		if (self.scope.window.locked):
			self.setIcon(Icons.core.lock)
			self.gui.resizeWidget.setEnabled(False)

		else:
			self.setIcon(Icons.core.unlock)
			self.gui.resizeWidget.setEnabled(True)



	def _triggered(self):
		self.scope.window.locked = self.isChecked()
		self.updateIcon()

