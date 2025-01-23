from engine.require import *

from .timer import *
from .canvas import *

from .system_tray import *





__all__ = ("Window",)





class Window(RFT_Object, QMainWindow):
	def __init__(self):
		super().__init__()


		# ~~~~~~~ Variables ~~~~~~
		self.scriptExit = False
		self.scriptRestart = False
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		# Title
		self.setWindowIcon(Icons.icon)
		self.setWindowTitle("Desktop Display")

		# Attributes
		self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground, True)
		self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
		self.setAttribute(Qt.WidgetAttribute.WA_NoChildEventsForParent, True)
		self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)

		# Flags
		self.setWindowFlags(
			Qt.WindowType.Tool |
			Qt.WindowType.FramelessWindowHint |
			Qt.WindowType.X11BypassWindowManagerHint |
			Qt.WindowType.WindowStaysOnTopHint
		)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Central Widget ~~~~~~~~
		self.canvas = Window_Canvas(self)
		self.setCentralWidget(self.canvas)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# ~~~~~~~~~~~~~ Timer ~~~~~~~~~~~~
		self.timer = Window_Timer(self)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# ~~~~~~~~~~ System Tray ~~~~~~~~~
		self.systemTray = Window_SystemTray(self)
		self.systemTray.show()
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def exit(self):
		QtApp.closeAllWindows()
		QtApp.quit()

		self.restarting = False

		Tables_Obj.saveAll()



	def restart(self):
		self.exit()

		self.restarting = True

