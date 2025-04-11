from engine.require import *





__all__ = ("Window_Alert_Message",)





class Window_Alert_Message(RFT_Object, QScrollArea):
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

		self.setStyleSheet("""
			QScrollBar{
				width: 8px;

				background-color: transparent;
			}

			QScrollBar::handle{
				border: none;

				background-color: rgb(50, 50, 50);
			}

			QScrollBar::handle::pressed{
				border: none;

				background-color: rgb(50, 50, 50);
			}

			QScrollBar::add-line{
				border: none;
				background: none;
			}

			QScrollBar::sub-line{
				border: none;
				background: none;
			}
		""")

		self.setWidget(self.widget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Widget ~~~~~~~~
		self.widget.setStyleSheet("""
			QLabel{
				background-color: rgb(10, 10, 10);

				border: 1px solid rgb(20, 20, 20);
				border-radius: 5px;

				padding: 4px;

				font-family: JetBrains Mono;
				font-size: 12px;
			}
		""")

		
		self.widget.setWordWrap(True)
		self.widget.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

		sizePolicy = self.widget.sizePolicy()
		sizePolicy.setHorizontalPolicy(QSizePolicy.Policy.Expanding)
		self.widget.setSizePolicy(sizePolicy)
		# ~~~~~~~~~~~~~~~~~~~~~~~~



	def reload(self):
		self.widget.setText(
			self.parent.error.message(extra = False).strip()
		)

