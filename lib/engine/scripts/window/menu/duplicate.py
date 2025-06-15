from engine.require import *





__all__ = ("Scripts_Window_Menu_Duplicate",)





class Scripts_Window_Menu_Duplicate(RFT_Object, QAction):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.scope = self.parent.parent.scope
		self.window = self.scope.window
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setText("Duplicate")

		self.setIcon(Icons.core.duplicate)

		self.setCheckable(False)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.triggered.connect(self._triggered)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _triggered(self):
		win = self.parent.parent.parent
		inst = self.scope.inst
		idS = self.scope.id

		# Create new id and table
		id_ = f"{idS}_{inst.newId()}"
		if ((dup := Tables.duplicates.get(idS)) is not None):
			# Add id to duplicates
			dup.append(id_)

			# Reload scripts
			inst.load(win, idS)

			# Enable scope
			scope = inst.scopes[id_]
			scope.setEnabled(True)

			# Reload window
			inst.loadWindows(win, id_)


