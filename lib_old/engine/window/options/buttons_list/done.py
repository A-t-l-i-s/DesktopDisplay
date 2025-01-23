from engine.require import *





__all__ = ("Window_ButtonsList_Done",)





class Window_ButtonsList_Done(RFT_Object, QPushButton):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Done")
		self.setCursor(Qt.CursorShape.PointingHandCursor)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.clicked.connect(self._clicked)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _clicked(self):
		if (self.parent.parent.optionsList.touched):
			Tables_Obj.saveAll()
			
			self.parent.parent.parent.restart()

		else:
			self.parent.parent.stop()

