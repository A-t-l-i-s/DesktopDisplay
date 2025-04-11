from engine.require import *





__all__ = ("Scripts_Window_Menu_Properties_Transparent",)





class Scripts_Window_Menu_Properties_Transparent(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.scope = self.parent.parent.parent.scope
		self.window = self.scope.window
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Transparent")

		self.setIcon(Icons.core.transparent)

		self.setCheckable(True)
		self.setChecked(self.window.transparent)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.triggered.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		self.window.transparent = not self.window.transparent


