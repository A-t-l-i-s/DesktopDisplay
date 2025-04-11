from engine.require import *





__all__ = ("Tasks",)





class Tasks(RFT_Object):
	tasks:list = []
	threads:list = []


	# ~~~~~~~~ Finish ~~~~~~~~
	@classmethod
	def finish(self):
		# Kill all tasks
		self.finishTasks()


		# Delete all instances
		path = Path("insts")
		for f in path.iterdir():
			try:
				os.remove(
					f.as_posix()
				)
			except:
				...


	@classmethod
	def finishTasks(self):
		for p in self.tasks:
			try:
				p.terminate()
				p.wait()
			
			except:
				...


		for p in psutil.process_iter():
			try:
				if (p.name() == Core.programFileTask()):
					p.terminate()
					p.wait()

			except:
				...



		self.tasks.clear()
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~ Tasks ~~~~~~~~
	@classmethod
	def newTask(self, filename:str, name:str):
		process = subprocess.Popen(
			[
				Core.programFileTask(),
				filename,
				name
			],
			executable = Core.programFileTask(),

			stdin = subprocess.PIPE,
			stdout = subprocess.PIPE,
			stderr = subprocess.PIPE,

			creationflags = subprocess.CREATE_NO_WINDOW
		)

		self.tasks.append(
			process
		)

		return process
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~ Threading ~~~~~~
	@classmethod
	def newThread(self, func, args:list | tuple = (), kwargs:dict | RFT_Structure = {}):
		thread = threading.Thread(
			target = func,
			args = tuple(args),
			kwargs = dict(kwargs),
			daemon = True
		)

		self.threads.append(
			thread
		)

		return thread
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~ Is Running ~~~~~~
	@classmethod
	def isRunning(self):
		if (Core.isProduction()):
			pid = Core.pid()

			for p in psutil.process_iter():
				if (p.name() in (Core.programFileWindowed(), Core.programFileDebug())):
					if (p.pid != pid):
						return True


		return False
	# ~~~~~~~~~~~~~~~~~~~~~~~~

