from engine.require import *
from engine.resources import *
from engine.window import *
from engine.scripts import *





__all__ = ("main", "task")





def main():
	try:
		# Check if already running
		if (not Tasks.isRunning()):
			# Init qt application
			qtApp = QApplication([""])
			qtApp.setStyle("Fusion")


			# Load all resources
			Resources.loadFonts(Scripts)
			Resources.loadResources(Scripts)


			if (not Internal.isExiting()):
				# Create window
				win = Window()
				win.hide()

				# Load scripts
				Scripts.load(win)
				Scripts.loadWindows(win)


				if (not Internal.isExiting()):
					# Start main loop
					qtApp.exec()


				# Terminate all scripts and tasks
				Scripts.finish()
				Scripts.finishTasks()

				# Save all tables
				Resources.Tables_Obj.saveAll()
				Resources.Tables_Scripts_Obj.saveAll()

	except:
		RFT_Exception.Traceback().alert("Unable to start")





def task(path):
	try:
		# Get parent/child path
		path = Path(path)

		if (path.is_file()):
			# Import module spec
			spec = importlib.util.spec_from_file_location("__DDTask__", path)

			# Get module
			mod = importlib.util.module_from_spec(spec)

			# Compile module
			spec.loader.exec_module(mod)

			# Module dict to scope
			struct = RFT_Structure(mod.__dict__)

			# Set value inside the parent
			if (struct.contains("main")):
				main = struct.main

				if (callable(main)):
					main()

	except:
		RFT_Exception.Traceback().print()

