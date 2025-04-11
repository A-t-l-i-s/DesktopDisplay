from engine.require import *





__all__ = ("Window_Settings_Scripts_Item_Console",)





class Window_Settings_Scripts_Item_Console(RFT_Object, QPushButton):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.scope = self.parent.scope
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setObjectName("console")

		self.setIcon(Icons.core.terminal)
		self.setCursor(Qt.CursorShape.PointingHandCursor)

		self.setFixedSize(30, 30)

		self.setStyleSheet(Styles.core.button + Styles.core.settings.tabs.scripts)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.clicked.connect(self._clicked)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _clicked(self):
		tab = self.parent.parent.parent
		widget = tab.consoleWidget
		
		# Change console buffer
		widget.buffer = self.scope.console
		
		# Change current tab to console
		tab.setCurrentWidget(
			widget
		)
