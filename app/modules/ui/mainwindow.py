import sys

from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class UiMain():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = QMainWindow()
        self.mainWindow.setBaseSize(800,480)
        self.mainWindow.setWindowTitle("Raspberry Audio Mixer")

        #self.ui_mainWindow = Ui_MainWindow()
        #self.ui_mainWindow.setupUi(self.mainWindow)

        self.mainWindow.show()
