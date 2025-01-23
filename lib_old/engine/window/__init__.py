from engine.require import *

from .timer import *
from .canvas import *

from .options import *

from .system_tray import *





__all__ = ("Window",)





class Window(RFT_Object, QMainWindow):
	def __init__(self):
		super().__init__()


		# ~~~~~~~ Variables ~~~~~~
		self.restarting = False
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		# Title
		self.setWindowIcon(Icons.icon)
		self.setWindowTitle("Desktop Display")

		# Attributes
		self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground, True)
		self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, Tables.window.transparentBackground)
		self.setAttribute(Qt.WidgetAttribute.WA_NoChildEventsForParent, True)
		self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, Tables.window.transparentEvents)

		# Flags
		self.setWindowFlags(
			Qt.WindowType.Tool |
			Qt.WindowType.FramelessWindowHint |
			Qt.WindowType.X11BypassWindowManagerHint |
			Qt.WindowType.WindowDoesNotAcceptFocus
		)

		if (Tables.window.topmost):
			self.setWindowFlags(
				self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint
			)
		else:
			self.setWindowFlags(
				self.windowFlags() | Qt.WindowType.WindowStaysOnBottomHint
			)


		# Get screen geometry
		screens = QtApp.screens()
		if (len(screens) > (i := Tables.window.display) >= 0):
			self.screen = screens[i]

		else:
			self.screen = QtApp.primaryScreen()
			Tables.window.display = 0

		

		self.screenSize = self.screen.availableGeometry()


		# Adjust program size
		self.width = self.screenSize.width()
		self.height = self.screenSize.height()
		self.x = (self.screenSize.width() - self.width) + self.screenSize.x()
		self.y = (self.screenSize.height() - self.height) + self.screenSize.y()

		# Size
		self.move(self.x, self.y)
		self.setFixedSize(self.width, self.height)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Central Widget ~~~~~~~~
		self.canvas = Window_Canvas(self)
		self.setCentralWidget(self.canvas)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Timer ~~~~~~~~
		self.timer = Window_Timer(self)


		# ~~~~~~~~ Options ~~~~~~~
		self.optionsWindow = Window_Options(self)


		# ~~~~~~ System Tray ~~~~~
		self.systemTray = Window_SystemTray(self)
		self.systemTray.show()



		# ~~~~~~~~ Scripts ~~~~~~~
		for k, v in Scripts.items():
			s = v.get("Script")
		

			if (isinstance(s, type)):
				# Convert class into structure
				t = RFT_Structure(s)

				d = t.get("default")

				table = Tables.scripts.allocate(k)
				table.default(d)
				Data.defaults[k] = d


				# Check if event structure has init function
				if (t.containsInst("init", types.MethodType)):
					while True:
						try:
							# Call function
							t.init(table)
							break
						except:
							# Print error
							if (RFT_Exception.Traceback().alert() != RFT_Exception.ALERT_RETRY):
								break



				# Check if event structure has run function
				if (t.containsInst("run", types.MethodType)):
					while True:
						try:
							# Call function in a new thread
							threading._start_new_thread(
								t.run,
								(),
								{}
							)

							break
						except:
							# Print error
							if (RFT_Exception.Traceback().alert() != RFT_Exception.ALERT_RETRY):
								break



				# Check if event structure has paint function and verify that it's callable
				if (t.containsInst("paint", types.MethodType)):
					if (callable(c := t.paint)):
						# Add function to paint events
						self.canvas.events.append(c)





	def exit(self):
		QtApp.closeAllWindows()
		QtApp.quit()

		self.restarting = False



	def restart(self):
		self.exit()

		self.restarting = True


