from engine.require import *





__all__ = ("Window_Tabs_Scripts_Item_Title",)





class Window_Tabs_Scripts_Item_Title(RFT_Object, QLabel):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setObjectName("title")

		self.setWordWrap(False)
		self.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)

		sizePolicy = self.sizePolicy()
		sizePolicy.setHorizontalPolicy(QSizePolicy.Policy.Ignored)
		self.setSizePolicy(sizePolicy)


		if ((t := self.parent.scope.locs.get("title")) is not None):
			self.setText(t)

		else:
			self.setText(self.parent.scope.id)


		if (self.parent.scope.duplicate):
			self.setText(f"{self.text()} (Duplicate)")


		if (not self.parent.scope.available):
			self.setStyleSheet("color: rgb(100, 100, 100);")
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


