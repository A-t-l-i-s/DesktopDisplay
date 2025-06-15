from engine.require import *

from .info import *
from .settings import *





__all__ = ("Window_Settings_Tabs_Window",)





class Window_Settings_Tabs_Window(RFT_Object, QScrollArea):
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

		self.layout.setSpacing(5)
		self.layout.setContentsMargins(5, 5, 5, 5)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Widgets ~~~~~~~
		self.settingsWidget = Window_Settings_Tabs_Window_Settings(self)
		self.layout.addWidget(self.settingsWidget)

		self.infoWidget = Window_Settings_Tabs_Window_Info(self)
		self.layout.addWidget(self.infoWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Timer ~~~~~~~~
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.reload)
		self.timer.start(500)
		# ~~~~~~~~~~~~~~~~~~~~~~~~



	def reload(self):
		self.infoWidget.fpsWidget.reload()
		self.infoWidget.threadsWidget.reload()
		self.infoWidget.tasksWidget.reload()



