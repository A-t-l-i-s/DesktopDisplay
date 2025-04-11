from engine.require import *





__all__ = ("Scripts_Window_Menu_Resize_Vertical_Cut",)





class Scripts_Window_Menu_Resize_Vertical_Cut(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Vertical Cut")

		self.setIcon(Icons.core.vertical_cut)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.triggered.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		win = self.parent.parent.parent

		win.resize(
			win.width() // 2,
			win.height()
		)


