import sys
import time
from RFTLib.Rypple import *



scope = RFT_Rypple.begin(RFT_Rypple_Process, RFT_Rypple_Filesystem, RFT_Rypple_C, RFT_Rypple_CPP)

if (sys.platform == "win32"):
	if (False):
		scope.run("windres src/resource.rc -O coff -o src/resource.res")
		scope.wait()

		scope.inFile("src/main.cpp")
		scope.outFile("DesktopDisplay.exe")

		scope.includePath("src/include")

		scope.libraryPath("C:/Python311/libs")
		scope.includePath("C:/Python311/include")

		scope.library("python3")
		scope.library("python311")

		scope.bit(64)
		scope.version("c++20")
		scope.compression(2)
		scope.add("src/resource.res")
		scope.add("-s")


		# Compile in production mode
		# scope.add("-D PRODUCTION")


		# Windowed Mode
		scope.ui(True)
		scope.done().wait()


		# Consoled Mode
		scope.define("DEBUG")

		scope.run("windres src/resource.rc -O coff -o src/resource.res -D DEBUG")
		scope.wait()

		scope.ui(False)
		scope.outFile("DesktopDisplay_Debug.exe")
		scope.done().wait()


		# Multiprocessing/Task Mode
		scope.defineRemove("DEBUG")
		scope.define("TASK")

		scope.run("windres src/resource.rc -O coff -o src/resource.res -D TASK")
		scope.wait()

		scope.ui(False)
		scope.outFile("DesktopDisplay_Task.exe")
		scope.done().wait()
		

		# Delete resources
		scope.path("src/resource.res").remove()


	else:
		scope.run("DesktopDisplay_Debug.exe").wait()
		# scope.run("DesktopDisplay_Task.exe res/tasks/rta_task.py TEST_TASK --is_output").wait()
		# while True:
		# 	print("Poll")
		# 	scope.run("DesktopDisplay_Debug.exe").wait()
		# 	time.sleep(1)


RFT_Rypple.end(scope)

