from engine.require import *

from .tabs import *
from .buttons import *





__all__ = ("Window_Settings",)





class Window_Settings(RFT_Object, QWidget):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setWindowIcon(Icons.core.icon)
		self.setWindowTitle("Settings")

		# Flags
		self.setWindowFlags(
			Qt.WindowType.Tool |
			Qt.WindowType.CustomizeWindowHint |
			Qt.WindowType.WindowTitleHint |
			Qt.WindowType.WindowStaysOnTopHint
		)

		# Stylesheet
		self.setStyleSheet(Styles.core.settings.main)


		# ~~~~~~ Move Window ~~~~~
		cur = QCursor()
		screen = QApplication.screenAt(cur.pos())
		size = screen.availableGeometry()


		# Geometry Variables
		self.width = size.width() // 4
		self.height = size.height() // 2

		self.x = round((size.x() + size.width() / 2) - (self.width / 2))
		self.y = round((size.y() + size.height() / 2) - (self.height / 2))
		

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


		# Set Window Minimum Size
		self.setMinimumSize(300, 100)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QVBoxLayout(self)
		self.layout.setSpacing(0)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Widgets ~~~~~~~~~~~
		self.tabsWidget = Window_Settings_Tabs(self)
		self.layout.addWidget(self.tabsWidget)

		self.buttonsWidget = Window_Settings_Buttons(self)
		self.layout.addWidget(self.buttonsWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


