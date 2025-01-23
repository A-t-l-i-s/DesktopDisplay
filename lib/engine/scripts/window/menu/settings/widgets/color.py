from engine.require import *





__all__ = ("Scripts_Window_Menu_Settings_Color",)





class Scripts_Window_Menu_Settings_Color(RFT_Object, QPushButton):
	def __init__(self, parent):
		super().__init__(parent.parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.reload()

		self.setFixedSize(70, 20)
		self.setCursor(Qt.CursorShape.PointingHandCursor)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.clicked.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def reload(self, changed = False):
		k = self.parent.key
		v = self.parent.value

		self.setStyleSheet("""
			background-color: rgba({0}, {1}, {2}, {3});
			border: 1px solid rgb({0}, {1}, {2});
		""".format(*v))

		if (changed):
			# ~~~ Setting Function ~~~
			if ((func := self.parent.script.settingsEvent) != None):
				while True:
					try:
						func(self.parent.parent.parent.parent, k, v)

					except:
						if (RFT_Exception.Traceback().alert(f"{self.parent.script.path} : settingsEvent()") != RFT_Exception.ALERT_RETRY):
							break

					else:
						break



	def _triggered(self):
		k = self.parent.key
		v = self.parent.value


		dialog = QColorDialog(self.parent.parent)
		dialog.setOptions(QColorDialog.ColorDialogOption.ShowAlphaChannel)
		dialog.setCurrentColor(QColor(*v))

		dialog.setWindowFlags(
			Qt.WindowType.Tool |
			Qt.WindowType.FramelessWindowHint |
			Qt.WindowType.WindowStaysOnTopHint
		)

		if (dialog.exec()):
			c = dialog.currentColor()

			if (c):
				self.parent.value = [
					c.red(),
					c.green(),
					c.blue(),
					c.alpha()
				]

				self.parent.settings[k] = self.parent.value
				self.reload(True)






