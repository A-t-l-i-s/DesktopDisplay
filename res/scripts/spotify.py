from engine.require import *
from engine.tasks import *

import spotipy





class Window(RFT_Object):
	@classmethod
	def init(self, scope, window):
		self.scope = scope


		# ~~~~~~~~ Colors ~~~~~~~~
		self.titleFont = QFont("Dosis Bold", 26)
		self.artistFont = QFont("Dosis Bold", 18)

		self.titleColor = QColor(255, 255, 255)
		self.artistColor = QColor(255, 255, 255)
		self.progressColor = QColor(255, 255, 255)

		self.average = QColor(0, 0, 0, 0)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Spotify ~~~~~~~
		self.client = None
		
		self.current = None
		self.currentImage = None
		self.currentImageUrl = None
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Threads ~~~~~~~
		scope.launchThread(
			self.run
		)
		# ~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Draw ~~~~~~~~~
	@classmethod
	def draw(self, scope, painter):
		w = scope.window.width
		h = scope.window.height

		m = scope.settings.margin
		m_ = m * 2


		if ((song := self.current) is not None):
			# ~~~~~~~~~ Title ~~~~~~~~
			painter.setPen(self.titleColor)
			painter.setFont(self.titleFont)

			textFlags = (Qt.AlignmentFlag.AlignLeft if scope.settings.left else Qt.AlignmentFlag.AlignRight)

			# Draw title
			painter.drawText(
				m, h - 65 - m,
				w - m_, 50,
				Qt.AlignmentFlag.AlignVCenter | textFlags,
				song.title
			)
			# ~~~~~~~~~~~~~~~~~~~~~~~~

			# ~~~~~~~~ Artist ~~~~~~~~
			painter.setPen(self.artistColor)
			painter.setFont(self.artistFont)

			# Draw artist
			painter.drawText(
				m, h - m - 20,
				w - m_, 40,
				Qt.AlignmentFlag.AlignTop | textFlags,
				song.artistsStr
			)
			# ~~~~~~~~~~~~~~~~~~~~~~~~


			# ~~~~~~~ Progress ~~~~~~~
			s = scope.settings.size

			if (scope.settings.left):
				x = m
			else:
				x = w - m - s
			
			y = h - m - 66

			prog = round((song.progress[0] / song.progress[1]) * s)
			progH = 4

			painter.fillRect(
				x, y,
				prog, progH,
				self.progressColor
			)
			# ~~~~~~~~~~~~~~~~~~~~~~~~


			# ~~~~~~ Draw Image ~~~~~~
			if ((img := self.currentImage) is not None):
				if (not scope.settings.left):
					x = (w - s) - m

				y = y - s - 9

				# ~~~~~~~~~ Image ~~~~~~~~
				painter.drawImage(
					x, y,
					img
				)
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~ Settings Update ~~~
	@classmethod
	def settingsUpdate(self, scope, key, value):
		if (key in ("clientId", "secretId", "redirectUri")):
			self.client = None
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~ Run ~~~~~~~~~
	@classmethod
	def run(self):
		while not Internal.isExiting():
			if (self.client is None):
				self.connect()

			else:
				p = self.playing()

				if (p):
					i = p.pop("image")

					# Check if song title changed
					if (self.current is None or (self.current is not None and self.current.title != p.title)):
						# Print to console
						self.scope.print(f"Now Playing \"{p.title}\" by \"{p.artistsStr}\"")

					# Change current song
					self.current = p

					if (self.currentImageUrl != i):
						self.currentImageUrl = i

						req = requests.get(
							i,
							headers = {
								"User-Agent": "DesktopDisplay_Spotify/1.0"
							}
						)

						if (req.status_code == 200):
							# Get image data
							data = req.content


							# Create new image and allocate it with image data
							img = QImage()
							img.loadFromData(data, "RGB888")

							s = self.scope.settings.size

							# Resize image
							img = img.scaled(
								s, s,
								Qt.AspectRatioMode.IgnoreAspectRatio,
								Qt.TransformationMode.FastTransformation
							)

							self.currentImage = img


							# Resize Image
							single = img.scaled(
								1, 1,
								Qt.AspectRatioMode.IgnoreAspectRatio,
								Qt.TransformationMode.SmoothTransformation
							)

							# Get pixel
							self.average = single.pixelColor(0, 0)
							
							self.progressColor = QColor(min(self.average.red() + 120, 255), min(self.average.green() + 120, 255), min(self.average.blue() + 120, 255))
							self.titleColor = QColor(min(self.average.red() + 80, 255), min(self.average.green() + 80, 255), min(self.average.blue() + 80, 255))
							self.artistColor = QColor(min(self.average.red() + 50, 255), min(self.average.green() + 50, 255), min(self.average.blue() + 50, 255))

			# Wait
			time.sleep(0.66)
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~ Playing ~~~~~~~
	@classmethod
	def playing(self):
		if (self.client is not None):
			# Get currently playing
			try:
				current = self.client.current_playback()
			
			except:
				current = None

			else:
				if (current):
					data = RFT_Structure(current)

					if (data.contains(("item", "is_playing", "progress_ms"))):
						# Get item
						item = data.item

						if (item):
							if (item.contains(("name", "artists", "duration_ms", "album"))):
								i = None
								m = 0
								for v in item.album.images:
									if (v["width"] == 300):
										i = v["url"]
										break

									if ((w := v["width"]) > m):
										m = w
										i = v["url"]

								# Get all artists
								artists = []

								for a in data.item.artists:
									artists.append(
										a["name"]
									)


								# Format artist's text
								match len(artists):
									case 0:
										# No artists -_-
										arts = ""

									case 1:
										# Single artists
										arts = artists[0]

									case 2:
										# Two artists
										arts = " and ".join(artists)

									case _:
										# Three or more artists
										arts = ", ".join(artists[:-1]) + ", and "  + artists[-1]


								# Build and retrun data
								return RFT_Structure({
									"title": item.name,
									"artists": artists,
									"artistsStr": arts,
									"playing": data.is_playing,
									"image": i,

									"progress": (
										data.progress_ms,
										item.duration_ms
									)
								})

		return None
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~ Connect ~~~~~~~
	@classmethod
	def connect(self):
		# Reset client
		self.client = None
		
		# Get client and secret id
		clientId = self.scope.settings.clientId
		secretId = self.scope.settings.secretId
		redirectUri = self.scope.settings.redirectUri


		if (clientId and secretId and redirectUri):
			try:
				self.client = spotipy.Spotify(
					oauth_manager = spotipy.oauth2.SpotifyOAuth( # Spotify OAuth Authentication
						client_id = clientId, # Client ID
						client_secret = secretId, # Secret Client ID
						redirect_uri = redirectUri, # Redirect URI
						scope = "user-read-playback-state user-read-currently-playing", # Access Scopes,
						cache_path = "res/spotify.cache" # Change cache location
					)
				)

			except:
				self.scope.printErr(RFT_Exception.Traceback())
	# ~~~~~~~~~~~~~~~~~~~~~~~~





def main(scope):
	# ~~~~~~~ Settings ~~~~~~~
	scope.addSetting("margin", 6, scope.SETTINGS.INPUT)
	scope.addSetting("size", 300, scope.SETTINGS.INPUT)
	scope.addSetting("left", False, scope.SETTINGS.TOGGLE, separator = True)

	scope.addSetting("clientId", "", scope.SETTINGS.INPUT, callback = Window.settingsUpdate)
	scope.addSetting("secretId", "", scope.SETTINGS.INPUT, callback = Window.settingsUpdate)
	scope.addSetting("redirectUri", "", scope.SETTINGS.INPUT, callback = Window.settingsUpdate)
	# ~~~~~~~~~~~~~~~~~~~~~~~~

	
	scope.setInitEvent(Window.init)
	scope.setDrawEvent(Window.draw)

