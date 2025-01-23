import sys
sys.path.append("G:/RFTLib/src")

import io
import os
import re
import ast
import time
import json
import math
import yaml
import shlex
import types
import ctypes
import psutil
import socket
import asyncio
import zipfile
import requests
import datetime
import importlib
import threading
import collections

from pathlib import Path

from winsdk.windows.storage.streams import Buffer, DataReader, InputStreamOptions
from winsdk.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager

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
	QGraphicsDropShadowEffect, QSizeGrip,
	QWidgetAction
)

# RFTLib
from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Random import *
from RFTLib.Core.Structure import *
from RFTLib.Core.Exception import *

from RFTLib.Core.Table import *
from RFTLib.Core.Server import *
from RFTLib.Core.Script import *
from RFTLib.Core.Resource import *

RFT_Exception.ui = True



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


# ~~~~~~~~~~~~ Tables ~~~~~~~~~~~~
Tables_Obj = RFT_Table(
	"./res/tables"
)
Tables_Obj.indent = True

Tables_Obj.saveEvery(30)

Tables = Tables_Obj.data
Tables.lift("Tables")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~ Scripts ~~~~~~~~~~~
Scripts_Obj = RFT_Script(
	"./res/scripts"
)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

