from engine.require import *





__all__ = ("Scripts_Window_Menu_Disable",)





class Scripts_Window_Menu_Disable(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.scope = self.parent.parent.scope
		self.window = self.scope.window
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Disable")

		self.setIcon(Icons.core.close)

		self.setCheckable(False)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.triggered.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		self.scope.setEnabled(False)

		# Reload windows
		win = self.parent.parent.parent
		self.scope.inst.loadWindows(win, self.scope.id)


