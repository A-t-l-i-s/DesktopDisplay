from engine.require import *





__all__ = ("Scripts_Window_Resize",)





class Scripts_Window_Resize(RFT_Object, QSizeGrip):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setFixedSize(15, 15)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

