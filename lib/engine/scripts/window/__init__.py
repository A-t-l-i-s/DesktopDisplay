from engine.require import *

from .menu import *

from .canvas import *
from .resize import *
from .locked import *





__all__ = ("Scripts_Window",)





class Scripts_Window(RFT_Object, QMainWindow):
	def __init__(self, parent, script):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.script = script
		self.settings = script.table.settings

		self.threads = []
		self.click = None
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.reloadProperties()


		# Set Window Size
		self.resize(
			self.script.window.width,
			self.script.window.height
		)

		# Set Window Minimum Size
		self.setMinimumSize(100, 20)


		# ~~~~~~ Move Window ~~~~~
		cur = QCursor()
		screen = QtApp.screenAt(cur.pos())
		size = screen.availableGeometry()


		if (self.script.window.x is None):
			self.script.window.x = round((size.x() + size.width() / 2) - (self.width() / 2))

		if (self.script.window.y is None):
			self.script.window.y = round((size.y() + size.height() / 2) - (self.height() / 2))
		

		self.move(
			self.script.window.x,
			self.script.window.y
		)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Widgets ~~~~~~~~~~~
		self.canvas = Scripts_Window_Canvas(self)
		self.setCentralWidget(self.canvas)

		self.resizeWidget = Scripts_Window_Resize(self)
		self.resizeWidget.move(1, 1)
		self.resizeWidget.hide()

		self.lockedWidget = Scripts_Window_Locked(self)
		self.lockedWidget.move(20, 3)
		self.lockedWidget.hide()

		self.menuWidget = Scripts_Window_Menu(self)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~ Init Script ~~~~~
		if ((func := self.script.init) != None):
			while True:
				try:
					func(self)

				except:
					if (RFT_Exception.Traceback().alert(f"{self.script.path} : init()") != RFT_Exception.ALERT_RETRY):
						break

				else:
					break
		# ~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~ Threads ~~~~~~~
	def startThread(self, func, args = (), kwargs = {}):
		thread = threading.Thread(
			target = func,
			args = args,
			kwargs = kwargs,
			daemon = True
		)

		self.threads.append(thread)

		thread.start()
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~ Size Events ~~~~~~~~~
	def moveEvent(self, event):
		self.script.window.x = self.x()
		self.script.window.y = self.y()


	def resizeEvent(self, event):
		self.script.window.width = self.width()
		self.script.window.height = self.height()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~ Reloading ~~~~~~~~~~
	def reloadProperties(self):
		# Attributes
		self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground, True)
		self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, self.script.window.transparent)
		self.setAttribute(Qt.WidgetAttribute.WA_NoChildEventsForParent, True)

		# Flags
		self.setWindowFlags(
			Qt.WindowType.Tool |
			Qt.WindowType.FramelessWindowHint |
			Qt.WindowType.X11BypassWindowManagerHint
		)

		# Transparent Events
		if (not self.script.window.events):
			self.setWindowFlags(
				self.windowFlags() | Qt.WindowType.WindowTransparentForInput
			)

		# Topmost Flags
		if (self.script.window.topmost):
			self.setWindowFlags(
				self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint
			)
			self.raise_()

		else:
			self.setWindowFlags(
				self.windowFlags() | Qt.WindowType.WindowStaysOnBottomHint
			)
			self.lower()


		# Mouse Tracking
		self.setMouseTracking(self.script.window.events)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~ Editing ~~~~~~~~~~~
	def startEditing(self):
		self.script.editing = True

		self.resizeWidget.show()
		self.lockedWidget.show()

		self.setMouseTracking(True)
		self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowStaysOnBottomHint)
		self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
		self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowTransparentForInput)

		self.show()
		self.raise_()


	def stopEditing(self):
		self.script.editing = False

		self.resizeWidget.hide()
		self.lockedWidget.hide()

		self.reloadProperties()

		self.show()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~ Mouse Events ~~~~~~~~~
	def leaveEvent(self, event):
		self.click = None


	def mousePressEvent(self, event):
		if (self.script.editing):
			btn = event.button()
			pos = event.pos()
			x, y = pos.x(), pos.y()

			cur = QCursor()
			curPos = cur.pos()

			if (btn == Qt.MouseButton.LeftButton):
				self.click = x, y

			elif (btn == Qt.MouseButton.RightButton):
				self.menuWidget.popup(curPos)


		else:
			# ~~~~~~ Press Event ~~~~~
			if (self.script.mousePress != None):
				try:
					self.script.mousePress(self, event)

				except:
					if (RFT_Exception.Traceback().alert(f"{self.script.path} : mousePress()") == RFT_Exception.ALERT_ABORT):
						self.script.mousePress = None
			# ~~~~~~~~~~~~~~~~~~~~~~~~


	def mouseReleaseEvent(self, event):
		if (self.script.editing):
			btn = event.button()

			if (btn == Qt.MouseButton.LeftButton):
				self.click = None

		else:
			# ~~~~~ Release Event ~~~~
			if (self.script.mouseRelease != None):
				try:
					self.script.mouseRelease(self, event)

				except:
					if (RFT_Exception.Traceback().alert(f"{self.script.path} : mouseRelease()") == RFT_Exception.ALERT_ABORT):
						self.script.mouseRelease = None
			# ~~~~~~~~~~~~~~~~~~~~~~~~


	def mouseMoveEvent(self, event):
		if (self.script.editing):
			btn = event.button()
			pos = event.pos()

			cur = QCursor()
			curPos = cur.pos()

			w = self.width()

			if (btn == Qt.MouseButton.NoButton):
				if (self.click is not None):
					if (not self.script.window.locked):
						x = curPos.x() - self.click[0]
						y = curPos.y() - self.click[1]

						self.move(x, y)

		else:
			# ~~~~~~ Move Event ~~~~~~
			if (self.script.mouseMove != None):
				try:
					self.script.mouseMove(self, event)

				except:
					if (RFT_Exception.Traceback().alert(f"{self.script.path} : mouseMove()") == RFT_Exception.ALERT_ABORT):
						self.script.mouseMove = None
			# ~~~~~~~~~~~~~~~~~~~~~~~~
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~ Key Events ~~~~~~~~~~
	def keyPressEvent(self, event):
		if (not self.script.editing):
			if (self.script.keyPress != None):
				try:
					self.script.keyPress(self, event)

				except:
					if (RFT_Exception.Traceback().alert(f"{self.script.path} : keyPress()") == RFT_Exception.ALERT_ABORT):
						self.script.keyPress = None


	def keyReleaseEvent(self, event):
		if (not self.script.editing):
			if (self.script.keyRelease != None):
				try:
					self.script.keyRelease(self, event)

				except:
					if (RFT_Exception.Traceback().alert(f"{self.script.path} : keyRelease()") == RFT_Exception.ALERT_ABORT):
						self.script.keyRelease = None
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



