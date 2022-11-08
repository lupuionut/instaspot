#! /usr/bin/env python3

from PyQt6.QtWidgets import QApplication, QWidget
from gui.gui import InitGui
import sys

app = QApplication([])
root = QWidget()
InitGui(root, 400, 40)
root.show()
sys.exit(app.exec())
