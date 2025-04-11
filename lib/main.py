from engine.require import *

from engine.resources import *

from engine.tasks import *
from engine.window import *
from engine.updater import *
from engine.scripts import *





def main():
	# Check if already running
	if (not Tasks.isRunning()):
		# Terminate all previous running tasks
		Tasks.finishTasks()


		# Init qt application
		qtApp = QApplication([""])
		qtApp.setStyle("Fusion")


		# Load core resources
		Resources.loadCore()
		Resources.loadFonts()


		if (not Core.isExiting()):
			# Create window
			win = Window()
			win.hide()


			# Load script resources
			Resources.loadScripts(win)

			# Load scripts
			Scripts.load(win)
			Scripts.loadWindows(win)


			if (not Core.isExiting()):
				# Start main loop
				qtApp.exec()


			# Terminate all scripts
			Scripts.finish()

			# Terminate all tasks
			Tasks.finish()

			# Save all tables
			Resources.Tables_Obj.saveAll()
			Resources.Tables_Scripts_Obj.saveAll()


