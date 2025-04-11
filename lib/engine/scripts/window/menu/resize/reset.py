from engine.require import *





__all__ = ("Scripts_Window_Menu_Resize_Reset",)





class Scripts_Window_Menu_Resize_Reset(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Reset")

		self.setIcon(Icons.core.reset)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.triggered.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		cur = QCursor()
		curPos = cur.pos()

		win = self.parent.parent.parent
		dw = win.scope.windowDefault

		win.resize(
			dw.width,
			dw.height
		)

		win.move(
			curPos.x() - (win.width() // 2),
			curPos.y() - 10,
		)

