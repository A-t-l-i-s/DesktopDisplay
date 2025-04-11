from engine.require import *





__all__ = ("Scripts_Window_Menu_Properties_Topmost",)





class Scripts_Window_Menu_Properties_Topmost(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.scope = self.parent.parent.parent.scope
		self.window = self.scope.window
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Topmost")

		self.setIcon(Icons.core.topmost)

		self.setCheckable(True)
		self.setChecked(self.window.topmost)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.triggered.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		self.window.topmost = not self.window.topmost


