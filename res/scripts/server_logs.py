from engine.require import *





__all__ = ("Script",)





class Script(RFT_Object):
	default = {	
		"enabled": False,

		"width": 400,
		"height": 600,
	}


	# ~~~~~~~~~~ Init ~~~~~~~~
	@classmethod
	def init(self, table):
		self.table = table
		
		if (self.table.enabled and Tables.window.debug):
			self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			self.socket.bind(("", 9603))

			self.lines = collections.deque([], maxlen = math.ceil(self.table.height / 20))
	# ~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~ Run ~~~~~~~~~
	@classmethod
	def run(self):
		while (self.table.enabled and Tables.window.debug):
			data, addr = self.socket.recvfrom(8192)

			buf = RFT_Buffer(data)
			s = buf.toStr()

			t = re.sub(r"[\[\]]", "", s)
			m = shlex.split(t)

			ip = m[0].strip()
			tmstmp = m[3].strip()
			meth = m[5].strip()
			status = m[6].strip()
			uri = m[8].strip()
			headers = m[9].strip()

			self.lines.append(
				f"{ip} {status} {uri} {headers}"
			)
	# ~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Paint ~~~~~~~~
	@classmethod
	def paint(self, painter):
		if (self.table.enabled and Tables.window.debug):
			painter.setPen(QColor(255, 255, 255))
			painter.setFont(QFont("Dosis Bold", 7))

			h = self.table.height
			l = math.ceil(h / 20)
			s = 200

			path = QPainterPath()

			path.addRoundedRect(
				5, s,
				self.table.width + 8, (l * 20) + 2,
				10, 10
			)

			painter.fillPath(path, QColor(0, 0, 0, 100))


			for i, l in enumerate(self.lines):
				painter.drawText(
					5 + 4, i * 20 + s + 4,
					self.table.width - 4, 20,
					Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft,
					l
				)
	# ~~~~~~~~~~~~~~~~~~~~~~~~





