from engine.require import *





__all__ = ("Scripts_Window_Menu_Settings_Toggle",)





class Scripts_Window_Menu_Settings_Toggle(RFT_Object, QCheckBox):
	def __init__(self, parent):
		super().__init__(parent.parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.reload()
		
		self.setCursor(Qt.CursorShape.PointingHandCursor)

		self.setStyleSheet(Styles.core.toggle)
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
						win = self.parent.scope.gui.parent

						if (win.alert_disable_ignore(f"{self.parent.scope.id} : {k}.callback()").wait() != win.alertWindow.ALERT_IGNORE):
							self.parent.callback = None


	def _triggered(self):
		k = self.parent.key

		self.parent.value = self.isChecked()
		self.parent.table[k] = self.parent.value

		self.reload(True)







