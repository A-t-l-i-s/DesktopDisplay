from engine.require import *
from engine.scripts import *





__all__ = ("Window_Tabs_Console_Input",)





class Window_Tabs_Console_Input(RFT_Object, QLineEdit):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.commands = RFT_Structure({
			"clear": self.consoleClear,
		})
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~ Settings ~~~~~~~
		self.setStyleSheet(Styles.core.input)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Events ~~~~~~~~
		self.editingFinished.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		text = self.text()
		text = text.strip()

		if (text):
			# Split into arguments
			args = shlex.split(text)
			values = []

			# Get command
			cmd = args.pop(0)

			for t in args:
				try:
					v = eval(
						t
					)
				
				except:
					values.append(t)

				else:
					values.append(v)


			if (cmd):
				if ((func := self.commands.get(cmd)) is not None):
					try:
						r = func(
							*values
						)
						
						if (r is not None):
							Scripts.print(
								f"command : {cmd}",
								r
							)

					except:
						Scripts.printErr(
							f"command : {cmd}",
							RFT_Exception.Traceback()
						)


		self.clear()



	def consoleClear(self):
		self.parent.messageWidget.widget.clear()
		

