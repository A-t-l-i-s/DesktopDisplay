from engine.require import *

from .center import *
from .top import *
from .bottom import *
from .left import *
from .right import *





__all__ = ("Scripts_Window_Menu_Move",)





class Scripts_Window_Menu_Move(RFT_Object, QMenu):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setTitle("Move")

		self.setIcon(Icons.move)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Actions ~~~~~~~~~~~
		self.actionCenter = Scripts_Window_Menu_Move_Center(self)
		self.addAction(self.actionCenter)

		self.addSeparator()

		self.actionTop = Scripts_Window_Menu_Move_Top(self)
		self.addAction(self.actionTop)

		self.actionBottom = Scripts_Window_Menu_Move_Bottom(self)
		self.addAction(self.actionBottom)

		self.actionLeft = Scripts_Window_Menu_Move_Left(self)
		self.addAction(self.actionLeft)

		self.actionRight = Scripts_Window_Menu_Move_Right(self)
		self.addAction(self.actionRight)
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
	


