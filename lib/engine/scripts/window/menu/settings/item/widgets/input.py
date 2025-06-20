from engine.require import *





__all__ = ("Scripts_Window_Menu_Settings_Input",)





class Scripts_Window_Menu_Settings_Input(RFT_Object, QLineEdit):
	def __init__(self, parent):
		super().__init__(parent.parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setFixedSize(*self.parent.size)
		self.setStyleSheet(Styles.core.input)

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
					self.parent.table[k] = value
					self.reload(True)

					

			finally:
				self.setText(None)

		else:
			self.parent.table[k] = v






