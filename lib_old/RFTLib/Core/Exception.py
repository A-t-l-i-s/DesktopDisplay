from RFTLib.Require import *





__all__ = ("RFT_Exception",)





class RFT_Exception(BaseException):
	# ~~~~~~~~~~~ Variables ~~~~~~~~~~
	INFO:int = 			0
	WARNING:int = 		1
	ERROR:int = 		2
	CRITICAL:int = 		3

	ALERT_IGNORE:int = 	0
	ALERT_ABORT:int = 	1
	ALERT_RETRY:int = 	2

	stderr = 			sys.stderr
	ui:bool = 			False
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def __init__(self,
			text = "",
			level = INFO
		):

		self.text = text
		self.level = level



	# ~~~~~~~~~~~~ Message ~~~~~~~~~~~
	def message(self):
		# Get current datetime
		timestamp = datetime.datetime.now()


		# No threat
		if (self.level <= self.INFO):
			type_ = "Info"


		# Be aware
		elif (self.level == self.WARNING):
			type_ = "Warning"


		# Is a problem
		elif (self.level == self.ERROR):
			type_ = "Error"


		# Panic everything is wrong! (Critical)
		else:
			type_ = "Critical"


		# Format message
		msg = f"[{timestamp.hour:>2}:{timestamp.minute:>2}:{str(timestamp.second) + '.' + str(timestamp.microsecond)[:4]:<7}]({type_}): {self.text}"

		return msg
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~~ Print ~~~~~~~~~~~~
	def print(self, end = "\n"):
		self.stderr.write(self.message() + end)
		self.stderr.flush()
		
		return self


	def __str__(self):
		return self.message()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~~ Alert ~~~~~~~~~~~~
	def alert(self, title = "RFT_Exception"):
		if (self.ui):
			if (sys.platform == "win32"):
				r = ctypes.windll.user32.MessageBoxW(None, self.message(), title, 2)

				if (r == 3):
					return self.ALERT_ABORT

				elif (r == 4):
					return self.ALERT_RETRY

				else:
					return self.ALERT_IGNORE

		else:
			self.print()

		return self.ALERT_ABORT
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~~ Wait ~~~~~~~~~~~~~
	def wait(self, secs = None):
		if (secs != None):
			time.sleep(secs)

		else:
			input()

		return self
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Class Methods ~~~~~~~~
	@classmethod
	def TypeError(cls, t:type, level:int = ERROR):
		return RFT_Exception(
			f"Invalid type '{t.__name__}'",
			level
		)


	@classmethod
	def NoValue(cls, level:int = ERROR):
		return RFT_Exception(
			"No value provided",
			level
		)


	@classmethod
	def HasValue(cls, level:int = ERROR):
		return RFT_Exception(
			"Values are not needed",
			level
		)


	@classmethod
	def Traceback(cls, level:int = WARNING):
		return RFT_Exception(
			"\n" + traceback.format_exc().strip(),
			level
		)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~











