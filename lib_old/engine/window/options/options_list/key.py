from engine.require import *





__all__ = ("Window_OptionsList_Item_Key",)





class Window_OptionsList_Item_Key(RFT_Object, QFrame):
	def __init__(self, parent, key, locs, table, default):
		super().__init__(parent)


		# ~~~~~~~ Variables ~~~~~~
		self.parent = parent

		self.key = key
		
		self.locs = locs
		self.table = table
		self.default = default

		self.value = table.get(key)
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Settings ~~~~~~~~~~~
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QHBoxLayout()
		self.layout.setSpacing(3)
		self.layout.setContentsMargins(3, 0, 0, 0)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)

		self.setLayout(self.layout)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Key Widget ~~~~~~~~~~
		self.keyWidget = QLabel()
		self.keyWidget.setFixedHeight(25)

		# ~~~~~~~ Key Name ~~~~~~~
		k = self.locs.get(self.key, self.key)

		if (k.endswith(":group")):
			k = k.rstrip(":group")
			self.setFixedHeight(40)


		self.keyWidget.setText(k)
		# ~~~~~~~~~~~~~~~~~~~~~~~~
	
		self.keyWidget.setFixedWidth(160)

		self.keyWidget.setStyleSheet("""
			QLabel{
				color: rgb(200, 200, 200);
			}
		""")

		self.keyWidget.setFont(
			QFont("Dosis", 12, 600, False)
		)

		self.layout.addWidget(self.keyWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Value Widget ~~~~~~~~~
		if (isinstance(self.value, bool)):
			self.valueWidget = QCheckBox(self)
			self.valueWidget.setChecked(self.value)
			self.valueWidget.setCursor(Qt.CursorShape.PointingHandCursor)

			self.valueWidget.checkStateChanged.connect(self.valueBool)


		elif (isinstance(self.value, tuple | list) and len(self.value) == 4):
			self.valueWidget = QPushButton()
			self.valueWidget.setFixedSize(70, 20)
			self.valueWidget.setCursor(Qt.CursorShape.PointingHandCursor)
			self.valueWidget.setStyleSheet(
				f"background-color: rgba({self.value[0]}, {self.value[1]}, {self.value[2]}, {self.value[3]}); border: 1px solid rgb({self.value[0]}, {self.value[1]}, {self.value[2]});"
			)

			self.valueWidget.clicked.connect(self.valueColor)


		else:
			self.valueWidget = QLineEdit(self)
			self.valueWidget.setPlaceholderText(str(self.value))

			self.valueWidget.editingFinished.connect(self.valueString)

		
		self.layout.addWidget(self.valueWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def valueBool(self, value):
		self.parent.parent.touched = True

		self.table[self.key] = (value == Qt.CheckState.Checked)


	def valueColor(self):
		self.parent.parent.touched = True

		dialog = QColorDialog(self)
		dialog.setOptions(QColorDialog.ColorDialogOption.ShowAlphaChannel)
		dialog.setCurrentColor(QColor(*self.value))

		dialog.setWindowFlags(
			Qt.WindowType.Tool |
			Qt.WindowType.FramelessWindowHint |
			Qt.WindowType.WindowStaysOnTopHint
		)

		if (dialog.exec()):
			c = dialog.currentColor()

			if (c):
				self.table[self.key] = [
					c.red(),
					c.green(),
					c.blue(),
					c.alpha()
				]

				self.valueWidget.setStyleSheet(
					f"background-color: rgba({c.red()}, {c.green()}, {c.blue()}, {c.alpha()}); border: 1px solid rgb({c.red()}, {c.green()}, {c.blue()});"
				)


	def valueString(self):
		self.parent.parent.touched = True

		text = self.valueWidget.text()
		text = text.strip()


		if (text):
			try:
				if (isinstance(self.value, str)):
					value = text

				else:
					value = ast.literal_eval(text)
			
			except:
				...

			else:
				if (isinstance(value, type(self.value)) or self.value is None):
					self.table[self.key] = value
					self.value = value
					self.valueWidget.setPlaceholderText(str(value))

			finally:
				self.valueWidget.setText(None)

		else:
			self.table[self.key] = self.value


