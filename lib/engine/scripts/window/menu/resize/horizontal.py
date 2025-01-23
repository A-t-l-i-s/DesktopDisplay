from engine.require import *





__all__ = ("Scripts_Window_Menu_Resize_Horizontal",)





class Scripts_Window_Menu_Resize_Horizontal(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Horizontal")

		self.setIcon(Icons.horizontal)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.triggered.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		cur = QCursor()
		screen = QtApp.screenAt(cur.pos())
		size = screen.availableGeometry()

		win = self.parent.parent.parent
		
		win.move(
			win.x(),
			size.y()
		)

		win.resize(
			win.width(),
			size.height()
		)


