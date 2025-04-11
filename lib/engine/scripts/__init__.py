from engine.require import *

from .scope import *
from .window import *





__all__ = ("Scripts",)





class Scripts(RFT_Object):
	scopes:RFT_Structure = RFT_Structure()

	editing:bool = False

	enabled:RFT_Structure = Tables.enabled


	# ~~~~~~~~ Finish ~~~~~~~~
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
						RFT_Exception.Traceback().print()
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~ Update ~~~~~~~~
	@classmethod
	def update(self):
		for key, scope in self.scopes.items():
			if (scope.getEnabled()):
				if ((win := scope.gui) is not None):
					win.canvas.update()
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~ Editing ~~~~~~~~~~~
	@classmethod
	def startEditing(self):
		self.editing = True

		for key, scope in self.scopes.items():
			if (scope.getEnabled()):
				if ((win := scope.gui) is not None):
					# Turn events property on window
					win.reloadProperties(events = True)
					win.show()
					win.resizeWidget.show()

					# Hide all widgets in canvas
					for i in range(win.canvas.layout.count()):
						item = win.canvas.layout.itemAt(i)
						widget = item.widget()
						widget.hide()


	@classmethod
	def stopEditing(self):
		self.editing = False

		for key, scope in self.scopes.items():
			if (scope.getEnabled()):
				if ((win := scope.gui) is not None):
					if (not scope.window.hidden):
						# Reset window properties
						win.reloadProperties()
						win.show()
						win.resizeWidget.hide()

						# Show all widgets in canvas
						for i in range(win.canvas.layout.count()):
							item = win.canvas.layout.itemAt(i)
							widget = item.widget()
							widget.show()

					else:
						win.hide()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~ Load Scripts ~~~~~~~~~
	@classmethod
	def load(self, window):
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
					id_ = "_".join(attr)


					if (not self.scopes.contains(id_)):
						if (ext in ("py", "pyc")):
							# Create scope
							scope = Scripts_Scope(id_, self)
							scope.path = f.resolve()

							self.scopes[id_] = scope

							# Add scope to enabled
							self.enabled += {id_: False}

							while True:
								try:
									# Import module spec
									spec = importlib.util.spec_from_file_location("__DDScript__", f)

									# Get module
									mod = importlib.util.module_from_spec(spec)
									# mod.__dict__["print"] = scope.print

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
									if (window.alert(RFT_Exception.Traceback(), (window.alertWindow.ALERT_RETRY, window.alertWindow.ALERT_DISABLE), f"{id_}").wait() != window.alertWindow.ALERT_RETRY):
										self.enabled[id_] = False
										break

								else:
									break
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~ Load Scripts Window ~~~~~
	@classmethod
	def loadWindows(self, window):
		for key, scope in self.scopes.items():
			if ((win := scope.gui) is None):
				if (scope.getEnabled()):
					try:
						# ~~~~~~ Init Window ~~~~~
						win = Scripts_Window(scope, window)
						win.show()

						scope.gui = win
								
						# ~~~~~~~~~~ Init Script ~~~~~~~~~				
						if ((func := scope.initEvent) is not None):
							func(scope, win)

					except:
						if (window.alert_disable_ignore(f"{scope.id} : initEvent()").wait() != window.alertWindow.ALERT_IGNORE):
							self.enabled[id_] = False

			else:
				if (scope.getEnabled()):
					win.show()

				else:
					win.hide()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

