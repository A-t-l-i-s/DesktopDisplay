from engine.require import *





__all__ = ("Script",)





class Script(RFT_Object):
	default = {	
		"enabled": False,
		
		"enableVolume": True,
		"enableBass": True,
		"enableTreble": True,
		"enableBorder": True,

		"height": 75,
		"spacing": 150,
		"frames": 60,

		"borderColor": [255, 255, 255, 255]
	}


	# ~~~~~~~~~~ Init ~~~~~~~~
	@classmethod
	def init(self, table):
		self.table = table
		
		if (self.table.enabled):
			# Colors
			self.borderColor = QColor(*self.table.borderColor)

			# RTA Server
			self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			self.socket.bind(("", 9600))


			amt = self.table.frames

			self.rmsL = collections.deque([0] * amt, maxlen = amt)
			self.bassL = collections.deque([0] * amt, maxlen = amt)
			self.trebleL = collections.deque([0] * amt, maxlen = amt)
	# ~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~ Run ~~~~~~~~~
	@classmethod
	def run(self):
		while (self.table.enabled):
			data, addr = self.socket.recvfrom(4)

			self.rmsL.append(data[0] / 0xff)
			self.bassL.append(data[1] / 0xff)
			self.trebleL.append(data[3] / 0xff)

			time.sleep(0.01)
	# ~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Paint ~~~~~~~~
	@classmethod
	def paint(self, painter):
		if (self.table.enabled):
			# ~~~~~~~ Variables ~~~~~~
			# Get screen size
			w = painter.parent.width()
			h = painter.parent.height()

			w_ = (w / 2)
			r = self.table.spacing

			le = self.table.frames
			s = (w_ - r) / (le - 1)
			h = self.table.height

			st = round(w_ - r)
			pos = st - 1
			rpos = round(pos)
			sep = s / 3
			sepr = round(sep)

			prevRms = [round(self.rmsL[-1] * h), 0]
			prevBass = [round(self.bassL[-1] * h), 0]
			prevTreble = [round(self.trebleL[-1] * h), 0]
			# ~~~~~~~~~~~~~~~~~~~~~~~~


			# ~~~~~~~~ Border ~~~~~~~~
			if (self.table.enableBorder):
				painter.setPen(self.borderColor)

				painter.drawLine(st, 0, st, h + 1)
				painter.drawLine(st, h + 1, 0, h + 1)
			# ~~~~~~~~~~~~~~~~~~~~~~~~


			for i in range(le):
				i_ = le - 1 - (i + 1)

				rms = self.rmsL[i_]
				bass = self.bassL[i_]
				treble = self.trebleL[i_]


				if (self.table.enableVolume):
					# ~~~~~~~~~~~~ Volume ~~~~~~~~~~~~
					y = round(rms * h)
					d = prevRms[1] - rms

					painter.setPen(
						c := QColor(
							min(round(max(abs(d), rms) * 255), 255),
							0,
							min(round(abs(d) * 255 + 150), 255),
						)
					)

					painter.drawLine(
						round(pos - s),
						h - y,
						rpos,
						h - prevRms[0]
					)

					prevRms[0] = y
					prevRms[1] = rms
					# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


				if (self.table.enableTreble):
					# ~~~~~~~~~~~~ Treble ~~~~~~~~~~~~
					y = round(treble * (h - 1))
					d = prevTreble[1] - treble

					painter.setPen(
						c := QColor(
							200,
							min(round(abs(d) * 255 + 100), 255),
							0,
						)
					)

					painter.drawLine(
						round(pos - s),
						h - y - 1,
						rpos,
						h - prevTreble[0] - 1
					)

					prevTreble[0] = y
					prevTreble[1] = treble
					# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


				if (self.table.enableBass):
					# ~~~~~~~~~~~~~ Bass ~~~~~~~~~~~~~
					y = round(bass * (h - 2))
					d = prevBass[1] - bass

					painter.setPen(
						c := QColor(
							0,
							200,
							min(round(abs(d) * 255 + 120), 255),
						)
					)

					painter.drawLine(
						round(pos - s),
						h - y - 2,
						rpos,
						h - prevBass[0] - 2
					)

					prevBass[0] = y
					prevBass[1] = bass
					# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



				pos -= s
				rpos = round(pos)
	# ~~~~~~~~~~~~~~~~~~~~~~~~
