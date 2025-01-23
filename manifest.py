from RFTLib.Rypple import *



scope = RFT_Rypple.begin(RFT_Rypple_Process, RFT_Rypple_Filesystem, RFT_Rypple_C, RFT_Rypple_CPP)

if (False):
	scope.run("windres src/res/icon.rc -O coff -o src/icon.res")
	scope.run("windres src/res/application.rc -O coff -o src/application.res")
	scope.wait()


	scope.inFile("src/main.cpp")
	scope.outFile("DesktopDisplay.exe")

	scope.includePath("src/include")
	scope.includePath("C:/Python311/include")

	scope.libraryPath("C:/Python311/libs")

	scope.library("python3")
	scope.library("python311")

	scope.bit(64)
	scope.version("c++20")
	scope.compression(2)
	scope.ui(False)

	scope.add("src/icon.res")
	scope.add("src/application.res")
	scope.add("-s")
	scope.add("-finput-charset=utf-8")
	scope.add("-fexec-charset=utf-8")

	scope.done().wait()

	scope.path("src/icon.res").delete()
	scope.path("src/application.res").delete()

if (True):
	scope.run("DesktopDisplay.exe").wait()

RFT_Rypple.end(scope)

