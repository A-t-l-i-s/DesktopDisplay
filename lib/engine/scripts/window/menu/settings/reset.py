from engine.require import *





__all__ = ("Scripts_Window_Menu_Settings_Reset",)





class Scripts_Window_Menu_Settings_Reset(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Reset")

		self.setIcon(Icons.reset)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.triggered.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		for a in self.parent.actions:
			a.value = a.defaultValue
			a.settings[a.key] = a.defaultValue

			if (a.type is not None):
				a.widget.reload(True)


