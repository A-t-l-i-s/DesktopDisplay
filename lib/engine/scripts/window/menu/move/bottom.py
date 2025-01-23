from engine.require import *





__all__ = ("Scripts_Window_Menu_Move_Bottom",)





class Scripts_Window_Menu_Move_Bottom(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Bottom")

		self.setIcon(Icons.bottom_double)
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
			size.y() + size.height() - win.height()
		)


