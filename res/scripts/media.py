from engine.require import *
from engine.tasks import *

from winsdk.windows.storage.streams import Buffer, DataReader, InputStreamOptions
from winsdk.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager





class Script(RFT_Object):
	@classmethod
	def init(self, scope, window):
		self.titleFont = QFont("Dosis Bold", 26)
		self.artistFont = QFont("Dosis Bold", 18)

		self.titleColor = QColor(255, 255, 255)
		self.artistColor = QColor(255, 255, 255)

		self.title = None
		self.artist = None

		self.image = None
		self.average = QColor(0, 0, 0, 0)

		self.scope = scope


		# ~~~~~ Default Icons ~~~~
		self.iconsTitle = RFT_Structure({
			"Hulu | Series": "hulu",
			"Hulu | Watch": "hulu"
		})


		# ~~~~~~ New Thread ~~~~~~
		scope.launchThread(
			asyncio.run,
			(
				self.loop(scope),
			)
		)



	@classmethod
	def draw(self, scope, painter):
		w = scope.window.width
		h = scope.window.height


		m = scope.settings.margin
		m_ = m * 2


		# ~~~~~~~~~ Title ~~~~~~~~
		painter.setPen(self.titleColor)
		painter.setFont(self.titleFont)

		textFlags = (Qt.AlignmentFlag.AlignLeft if scope.settings.left else Qt.AlignmentFlag.AlignRight)

		# Draw title
		painter.drawText(
			m, h - 75 - m,
			w - m_, 50,
			Qt.AlignmentFlag.AlignVCenter | textFlags,
			self.title
		)
		# ~~~~~~~~~~~~~~~~~~~~~~~~

		# ~~~~~~~~ Artist ~~~~~~~~
		painter.setPen(self.artistColor)
		painter.setFont(self.artistFont)

		# Draw artist
		painter.drawText(
			m, h - 30 - m,
			w - m_, 40,
			Qt.AlignmentFlag.AlignTop | textFlags,
			self.artist
		)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~ Draw Image ~~~~~~
		if (self.image is not None):
			p = scope.settings.imagePadding
			p_ = p * 2


			# ~~~~~~ Background ~~~~~~
			path = QPainterPath()

			wi = self.image.width()
			hi = self.image.height()

			if (hi != scope.settings.imageSize):
				self.image = None
				self.title = None

			else:
				if (scope.settings.left):
					x = m
				else:
					x = (w - wi) - m - p_

				y = (h - hi) - m - p_ - 73

				path.addRoundedRect(
					x, y,
					wi + p_, hi + p_,
					5, 5
				)

				painter.fillPath(path, self.average)


				# ~~~~~~~~~ Image ~~~~~~~~
				painter.drawImage(
					x + p, y + p,
					self.image
				)



	@classmethod
	async def loop(self, scope):
		sessions = await MediaManager.request_async()
		
		while True:
			cur = sessions.get_current_session()

			if (cur):
				info = await cur.try_get_media_properties_async()

				# ~~~~~~~ Thumbnail ~~~~~~
				if ((title := info.title) != self.title):
					img = None

					scope.print(f"Now Playing \"{title}\" by \"{info.album_artist}\"")

					if ((thumb := info.thumbnail) is not None):
						buf = Buffer(2_500_000)

						stream = await thumb.open_read_async()
						await stream.read_async(buf, buf.capacity, InputStreamOptions.READ_AHEAD)
						stream.close()

						# ~~~~~~ Load Image ~~~~~~
						img = QImage()
						img.loadFromData(buf, "RGB888")
						# ~~~~~~~~~~~~~~~~~~~~~~~~


					else:
						if (title is not None):
							ti = self.iconsTitle.get(title)
							img = self.scope.images.get(ti)


					if (img is not None):
						# ~~~~~ Average Color ~~~~
						single = img.scaled(
							1, 1,
							Qt.AspectRatioMode.IgnoreAspectRatio,
							Qt.TransformationMode.SmoothTransformation
						)

						# Get pixel
						self.average = single.pixelColor(0, 0)

						self.titleColor = QColor(min(self.average.red() + 50, 255), min(self.average.green() + 50, 255), min(self.average.blue() + 50, 255))
						self.artistColor = QColor(min(self.average.red() + 30, 255), min(self.average.green() + 30, 255), min(self.average.blue() + 30, 255))

						self.average.setAlpha(100)
						# ~~~~~~~~~~~~~~~~~~~~~~~~


						# ~~~~~ Resize Image ~~~~~
						s = scope.settings.imageSize
						w = round(img.width() * (s / img.height()))

						self.image = img.scaled(
							w, s,
							Qt.AspectRatioMode.IgnoreAspectRatio,
							Qt.TransformationMode.SmoothTransformation
						)
						# ~~~~~~~~~~~~~~~~~~~~~~~~

					else:
						self.image = None
				# ~~~~~~~~~~~~~~~~~~~~~~~~

				# ~~~~~~~~~ Info ~~~~~~~~~
				self.title = title
				self.artist = info.artist
				self.genres = info.genres

				self.albumArtist = info.album_artist
				self.albumTitle = info.album_title
				# ~~~~~~~~~~~~~~~~~~~~~~~~


			await asyncio.sleep(0.1)





def main(scope):
	# ~~~~~~~ Settings ~~~~~~~
	scope.addSetting("margin", 6, scope.SETTINGS.INPUT, separator = True)

	scope.addSetting("imageSize", 300, scope.SETTINGS.INPUT)
	scope.addSetting("imagePadding", 3, scope.SETTINGS.INPUT, separator = True)

	scope.addSetting("left", False, scope.SETTINGS.TOGGLE)
	# ~~~~~~~~~~~~~~~~~~~~~~~~

	
	scope.setInitEvent(Script.init)
	scope.setDrawEvent(Script.draw)


