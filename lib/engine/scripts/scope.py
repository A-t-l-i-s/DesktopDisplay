from engine.require import *

from .window import *





__all__ = ("Scripts_Scope",)





class Scripts_Scope(RFT_Object):

	SETTINGS_COLOR:int = 0
	SETTINGS_INPUT:int = 1
	SETTINGS_TOGGLE:int = 2


	def __init__(self, id_:str, inst:RFT_Object):
		self.id = id_

		self.path = None

		self.inst = inst


		# GUI
		self.gui = None


		# Console
		self.console = RFT_Buffer()


		# Resources
		self.data = Data.allocate(self.id)
		self.icons = Icons.allocate(self.id)
		self.images = Images.allocate(self.id)
		self.styles = Styles.allocate(self.id)

		# Localization
		self.locs = Locs.allocate(self.id)
		self.locs.allocate("settings")


		# Table
		self.table = Tables_Scripts[self.id]


		# Window
		self.window = self.table.allocate("window")
		self.window += Data.core.defaults.scripts.window
		self.windowDefault = self.window.copy()


		# Settings
		self.settings = self.table.allocate("settings")
		self.settingsDefault = RFT_Structure()
		self.settingsDefault += Data.core.defaults.scripts.settings


		# Functions
		self.initEvent = None
		self.drawEvent = None
		self.exitEvent = None

		self.moveEvent = None
		self.resizeEvent = None

		self.mousePressEvent = None
		self.mouseReleaseEvent = None
		self.mouseMoveEvent = None

		self.keyPressEvent = None
		self.keyReleaseEvent = None



	# ~~~~~~~~ Console ~~~~~~~
	def print(self, val:str, end:str = "\n"):
		self.console += str(val) + str(end)
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~ Enabled ~~~~~~~
	def setEnabled(self, val:bool = True):
		self.inst.enabled[self.id] = val


	def getEnabled(self):
		return self.inst.enabled[self.id]
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~ Settings ~~~~~~~
	def addSetting(self, var:str, value, type_:str, *, callback:types.FunctionType = None, separator:bool = False):
		self.settingsDefault[var] = {
			"value": value,
			"type": type_,

			"callback": callback,
			"separator": separator
		}

		if (not self.settings.containsInst(var, type(value))):
			self.settings[var] = value
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~ Events ~~~~~~~~
	def setInitEvent(self, func):
		if (callable(func)):
			self.initEvent = func

	def setDrawEvent(self, func):
		if (callable(func)):
			self.drawEvent = func

	def setExitEvent(self, func):
		if (callable(func)):
			self.exitEvent = func


	def setMoveEvent(self, func):
		if (callable(func)):
			self.moveEvent = func

	def setResizeEvent(self, func):
		if (callable(func)):
			self.resizeEvent = func


	def setMousePressEvent(self, func):
		if (callable(func)):
			self.mousePressEvent = func

	def setMouseReleaseEvent(self, func):
		if (callable(func)):
			self.mouseReleaseEvent = func

	def setMouseMoveEvent(self, func):
		if (callable(func)):
			self.mouseMoveEvent = func


	def setKeyPressEvent(self, func):
		if (callable(func)):
			self.keyPressEvent = func

	def setKeyReleaseEvent(self, func):
		if (callable(func)):
			self.keyReleaseEvent = func
	# ~~~~~~~~~~~~~~~~~~~~~~~~

