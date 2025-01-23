from engine.require import *





__all__ = ("Scripts_Window_Menu_Resize_Horizontal_Cut",)





class Scripts_Window_Menu_Resize_Horizontal_Cut(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Horizontal Cut")

		self.setIcon(Icons.horizontal_cut)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.triggered.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		win = self.parent.parent.parent

		win.resize(
			win.width(),
			win.height() // 2
		)


