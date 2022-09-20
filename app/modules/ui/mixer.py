from PyQt5 import QtCore, QtGui, QtWidgets

class MixerWidget():
    def setupUi(self, MixerWidget):
        MixerWidget.setObjectName("MixerWidget")
        MixerWidget.resize(100, 480)
        self.pushButton = QtWidgets.QPushButton(MixerWidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 440, 80, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(MixerWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 400, 80, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(MixerWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 360, 80, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(MixerWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 320, 80, 24))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(MixerWidget)
        QtCore.QMetaObject.connectSlotsByName(MixerWidget)

    def retranslateUi(self, MixerWidget):
        _translate = QtCore.QCoreApplication.translate
        MixerWidget.setWindowTitle(_translate("MixerWidget", "Form"))
        self.pushButton.setText(_translate("MixerWidget", "PushButton"))
        self.pushButton_2.setText(_translate("MixerWidget", "PushButton"))
        self.pushButton_3.setText(_translate("MixerWidget", "PushButton"))
        self.pushButton_4.setText(_translate("MixerWidget", "PushButton"))