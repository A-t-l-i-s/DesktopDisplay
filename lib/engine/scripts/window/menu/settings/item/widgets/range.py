from engine.require import *





__all__ = ("Scripts_Window_Menu_Settings_Range",)





class Scripts_Window_Menu_Settings_Range(RFT_Object, QSlider):
	def __init__(self, parent):
		super().__init__(Qt.Orientation.Horizontal, parent.parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent

		self.minumum = 0
		self.maximum = 100
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setFixedSize(*self.parent.size)

		self.setCursor(Qt.CursorShape.PointingHandCursor)
		
		self.setTickInterval(1)
		self.setTickPosition(QSlider.TickPosition.NoTicks)

		self.setMinimum(self.minumum)
		self.setMaximum(self.maximum)

		self.setStyleSheet(Styles.core.range)

		self.reload()
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.valueChanged.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def reload(self, changed = False):
		k = self.parent.key
		v = self.parent.value

		self.setValue(
			self.minumum + round(self.parent.value * self.maximum)
		)

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

		self.parent.value = self.value() / 100
		self.parent.table[k] = self.parent.value

		self.reload(True)







