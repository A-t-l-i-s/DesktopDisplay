from engine.require import *
from engine.tasks import *

import numpy as np
import scipy.signal as signal
import pyaudiowpatch as pyaudio




class Task(RFT_Object):

	rms:float = 0.0
	update:float = time.time()


	@classmethod
	def init(self, output:bool):
		self.output = output

		self.inst = pyaudio.PyAudio()

		self.instInfo = self.inst.get_host_api_info_by_type(
			pyaudio.paWASAPI
		)


		self.server = socket.socket(
			socket.AF_INET,
			socket.SOCK_DGRAM
		)


		# Default Device
		if (output):
			self.device = self.inst.get_device_info_by_index(
				self.instInfo["defaultOutputDevice"]
			)

			print("Default Device: " + self.device.get("name", "none"))

		else:
			self.device = self.inst.get_device_info_by_index(
				self.instInfo["defaultInputDevice"]
			)

			print("Default Device: " + self.device.get("name", "none"))


		# Loopback
		if (not self.device["isLoopbackDevice"]):
			for loopback in self.inst.get_loopback_device_info_generator():
				if (self.device["name"] in loopback["name"]):
					self.device = loopback
					break

		else:
			print("No Doopback Device")
			time.sleep(10)


		# Variables
		self.channels = self.device["maxInputChannels"]
		self.rate = self.device["defaultSampleRate"]
		self.index = self.device["index"]

		self.chunkSize = 256

		self.maxArr = 4
		self.maxTimestamps = 10

		self.fpsRate = 60
		
		self.fpsAudio = 0
		self.fpsDispatch = 0

		self.rmsArr = collections.deque([], maxlen = self.maxArr)
		self.bassArr = collections.deque([], maxlen = self.maxArr)
		self.trebleArr = collections.deque([], maxlen = self.maxArr)


		# Get low and high cut
		self.cut = 0.5 * self.rate
		lowCut = 100 / self.cut
		highCut = 200 / self.cut


		# Initialize signal slices
		# Bass
		self.lowPass = signal.butter(4, lowCut, btype = "lowpass", analog = False)

		# Treble
		self.highPass = signal.butter(4, highCut, btype = "highpass", analog = False)



	@classmethod
	def run(self):
		timestamps = collections.deque([time.time() - 1], maxlen = self.maxTimestamps)


		try:
			# ~~~~~~ Open Stream ~~~~~
			stream = self.inst.open(
				format = pyaudio.paInt16,
				channels = self.channels,
				rate = round(self.rate),
				frames_per_buffer = self.chunkSize,
				input = True,
				input_device_index = self.index
			)

		except:
			...

		else:
			while (not Internal.isExiting()):
				start = time.time()


				try:
					# ~~~~~~ Read Stream ~~~~~
					data = stream.read(
						self.chunkSize,
						exception_on_overflow = False
					)


					self.update = time.time()

				except:
					print("Stream Disconnected")
					stream.close()
					break

				else:
					# ~~~~~ Data to Array ~~~~
					frame = np.frombuffer(
						data,
						dtype = np.int16
					)


					# ~~~~~~~~ Volume ~~~~~~~~
					self.rms = np.sqrt(np.mean(frame ** 2)) / 100


					if (not np.isnan(self.rms)):
						# Add rms to average array
						self.rmsArr.append(
							self.rms
						)

						# ~~~~~~~~~ Bass ~~~~~~~~~
						bass = signal.filtfilt(
							*self.lowPass,
							frame
						)

						self.bassArr.append(
							np.sqrt(np.mean(bass ** 2)) / self.cut
						)
						# ~~~~~~~~~~~~~~~~~~~~~~~~

						# ~~~~~~~~ Treble ~~~~~~~~
						treble = signal.filtfilt(
							*self.highPass,
							frame
						)

						self.trebleArr.append(
							np.sqrt(np.mean(treble ** 2)) / self.cut
						)
						# ~~~~~~~~~~~~~~~~~~~~~~~~

				finally:
					# ~~~~~~~~~ Wait ~~~~~~~~~
					# Add current time to timestamp
					t = time.time()
					timestamps.append(t)

					# Wait for frame
					max_ = (0.96 / self.fpsRate)
					end = (t - start)
					if (end < max_):
						time.sleep(max_ - end)

					# Get adjusted fps
					last = t
					first = timestamps[0]

					self.fpsAudio = self.maxTimestamps / (last - first)
					# ~~~~~~~~~~~~~~~~~~~~~~~~


	@classmethod
	def dispatcher(self):
		timestamps = collections.deque([time.time() - 1], maxlen = self.maxTimestamps)


		while (not Internal.isExiting()):
			start = time.time()

			# ~~~~~~~~ Prepare ~~~~~~~
			# Add rms line
			rmsT = sum(self.rmsArr) / self.maxArr
			rmsLvl = math.ceil(rmsT * 0xff) % 0xff

			# Add bass line
			bassT = sum(self.bassArr) / self.maxArr
			bassLvl = math.ceil(bassT * 0xff) % 0xff

			# Add treble line
			trebleT = sum(self.trebleArr) / self.maxArr
			trebleLvl = math.ceil(trebleT * 0xff) % 0xff
			# ~~~~~~~~~~~~~~~~~~~~~~~~


			# ~~~~~~~ Dispatch ~~~~~~~
			buf = bytearray([rmsLvl, bassLvl, trebleLvl])

			if (not self.output):
				self.server.sendto(
					buf,
					("127.0.0.1", 9600)
				)

			else:
				self.server.sendto(
					buf,
					("127.0.0.1", 9601)
				)
			# ~~~~~~~~~~~~~~~~~~~~~~~~

			# ~~~~~~~~~ Wait ~~~~~~~~~
			# Add current time to timestamp
			t = time.time()
			timestamps.append(t)

			# Wait for frame
			max_ = (0.96 / self.fpsRate)
			end = (t - start)
			if (end < max_):
				time.sleep(max_ - end)

			# Get adjusted fps
			last = t
			first = timestamps[0]

			self.fpsDispatch = self.maxTimestamps / (last - first)
			# ~~~~~~~~~~~~~~~~~~~~~~~~



def main():
	# Check if output
	arg = " ".join(sys.argv).lower()


	if ("--is_output" in arg):
		output = True

	elif ("--is_input" in arg):
		output = False

	else:
		output = False


	# Init task
	Task.init(output)

	threading.Thread(target = Task.run, daemon = True).start()
	threading.Thread(target = Task.dispatcher, daemon = True).start()



	sinceNone = time.time()

	while (not Internal.isExiting()):
		if (time.time() - Task.update >= 5.0):
			Internal.isExiting(True)
			Internal.isRestarting(True)

		if (Task.rms <= 0.0):
			if (time.time() - sinceNone > 0.5):
				if (not output):
					Task.server.sendto(
						bytearray(4),
						("127.0.0.1", 9600)
					)

				else:
					Task.server.sendto(
						bytearray(4),
						("127.0.0.1", 9601)
					)

		else:
			sinceNone = time.time()
		
		time.sleep(0.1)

