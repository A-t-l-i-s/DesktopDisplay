from engine.require import *





__all__ = ("Script",)





class Script(RFT_Object):
	default = {	
		"enabled": False,

		"enableNetwork": True,
		"enableCPU": True,
		"enableMemory": True,
		"enableBorder": True,

		"networkColor": [255, 255, 255, 255],
		
		"cpuColor": [255, 255, 255, 255],
		"cpuColorProgress": [255, 255, 255, 255],

		"memoryColor": [255, 255, 255, 255],
		"memoryColorProgress": [255, 255, 255, 255],

		"borderColor": [255, 255, 255, 255]
	}


	# ~~~~~~~~~~ Init ~~~~~~~~
	@classmethod
	def init(self, table):
		self.table = table
		
		if (self.table.enabled and Tables.window.debug):
			self.data = RFT_Structure({
				"cpu": 0,
				"memory": 0,

				"netSent": "0 Kbps",
				"netSentAvg": "0 Kbps",
				"netSentMax": "0 Kbps",

				"netRecv": "0 Kbps",
				"netRecvAvg": "0 Kbps",
				"netRecvMax": "0 Kbps",
			})

			# Colors
			self.networkColor = QColor(*self.table.networkColor)

			self.cpuColor = QColor(*self.table.cpuColor)
			self.cpuColorProgress = QColor(*self.table.cpuColorProgress)

			self.memoryColor = QColor(*self.table.memoryColor)
			self.memoryColorProgress = QColor(*self.table.memoryColorProgress)

			self.borderColor = QColor(*self.table.borderColor)

			self.transparent = QColor(0, 0, 0, 0)

			# Fonts
			self.defaultFont = QFont("Dosis ExtraBold", 12)
			self.netTitleFont = QFont("Dosis ExtraBold", 14)
			self.netUsageFont = QFont("Dosis Bold", 11)
			self.netAvgFont = QFont("Dosis Bold", 10)
			self.netMaxFont = QFont("Dosis Bold", 10)


			# Attach structure to listening surver
			Server.attach(self.data, "system_server")
	# ~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Paint ~~~~~~~~
	@classmethod
	def paint(self, painter):
		if (self.table.enabled and Tables.window.debug):
			# Get screen size
			w = painter.parent.width()
			h = painter.parent.height()

			barH = 140

			xS = 50

			yS = h - 10
			if (s := Tables.scripts.get("system")):
				if (s.enabled):
					yS = h - 10 - barH - 75

			ySS = yS - 70 - barH - 70

			# Set font family/color
			painter.setBrush(self.transparent)



			if (self.table.enableNetwork):
				# ~~~~~~~~ Network ~~~~~~~
				painter.setPen(self.networkColor)
				painter.setFont(self.netTitleFont)

				sep1 = 95
				sep2 = 185

				painter.drawText(
					xS - 45, yS - sep1 - 10,
					100, 60,
					Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
					"Net Out"
				)

				painter.drawText(
					xS - 45, yS - sep2 - 10,
					100, 60,
					Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
					"Net In"
				)


				painter.setFont(self.netUsageFont)

				painter.drawText(
					xS - 45, yS - sep1 + 12,
					100, 60,
					Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
					f"{self.data.netSent}"
				)

				painter.drawText(
					xS - 45, yS - sep2 + 12,
					100, 60,
					Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
					f"{self.data.netRecv}"
				)



				painter.setFont(self.netAvgFont)

				painter.drawText(
					xS - 45, yS - sep1 + 28,
					100, 60,
					Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
					f"*{self.data.netSentAvg}"
				)

				painter.drawText(
					xS - 45, yS - sep2 + 28,
					100, 60,
					Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
					f"*{self.data.netRecvAvg}"
				)



				painter.setFont(self.netMaxFont)

				painter.drawText(
					xS - 45, yS - sep1 + 42,
					100, 60,
					Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
					f">{self.data.netSentMax}"
				)

				painter.drawText(
					xS - 45, yS - sep2 + 42,
					100, 60,
					Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
					f">{self.data.netRecvMax}"
				)

				xS += 70
				# ~~~~~~~~~~~~~~~~~~~~~~~~


			if (self.table.enableCPU):
				# ~~~~~~~~~~ CPU ~~~~~~~~~
				painter.setPen(self.cpuColor)
				painter.setFont(self.defaultFont)
				
				cp = self.data.cpu

				# Draw border
				painter.drawRect(
					xS, yS - 60,
					10, -barH
				)

				# Fill border
				painter.fillRect(
					xS, yS - 60,
					11, round(-barH * cp),
					self.cpuColorProgress
				)


				# Draw text
				painter.drawText(
					xS - 45, yS - 60,
					100, 60,
					Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
					f"CPU\n{round(cp * 100, 2):02}%"
				)

				xS += 60
				# ~~~~~~~~~~~~~~~~~~~~~~~~


			if (self.table.enableMemory):
				# ~~~~~~~~ Memory ~~~~~~~~
				painter.setPen(self.memoryColor)
				painter.setFont(self.defaultFont)

				mem = self.data.memory

				# Draw border
				painter.drawRect(
					xS, yS - 60,
					10, -barH
				)

				# Fill border
				painter.fillRect(
					xS, yS - 60,
					11, round(-barH * mem),
					self.memoryColorProgress
				)

				# Draw text
				painter.drawText(
					xS - 45, yS - 60,
					100, 60,
					Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
					f"Memory\n{round(mem * 100, 2):02}%"
				)
				
				xS += 70
				# ~~~~~~~~~~~~~~~~~~~~~~~~


			if (self.table.enableBorder):
				# Draw border
				painter.fillRect(10, yS, xS - 80 + 45, 2, self.borderColor)
	# ~~~~~~~~~~~~~~~~~~~~~~~~





	@classmethod
	def formatBytes(self, size):
		for unit in ("", "K", "M", "G", "T", "P", "E", "Z"):
			if abs(size) < 1024.0:
				return f"{size:3.1f} {unit}bps"

			size /= 1024.0

		return f"{size:.1f} Ybps"





