from engine.require import *
from engine.scripts import *





__all__ = ("Window_Tabs_Scripts_Item_Remove",)





class Window_Tabs_Scripts_Item_Remove(RFT_Object, QPushButton):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.scope = parent.scope
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setObjectName("remove")

		self.setToolTip("Delete")

		self.setIcon(Icons.core.remove)
		self.setCursor(Qt.CursorShape.PointingHandCursor)

		self.setFixedSize(30, 30)

		self.setStyleSheet(Styles.core.button + Styles.core.window.tabs.scripts)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
		self.clicked.connect(self._clicked)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _clicked(self):
		id_ = self.scope.id

		self.scope.setEnabled(False)

		if (self.scope.duplicate):
			if ((p := Tables.duplicates.get(self.scope.resId)) is not None):
				if (id_ in p):
					p.remove(id_)
					self.parent.deleteLater()

		else:
			path = self.parent.scope.path

			if (path.is_file()):
				try:
					os.remove(
						path
					)

				except:
					...

				else:
					self.parent.deleteLater()



		# Reload windows
		Scripts.loadWindows(
			self.parent.parent.parent.parent.parent
		)

		# Clear found widget
		f = self.parent.parent.found
		f[id_] = None

