from engine.require import *





__all__ = ("Scripts_Window_Menu_Settings_Color",)





class Scripts_Window_Menu_Settings_Color(RFT_Object, QPushButton):
	def __init__(self, parent):
		super().__init__(parent.parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setFixedSize(*self.parent.size)
		self.setCursor(Qt.CursorShape.PointingHandCursor)
		
		self.reload()
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
			border-radius: 5px;
		""".format(*v))

		if (changed):
			if (self.parent.scope.getEnabled()):
				if ((func := self.parent.callback) is not None):
					try:
						func(self.parent.scope, k, v)

					except:
						self.parent.scope.printErr(
							RFT_Exception.Traceback(),
							uidEnd = f" : {k} : callback()"
						)



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

				self.parent.table[k] = self.parent.value
				self.reload(True)






