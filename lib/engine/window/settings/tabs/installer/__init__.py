from engine.require import *

from .item import *





__all__ = ("Window_Settings_Tabs_Installer",)





class Window_Settings_Tabs_Installer(RFT_Object, QScrollArea):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.reload = True

		self.widget = QWidget(self)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~ Settings ~~~~~~~
		self.setWidgetResizable(True)

		self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
		self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

		self.setStyleSheet(Styles.core.scrollbar)

		self.setWidget(self.widget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Layout ~~~~~~~~
		self.layout = QVBoxLayout(self.widget)

		self.layout.setSpacing(3)
		self.layout.setContentsMargins(5, 5, 5, 5)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		self.testWidget = Window_Settings_Tabs_Installer_Item(self, None)
		self.layout.addWidget(self.testWidget)


		# ~~~~~~~~ Thread ~~~~~~~~
		self.thread = threading.Thread(
			target = self.loop,
			args = (),
			kwargs = {},
			daemon = True
		)

		self.thread.start()
		# ~~~~~~~~~~~~~~~~~~~~~~~~



	def loop(self):
		while True:
			if (self.reload):
				try:
					req = requests.get(
						Data.updater.scripts.url,
						headers = {
							"User-Agent": "DesktopDisplay / 1.0.0"
						},
						json = True,
						timeout = 10
					)

				except:
					...

				else:
					try:
						data = RFT_Structure(
							req.json()
						)
					
					except:
						...

					else:
						... # Iterate and add all packages

				finally:
					self.reload = False


			time.sleep(0.1)


