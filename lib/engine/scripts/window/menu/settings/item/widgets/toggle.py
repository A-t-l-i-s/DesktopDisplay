from engine.require import *





__all__ = ("Scripts_Window_Menu_Settings_Toggle",)





class Scripts_Window_Menu_Settings_Toggle(RFT_Object, QCheckBox):
	def __init__(self, parent):
		super().__init__(parent.parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~		
		self.setCursor(Qt.CursorShape.PointingHandCursor)

		self.setStyleSheet(Styles.core.toggle)

		self.reload()
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.checkStateChanged.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def reload(self, changed = False):
		k = self.parent.key
		v = self.parent.value

		self.setChecked(v)

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

		self.parent.value = self.isChecked()
		self.parent.table[k] = self.parent.value

		self.reload(True)







