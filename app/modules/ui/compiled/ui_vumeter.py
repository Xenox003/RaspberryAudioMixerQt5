# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './.compileui/vumeter.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VuMeterWidget(object):
    def setupUi(self, VuMeterWidget):
        VuMeterWidget.setObjectName("VuMeterWidget")
        VuMeterWidget.resize(50, 430)
        VuMeterWidget.setStyleSheet("")
        self.MeterLeft = QtWidgets.QFrame(VuMeterWidget)
        self.MeterLeft.setGeometry(QtCore.QRect(10, 0, 10, 431))
        self.MeterLeft.setStyleSheet("background-color: qlineargradient(spread:pad, \n"
"x1:0,\n"
"y1:1, \n"
"x2:0, \n"
"y2:0, \n"
"stop:0 rgba(0, 255, 0, 255),\n"
"stop:0.75 rgba(255,255,0,255), \n"
"stop:1 rgba(255, 0, 0, 255));")
        self.MeterLeft.setObjectName("MeterLeft")
        self.MeterRight = QtWidgets.QFrame(VuMeterWidget)
        self.MeterRight.setGeometry(QtCore.QRect(30, 0, 10, 431))
        self.MeterRight.setStyleSheet("background-color: qlineargradient(spread:pad, \n"
"x1:0,\n"
"y1:1, \n"
"x2:0, \n"
"y2:0, \n"
"stop:0 rgba(0, 255, 0, 255),\n"
"stop:0.75 rgba(255,255,0,255), \n"
"stop:1 rgba(255, 0, 0, 255));")
        self.MeterRight.setObjectName("MeterRight")
        self.ClipLeft = QtWidgets.QFrame(VuMeterWidget)
        self.ClipLeft.setGeometry(QtCore.QRect(10, 0, 10, 430))
        self.ClipLeft.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.ClipLeft.setObjectName("ClipLeft")
        self.ClipRight = QtWidgets.QFrame(VuMeterWidget)
        self.ClipRight.setGeometry(QtCore.QRect(30, 0, 10, 430))
        self.ClipRight.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.ClipRight.setObjectName("ClipRight")

        self.retranslateUi(VuMeterWidget)
        QtCore.QMetaObject.connectSlotsByName(VuMeterWidget)

    def retranslateUi(self, VuMeterWidget):
        _translate = QtCore.QCoreApplication.translate
        VuMeterWidget.setWindowTitle(_translate("VuMeterWidget", "Form"))
