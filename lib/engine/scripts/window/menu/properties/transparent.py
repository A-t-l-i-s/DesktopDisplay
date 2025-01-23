from engine.require import *





__all__ = ("Scripts_Window_Menu_Properties_Transparent",)





class Scripts_Window_Menu_Properties_Transparent(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Transparent")

		self.setIcon(Icons.transparent)

		self.setCheckable(True)
		self.setChecked(self.parent.parent.parent.script.window.transparent)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.triggered.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		win = self.parent.parent.parent

		win.script.window.transparent = not win.script.window.transparent

		win.reloadProperties()
		win.startEditing()


