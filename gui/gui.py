from PyQt6.QtWidgets import QLineEdit, QListWidget, QGridLayout, QWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from listeners.input import onTextInput
import state


def InitGui(root: QWidget, layout: QGridLayout, width: int, height: int):
    root.resize(width, height)
    root.setWindowFlags(Qt.WindowType.FramelessWindowHint)
    state.search = DisplaySearchBox(layout)
    state.results = DisplayResults(layout)


def DisplaySearchBox(layout: QGridLayout):
    sb = QLineEdit()
    sb.setFixedWidth(400)
    sb.setFixedHeight(40)
    f = QFont()
    f.setPixelSize(18)
    sb.setFont(f)
    sb.textChanged.connect(onTextInput)
    layout.addWidget(sb)
    return sb


def DisplayResults(layout: QGridLayout):
    results = QListWidget()
    results.addItem("Testing")
    f = QFont()
    f.setPixelSize(18)
    results.setFont(f)
    layout.addWidget(results)
    return results
