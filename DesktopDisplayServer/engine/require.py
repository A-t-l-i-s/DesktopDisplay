import sys
sys.path += ["/root/RFTLib/src"]

import time
import psutil
import socket
import threading
import collections

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Server import *
from RFTLib.Core.Structure import *





# ~~~~~~~~~~~~~ Data ~~~~~~~~~~~~~
Data = RFT_Structure({
	"cpu": 0,
	"memory": 0,

	"netSent": "0 Kbps",
	"netSentAvg": "0 Kbps",
	"netSentMax": "0 Kbps",

	"netRecv": "0 Kbps",
	"netRecvAvg": "0 Kbps",
	"netRecvMax": "0 Kbps"
})
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~ Server ~~~~~~~~~~~~
Server = RFT_Server(
	"192.168.1.224",
	9500,
	True
)

Server.lift("Server")

Server.attach(Data, "system_server")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

