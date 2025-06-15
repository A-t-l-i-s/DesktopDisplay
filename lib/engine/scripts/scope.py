from engine.require import *

from .window import *





__all__ = ("Scripts_Scope",)





class Scripts_Scope(RFT_Object):
	SETTINGS = RFT_Enum(
		(
			"COLOR",
			"INPUT",
			"TOGGLE",
			"RANGE",
			"LIST"
		)
	)


	def __init__(self, id_:str, resId:str = None):
		self.id = id_

		self.path = None

		self.inst = None
		self.available = False

		self.duplicate = False
		self.duplicateAllow = True

		# GUI
		self.gui = None


		# Resource ID
		"""
			Resource id's are used to access resources of
			that specific id (data, icons, images, styles, and localization).
			Used to make duplicate scripts to access resources and save resources to different id's.
		"""
		if (resId is None):
			self.resId = id_
		else:
			self.resId = resId


		# Resources
		self.data = Data.allocate(self.resId)
		self.icons = Icons.allocate(self.resId)
		self.images = Images.allocate(self.resId)
		self.styles = Styles.allocate(self.resId)

		# Localization
		self.locs = Locs.allocate(self.resId)
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



	# ~~~~~~~ Threading ~~~~~~
	def newThread(self, func, args:list | tuple = (), kwargs:dict | RFT_Structure = {}):
		def wrapper():
			try:
				# Call function
				func(
					*tuple(args),
					**dict(kwargs)
				)

			except:
				self.printErr(RFT_Exception.Traceback(), uidEnd = f" : {thread.name}")


		# Create new thread
		thread = threading.Thread(
			target = wrapper,
			args = (),
			kwargs = {},
			daemon = True
		)

		return thread


	def launchThread(self, func, args:list | tuple = (), kwargs:dict | RFT_Structure = {}):
		thread = self.newThread(func, args, kwargs)
		thread.start()

		return thread
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~ Tasks ~~~~~~~~
	def launchTask(self, filename:str, name:str, args:list | tuple = ()):
		def wrapper():
			while not Internal.isExiting():
				try:
					# Get process stdout
					line = process.stdout.readline()

					for l in line.split("\n"):
						l = l.strip()

						if (l):
							self.print(
								l,
								uidEnd = f" : {name}"
							)

				except:
					self.printErr(
						RFT_Exception("IO Disconnected"),
						uidEnd = f" : {name}"
					)
					break


		# Launch new process
		process = subprocess.Popen(
			[
				Internal.programFileTask(),
				(Path("res/tasks") / filename).as_posix(),
				name,
				*args
			],
			executable = Internal.programFileTask(),

			stdin = subprocess.PIPE,
			stdout = subprocess.PIPE,
			stderr = subprocess.STDOUT,
			text = True,

			creationflags = subprocess.CREATE_NO_WINDOW
		)

		# Create new thread
		self.launchThread(
			wrapper
		)

		return process
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~ Console ~~~~~~~
	def print(self, val:object, uidEnd:str = ""):
		self.inst.print(
			f"{self.id}{uidEnd}",
			val
		)


	def printErr(self, exc:RFT_Exception, uidEnd:str = ""):
		self.inst.printErr(
			f"{self.id}{uidEnd}",
			exc
		)
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~ Enabled ~~~~~~~
	def setEnabled(self, val:bool = True):
		self.inst.enabled[self.id] = val


	def getEnabled(self):
		return self.inst.enabled[self.id]
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~ Settings ~~~~~~~
	def addSetting(self, var:str, value, type_:str, *, callback:types.FunctionType = None, separator:bool = False):
		# Format Color Value
		if (type_ == self.SETTINGS.COLOR):
			if (isinstance(value, tuple | list)):
				value = list(value)
				value += [0, 0, 0, 0]
				value = value[:4]

			else:
				value = [0, 0, 0, 0]

		# Format Input Value
		elif (type_ == self.SETTINGS.INPUT):
			...

		# Format Toggle Value
		elif (type_ == self.SETTINGS.TOGGLE):
			value = bool(value)

		# Format Range Value
		elif (type_ == self.SETTINGS.RANGE):
			if (isinstance(value, int | float)):
				value = max(min(value, 1.0), 0.0)

			else:
				value = 0.0

		# Format List Value
		elif (type_ == self.SETTINGS.LIST):
			if (isinstance(value, tuple | list)):
				value = list(value)
				value += [None, None]

				l = value[1]

				if (isinstance(l, tuple | list)):
					value[1] = list(l)

				value = value[:2]


		# Add settings to collection
		self.settingsDefault[var] = {
			"value": value,
			"type": type_,

			"callback": callback,
			"separator": separator
		}

		# Add setting value
		if (not self.settings.contains(var)):
			self.settings[var] = value


	def addSettingSeparator(self):
		if ((k := self.settingsDefault.last()) is not None):
			self.settingsDefault[k].separator = True
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

