from engine.require import *
from engine.scripts import *





__all__ = ("Window_Tabs_Scripts_Item_Enable",)





class Window_Tabs_Scripts_Item_Enable(RFT_Object, QCheckBox):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setFixedSize(14, 14)

		self.setCursor(Qt.CursorShape.PointingHandCursor)

		self.setChecked(
			self.parent.scope.getEnabled()
		)
		
		self.setStyleSheet(Styles.core.toggle)

		if (not self.parent.scope.available):
			self.setEnabled(False)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.checkStateChanged.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		self.parent.scope.setEnabled(
			self.isChecked()
		)

		Scripts.loadWindows(
			self.parent.parent.parent.parent.parent,
			self.parent.scope.id
		)


