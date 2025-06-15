from engine.require import *





__all__ = ("Window_Settings_Tabs_Tasks_Item_PID",)





class Window_Settings_Tabs_Tasks_Item_PID(RFT_Object, QLabel):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setObjectName("pid")

		self.setWordWrap(False)
		self.setAlignment(Qt.AlignmentFlag.AlignCenter)

		self.setFixedWidth(80)

		self.setText(str(self.parent.data.pid))
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


