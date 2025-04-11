from engine.require import *





__all__ = ("Window_Settings_Tabs_Console_Message",)





class Window_Settings_Tabs_Console_Message(RFT_Object, QScrollArea):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.widget = QLabel(self)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~ Settings ~~~~~~~
		self.setWidgetResizable(True)
		
		self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
		self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

		self.setStyleSheet(Styles.core.scrollbar)

		self.setWidget(self.widget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Widget ~~~~~~~~
		self.widget.setStyleSheet(Styles.core.console)
		
		self.widget.setWordWrap(True)
		self.widget.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

		self.widget.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

		sizePolicy = self.widget.sizePolicy()
		sizePolicy.setHorizontalPolicy(QSizePolicy.Policy.Expanding)
		self.widget.setSizePolicy(sizePolicy)
		# ~~~~~~~~~~~~~~~~~~~~~~~~

