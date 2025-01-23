from engine.require import *





__all__ = ("Scripts_Window_Menu_Resize_Fill",)





class Scripts_Window_Menu_Resize_Fill(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Fill")

		self.setIcon(Icons.fill)
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
			size.x(),
			size.y()
		)

		win.resize(
			size.width(),
			size.height()
		)


