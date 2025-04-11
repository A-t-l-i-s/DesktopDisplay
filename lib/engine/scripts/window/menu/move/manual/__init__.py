from engine.require import *

from .width import *
from .height import *

from .x import *
from .y import *





__all__ = ("Scripts_Window_Menu_Move_Manual",)





class Scripts_Window_Menu_Move_Manual(RFT_Object, QMenu):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setTitle("Manual")

		self.setIcon(Icons.core.move)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Actions ~~~~~~~~~~~
		self.actionWidth = Scripts_Window_Menu_Move_Manual_Width(self)
		self.addAction(self.actionWidth)

		self.actionHeight = Scripts_Window_Menu_Move_Manual_Height(self)
		self.addAction(self.actionHeight)

		self.addSeparator()

		self.actionX = Scripts_Window_Menu_Move_Manual_X(self)
		self.addAction(self.actionX)

		self.actionY = Scripts_Window_Menu_Move_Manual_Y(self)
		self.addAction(self.actionY)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def mouseReleaseEvent(self, event):
		action = self.activeAction()

		if (action):
			if (action.isCheckable()):
				action.setChecked(not action.isChecked())
			
			action.triggered.emit()
			event.accept()
		else:
			QMenu.mouseReleaseEvent(self, event)
	


