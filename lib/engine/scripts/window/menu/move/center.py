from engine.require import *





__all__ = ("Scripts_Window_Menu_Move_Center",)





class Scripts_Window_Menu_Move_Center(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Center")

		self.setIcon(Icons.center)
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
			round((size.x() + size.width() / 2) - (win.width() / 2)),
			round((size.y() + size.height() / 2) - (win.height() / 2))
		)


