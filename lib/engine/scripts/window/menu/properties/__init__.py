from engine.require import *

from .events import *
from .topmost import *
from .transparent import *

from .locked import *
from .hidden import *





__all__ = ("Scripts_Window_Menu_Properties",)





class Scripts_Window_Menu_Properties(RFT_Object, QMenu):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setTitle("Properties")

		self.setIcon(Icons.core.window)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Actions ~~~~~~~~~~~
		self.actionTopmost = Scripts_Window_Menu_Properties_Topmost(self)
		self.addAction(self.actionTopmost)

		self.actionTransparent = Scripts_Window_Menu_Properties_Transparent(self)
		self.addAction(self.actionTransparent)

		self.actionEvents = Scripts_Window_Menu_Properties_Events(self)
		self.addAction(self.actionEvents)

		self.addSeparator()

		self.actionLocked = Scripts_Window_Menu_Properties_Locked(self)
		self.addAction(self.actionLocked)

		self.actionHidden = Scripts_Window_Menu_Properties_Hidden(self)
		self.addAction(self.actionHidden)
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

