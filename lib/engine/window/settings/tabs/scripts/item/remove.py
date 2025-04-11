from engine.require import *





__all__ = ("Window_Settings_Scripts_Item_Remove",)





class Window_Settings_Scripts_Item_Remove(RFT_Object, QPushButton):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setObjectName("remove")

		self.setIcon(Icons.core.remove)
		self.setCursor(Qt.CursorShape.PointingHandCursor)

		self.setFixedSize(30, 30)

		self.setStyleSheet(Styles.core.button + Styles.core.settings.tabs.scripts)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.clicked.connect(self._clicked)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _clicked(self):
		path = self.parent.scope.path

		self.parent.scope.setEnabled(False)

		if (path.is_file()):
			try:
				os.remove(
					path
				)

			except:
				...

			else:
				self.parent.hide()

