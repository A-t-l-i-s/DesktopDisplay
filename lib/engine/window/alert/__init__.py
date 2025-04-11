from engine.require import *

from .buttons import *
from .message import *





__all__ = ("Window_Alert",)





class Window_Alert(RFT_Object, QWidget):

	ALERT_OK:int = 0
	ALERT_EXIT:int = 1
	ALERT_RETRY:int = 2
	ALERT_CANCEL:int = 3
	ALERT_IGNORE:int = 4
	ALERT_DISABLE:int = 5
	ALERT_RESET:int = 6


	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.error = None

		self.buttons = ()

		self.code = None
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		# Title
		self.setWindowIcon(Icons.core.icon)
		self.setWindowTitle("Alert")

		# Flags
		self.setWindowFlags(
			Qt.WindowType.Tool |
			Qt.WindowType.CustomizeWindowHint |
			Qt.WindowType.WindowTitleHint |
			Qt.WindowType.WindowStaysOnTopHint
		)

		# Stylesheet
		self.setStyleSheet("""
			QWidget{
				background-color: rgb(30, 30, 30);
			}
		""")


		# ~~~~~~ Move Window ~~~~~
		cur = QCursor()
		screen = QApplication.screenAt(cur.pos())
		size = screen.availableGeometry()


		# Geometry Variables
		self.width = 450
		self.height = 300

		self.x = round((size.x() + size.width() / 2) - (self.width / 2))
		self.y = round((size.y() + size.height() / 2) - (self.height / 2))


		self.setMinimumSize(150, 100)
		

		# Set Window Size
		self.resize(
			self.width,
			self.height
		)

		# Set Window Position
		self.move(
			self.x,
			self.y
		)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QVBoxLayout(self)

		self.layout.setSpacing(3)
		self.layout.setContentsMargins(3, 3, 3, 3)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Widgets ~~~~~~~~~~~
		self.messageWidget = Window_Alert_Message(self)
		self.layout.addWidget(self.messageWidget)

		self.buttonsWidget = Window_Alert_Buttons(self)
		self.layout.addWidget(self.buttonsWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def wait(self):
		fps = Tables.window.rate / 1000

		self.show()

		while not Core.isExiting():
			QCoreApplication.processEvents()

			if (self.code is not None):
				break

			time.sleep(fps)

		self.hide()

		return self.code


