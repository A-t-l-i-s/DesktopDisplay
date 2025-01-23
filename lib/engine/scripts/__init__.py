from engine.require import *

from .window import *





__all__ = ("Scripts",)





class Scripts(RFT_Object):
	scripts:list = []



	@classmethod
	def load(self, window, path:str, namespace:str = ""):
		path = Path(path)

		for d in path.iterdir():
			if (d.is_dir()):
				if ((m := (d / "main.py")).is_file()):
					while True:
						try:
							# Import module spec
							spec = importlib.util.spec_from_file_location("__RFTScript__", m)

							# Get module
							mod = importlib.util.module_from_spec(spec)

							# Compile module
							spec.loader.exec_module(mod)

							# Module dict to scope
							scope = RFT_Structure(mod.__dict__)

						except:
							if (RFT_Exception.Traceback().alert(f"{m}") != RFT_Exception.ALERT_RETRY):
								break

						else:
							script = RFT_Structure({
								"init": None,
								"draw": None,
								
								"settingsEvent": None,

								"mousePress": None,
								"mouseRelease": None,
								"mouseMove": None,

								"keyPress": None,
								"keyRelease": None,

								"path": d,
								"editing": False,

								"table": {},
								"window": {},
								
								"config": {},
								"settings": {}
							})


							# ~~~~~ Init Function ~~~~
							if (func := scope.get("init")):
								if (callable(func)):
									script.init = func
							# ~~~~~~~~~~~~~~~~~~~~~~~~

							# ~~~~ Paint Function ~~~~
							if (func := scope.get("draw")):
								if (callable(func)):
									script.draw = func
							# ~~~~~~~~~~~~~~~~~~~~~~~~

							# ~~~ Setting Function ~~~
							if (func := scope.get("settingsEvent")):
								if (callable(func)):
									script.settingsEvent = func
							# ~~~~~~~~~~~~~~~~~~~~~~~~


							# ~~~~~ Mouse Events ~~~~~
							if (func := scope.get("mousePress")):
								if (callable(func)):
									script.mousePress = func

							if (func := scope.get("mouseRelease")):
								if (callable(func)):
									script.mouseRelease = func

							if (func := scope.get("mouseMove")):
								if (callable(func)):
									script.mouseMove = func
							# ~~~~~~~~~~~~~~~~~~~~~~~~


							# ~~~~~~ Key Events ~~~~~~
							if (func := scope.get("keyPress")):
								if (callable(func)):
									script.keyPress = func

							if (func := scope.get("keyRelease")):
								if (callable(func)):
									script.keyRelease = func
							# ~~~~~~~~~~~~~~~~~~~~~~~~


							# ~~~~~~~~~ Table ~~~~~~~~
							name = namespace + d.name

							script.table = Tables.scripts.allocate(name)

							script.window = Tables.windows.allocate(name)
							# ~~~~~~~~~~~~~~~~~~~~~~~~


							# ~~~~~~~~ Settings ~~~~~~
							if ((p := (d / "settings.yaml")).is_file()):
								while True:
									with p.open("rb") as file:
										try:
											data = yaml.load(
												file,
												Loader = yaml.FullLoader
											)
										
										except:
											if (RFT_Exception.Traceback().alert(f"{p}") != RFT_Exception.ALERT_RETRY):
												break

										else:
											t = script.table.allocate("settings")
											
											if (data is not None):
												script.settings *= data

												for k, v in data.items():
													if (not t.contains(k)):
														t[k] = v.get("value", None)

											break
							# ~~~~~~~~~~~~~~~~~~~~~~~~


							# ~~~~~~~~~ Window ~~~~~~~
							if ((p := (d / "window.yaml")).is_file()):
								while True:
									with p.open("rb") as file:
										try:
											data = yaml.load(
												file,
												Loader = yaml.FullLoader
											)
										
										except:
											if (RFT_Exception.Traceback().alert(f"{p}") != RFT_Exception.ALERT_RETRY):
												break

										else:
											if (data is not None):
												script.window.default(data)
												break


							script.window.default({
								"title": d.name,

								"width": 200,
								"height": 200,

								"x": None,
								"y": None,
								"locked": False,

								"topmost": False,
								"transparent": False,
								"events": False
							})
							# ~~~~~~~~~~~~~~~~~~~~~~~~


							# ~~~~~ Create Window ~~~~
							try:
								win = Scripts_Window(window, script)
							
							except:
								if (RFT_Exception.Traceback().alert(f"{d} : Scripts_Window") != RFT_Exception.ALERT_RETRY):
									break

							else:
								self.scripts.append(win)
								break
							# ~~~~~~~~~~~~~~~~~~~~~~~~


				else:
					self.load(window, d, f"{d.name}_")

