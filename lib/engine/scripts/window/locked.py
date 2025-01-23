from engine.require import *





__all__ = ("Scripts_Window_Locked",)





class Scripts_Window_Locked(RFT_Object, QPushButton):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.updateIcon()

		self.setFixedSize(15, 13)
		self.setCursor(Qt.CursorShape.PointingHandCursor)
		
		self.setStyleSheet("""
			QPushButton{
				background-color: transparent;
				icon-size: 13px;
			}
		""")
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		self.clicked.connect(self._clicked)



	def updateIcon(self):
		if (self.parent.script.window.locked):
			self.setIcon(Icons.lock)
			self.parent.resizeWidget.setEnabled(False)

		else:
			self.setIcon(Icons.unlock)
			self.parent.resizeWidget.setEnabled(True)



	def _clicked(self):
		self.parent.script.window.locked = not self.parent.script.window.locked
		self.updateIcon()



