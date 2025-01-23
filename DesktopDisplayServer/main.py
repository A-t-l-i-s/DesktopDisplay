from engine.require import *





def cpuLoop():
	cpuL = collections.deque([0], maxlen = 10)
	memL = collections.deque([0], maxlen = 10)


	while True:
		cpu = psutil.cpu_percent() / 100
		cpuL.append(cpu)

		Data.cpu = sum(cpuL) / len(cpuL)

		mem_ = psutil.virtual_memory()
		mem = mem_.used / mem_.total
		memL.append(mem)

		Data.memory = sum(memL) / len(memL)

		time.sleep(0.1)



def networkLoop():
	netSentAvgL = collections.deque([0], maxlen = 50)
	netRecvAvgL = collections.deque([0], maxlen = 50)

	netSentUsage = 0
	netRecvUsage = 0

	while True:
		counterBegin = psutil.net_io_counters()

		time.sleep(1)

		counterEnd = psutil.net_io_counters()


		# Compare differences
		sent = counterEnd.bytes_sent - counterBegin.bytes_sent
		recv = counterEnd.bytes_recv - counterBegin.bytes_recv

		# Format sizes
		Data.netSent = formatBytes(sent)
		Data.netRecv = formatBytes(recv)

		# Add numbers to average
		netSentAvgL.append(sent)
		netRecvAvgL.append(recv)

		# Calculate average
		Data.netSentAvg = formatBytes(round(sum(netSentAvgL) / len(netSentAvgL)))
		Data.netRecvAvg = formatBytes(round(sum(netRecvAvgL) / len(netRecvAvgL)))

		# Check if current is greater than max size
		if (sent > netSentUsage):
			netSentUsage = sent
			Data.netSentMax = Data.netSent

		if (recv > netRecvUsage):
			netRecvUsage = recv
			Data.netRecvMax = Data.netRecv




def formatBytes(size):
	for unit in ("", "K", "M", "G", "T", "P", "E", "Z"):
		if abs(size) < 1024.0:
			return f"{size:3.1f} {unit}bps"

		size /= 1024.0

	return f"{size:.1f} Ybps"



def logsLoop():
	file = open("/var/log/nginx/access.log", "rb")
	file.seek(0, 2)

	server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


	while True:
		l = file.readline()

		if (l):
			server.sendto(l, (Server.ip, 9603))

		else:
			time.sleep(0.1)



if (__name__ == "__main__"):
	threading.Thread(target = cpuLoop, daemon = True).start()
	threading.Thread(target = networkLoop, daemon = True).start()
	threading.Thread(target = logsLoop, daemon = True).start()

	while True:
		Server.refresh("system_server")
		time.sleep(0.1)


