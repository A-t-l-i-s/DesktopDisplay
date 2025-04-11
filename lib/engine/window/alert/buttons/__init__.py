from engine.require import *

from .ok import *
from .exit import *
from .retry import *
from .reset import *
from .cancel import *
from .ignore import *
from .disable import *





__all__ = ("Window_Alert_Buttons",)





class Window_Alert_Buttons(RFT_Object, QFrame):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setFixedHeight(50)

		self.setStyleSheet("""
			QPushButton{
				font-family: Dosis ExtraBold;
				font-size: 14px;

				color: white;
				background-color: rgb(70, 70, 70);

				border: none;
				border-radius: 4px;

				padding: 7px 14px;

				width: 65px;
			}

			QPushButton:hover{
				background-color: rgb(90, 90, 90);
			}


			QPushButton:disabled{
				background-color: rgb(40, 40, 40);
			}
		""")
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QHBoxLayout(self)

		self.layout.setSpacing(5)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




	def reload(self):
		# Delete old buttons
		while self.layout.count():
			item = self.layout.itemAt(0)
			if (item is not None):
				widget = item.widget()
				
				if (widget is not None):
					widget.deleteLater()
				
				self.layout.removeItem(item)



		for v in self.parent.buttons:
			if (v == self.parent.ALERT_OK):
				self.layout.addWidget(Alert_Buttons_Ok(self))

			elif (v == self.parent.ALERT_EXIT):
				self.layout.addWidget(Alert_Buttons_Exit(self))

			elif (v == self.parent.ALERT_RETRY):
				self.layout.addWidget(Alert_Buttons_Retry(self))

			elif (v == self.parent.ALERT_CANCEL):
				self.layout.addWidget(Alert_Buttons_Cancel(self))

			elif (v == self.parent.ALERT_IGNORE):
				self.layout.addWidget(Alert_Buttons_Ignore(self))

			elif (v == self.parent.ALERT_DISABLE):
				self.layout.addWidget(Alert_Buttons_Disable(self))

			elif (v == self.parent.ALERT_RESET):
				self.layout.addWidget(Alert_Buttons_Reset(self))



