from engine.require import *





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

		self.setStyleSheet(Styles.core.button + Styles.core.settings.tabs.tasks)
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
			win = self.parent.parent.parent.parent.parent

			win.alert(RFT_Exception.Traceback(), (win.alertWindow.ALERT_OK,), f"Failed to kill process {self.parent.data.pid}").wait()


