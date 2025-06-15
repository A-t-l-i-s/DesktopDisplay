from engine.require import *
from engine.tasks import *





class Window(RFT_Object):
	@classmethod
	def init(self, scope, window):
		# Init servers
		self.inputServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.inputServer.bind(("127.0.0.1", 9600))

		self.outputServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.outputServer.bind(("127.0.0.1", 9601))

		# Input relay server
		self.inputRelayServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
		self.inputRelayServer.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

		# Output relay server
		self.outputRelayServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
		self.outputRelayServer.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

		self.levelsLength = 100

		self.rmsInput = collections.deque([0], maxlen = self.levelsLength)
		self.rmsOutput = collections.deque([0], maxlen = self.levelsLength)
		
		self.bassInput = collections.deque([0], maxlen = self.levelsLength)
		self.bassOutput = collections.deque([0], maxlen = self.levelsLength)
		
		self.trebleInput = collections.deque([0], maxlen = self.levelsLength)
		self.trebleOutput = collections.deque([0], maxlen = self.levelsLength)


		# ~~~~~~ New Threads ~~~~~
		scope.launchThread(
			self.inputThread,
			(scope,)
		)

		scope.launchThread(
			self.outputThread,
			(scope,)
		)
		# ~~~~~~~~~~~~~~~~~~~~~~~~

		# ~~~~~~~ New Tasks ~~~~~~
		if (not scope.duplicate):
			scope.launchTask(
				"rta_task.py",
				"RTA Input",
				("--is_input",)
			)

			scope.launchTask(
				"rta_task.py",
				"RTA Output",
				("--is_output",)
			)
		# ~~~~~~~~~~~~~~~~~~~~~~~~



	@classmethod
	def draw(self, scope, painter):
		painter.setRenderHint(QPainter.RenderHint.Antialiasing)
		painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Source)

		w = scope.window.width
		h = scope.window.height

		wh = w // 3
		whl = wh / self.levelsLength
		whlr = round(whl)

		painter.setPen(Qt.PenStyle.NoPen)

		# Volume
		for i, rms in enumerate(tuple(self.rmsOutput)):
			v = round(rms * h)
			
			painter.setBrush(
				QColor(
					*RFT_Color.HSVA(340, 1.0, rms + 0.3, rms + 0.5).toRGBA()
				)
			)
			
			painter.drawPie(round(i * whl), h, whlr, -v, 0, 180 * 16)
			painter.drawRect(round(i * whl), h, whlr, -(v // 2 + 1))


		# Bass
		for i, bass in enumerate(tuple(self.bassOutput)):
			v = round(bass * h)

			painter.setBrush(
				QColor(
					*RFT_Color.HSVA(270, 1.0, bass + 0.3, bass + 0.5).toRGBA()
				)
			)

			painter.drawPie(round(i * whl) + wh, h, whlr, -v, 0, 180 * 16)
			painter.drawRect(round(i * whl) + wh, h, whlr, -(v // 2 + 1))


		# Treble
		for i, treble in enumerate(tuple(self.trebleOutput)):
			v = round(treble * h)

			painter.setBrush(
				QColor(
					*RFT_Color.HSVA(220, 1.0, treble + 0.3, treble + 0.5).toRGBA()
				)
			)

			painter.drawPie(round(i * whl) + wh * 2, h, whlr, -v, 0, 180 * 16)
			painter.drawRect(round(i * whl) + wh * 2, h, whlr, -(v // 2 + 1))



	@classmethod
	def inputThread(self, scope):
		while not Internal.isExiting():
			try:
				data, addr = self.inputServer.recvfrom(3)

			except:
				...

			else:
				rms = data[0] / 0xff
				bass = data[1] / 0xff
				treble = data[2] / 0xff

				self.rmsInput.append(rms)
				self.bassInput.append(bass)
				self.trebleInput.append(treble)

				if (scope.settings.inputRelay):
					try:
						self.inputRelayServer.sendto(
							data,
							("<broadcast>", scope.settings.inputRelayPort)
						)

					except:
						...


	@classmethod
	def outputThread(self, scope):
		while not Internal.isExiting():
			try:
				data, addr = self.outputServer.recvfrom(3)

			except:
				...

			else:
				rms = data[0] / 0xff
				bass = data[1] / 0xff
				treble = data[2] / 0xff

				self.rmsOutput.append(rms)
				self.bassOutput.append(bass)
				self.trebleOutput.append(treble)

				if (scope.settings.outputRelay):
					try:
						self.outputRelayServer.sendto(
							data,
							("<broadcast>", scope.settings.outputRelayPort)
						)

					except:
						...



def main(scope):
	scope.duplicateAllow = False
	
	scope.addSetting("inputRelay", False, scope.SETTINGS.TOGGLE)
	scope.addSetting("inputRelayPort", 9998, scope.SETTINGS.INPUT)

	scope.addSettingSeparator()

	scope.addSetting("outputRelay", False, scope.SETTINGS.TOGGLE)
	scope.addSetting("outputRelayPort", 9999, scope.SETTINGS.INPUT)


	scope.setInitEvent(Window.init)
	scope.setDrawEvent(Window.draw)


