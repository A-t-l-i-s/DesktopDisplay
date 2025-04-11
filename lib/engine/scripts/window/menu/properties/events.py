from engine.require import *





__all__ = ("Scripts_Window_Menu_Properties_Events",)





class Scripts_Window_Menu_Properties_Events(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.scope = self.parent.parent.parent.scope
		self.window = self.scope.window
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Events")

		self.setIcon(Icons.core.mouse)

		self.setCheckable(True)
		self.setChecked(self.window.events)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.triggered.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		self.window.events = not self.window.events


