from engine.require import *

from .message import *





__all__ = ("Window_Settings_Tabs_Console",)





class Window_Settings_Tabs_Console(RFT_Object, QScrollArea):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.buffer = None

		self.widget = QWidget(self)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~ Settings ~~~~~~~
		self.setWidgetResizable(True)

		self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
		self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

		self.setStyleSheet(Styles.core.scrollbar)

		self.setWidget(self.widget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Layout ~~~~~~~~
		self.layout = QVBoxLayout(self.widget)

		self.layout.setSpacing(3)
		self.layout.setContentsMargins(5, 5, 5, 5)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Widgets ~~~~~~~
		self.messageWidget = Window_Settings_Tabs_Console_Message(self)
		self.layout.addWidget(self.messageWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Timer ~~~~~~~~
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.reload)
		self.timer.start(100)
		# ~~~~~~~~~~~~~~~~~~~~~~~~



	def reload(self):
		if (self.parent.currentWidget() == self and self.parent.parent.isVisible()):
			if (isinstance(self.buffer, RFT_Buffer)):
				try:
					self.messageWidget.widget.setText(
						self.buffer.toStr()
					)

				except:
					self.messageWidget.widget.setText(
						RFT_Exception.Traceback().message()
					)

					self.buffer = None



