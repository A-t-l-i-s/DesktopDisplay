from engine.require import *




# ~~~~~~~~~~~~~ Init ~~~~~~~~~~~~~
def init(self):
	self.show()

	self.titleFont = QFont("Dosis Bold", 20)
	self.artistFont = QFont("Dosis Bold", 16)

	self.title = None
	self.artist = None

	self.image = None
	self.average = QColor(0, 0, 0, 0)

	r = RFT_Resource(
		self.script.path / "icons",
		{
			r"png": RFT_Resource_QT_QIMAGE,
		}
	)

	self.icons = r.load()
	self.iconsTitle = RFT_Structure({
		"Hulu | Series": "hulu",
		"Hulu | Watch": "hulu"
	})


	# ~~~~~~ Drop Shadow ~~~~~
	self.shadow = QGraphicsDropShadowEffect()
	self.shadow.setEnabled(self.settings.dropShadow)
			
	self.shadow.setBlurRadius(self.settings.dropShadowRadius)
	self.shadow.setOffset(self.settings.dropShadowX, self.settings.dropShadowY)
	self.shadow.setColor(self.average)

	self.setGraphicsEffect(self.shadow)
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# Start Loop Thread
	self.startThread(
		asyncio.run,
		(
			loop(self),
		)
	)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# ~~~~~~~~ Settings Event ~~~~~~~~
def settingsEvent(self, key, value):
	if (key == "dropShadow"):
		self.shadow.setEnabled(value)

	elif (key == "dropShadowRadius"):
		self.shadow.setBlurRadius(value)

	elif (key == "dropShadowX" or key == "dropShadowY"):
		self.shadow.setOffset(
			self.settings.dropShadowX,
			self.settings.dropShadowY
		)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# ~~~~~~~~~~~~~ Loop ~~~~~~~~~~~~~
async def loop(self):
	sessions = await MediaManager.request_async()
	
	while True:
		cur = sessions.get_current_session()

		if (cur):
			info = await cur.try_get_media_properties_async()

			# ~~~~~~~ Thumbnail ~~~~~~
			if ((title := info.title) != self.title):					
				img = None

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
						img = self.icons.get(ti)


				if (img is not None):
					# ~~~~~ Average Color ~~~~
					single = img.scaled(
						1, 1,
						Qt.AspectRatioMode.IgnoreAspectRatio,
						Qt.TransformationMode.SmoothTransformation
					)

					# Get pixel
					self.average = single.pixelColor(0, 0)

					self.shadow.setColor(self.average)

					self.average.setAlpha(100)
					# ~~~~~~~~~~~~~~~~~~~~~~~~


					# ~~~~~ Resize Image ~~~~~
					s = self.settings.imageSize
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
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# ~~~~~~~~~~~~~ Draw ~~~~~~~~~~~~~
def draw(self, painter):
	w = self.width()
	h = self.height()

	# Init Colors
	titleColor = QColor(*self.settings.titleColor)
	artistColor = QColor(*self.settings.artistColor)
	progressColor = QColor(*self.settings.progressColor)


	m = self.settings.margin
	m_ = m * 2


	# ~~~~~~~~~ Title ~~~~~~~~
	painter.setPen(titleColor)
	painter.setFont(self.titleFont)

	textFlags = Qt.AlignmentFlag.AlignTop | (Qt.AlignmentFlag.AlignLeft if self.settings.left else Qt.AlignmentFlag.AlignRight)

	# Draw title
	painter.drawText(
		m, h - 50 - m,
		w - m_, 40,
		textFlags,
		self.title
	)
	# ~~~~~~~~~~~~~~~~~~~~~~~~

	# ~~~~~~~~ Artist ~~~~~~~~
	painter.setPen(artistColor)
	painter.setFont(self.artistFont)

	# Draw artist
	painter.drawText(
		m, h - 20 - m,
		w - m_, 25,
		textFlags,
		self.artist
	)
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~ Draw Image ~~~~~~
	if (self.image is not None):
		p = self.settings.imagePadding
		p_ = p * 2


		# ~~~~~~ Background ~~~~~~
		path = QPainterPath()

		wi = self.image.width()
		hi = self.image.height()

		if (hi != self.settings.imageSize):
			self.image = None
			self.title = None

		else:
			if (self.settings.left):
				x = m
			else:
				x = (w - wi) - m - p_

			y = (h - hi) - m - p_ - 53

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
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


