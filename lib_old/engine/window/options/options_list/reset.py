from engine.require import *





__all__ = ("Window_OptionsList_Item_Reset",)





class Window_OptionsList_Item_Reset(RFT_Object, QPushButton):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Reset")
		self.setFixedSize(90, 40)
		self.setCursor(Qt.CursorShape.PointingHandCursor)

		self.setStyleSheet("QPushButton{margin-top: 10px;}")
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.clicked.connect(self._clicked)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _clicked(self):
		self.parent.table.clear()
		
		for k, v in self.parent.default.items():
			self.parent.table[k] = v

		self.parent.parent.reload()
		self.parent.parent.touched = True

