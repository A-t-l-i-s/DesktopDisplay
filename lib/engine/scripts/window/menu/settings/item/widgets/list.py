from engine.require import *





__all__ = ("Scripts_Window_Menu_Settings_List",)





class Scripts_Window_Menu_Settings_List(RFT_Object, QComboBox):
	def __init__(self, parent):
		super().__init__(parent.parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setFixedSize(*self.parent.size)

		self.setEditable(False)
		self.setCursor(Qt.CursorShape.PointingHandCursor)

		self.setStyleSheet(Styles.core.list)

		for t in self.parent.value[1]:
			self.addItem(t)

		self.reload()
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.currentIndexChanged.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def reload(self, changed = False):
		k = self.parent.key
		v = self.parent.value[0]

		self.setCurrentText(v)

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

		self.parent.value[0] = self.currentText()
		self.parent.table[k][0] = self.parent.value[0]

		self.reload(True)







