from engine.require import *





def init(self):
	self.show()

	self.timeFont = QFont("Dosis ExtraBold", 32)
	self.dateFont = QFont("Dosis Bold", 16)



def draw(self, painter):
	w = self.width()
	h = self.height()


	# Init Colors
	timeColor = QColor(*self.settings.timeColor)
	dateColor = QColor(*self.settings.dateColor)
	secsColor = QColor(*self.settings.secsColor)


	# Current time
	date = datetime.datetime.now()


	# ~~~~~~~~~ Time ~~~~~~~~~
	painter.setPen(timeColor)
	painter.setFont(self.timeFont)

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
	painter.setFont(self.dateFont)

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


