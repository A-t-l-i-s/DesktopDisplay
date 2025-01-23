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
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.checkStateChanged.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def reload(self, changed = False):
		k = self.parent.key
		v = self.parent.value

		self.setChecked(v)

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

		self.parent.value = self.isChecked()
		self.parent.settings[k] = self.parent.value

		self.reload(True)







