from engine.require import *





def init(scope, window):
	scope.timeFont = QFont("Dosis ExtraBold", 32)
	scope.dateFont = QFont("Dosis Bold", 16)



def draw(scope, painter):
	w = scope.window.width
	h = scope.window.height


	# Init Colors
	timeColor = QColor(*scope.settings.timeColor)
	dateColor = QColor(*scope.settings.dateColor)
	secsColor = QColor(*scope.settings.secsColor)


	# Current time
	date = datetime.datetime.now()


	# ~~~~~~~~~ Time ~~~~~~~~~
	painter.setPen(timeColor)
	painter.setFont(scope.timeFont)

	# Draw time text
	painter.drawText(
		0, 0,
		w, 50,
		Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
		date.strftime("%a %I:%M%p").replace(" 0", " ")
	)
	# ~~~~~~~~~~~~~~~~~~~~~~~~

	# ~~~~~~~~~ Date ~~~~~~~~~
	painter.setPen(dateColor)
	painter.setFont(scope.dateFont)

	# Draw date text
	painter.drawText(
		0, 35,
		w, 50,
		Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
		date.strftime("%m/%d/%y")
	)

	sPB = 100
	# ~~~~~~~~~~~~~~~~~~~~~~~~

	# ~~~~~~~~ Seconds ~~~~~~~
	# Seconds progress bar
	painter.fillRect(
		w // 2 - sPB, 47,
		math.floor(((date.second + (date.microsecond / (10 ** 6))) / 60) * (sPB * 2)), 2,
		secsColor
	)
	# ~~~~~~~~~~~~~~~~~~~~~~~~





def main(scope):
	scope.addSetting("timeColor", [255, 255, 255, 255], scope.SETTINGS.COLOR)
	scope.addSetting("dateColor", [255, 255, 255, 255], scope.SETTINGS.COLOR)
	scope.addSetting("secsColor", [255, 255, 255, 255], scope.SETTINGS.COLOR)
	
	scope.setInitEvent(init)
	scope.setDrawEvent(draw)


