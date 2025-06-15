from engine.require import *
from engine.tasks import *





def init(scope, window):
	...


def draw(scope, painter):
	w = scope.window.width
	h = scope.window.height



def thread1(scope):
	s = time.time()
	print(scope.inst.scopes.waitFor("test_error", timeout = 10).id)
	print(time.time() - s)

def thread2(scope):
	s = time.time()
	print(scope.inst.scopes.waitFor("media", timeout = 10).id)
	print(time.time() - s)



def main(scope):
	scope.setInitEvent(init)
	scope.setDrawEvent(draw)

	# Tasks.newThread(thread1, (scope,), uid = "thread1", start = True)
	# Tasks.newThread(thread2, (scope,), uid = "thread2", start = True)


