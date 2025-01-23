from engine.require import *





__all__ = ("Updater",)





class Updater(RFT_Object):
	@classmethod
	def latest(self):
		url = Data.updater.url

		path = Path("res/version.json")
		ver = "unreleased"
		currentI = 0

		if (path.is_file()):
			with path.open("rb") as file:
				try:
					version = RFT_Structure(
						json.load(file)
					)
	
				except:
					RFT_Exception.Traceback().alert()

				else:
					if (version.containsInst(("major", "minor", "patch"), int)):
						ver = f"{version.major}.{version.minor}.{version.patch}"
						currentI = version.patch | version.minor << 8 | version.major << 16


		try:
			req = requests.get(
				url,
				params = {},
				headers = {
					"User-Agent": f"DesktopDisplay/{ver} {sys.platform}"
				},
				json = True,
				timeout = 5
			)

			versions = req.json()
		
		except:
			RFT_Exception.Traceback().alert()

		else:
			if (req.status_code == 200):
				highest = 0
				latest = None

				for v in versions:
					if (isinstance(v, dict)):
						ve = RFT_Structure(v)

						if (ve.containsInst("version", list | tuple)):
							ver = ve.version

							if (len(ver) == 3):
								i = ver[2] | ver[1] << 8 | ver[0] << 16

								if (i > currentI and i > highest):
									highest = i
									latest = ve


				if (latest is not None):
					return latest





	@classmethod
	def download(self, version):
		if (version is not None):
			if (version.containsInst("file", str)):
				url = Data.updater.url
				url += "/" + version.file


				try:
					req = requests.get(
						url,
						params = {},
						headers = {
							"User-Agent": f"DesktopDisplay/{ver} {sys.platform}"
						},
						stream = True,
						timeout = 5
					)

				except:
					...

				else:
					if (req.status_code == 200):
						f = Path("update.zip")

						with open(f, "wb") as file:
							for c in req.iter_content(chunk_size = 8192):
								file.write(c)


						with zipfile.ZipFile(f, "r") as file:
							for n in file.namelist():
								try:
									file.extract(
										n,
										"."
									)

								except:
									RFT_Exception.Traceback().alert()


						os.remove(f)


						with open("res/version.json", "w") as file:
							json.dump({
								"major": version.version[0],
								"minor": version.version[1],
								"patch": version.version[2]
							}, file)


						return True

		return False



