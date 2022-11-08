from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from listeners.input import onTextInput


def InitGui(root, width, height):
    root.resize(width, height)
    root.setWindowFlags(Qt.WindowType.FramelessWindowHint)
    DisplaySearchBox(root)


def DisplaySearchBox(root):
    sb = QLineEdit(root)
    sb.setFixedWidth(400)
    sb.setFixedHeight(40)
    f = QFont()
    f.setPixelSize(18)
    sb.setFont(f)
    sb.textChanged.connect(onTextInput)
