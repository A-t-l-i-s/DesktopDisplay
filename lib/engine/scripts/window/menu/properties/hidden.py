from engine.require import *





__all__ = ("Scripts_Window_Menu_Properties_Hidden",)





class Scripts_Window_Menu_Properties_Hidden(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.scope = self.parent.parent.parent.scope
		self.gui = self.parent.parent.parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Hidden")

		self.setCheckable(True)
		self.setChecked(self.scope.window.hidden)

		self.setIcon(Icons.core.hide)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.triggered.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		self.scope.window.hidden = self.isChecked()

