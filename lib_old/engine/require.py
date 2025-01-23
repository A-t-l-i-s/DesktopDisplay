import sys

import os
import re
import ast
import time
import json
import math
import shlex
import types
import ctypes
import psutil
import socket
import spotipy
import zipfile
import requests
import datetime
import threading
import collections

from pathlib import Path

# Qt6
from PyQt6.QtGui import (
	QFontDatabase, QFontMetrics,
	QAction, QImage, QPixmap, QIcon,
	QColor, QPen, QBrush, QMouseEvent,
	QCursor, QFont, QPainter, QPainterPath,
	QScreen, QLinearGradient
)

from PyQt6.QtCore import (
	Qt, QObject, pyqtSlot,
	QEvent, QTimer, QPoint
)

from PyQt6.QtWidgets import (
	QApplication, QMainWindow,
	QMenu, QSystemTrayIcon,
	QVBoxLayout, QHBoxLayout,
	QScrollArea, QWidget, QFrame,
	QLabel, QLineEdit, QPushButton,
	QCheckBox, QSlider, QColorDialog,
	QGraphicsDropShadowEffect
)

# RFTLib
from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Structure import *
from RFTLib.Core.Exception import *

from RFTLib.Core.Table import *
from RFTLib.Core.Server import *
from RFTLib.Core.Script import *
from RFTLib.Core.Resource import *



# ~~~~~~~~~~~~~~ Qt ~~~~~~~~~~~~~~
QtApp = QApplication([])

QFontDatabase.addApplicationFont("./res/fonts/Dosis-Bold.ttf")
QFontDatabase.addApplicationFont("./res/fonts/Dosis-ExtraBold.ttf")
QFontDatabase.addApplicationFont("./res/fonts/Dosis-ExtraLight.ttf")
QFontDatabase.addApplicationFont("./res/fonts/Dosis-Light.ttf")
QFontDatabase.addApplicationFont("./res/fonts/Dosis-Medium.ttf")
QFontDatabase.addApplicationFont("./res/fonts/Dosis-Regular.ttf")
QFontDatabase.addApplicationFont("./res/fonts/Dosis-SemiBold.ttf")

QtApp.setStyle("Fusion")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~ Data ~~~~~~~~~~~~~
Data_Obj = RFT_Resource(
	"./res/data",
	{
		r"yaml": RFT_Resource_YAML,
		r"json": RFT_Resource_JSON
	}
)

Data = Data_Obj.load()
Data.lift("Data")

Data.defaults = {}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~ Icons ~~~~~~~~~~~~
Icons_Obj = RFT_Resource(
	"./res/icons",
	{
		r"png": RFT_Resource_QT_QICON
	}
)

Icons = Icons_Obj.load()
Icons.lift("Icons")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~ Styles ~~~~~~~~~~~~
Styles_Obj = RFT_Resource(
	"./res/styles",
	{
		r"[cq]ss": RFT_Resource_TEXT
	}
)

Styles = Styles_Obj.load()
Styles.lift("Styles")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~ Localization ~~~~~~~~~
Locs_Obj = RFT_Resource(
	"./res/locs",
	{
		r"yaml": RFT_Resource_YAML
	}
)

Locs = Locs_Obj.load()
Locs.lift("Locs")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~ Tables ~~~~~~~~~~~~
Tables_Obj = RFT_Table(
	"./res/tables"
)
Tables_Obj.indent = True

Tables_Obj.saveEvery(30)

Tables = Tables_Obj.data
Tables.lift("Tables")

Tables.window.default(Data.window)
Tables.scripts.default({})


if (Tables.window.debug):
	RFT_Exception.gui = False

else:
	RFT_Exception.gui = True
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~ Server ~~~~~~~~~~~~
Server = RFT_Server(
	Data.server.ip,
	Data.server.port
)

Server.start()
Server.lift("Server")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~ Scripts ~~~~~~~~~~~
Scripts_Obj = RFT_Script(
	"./res/scripts"
)

Scripts = Scripts_Obj.load()
Scripts.lift("Scripts")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





