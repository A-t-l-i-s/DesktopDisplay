from engine.require import *

from .vertical import *
from .horizontal import *
from .vertical_cut import *
from .horizontal_cut import *
from .fill import *
from .reset import *





__all__ = ("Scripts_Window_Menu_Resize",)





class Scripts_Window_Menu_Resize(RFT_Object, QMenu):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setTitle("Resize")

		self.setIcon(Icons.resize)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Actions ~~~~~~~~~~~
		self.actionVertical = Scripts_Window_Menu_Resize_Vertical(self)
		self.addAction(self.actionVertical)

		self.actionHorizontal = Scripts_Window_Menu_Resize_Horizontal(self)
		self.addAction(self.actionHorizontal)

		self.addSeparator()
		
		self.actionVerticalCut = Scripts_Window_Menu_Resize_Vertical_Cut(self)
		self.addAction(self.actionVerticalCut)

		self.actionHorizontalCut = Scripts_Window_Menu_Resize_Horizontal_Cut(self)
		self.addAction(self.actionHorizontalCut)

		self.addSeparator()

		self.actionFill = Scripts_Window_Menu_Resize_Fill(self)
		self.addAction(self.actionFill)

		self.addSeparator()

		self.actionReset = Scripts_Window_Menu_Resize_Reset(self)
		self.addAction(self.actionReset)
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


