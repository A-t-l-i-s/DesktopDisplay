from engine.require import *

from .item import *





__all__ = ("Window_Settings_Tabs_Tasks",)





class Window_Settings_Tabs_Tasks(RFT_Object, QScrollArea):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.index = -1

		self.tasks = RFT_Structure()
		self.queue = []
		self.path = Path("insts")

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


		# ~~~~~~~~ Thread ~~~~~~~~
		self.thread = threading.Thread(
			target = self.loop,
			args = (),
			kwargs = {},
			daemon = True
		)

		self.thread.start()
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Timer ~~~~~~~~
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.reload)
		self.timer.start(100)
		# ~~~~~~~~~~~~~~~~~~~~~~~~



	def reload(self):
		if (self.parent.currentWidget() == self and self.parent.parent.isVisible()):
			if (len(self.queue)):
				d = self.queue.pop(0)

				# Create new item
				widget = Window_Settings_Tabs_Tasks_Item(self, d)
				self.layout.addWidget(widget)

				d.widget = widget

				self.update()



	def loop(self):
		while not Internal.isExiting():
			if ((self.parent.currentWidget() == self or self.parent.currentWidget() == self.parent.windowWidget) and self.parent.parent.isVisible()):
				if (self.path.is_dir()):
					for f in self.path.iterdir():
						if (f.is_file()):
							try:
								with f.open("rb") as file:
									chunk = file.read(1024)

								attrs = chunk.split(b"\x01")
								
								name = str(attrs[0], "utf-8")
								pid = int(attrs[1])
								timestamp = float(attrs[2])
								
								alive = psutil.pid_exists(pid)
							except:
								...

							else:
								id_ = f"task_{pid}"

								if ((d := self.tasks.get(id_)) is not None):
									if (not alive):
										if ((w := d.widget) is not None):
											self.tasks.pop(id_)
											w.deleteLater()

											try:
												os.remove(
													f.as_posix()
												)
											except:
												...

									else:
										if ((w := d.widget) is not None):
											s = (time.time() - d.time)
											c = "s"
											
											if (s >= 60):
												s /= 60
												c = "m"

												if (s >= 60):
													s /= 60
													c = "h"

													if (s >= 24):
														s /= 24
														c = "d"

														if (s >= 7):
															s /= 7
															c = "w"

											w.timeLabel.setText(f"{s:.1f}{c}")

								else:
									if (alive):
										# Data structure
										d = RFT_Structure({
											"name": name,
											"pid": pid,
											"widget": None,
											"time": timestamp
										})

										# Add task
										self.tasks[id_] = d

										# Add task to queue
										self.queue.append(d)



			time.sleep(0.13)



