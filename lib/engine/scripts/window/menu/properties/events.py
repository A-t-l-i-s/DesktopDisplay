from engine.require import *





__all__ = ("Scripts_Window_Menu_Properties_Events",)





class Scripts_Window_Menu_Properties_Events(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Events")

		self.setIcon(Icons.mouse)

		self.setCheckable(True)
		self.setChecked(self.parent.parent.parent.script.window.events)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.triggered.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		win = self.parent.parent.parent

		win.script.window.events = not win.script.window.events

		win.reloadProperties()
		win.startEditing()


