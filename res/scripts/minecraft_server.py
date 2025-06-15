from engine.require import *
from engine.tasks import *

from mcstatus import JavaServer, BedrockServer





class Window:
	@classmethod
	def init(self, scope, window):
		# Minecraft server
		if (scope.settings.bedrock):
			self.server = BedrockServer.lookup(f"{scope.settings.ip}:{scope.settings.port}")

		else:
			self.server = JavaServer.lookup(f"{scope.settings.ip}:{scope.settings.port}")

		self.serverReload = True
		self.serverName = None
		self.serverIcon = None
		self.serverPing = None
		
		self.serverOnline = [0, 0]
		self.serverPlayers = []
		self.serverHeads = RFT_Structure()


		# Fonts
		self.nameFont = QFont("Dosis ExtraBold", 14)
		self.onlineFont = QFont("Dosis SemiBold", 12)
		self.headsFont = QFont("Dosis SemiBold", 14)
		self.pingFont = QFont("Dosis SemiBold", 10)


		# Thread
		scope.launchThread(
			self.run,
			(scope,),
		)



	# ~~~~~~~~~ Draw ~~~~~~~~~
	@classmethod
	def draw(self, scope, painter):
		w = scope.window.width
		h = scope.window.height

		colorBg = QColor(*scope.settings.colorBg)
		colorName = QColor(*scope.settings.colorName)
		colorOnline = QColor(*scope.settings.colorOnline)
		colorPlayer = QColor(*scope.settings.colorPlayer)
		colorPing = QColor(*scope.settings.colorPing)


		# Background
		painter.fillRect(
			0, 0,
			w, h,
			colorBg
		)


		# ~~~~~~~~~ Ping ~~~~~~~~~
		y = 10

		if (self.serverPing is not None):
			c = QColor(0, 255, 0)
			p = self.serverPing

		else:
			c = QColor(255, 0, 0)
			p = 0

		# Status Icon
		painter.setBrush(QBrush(c))
		painter.setPen(QColor(0, 0, 0, 0))

		painter.drawEllipse(
			10, y,
			10, 10
		)

		# Ping Text
		painter.setPen(colorPing)

		painter.drawText(
			25, y,
			100, 10,
			Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft,
			f"{p:.0f}ms"
		)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		if (self.serverName is not None):			
			if (self.serverIcon is not None):
				# ~~~~~~~~~ Icon ~~~~~~~~~
				s = scope.settings.iconSize
				l = 3
				x = w // 2 - s // 2

				painter.drawImage(x, y, self.serverIcon)

				y += s
				# ~~~~~~~~~~~~~~~~~~~~~~~~


			# ~~~~~~~~~ Name ~~~~~~~~~
			painter.setPen(colorName)
			painter.setFont(self.nameFont)

			y += 10
			h_ = 25 * (self.serverName.count("\n") + 1)

			# Draw date text
			painter.drawText(
				0, y,
				w, h_,
				Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
				self.serverName
			)
			# ~~~~~~~~~~~~~~~~~~~~~~~~

			# ~~~~~~~~ Online ~~~~~~~~
			painter.setPen(colorOnline)
			painter.setFont(self.onlineFont)

			y += h_

			# Draw date text
			painter.drawText(
				0, y,
				w, 20,
				Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
				f"{self.serverOnline[0]}/{self.serverOnline[1]}"
			)
			# ~~~~~~~~~~~~~~~~~~~~~~~~

			# ~~~~~~~~ Players ~~~~~~~
			painter.setPen(colorOnline)
			painter.setFont(self.headsFont)

			y += 25


			for p in self.serverPlayers:
				if ((img := self.serverHeads.get(p)) is not None):
					s = scope.settings.headSize

					x = w // 2 - 10 - s - 10 - 40

					painter.drawImage(x, y, img)

					x = w // 2 - 40

					painter.drawText(
						x, y,
						w - x, s,
						Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft,
						p
					)

					y += s + 10
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~ Run ~~~~~~~~~
	@classmethod
	def run(self, scope):
		while not Internal.isExiting():
			try:
				stat = self.server.status()
			
			except:
				self.serverPing = None
				self.serverReload = True

			else:
				self.serverOnline[0] = stat.players.online
				self.serverOnline[1] = stat.players.max

				self.serverPing = stat.latency
				
				name = ""
				for p in stat.motd.parsed:
					if (isinstance(p, str)):
						name += p

				self.serverName = name


				if (self.serverReload):
					self.serverReload = False

					# ~~~~~~~~~ Icon ~~~~~~~~~
					if (not scope.settings.bedrock):
						mime, icon = stat.icon.split(",")
						
						iconRaw = base64.b64decode(icon)

						img = QImage()
						img.loadFromData(iconRaw, "RGB888")

						s = scope.settings.iconSize

						# Resize image
						img = img.scaled(
							s, s,
							Qt.AspectRatioMode.IgnoreAspectRatio,
							Qt.TransformationMode.FastTransformation
						)

						self.serverIcon = img
					# ~~~~~~~~~~~~~~~~~~~~~~~~


				# ~~~~~~~~ Players ~~~~~~~
				if (not scope.settings.bedrock):
					try:
						query = self.server.query()

					except:
						...

					else:
						self.serverPlayers.clear()

						for v in query.players.names:
							self.serverPlayers.append(v)

							if (not self.serverHeads.contains(v)):
								req = requests.get(
									f"https://mc-heads.net/head/{v}/{scope.settings.headSize}",
									headers = {
										"User-Agent": "DesktopDisplay_MJS/1.0"
									}
								)

								if (req.status_code == 200):
									# Get image data
									data = req.content


									# Create new image and allocate it with image data
									img = QImage()
									img.loadFromData(data, "RGB888")

									self.serverHeads[v] = img
					# ~~~~~~~~~~~~~~~~~~~~~~~~

			finally:
				time.sleep(1)
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~ Settings Update ~~~
	@classmethod
	def settingsUpdate(self, scope, key, value):
		if (key in ("ip", "port", "bedrock", "iconSize", "headSize")):
			self.serverName = None
			self.serverIcon = None
			self.serverPing = None

			self.serverPlayers.clear()
			
			if (scope.settings.bedrock):
				self.server = BedrockServer.lookup(f"{scope.settings.ip}:{scope.settings.port}")

			else:
				self.server = JavaServer.lookup(f"{scope.settings.ip}:{scope.settings.port}")

			self.serverReload = True
	# ~~~~~~~~~~~~~~~~~~~~~~~~



def main(scope):
	scope.addSetting("ip", "127.0.0.1", scope.SETTINGS.INPUT, callback = Window.settingsUpdate)
	scope.addSetting("port", 25565, scope.SETTINGS.INPUT, callback = Window.settingsUpdate)
	scope.addSetting("bedrock", False, scope.SETTINGS.TOGGLE, callback = Window.settingsUpdate)

	scope.addSettingSeparator()

	scope.addSetting("iconSize", 64, scope.SETTINGS.INPUT, callback = Window.settingsUpdate)
	scope.addSetting("headSize", 32, scope.SETTINGS.INPUT, callback = Window.settingsUpdate)

	scope.addSettingSeparator()

	scope.addSetting("colorBg", [0, 0, 0, 100], scope.SETTINGS.COLOR)
	scope.addSetting("colorName", [255, 255, 255], scope.SETTINGS.COLOR)
	scope.addSetting("colorPing", [255, 255, 255], scope.SETTINGS.COLOR)
	scope.addSetting("colorOnline", [255, 255, 255], scope.SETTINGS.COLOR)
	scope.addSetting("colorPlayer", [255, 255, 255], scope.SETTINGS.COLOR)

	
	scope.setInitEvent(Window.init)
	scope.setDrawEvent(Window.draw)


