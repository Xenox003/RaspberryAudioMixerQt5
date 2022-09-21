from PyQt5 import QtCore, QtGui, QtWidgets

class VUMeterWidget(QtWidgets.QWidget):
    def setupUI(self, VUMeterWidget):
        VUMeterWidget.setObjectName("VUMeterWidget")
        VUMeterWidget.resize(50, 430)
        VUMeterWidget.setStyleSheet("")
        self.GradientLeft = QtWidgets.QWidget(VUMeterWidget)
        self.GradientLeft.setGeometry(QtCore.QRect(0, -1, 20, 431))
        self.GradientLeft.setStyleSheet("background-color: qlineargradient(spread:pad, \n"
"x1:0,\n"
"y1:1, \n"
"x2:0, \n"
"y2:0, \n"
"stop:0 rgba(0, 255, 0, 255),\n"
"stop:0.75 rgba(255,255,0,255), \n"
"stop:1 rgba(255, 0, 0, 255));")
        self.GradientLeft.setObjectName("GradientLeft")
        self.GradientRight = QtWidgets.QWidget(VUMeterWidget)
        self.GradientRight.setGeometry(QtCore.QRect(30, 0, 20, 431))
        self.GradientRight.setStyleSheet("background-color: qlineargradient(spread:pad, \n"
"x1:0,\n"
"y1:1, \n"
"x2:0, \n"
"y2:0, \n"
"stop:0 rgba(0, 255, 0, 255),\n"
"stop:0.75 rgba(255,255,0,255), \n"
"stop:1 rgba(255, 0, 0, 255));")
        self.GradientRight.setObjectName("GradientRight")

        self.retranslateUi(VUMeterWidget)
        QtCore.QMetaObject.connectSlotsByName(VUMeterWidget)

    def retranslateUi(self, VUMeterWidget):
        _translate = QtCore.QCoreApplication.translate
        VUMeterWidget.setWindowTitle(_translate("VUMeterWidget", "Form"))

class MixerWidget(QtWidgets.QWidget):
    def setupUi(self, MixerWidget):
        MixerWidget.setObjectName("MixerWidget")
        MixerWidget.resize(100, 430)
        self.widget = VUMeterWidget()
        self.widget.setupUI(MixerWidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 50, 430))
        self.widget.setObjectName("widget")

        self.retranslateUi(MixerWidget)
        QtCore.QMetaObject.connectSlotsByName(MixerWidget)

        self.retranslateUi(MixerWidget)
        QtCore.QMetaObject.connectSlotsByName(MixerWidget)

    def retranslateUi(self, MixerWidget):
        _translate = QtCore.QCoreApplication.translate
        MixerWidget.setWindowTitle(_translate("MixerWidget", "Form"))