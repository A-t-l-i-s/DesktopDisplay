from engine.require import *

from engine.scripts import *
from engine.scripts.window import *

from .alert import *
from .timer import *
from .settings import *
from .system_tray import *






__all__ = ("Window",)





class Window(RFT_Object, QMainWindow):
	def __init__(self):
		super().__init__()


		# ~~~~~~~ Variables ~~~~~~
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		self.setWindowIcon(Icons.core.icon)
		self.setWindowTitle(Tables.window.title)

		self.setStyleSheet(Styles.core.menu)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~~ Timer ~~~~~~~~~~~~
		self.timer = Window_Timer(self)
		self.timer.start(1000 // Tables.window.rate)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# ~~~~~~~~~~ System Tray ~~~~~~~~~
		self.systemTray = Window_SystemTray(self)
		self.systemTray.show()
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# ~~~~~~~~~ Window Alert ~~~~~~~~~
		self.alertWindow = Window_Alert(self)
		self.alertWindow.hide()
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# ~~~~~~~~ Window Settings ~~~~~~~
		self.settingsWindow = Window_Settings(self)
		self.settingsWindow.hide()
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Alert ~~~~~~~~
	def alert(self, error:RFT_Exception, buttons:list | tuple = [Window_Alert.ALERT_OK], title:str = "Alert"):
		self.alertWindow.error = error
		self.alertWindow.buttons = buttons
		self.alertWindow.code = None

		self.alertWindow.setWindowTitle(title)

		self.alertWindow.messageWidget.reload()
		self.alertWindow.buttonsWidget.reload()

		return self.alertWindow


	def alert_retry_ignore(self, title:str = "Alert"):
		return self.alert(RFT_Exception.Traceback(), (self.alertWindow.ALERT_RETRY, self.alertWindow.ALERT_IGNORE), title)

	def alert_disable_ignore(self, title:str = "Alert"):
		return self.alert(RFT_Exception.Traceback(), (self.alertWindow.ALERT_DISABLE, self.alertWindow.ALERT_IGNORE), title)
	# ~~~~~~~~~~~~~~~~~~~~~~~~



	def closeEvent(self, event):
		self.exit()



	def exit(self):
		QApplication.closeAllWindows()
		QApplication.quit()

		Core.isExiting(True)
		Core.isRestarting(False)


	def restart(self):
		self.exit()

		Core.isExiting(True)
		Core.isRestarting(True)

