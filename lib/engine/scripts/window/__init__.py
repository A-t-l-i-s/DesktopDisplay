from engine.require import *

from .menu import *

from .canvas import *
from .resize import *





__all__ = ("Scripts_Window",)





class Scripts_Window(RFT_Object, QMainWindow):
	def __init__(self, scope, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.scope = scope

		self.parent = parent

		self.window = scope.window
		self.settings = scope.settings

		self.inst = scope.inst

		self.click = None
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.reloadProperties()

		self.setStyleSheet(Styles.core.menu)


		# ~~~~~~ Move Window ~~~~~
		cur = QCursor()
		screen = QApplication.screenAt(cur.pos())
		size = screen.availableGeometry()


		if (self.window.x is None):
			self.window.x = round((size.x() + size.width() / 2) - (self.width() / 2))

		if (self.window.y is None):
			self.window.y = round((size.y() + size.height() / 2) - (self.height() / 2))
		

		# Set Window Size
		self.resize(
			self.window.width,
			self.window.height
		)

		# Set Window Position
		self.move(
			self.window.x,
			self.window.y
		)


		# Set Window Minimum Size
		self.setMinimumSize(20, 20)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Widgets ~~~~~~~~~~~
		self.canvas = Scripts_Window_Canvas(self)
		self.setCentralWidget(self.canvas)

		self.resizeWidget = Scripts_Window_Resize(self)
		self.resizeWidget.move(1, 1)
		self.resizeWidget.hide()

		self.menuWidget = Scripts_Window_Menu(self)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~ Reloading ~~~~~~~~~~
	def reloadProperties(self, *, topmost:bool = None, events:bool = None):
		# If default value isn't set then get the saved properties 
		if (topmost is None):
			topmost = self.window.topmost

		if (events is None):
			events = self.window.events


		# Attributes
		self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground, True)
		self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
		self.setAttribute(Qt.WidgetAttribute.WA_NoChildEventsForParent, True)

		# Flags
		self.setWindowFlags(
			Qt.WindowType.Tool |
			Qt.WindowType.FramelessWindowHint |
			Qt.WindowType.X11BypassWindowManagerHint
		)

		# Topmost Flags
		if (topmost):
			self.setWindowFlags(
				self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint
			)

		else:
			self.setWindowFlags(
				self.windowFlags() | Qt.WindowType.WindowStaysOnBottomHint
			)

		# Transparent Events
		if (not events):
			self.setWindowFlags(
				self.windowFlags() | Qt.WindowType.WindowTransparentForInput
			)

		# Mouse Tracking
		self.setMouseTracking(events)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~ Size Events ~~~~~~~~~
	def moveEvent(self, event):
		pos = event.pos()
		oldPos = event.oldPos()

		x, y = pos.x(), pos.y()
		x_, y_ = oldPos.x(), oldPos.y()

		self.window.x = x
		self.window.y = y

		self.menuWidget.menuMove.menuManual.actionX.reload()
		self.menuWidget.menuMove.menuManual.actionY.reload()

		# ~~~~~~ Move Event ~~~~~~
		if (self.scope.getEnabled()):
			if ((func := self.scope.moveEvent) is not None):
				try:
					func(self.scope, event)

				except:
					self.scope.printErr(
						RFT_Exception.Traceback(),
						uidEnd = " : moveEvent()"
					)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


	def resizeEvent(self, event):
		self.window.width = self.width()
		self.window.height = self.height()

		self.menuWidget.menuMove.menuManual.actionWidth.reload()
		self.menuWidget.menuMove.menuManual.actionHeight.reload()

		# ~~~~~ Resize Event ~~~~~
		if (self.scope.getEnabled()):
			if ((func := self.scope.resizeEvent) is not None):
				try:
					func(self.scope, event)

				except:
					self.scope.printErr(
						RFT_Exception.Traceback(),
						uidEnd = " : resizeEvent()"
					)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~ Mouse Events ~~~~~~~~~
	def leaveEvent(self, event):
		self.click = None


	def mousePressEvent(self, event):
		if (self.inst.editing):
			btn = event.button()
			pos = event.pos()
			x, y = pos.x(), pos.y()

			cur = QCursor()
			curPos = cur.pos()

			if (btn == Qt.MouseButton.LeftButton):
				self.click = x, y

			elif (btn == Qt.MouseButton.RightButton):
				self.menuWidget.exec(curPos)
				self.click = None


		else:
			# ~~~~~~ Press Event ~~~~~
			if (self.scope.getEnabled()):
				if ((func := self.scope.mousePressEvent) is not None):
					try:
						func(self.scope, event)

					except:
						self.scope.printErr(
							RFT_Exception.Traceback(),
							uidEnd = " : mousePressEvent()"
						)
			# ~~~~~~~~~~~~~~~~~~~~~~~~


	def mouseReleaseEvent(self, event):
		if (self.inst.editing):
			btn = event.button()

			if (btn == Qt.MouseButton.LeftButton):
				self.click = None

		else:
			# ~~~~~ Release Event ~~~~
			if (self.scope.getEnabled()):
				if ((func := self.scope.mouseReleaseEvent) is not None):
					try:
						func(self.scope, event)

					except:
						self.scope.printErr(
							RFT_Exception.Traceback(),
							uidEnd = " : mouseReleaseEvent()"
						)
			# ~~~~~~~~~~~~~~~~~~~~~~~~


	def mouseMoveEvent(self, event):
		if (self.inst.editing):
			btn = event.button()
			pos = event.pos()

			cur = QCursor()
			curPos = cur.pos()

			w = self.width()

			if (btn == Qt.MouseButton.NoButton):
				if (self.click is not None):
					if (not self.window.locked):
						x = curPos.x() - self.click[0]
						y = curPos.y() - self.click[1]

						self.move(x, y)

		else:
			# ~~~~~~ Move Event ~~~~~~
			if (self.scope.getEnabled()):
				if ((func := self.scope.mouseMoveEvent) is not None):
					try:
						func(self.scope, event)

					except:
						self.scope.printErr(
							RFT_Exception.Traceback(),
							uidEnd = " : mouseMoveEvent()"
						)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~ Key Events ~~~~~~~~~~
	def keyPressEvent(self, event):
		if (not self.inst.editing):
			if (self.scope.getEnabled()):
				if ((func := self.scope.keyPressEvent) is not None):
					try:
						func(self.scope, event)

					except:
						self.scope.printErr(
							RFT_Exception.Traceback(),
							uidEnd = " : keyPressEvent()"
						)


	def keyReleaseEvent(self, event):
		if (not self.inst.editing):
			if (self.scope.getEnabled()):
				if ((func := self.scope.keyReleaseEvent) is not None):
					try:
						func(self.scope, event)

					except:
						self.scope.printErr(
							RFT_Exception.Traceback(),
							uidEnd = " : keyReleaseEvent()"
						)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



