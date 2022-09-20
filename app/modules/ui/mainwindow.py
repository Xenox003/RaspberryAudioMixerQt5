import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.window.setGeometry(200,200,300,300)
        self.window.setWindowTitle("Raspberry Audio Mixer")

        self.window.show()
