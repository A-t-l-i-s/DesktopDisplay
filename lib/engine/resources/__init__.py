from engine.require import *

from .dosis.regular import *
from .dosis.extralight import *
from .dosis.light import *
from .dosis.medium import *
from .dosis.semibold import *
from .dosis.bold import *
from .dosis.extrabold import *

from .jetbrains_mono.regular import *
from .jetbrains_mono.extralight import *
from .jetbrains_mono.light import *
from .jetbrains_mono.medium import *
from .jetbrains_mono.semibold import *
from .jetbrains_mono.bold import *
from .jetbrains_mono.extrabold import *





__all__ = ("Resources",)





class Resources(RFT_Object):
	# ~~~~~~~~~~~~~ Data ~~~~~~~~~~~~~
	Data = RFT_Structure()

	Data.lift("Data")
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~ Localization ~~~~~~~~~
	Locs = RFT_Structure()

	Locs.lift("Locs")
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~~ Icons ~~~~~~~~~~~~
	Icons = RFT_Structure()

	Icons.lift("Icons")
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~~ Images ~~~~~~~~~~~
	Images = RFT_Structure()

	Images.lift("Images")
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~ Styles ~~~~~~~~~~~~
	Styles = RFT_Structure()

	Styles.lift("Styles")
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~ Tables ~~~~~~~~~~~~
	Tables_Obj = RFT_Table(
		"res/tables"
	)
	Tables_Obj.indent = True

	if (not Internal.isTask()):
		Tables_Obj.saveEvery(30)

	Tables = Tables_Obj.data
	Tables.lift("Tables")
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~ Tables Scripts ~~~~~~~~
	Tables_Scripts_Obj = RFT_Table(
		"res/tables_scripts"
	)
	Tables_Scripts_Obj.indent = True

	if (not Internal.isTask()):
		Tables_Scripts_Obj.saveEvery(30)

	Tables_Scripts = Tables_Scripts_Obj.data
	Tables_Scripts.lift("Tables_Scripts")
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	@classmethod
	def loadResources(self, obj:RFT_Object):
		def err(exc, file):
			obj.printErr(
				f"resources : {file}",
				exc
			)


		# ~~~~~~~~~ Data ~~~~~~~~~
		dataObj = RFT_Resource(
			"res/data",
			{
				r"yaml|yml": RFT_Resource_YAML,
				r"json": RFT_Resource_JSON,
				r"toml": RFT_Resource_TOML,
				r"txt|log": RFT_Resource_TEXT
			}
		)

		self.Data *= dataObj.load(err)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~ Localization ~~~~~
		locsObj = RFT_Resource(
			"res/locs",
			{
				r"yaml|yml": RFT_Resource_YAML
			}
		)

		self.Locs *= locsObj.load(err)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Icons ~~~~~~~~
		iconsObj = RFT_Resource(
			"res/icons",
			{
				r".*": RFT_Resource_QT_QICON
			}
		)

		self.Icons *= iconsObj.load(err)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Images ~~~~~~~~
		imagesObj = RFT_Resource(
			"res/images",
			{
				r".*": RFT_Resource_QT_QIMAGE
			}
		)

		self.Images *= imagesObj.load(err)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Styles ~~~~~~~~
		stylesObj = RFT_Resource(
			"res/styles",
			{
				r"[cq]ss": RFT_Resource_TEXT
			}
		)

		self.Styles *= stylesObj.load(err)
		# ~~~~~~~~~~~~~~~~~~~~~~~~



	@classmethod
	def loadFonts(self, obj:RFT_Object):
		try:
			# ~~~~~~~~~~~~~ Dosis ~~~~~~~~~~~~
			QFontDatabase.addApplicationFontFromData(
				base64.b64decode(FONTS_DOSIS_REGULAR)
			)

			QFontDatabase.addApplicationFontFromData(
				base64.b64decode(FONTS_DOSIS_EXTRALIGHT)
			)

			QFontDatabase.addApplicationFontFromData(
				base64.b64decode(FONTS_DOSIS_LIGHT)
			)

			QFontDatabase.addApplicationFontFromData(
				base64.b64decode(FONTS_DOSIS_MEDIUM)
			)

			QFontDatabase.addApplicationFontFromData(
				base64.b64decode(FONTS_DOSIS_SEMIBOLD)
			)

			QFontDatabase.addApplicationFontFromData(
				base64.b64decode(FONTS_DOSIS_BOLD)
			)

			QFontDatabase.addApplicationFontFromData(
				base64.b64decode(FONTS_DOSIS_EXTRABOLD)
			)
			# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

			# ~~~~~~~~ JetBrains Mono ~~~~~~~~
			QFontDatabase.addApplicationFontFromData(
				base64.b64decode(FONTS_JETBRAINS_MONO_REGULAR)
			)

			QFontDatabase.addApplicationFontFromData(
				base64.b64decode(FONTS_JETBRAINS_MONO_EXTRALIGHT)
			)

			QFontDatabase.addApplicationFontFromData(
				base64.b64decode(FONTS_JETBRAINS_MONO_LIGHT)
			)

			QFontDatabase.addApplicationFontFromData(
				base64.b64decode(FONTS_JETBRAINS_MONO_MEDIUM)
			)

			QFontDatabase.addApplicationFontFromData(
				base64.b64decode(FONTS_JETBRAINS_MONO_SEMIBOLD)
			)

			QFontDatabase.addApplicationFontFromData(
				base64.b64decode(FONTS_JETBRAINS_MONO_BOLD)
			)

			QFontDatabase.addApplicationFontFromData(
				base64.b64decode(FONTS_JETBRAINS_MONO_EXTRABOLD)
			)
			# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		except:
			obj.printErr(
				f"resources : fonts",
				RFT_Exception("Failed to load fonts")
			)

