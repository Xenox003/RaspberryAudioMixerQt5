# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './.compileui/vumeter.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(50, 430)
        Form.setStyleSheet("")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, -1, 20, 431))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:pad, \n"
"x1:0,\n"
"y1:1, \n"
"x2:0, \n"
"y2:0, \n"
"stop:0 rgba(0, 255, 0, 255),\n"
"stop:0.75 rgba(255,255,0,255), \n"
"stop:1 rgba(255, 0, 0, 255));")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(30, 0, 20, 431))
        self.widget_2.setStyleSheet("background-color: qlineargradient(spread:pad, \n"
"x1:0,\n"
"y1:1, \n"
"x2:0, \n"
"y2:0, \n"
"stop:0 rgba(0, 255, 0, 255),\n"
"stop:0.75 rgba(255,255,0,255), \n"
"stop:1 rgba(255, 0, 0, 255));")
        self.widget_2.setObjectName("widget_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))