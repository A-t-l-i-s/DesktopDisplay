from RFTLib.Rypple import *



scope = RFT_Rypple.begin(RFT_Rypple_Process, RFT_Rypple_Filesystem, RFT_Rypple_C, RFT_Rypple_CPP)

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
	scope.add("-D DEBUG")

	scope.run("windres src/resource.rc -O coff -o src/resource.res -D DEBUG")
	scope.wait()

	scope.ui(False)
	scope.outFile("DesktopDisplay_Debug.exe")
	scope.done().wait()


	# Multiprocessing/Task Mode
	scope.add("-D TASK")

	scope.run("windres src/resource.rc -O coff -o src/resource.res -D DEBUG -D TASK")
	scope.wait()

	scope.ui(False)
	scope.outFile("DesktopDisplay_Task.exe")
	scope.done().wait()
	

	# Delete resources
	scope.path("src/resource.res").remove()


else:
	scope.run("DesktopDisplay_Debug.exe").wait()


RFT_Rypple.end(scope)

