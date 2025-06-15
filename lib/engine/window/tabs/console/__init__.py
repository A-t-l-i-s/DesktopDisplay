from engine.require import *
from engine.scripts import *

from .input import *
from .message import *





__all__ = ("Window_Tabs_Console",)





class Window_Tabs_Console(RFT_Object, QScrollArea):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.index = -1

		self.widget = QWidget(self)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~ Settings ~~~~~~~
		self.setWidgetResizable(True)

		self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
		self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

		self.setStyleSheet(Styles.core.scrollbar)

		self.setWidget(self.widget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Layout ~~~~~~~~
		self.layout = QVBoxLayout(self.widget)

		self.layout.setSpacing(3)
		self.layout.setContentsMargins(5, 5, 5, 5)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Widgets ~~~~~~~
		self.messageWidget = Window_Tabs_Console_Message(self)
		self.layout.addWidget(self.messageWidget)

		# self.inputWidget = Window_Tabs_Console_Input(self)
		# self.layout.addWidget(self.inputWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Timer ~~~~~~~~
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.reload)
		self.timer.start(1000 // 30)
		# ~~~~~~~~~~~~~~~~~~~~~~~~



	def reload(self):
		if (self.parent.currentWidget() == self and self.parent.parent.isVisible()):
			# Reset notif icon
			Scripts.consoleNotif = False

			while Scripts.console:
				try:
					# Get oldest console item
					line = Scripts.console.pop(0)
					uid = line[0]

					if (not Tables.console_blacklist.get(uid)):
						# Write to display
						self.write(
							uid,
							line[1],
							line[2],
							line[3]
						)

				except:
					# Write latest traceback to console
					self.write(
						"system",
						time.time(),
						RFT_Exception.Traceback().message(extra = False),
						True
					)



	def write(self, uid:str, timestamp:float, text:str, error:bool = False):
		w = self.messageWidget.widget
		timestampFmt = datetime.datetime.fromtimestamp(timestamp)

		# Add new line
		w.append("")
		
		# Add timestamp line
		w.setTextColor(QColor(200, 50, 200))
		w.insertPlainText(
			 f"[{timestampFmt.hour:>2}:{timestampFmt.minute:>2}:{str(timestampFmt.second) + '.' + str(timestampFmt.microsecond)[:4]:<7}]"
		)

		# Add uid line
		w.setTextColor(QColor(100, 80, 255))
		w.insertPlainText(
			f"({uid})"
		)

		# Add text deliminator line
		w.setTextColor(QColor(255, 255, 255))
		w.insertPlainText(": ")

		# Add text line
		if (error):
			w.setTextColor(QColor(255, 50, 50))
		else:
			w.setTextColor(QColor(255, 255, 255))

		w.insertPlainText(
			f"{text}"
		)




