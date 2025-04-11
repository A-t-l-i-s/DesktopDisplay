from engine.require import *





__all__ = ("Window_ButtonsList_Done",)





class Window_ButtonsList_Done(RFT_Object, QPushButton):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Done")
		self.setCursor(Qt.CursorShape.PointingHandCursor)

		self.setStyleSheet(Styles.core.button)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.clicked.connect(self._clicked)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _clicked(self):
		self.parent.parent.parent.systemTray.trayMenu.actionSettings.trigger()

