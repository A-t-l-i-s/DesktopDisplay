from engine.require import *





__all__ = ("Window_Tabs_Scripts_Item_Icon",)





class Window_Tabs_Scripts_Item_Icon(RFT_Object, QLabel):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.size = 22
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.hide()

		self.setObjectName("icon")

		self.setFixedSize(self.size + 8, self.size + 8)
		self.setAlignment(Qt.AlignmentFlag.AlignCenter)


		if (t := self.parent.scope.locs.get("icon")):
			try:
				t = t.split(".")

				icon = self.parent.scope.icons[t]

				pixmap = icon.pixmap(self.size, self.size)
				self.setPixmap(pixmap)

			except:
				...

			else:
				self.show()
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


