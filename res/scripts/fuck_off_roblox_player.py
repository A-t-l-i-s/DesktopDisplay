from engine.require import *
from engine.tasks import *





def init(scope, window):
	scope.launchThread(
		run,
		(scope,)
	)



def run(scope):
	path = os.environ.get("USERPROFILE") / Path("Desktop/Roblox Player.lnk")

	while not Internal.isExiting():
		if (path.is_file()):
			try:
				os.remove(path)

			except:
				...

			else:
				scope.print(f"Deleted")

		# Wait
		time.sleep(1)



def main(scope):
	scope.duplicateAllow = False
	
	scope.setInitEvent(init)


