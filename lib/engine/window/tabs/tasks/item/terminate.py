from engine.require import *
from engine.scripts import *





__all__ = ("Window_Settings_Tabs_Tasks_Item_Terminate",)





class Window_Settings_Tabs_Tasks_Item_Terminate(RFT_Object, QPushButton):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setObjectName("terminate")

		self.setIcon(Icons.core.close)
		self.setCursor(Qt.CursorShape.PointingHandCursor)

		self.setFixedSize(30, 30)

		self.setStyleSheet(Styles.core.button + Styles.core.window.tabs.tasks)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.clicked.connect(self._clicked)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _clicked(self):
		try:
			proc = psutil.Process(self.parent.data.pid)

			proc.terminate()
			proc.wait()

		except:
			Scripts.printErr(
				"system",
				f"Failed to kill process {self.parent.data.pid}"
			)


