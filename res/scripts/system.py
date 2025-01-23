from engine.require import *





__all__ = ("Script",)





class Script(RFT_Object):
	default = {	
		"enabled": True,

		"enableNetwork": True,
		"enableCPU": True,
		"enableMemory": True,
		"enableDisks": True,
		"enableBorder": True,

		"networkColor": [255, 255, 255, 255],
		
		"cpuColor": [255, 255, 255, 255],
		"cpuColorProgress": [255, 255, 255, 255],

		"memoryColor": [255, 255, 255, 255],
		"memoryColorProgress": [255, 255, 255, 255],

		"disksColor": [255, 255, 255, 255],
		"disksColorProgress": [255, 255, 255, 255],

		"borderColor": [255, 255, 255, 255]
	}


	# ~~~~~~~~~~ Init ~~~~~~~~
	@classmethod
	def init(self, table):
		self.table = table

		if (self.table.enabled):
			# System
			self.cpuUsage = [0, collections.deque([0], 10)]
			self.memoryUsage = [0, collections.deque([0], 10)]

			self.diskUsage = RFT_Structure()

			# Network
			self.netSent = ""
			self.netRecv = ""

			self.netSentAvg = ""
			self.netRecvAvg = ""

			self.netSentAvgL = collections.deque([0], 50)
			self.netRecvAvgL = collections.deque([0], 50)

			self.netSentUsage = 0
			self.netRecvUsage = 0

			self.netSentMax = 0
			self.netRecvMax = 0

			# Colors
			self.networkColor = QColor(*self.table.networkColor)

			self.cpuColor = QColor(*self.table.cpuColor)
			self.cpuColorProgress = QColor(*self.table.cpuColorProgress)

			self.memoryColor = QColor(*self.table.memoryColor)
			self.memoryColorProgress = QColor(*self.table.memoryColorProgress)
			
			self.disksColor = QColor(*self.table.disksColor)
			self.disksColorProgress = QColor(*self.table.disksColorProgress)

			self.borderColor = QColor(*self.table.borderColor)

			self.transparent = QColor(0, 0, 0, 0)

			# Fonts
			self.defaultFont = QFont("Dosis ExtraBold", 12)
			self.netTitleFont = QFont("Dosis ExtraBold", 14)
			self.netUsageFont = QFont("Dosis Bold", 11)
			self.netAvgFont = QFont("Dosis Bold", 10)
			self.netMaxFont = QFont("Dosis Bold", 10)


			# Start threads
			threading._start_new_thread(self.cpuLoop, (), {}) # CPU
			threading._start_new_thread(self.memoryLoop, (), {}) # Memory
			threading._start_new_thread(self.networkLoop, (), {}) # Network
			threading._start_new_thread(self.diskLoop, (), {}) # Disk
	# ~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Paint ~~~~~~~~
	@classmethod
	def paint(self, painter):
		if (self.table.enabled):
			# Get screen size
			w = painter.parent.width()
			h = painter.parent.height()

			barH = 140

			xS = 50
			yS = h - 10

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
					f"{self.netSent}"
				)

				painter.drawText(
					xS - 45, yS - sep2 + 12,
					100, 60,
					Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
					f"{self.netRecv}"
				)



				painter.setFont(self.netAvgFont)

				painter.drawText(
					xS - 45, yS - sep1 + 28,
					100, 60,
					Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
					f"*{self.netSentAvg}"
				)

				painter.drawText(
					xS - 45, yS - sep2 + 28,
					100, 60,
					Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
					f"*{self.netRecvAvg}"
				)



				painter.setFont(self.netMaxFont)

				painter.drawText(
					xS - 45, yS - sep1 + 42,
					100, 60,
					Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
					f">{self.netSentMax}"
				)

				painter.drawText(
					xS - 45, yS - sep2 + 42,
					100, 60,
					Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
					f">{self.netRecvMax}"
				)

				xS += 70
				# ~~~~~~~~~~~~~~~~~~~~~~~~


			if (self.table.enableCPU):
				# ~~~~~~~~~~ CPU ~~~~~~~~~
				painter.setPen(self.cpuColor)
				painter.setFont(self.defaultFont)

				cp = self.cpuUsage[0]

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

				mem = self.memoryUsage[0]

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

				xS += 80
				# ~~~~~~~~~~~~~~~~~~~~~~~~

			
			if (self.table.enableDisks):
				# ~~~~~~~~~ Disks ~~~~~~~~
				painter.setPen(self.disksColor)
				painter.setFont(self.defaultFont)

				# Get disks keys
				ks = tuple(self.diskUsage.keys())

				for k in ks:
					v = self.diskUsage.get(k)
					if (v != None):
						# Draw border
						painter.drawRect(
							xS, yS - 60,
							10, -barH
						)

						# Fill border
						painter.fillRect(
							xS, yS - 60,
							11, round(-barH * v),
							self.disksColorProgress
						)

						# Draw text
						painter.drawText(
							xS - 45, yS - 60,
							100, 60,
							Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
							f"{k}\n{round(v * 100, 2):02}%"
						)

						xS += 60
				# ~~~~~~~~~~~~~~~~~~~~~~~~

			if (self.table.enableBorder):
				# Draw border
				painter.fillRect(10, yS, xS - 80 + 45, 2, self.borderColor)
	# ~~~~~~~~~~~~~~~~~~~~~~~~



	@classmethod
	def cpuLoop(self):
		while (self.table.enabled):
			# CPU Percent
			u = psutil.cpu_percent() / 100

			# Get list of previous usages
			l = self.cpuUsage[1]
			l.append(u)

			# Set average cpu percent
			self.cpuUsage[0] = (sum(l) / len(l))

			# Wait
			time.sleep(0.2)



	@classmethod
	def memoryLoop(self):
		while (self.table.enabled):
			# Get total used memory
			mem = psutil.virtual_memory()
			u = mem.used / mem.total

			# Get list of previous usages
			l = self.memoryUsage[1]
			l.append(u)

			# Set average cpu percent
			self.memoryUsage[0] = sum(l) / len(l)

			# Wait
			time.sleep(0.2)



	@classmethod
	def networkLoop(self):
		while (self.table.enabled):
			# Network io counter begin
			counterBegin = psutil.net_io_counters()

			time.sleep(1)

			# Network io counter end
			counterEnd = psutil.net_io_counters()


			# Compare differences
			sent = counterEnd.bytes_sent - counterBegin.bytes_sent
			recv = counterEnd.bytes_recv - counterBegin.bytes_recv

			# Format sizes
			self.netSent = self.formatBytes(sent)
			self.netRecv = self.formatBytes(recv)

			# Add numbers to average
			self.netSentAvgL.append(sent)
			self.netRecvAvgL.append(recv)

			# Calculate average
			self.netSentAvg = self.formatBytes(round(sum(self.netSentAvgL) / len(self.netSentAvgL)))
			self.netRecvAvg = self.formatBytes(round(sum(self.netRecvAvgL) / len(self.netRecvAvgL)))

			# Check if current is greater than max size
			if (sent > self.netSentUsage):
				self.netSentUsage = sent
				self.netSentMax = self.netSent

			if (recv > self.netRecvUsage):
				self.netRecvUsage = recv
				self.netRecvMax = self.netRecv



	@classmethod
	def diskLoop(self):
		while (self.table.enabled):
			# Disk usage
			for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
				p = f"{c}:\\"
				if (os.path.exists(p)):
					try:
						d = psutil.disk_usage(p)
					except:
						...
					else:
						self.diskUsage[p] = d.used / d.total

				else:
					# Remove if drive isn't available anymore
					if (self.diskUsage.contains(p)):
						self.diskUsage.pop(p)

			# Wait
			time.sleep(0.1)



	@classmethod
	def formatBytes(self, size):
		for unit in ("", "K", "M", "G", "T", "P", "E", "Z"):
			if abs(size) < 1024.0:
				return f"{size:3.1f} {unit}bps"

			size /= 1024.0

		return f"{size:.1f} Ybps"



