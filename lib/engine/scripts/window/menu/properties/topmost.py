from engine.require import *





__all__ = ("Scripts_Window_Menu_Properties_Topmost",)





class Scripts_Window_Menu_Properties_Topmost(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Topmost")

		self.setIcon(Icons.topmost)

		self.setCheckable(True)
		self.setChecked(self.parent.parent.parent.script.window.topmost)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.triggered.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		win = self.parent.parent.parent

		win.script.window.topmost = not win.script.window.topmost

		win.reloadProperties()
		win.startEditing()


