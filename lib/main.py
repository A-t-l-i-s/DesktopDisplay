from engine.require import *

from engine.window import *
from engine.scripts import *
from engine.scripts.window import *





def main():
	# Create window
	win = Window()
	win.hide()


	# Load scripts
	Scripts.load(win, "res/scripts")


	# Run app
	QtApp.exec()


	return win.restarting

