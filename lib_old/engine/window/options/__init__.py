from engine.require import *

from .options_list import *
from .buttons_list import *





__all__ = ("Window_Options",)





class Window_Options(RFT_Object, QMainWindow):
	def __init__(self, parent):
		super().__init__()


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.widget = QFrame()
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setWindowIcon(Icons.icon)
		self.setWindowTitle("Desktop Display Options")

		self.setWindowFlags(
			Qt.WindowType.Tool |
			Qt.WindowType.FramelessWindowHint |
			Qt.WindowType.WindowStaysOnTopHint
		)


		self.width = self.parent.width // 4
		self.height = self.parent.height // 2

		self.x = self.parent.x + self.parent.width // 2 - self.width // 2
		self.y = self.parent.y + self.parent.height // 2 - self.height // 2

		# Size
		self.move(self.x, self.y)
		self.setFixedSize(self.width, self.height)

		self.setStyleSheet(Styles.options)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Central Widget ~~~~~~~~
		self.widget = QWidget()

		self.setCentralWidget(self.widget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QVBoxLayout()
		self.layout.setSpacing(0)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

		self.widget.setLayout(self.layout)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Widgets ~~~~~~~~~~~
		self.optionsList = Window_OptionsList(self)
		self.layout.addWidget(self.optionsList)

		self.buttonsList = Window_ButtonsList(self)
		self.layout.addWidget(self.buttonsList)




	def start(self):
		self.parent.timer.paused = True

		self.optionsList.reload()
		self.show()



	def stop(self):
		self.parent.timer.paused = False

		self.hide()





