from engine.require import *

from .scope import *
from .window import *





__all__ = ("Scripts",)





class Scripts(RFT_Object):
	"""
	Contains all scopes for all scripts

	Format: {uid:str = scope:Scripts_Scope}
	"""
	scopes:RFT_Structure = RFT_Structure()


	"""
	Used to determine if in edit mode
	"""
	editing:bool = False


	"""
	Table containing all enabled scripts

	Format: {uid:str = enabled:bool}
	"""
	enabled:RFT_Structure = Tables.enabled


	"""
	Contains queried contents and removes item when
	displayed on the console widget in settings.
	
	Format: [uid:str, timestamp:float, text:str, error:bool]
	"""
	console:list = []
	consoleNotif:bool = False



	# ~~~~~~~~ Finish ~~~~~~~~
	"""
	Turn editing mode off and call exit event on all scopes.
	"""
	@classmethod
	def finish(self):
		# Turn off editing mode
		self.stopEditing()

		# Call all exit events
		for key, scope in self.scopes.items():
			if (scope.getEnabled()):
				if ((func := scope.exitEvent) is not None):
					try:
						func(scope)

					except:
						...


	@classmethod
	def finishTasks(self):
		# Kill all tasks
		for p in psutil.process_iter():
			try:
				if (p.name() == Internal.programFileTask()):
					p.terminate()
					p.wait()

			except:
				...

		# Delete all instances
		path = Path("insts")
		for f in path.iterdir():
			try:
				os.remove(
					f.as_posix()
				)
			except:
				...
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~ Update ~~~~~~~~
	"""
	Update canvas on all scopes if window is present.
	"""
	@classmethod
	def update(self):
		for key, scope in self.scopes.items():
			if (scope.getEnabled()):
				if ((win := scope.gui) is not None):
					win.canvas.update()
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~ Restart Window ~~~~
	"""
	Close window and create a new one

	Args: window:QMainWindow (parent object), uid:str (scope id)
	"""
	@classmethod
	def restartWindow(self, window, uid:str):
		if ((scope := self.scopes.get(uid)) is not None):
			if (scope.gui is not None):
				scope.gui.close()
			
			scope.gui = None
			
			scope.inst.loadWindows(window, None, False)
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~ Editing ~~~~~~~~~~~
	"""
	Turn on edit mode and reload all windows with events enabled

	Args: uid:str (scope id)[optional]
	"""
	@classmethod
	def startEditing(self, uid:str = None):
		self.editing = True

		for key, scope in self.scopes.items():
			if (uid is None or uid == key):
				if (scope.getEnabled()):
					if ((win := scope.gui) is not None):
						# Turn events property on window
						win.reloadProperties(topmost = False, events = True)
						win.show()
						win.resizeWidget.show()


	"""
	Turn off edit mode and reload all windows with saved properties

	Args: uid:str (scope id)[optional]
	"""
	@classmethod
	def stopEditing(self, uid:str = None):
		self.editing = False

		for key, scope in self.scopes.items():
			if (uid is None or uid == key):
				if (scope.getEnabled()):
					if ((win := scope.gui) is not None):
						# Reset window properties
						win.reloadProperties()
						win.show()
						win.resizeWidget.hide()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~ Load Scripts ~~~~~~~~~
	"""
	Load all scripts from given path.
	Parent window is only provided for alerts.

	Args: window:QMainWindow, onlyId:str (load only that script by id)[optional]
	"""
	@classmethod
	def load(self, window, onlyId:str = None):
		# Create structure
		data = RFT_Structure()

		# Create path
		path = Path("res/scripts")

		# Allocate path
		path.mkdir(
			parents = True,
			exist_ok = True
		)

		if (path.is_dir()):
			for f in path.glob("**/*"):
				if (not f.is_dir()):
					# Get parent/child path
					parent = f.as_posix()
					child = Path(parent.replace(path.as_posix(), ""))
					filename = child.as_posix().strip("/")

					# Get attribute
					attr, ext = RFT_Resource.getAttr(child)

					# Create id
					uid = "_".join(attr)

					if (uid == onlyId or onlyId is None):
						# Get duplicate amount
						Tables.duplicates += {uid: []}

						dups = (uid, *Tables.duplicates[uid])


						if (ext in ("py", "pyc")):
							for idN in dups:
								if (not self.scopes.contains(idN)):
									# Create scope
									scope = Scripts_Scope(idN, uid)
									scope.inst = self
									scope.path = f.resolve()
									scope.duplicate = (idN != uid)

									while True:
										try:
											# Import module spec
											spec = importlib.util.spec_from_file_location("__DDScript__", f)

											# Get module
											mod = importlib.util.module_from_spec(spec)
											mod.__dict__["print"] = scope.print
											mod.__dict__["printErr"] = scope.printErr

											# Compile module
											spec.loader.exec_module(mod)

											# Module dict to scope
											struct = RFT_Structure(mod.__dict__)

											# Set value inside the parent
											if (struct.contains("main")):
												main = struct.main

												if (callable(main)):
													main(scope)

										except:
											scope.printErr(
												RFT_Exception.Traceback(),
												uidEnd = " : load"
											)

											scope.available = False
											break

										else:
											scope.available = True
											break


									# Add scope to enabled
									self.enabled += {scope.id: False}

									# Add scope to structure
									self.scopes[scope.id] = scope
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~ Load Scripts Window ~~~~~
	"""
	Load all scope gui's.

	Args: window:QMainWindow, onlyId:str (load only that script by id)[optional], callInit:bool (whether or not to call the init event)
	"""
	@classmethod
	def loadWindows(self, window, onlyId:str = None, callInit:bool = True):
		for key, scope in self.scopes.items():
			if (scope.id == onlyId or onlyId is None):
				if (scope.available):
					if ((win := scope.gui) is None):
						if (scope.getEnabled()):
							try:
								# ~~~~~~ Init Window ~~~~~
								win = Scripts_Window(scope, window)
								scope.gui = win
										
								# ~~~~~~~~~~ Init Script ~~~~~~~~~
								if (callInit):				
									if ((func := scope.initEvent) is not None):
										func(scope, win)

								# ~~~~~~ Show Window ~~~~~
								win.show()

								if (self.editing):
									self.startEditing(scope.id)
								else:
									self.stopEditing(scope.id)
								# ~~~~~~~~~~~~~~~~~~~~~~~~

							except:
								scope.printErr(
									RFT_Exception.Traceback(),
									uidEnd = " : init"
								)

					else:
						if (scope.getEnabled()):
							if (not win.isVisible()):
								win.show()

								if (self.editing):
									self.startEditing(scope.id)
								else:
									self.stopEditing(scope.id)

						else:
							win.hide()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~ ID ~~~~~~~~~~
	"""
	Generate new id based off uuid v4
	"""
	@classmethod
	def newId(self):
		return str(uuid.uuid4()).replace("-", "_")
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~ Console ~~~~~~~
	@classmethod
	def print(self, uid:str, val:object):
		if (not Internal.isTask()):
			self.console.append(
				(
					uid,
					time.time(),
					str(val),
					False
				)
			)

			if (Internal.isDebug()):
				# Print to console too
				self.printCon(
					uid,
					str(val)
				)

		else:
			# Only print to console too
			self.printCon(
				uid,
				str(val)
			)


	@classmethod
	def printErr(self, uid:str, exc:RFT_Exception):
		if (not Internal.isTask()):
			self.consoleNotif = True

			self.console.append(
				(
					uid,
					time.time(),
					exc.message(extra = False).strip(),
					True
				)
			)

			# Print error to console too
			if (Internal.isDebug()):
				self.printCon(
					uid,
					exc.message(extra = False).strip()
				)

		else:
			self.printCon(
				uid,
				exc.message(extra = False).strip()
			)



	@classmethod
	def printCon(self, uid:str, text:str):
		if (text):
			if (sys.stdout is not None):
				timestampFmt = datetime.datetime.now()

				try:
					print(
						f"[{timestampFmt.hour:>2}:{timestampFmt.minute:>2}:{str(timestampFmt.second) + '.' + str(timestampFmt.microsecond)[:4]:<7}]({uid}): {text}",
						end = '\n'
					)

				except:
					...
	# ~~~~~~~~~~~~~~~~~~~~~~~~

