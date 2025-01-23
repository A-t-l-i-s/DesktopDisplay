from engine.require import *





__all__ = ("Scripts_Window_Menu_Settings_Input",)





class Scripts_Window_Menu_Settings_Input(RFT_Object, QLineEdit):
	def __init__(self, parent):
		super().__init__(parent.parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.reload()
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.editingFinished.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def reload(self, changed = False):
		k = self.parent.key
		v = self.parent.value

		self.setPlaceholderText(str(v))
		
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
		text = self.text()
		text = text.strip()

		k = self.parent.key
		v = self.parent.value


		if (text):
			try:
				if (isinstance(v, str)):
					value = text

				else:
					value = ast.literal_eval(text)
			
			except:
				...

			else:
				if (isinstance(value, type(v)) or v is None):
					self.parent.value = value
					self.parent.settings[k] = value
					self.reload(True)

					

			finally:
				self.setText(None)

		else:
			self.parent.settings[k] = v






