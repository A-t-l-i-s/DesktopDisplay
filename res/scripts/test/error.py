from engine.require import *





def init(scope, window):
	...



def draw(scope, painter):
	...


def err(*args, **kwargs):
	raise RFT_Exception("Test Error")




def main(scope):
	scope.addSetting("var1", 0.5, scope.SETTINGS.RANGE, callback = err)
	scope.addSetting("var2", ["b", ("a", "b", "c", "d", "e")], scope.SETTINGS.LIST)

	scope.addSetting("var3", 0, scope.SETTINGS.INPUT)
	scope.addSetting("var4", False, scope.SETTINGS.TOGGLE)
	scope.addSetting("var5", [0, 0, 0, 0], scope.SETTINGS.COLOR)
	
	scope.setInitEvent(init)
	scope.setDrawEvent(draw)

	# scope.setInitEvent(err)
	# scope.setDrawEvent(err)
	# scope.setExitEvent(err)

	# scope.setMoveEvent(err)

	# scope.setMousePressEvent(err)
	# scope.setMouseReleaseEvent(err)
	# scope.setMouseMoveEvent(err)

	# scope.setKeyPressEvent(err)
	# scope.setKeyReleaseEvent(err)


