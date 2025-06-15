from engine.require import *





__all__ = ("Window_Settings_Tabs_Tasks_Item_Title",)





class Window_Settings_Tabs_Tasks_Item_Title(RFT_Object, QLabel):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setObjectName("title")

		self.setWordWrap(False)
		self.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)

		self.setText(self.parent.data.name)

		sizePolicy = self.sizePolicy()
		sizePolicy.setHorizontalPolicy(QSizePolicy.Policy.Ignored)
		self.setSizePolicy(sizePolicy)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


