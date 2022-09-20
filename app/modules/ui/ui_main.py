import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from .mainwindow_ui import Ui_MainWindow

class MainWindow():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = QMainWindow()

        self.ui_mainWindow = Ui_MainWindow()
        self.ui_mainWindow.setupUi(self.mainWindow)

        self.mainWindow.show()
