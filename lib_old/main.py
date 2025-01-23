from engine.require import *
from engine.window import *
from engine.updater import *





def main():
	if (ver := Updater.latest()):
		if (Updater.download(ver)):
			return True


	if (not Server.running):
		if (RFT_Exception("Instance already running", RFT_Exception.CRITICAL).alert() == RFT_Exception.ALERT_RETRY):
			return True
		else:
			return False


	# Create window
	win = Window()
	win.show()

	# Lower window
	win.lower()
	
	# Run app
	QtApp.exec()


	return win.restarting


