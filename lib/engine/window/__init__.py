from engine.require import *

from engine.scripts import *
from engine.scripts.window import *

from .timer import *
from .canvas import *
from .system_tray import *






__all__ = ("Window",)





class Window(RFT_Object, QMainWindow):
	def __init__(self):
		super().__init__()


		# ~~~~~~~ Variables ~~~~~~
		self.width = 0
		self.height = 0
		
		self.x = 0
		self.y = 0
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setWindowIcon(Icons.core.icon)
		self.setWindowTitle(Tables.window.title)

		# Flags
		self.setWindowFlags(
			Qt.WindowType.Tool |
			Qt.WindowType.WindowStaysOnBottomHint |
			Qt.WindowType.CustomizeWindowHint |
			Qt.WindowType.WindowTitleHint
		)


		cur = QCursor()
		screen = QApplication.screenAt(cur.pos())
		size = screen.availableGeometry()


		# Geometry Variables
		self.width = size.width() // 3
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
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Canvas ~~~~~~~~~~~~
		self.canvas = Window_Canvas(self)
		self.setCentralWidget(self.canvas)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# ~~~~~~~~~~~~~ Timer ~~~~~~~~~~~~
		self.timer = Window_Timer(self)
		self.timer.restart()
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# ~~~~~~~~~~ System Tray ~~~~~~~~~
		self.systemTray = Window_SystemTray(self)
		self.systemTray.show()
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~ Console ~~~~~~~
	def print(self, val:object):
		Scripts.print("window", val)


	def printErr(self, exc:RFT_Exception):
		Scripts.printErr("window", exc)
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~ Events ~~~~~~~~
	def exit(self):
		QApplication.closeAllWindows()
		QApplication.quit()

		Internal.isExiting(True)
		Internal.isRestarting(False)


	def restart(self):
		self.exit()

		Internal.isExiting(True)
		Internal.isRestarting(True)
	# ~~~~~~~~~~~~~~~~~~~~~~~~

