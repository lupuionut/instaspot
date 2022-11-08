#! /usr/bin/env python3

from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout
from gui.gui import InitGui
import sys

app = QApplication([])
root = QWidget()
layout = QGridLayout(root)
InitGui(root, layout, 400, 140)
root.show()
sys.exit(app.exec())
