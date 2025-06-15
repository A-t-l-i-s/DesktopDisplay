from engine.require import *





def init(scope, window):
	scope.font = QFont("Dosis ExtraBold", 32)



def draw(scope, painter):
	w = scope.window.width
	h = scope.window.height


	# Init Colors
	color = QColor(*scope.settings.color)


	# ~~~~~~~~~ Time ~~~~~~~~~
	painter.setPen(color)
	painter.setFont(scope.font)

	# Draw time text
	painter.drawText(
		0, 0,
		w, h,
		Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
		scope.settings.text
	)
	# ~~~~~~~~~~~~~~~~~~~~~~~~




def main(scope):
	scope.addSetting("text", "", scope.SETTINGS.INPUT)
	scope.addSetting("color", [255, 255, 255, 255], scope.SETTINGS.COLOR)
	
	scope.setInitEvent(init)
	scope.setDrawEvent(draw)


