


if (Internal.isProduction()):
	pid = Internal.pid()

	for p in psutil.process_iter():
		if (p.name() in (Internal.programFileWindowed(), Internal.programFileDebug())):
			if (p.pid != pid):
				return True


