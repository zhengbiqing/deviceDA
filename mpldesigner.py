# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mpldesigner.ui'
#
# Created: Sat May 27 11:31:18 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1099, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.comboBoxCrosstalkDev = QtGui.QComboBox(self.centralwidget)
        self.comboBoxCrosstalkDev.setGeometry(QtCore.QRect(90, 10, 69, 22))
        self.comboBoxCrosstalkDev.setObjectName(_fromUtf8("comboBoxCrosstalkDev"))
        self.comboBoxCrosstalkDev.addItem(_fromUtf8(""))
        self.comboBoxCrosstalkDev.addItem(_fromUtf8(""))
        self.comboBoxCrosstalkCom = QtGui.QComboBox(self.centralwidget)
        self.comboBoxCrosstalkCom.setGeometry(QtCore.QRect(170, 10, 69, 22))
        self.comboBoxCrosstalkCom.setObjectName(_fromUtf8("comboBoxCrosstalkCom"))
        self.comboBoxCrosstalkCom.addItem(_fromUtf8(""))
        self.comboBoxCrosstalkCom.addItem(_fromUtf8(""))
        self.comboBoxCrosstalkCom.addItem(_fromUtf8(""))
        self.comboBoxCrosstalkCom.addItem(_fromUtf8(""))
        self.comboBoxThermDev = QtGui.QComboBox(self.centralwidget)
        self.comboBoxThermDev.setGeometry(QtCore.QRect(270, 10, 69, 22))
        self.comboBoxThermDev.setObjectName(_fromUtf8("comboBoxThermDev"))
        self.comboBoxThermDev.addItem(_fromUtf8(""))
        self.comboBoxThermDev.addItem(_fromUtf8(""))
        self.comboBoxThermCom = QtGui.QComboBox(self.centralwidget)
        self.comboBoxThermCom.setGeometry(QtCore.QRect(350, 10, 69, 22))
        self.comboBoxThermCom.setObjectName(_fromUtf8("comboBoxThermCom"))
        self.comboBoxThermCom.addItem(_fromUtf8(""))
        self.comboBoxThermCom.addItem(_fromUtf8(""))
        self.comboBoxThermCom.addItem(_fromUtf8(""))
        self.comboBoxThermCom.addItem(_fromUtf8(""))
        self.lineEditRate = QtGui.QLineEdit(self.centralwidget)
        self.lineEditRate.setGeometry(QtCore.QRect(130, 520, 113, 20))
        self.lineEditRate.setObjectName(_fromUtf8("lineEditRate"))
        self.mplWidget = MplWidget(self.centralwidget)
        self.mplWidget.setGeometry(QtCore.QRect(30, 40, 1041, 471))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplWidget.sizePolicy().hasHeightForWidth())
        self.mplWidget.setSizePolicy(sizePolicy)
        self.mplWidget.setObjectName(_fromUtf8("mplWidget"))
        self.pushButtonStart = QtGui.QPushButton(self.centralwidget)
        self.pushButtonStart.setGeometry(QtCore.QRect(320, 520, 75, 23))
        self.pushButtonStart.setObjectName(_fromUtf8("pushButtonStart"))
        self.pushButtonStop = QtGui.QPushButton(self.centralwidget)
        self.pushButtonStop.setGeometry(QtCore.QRect(420, 520, 75, 23))
        self.pushButtonStop.setObjectName(_fromUtf8("pushButtonStop"))
        self.pushButtonExit = QtGui.QPushButton(self.centralwidget)
        self.pushButtonExit.setGeometry(QtCore.QRect(530, 520, 75, 23))
        self.pushButtonExit.setObjectName(_fromUtf8("pushButtonExit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1099, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.comboBoxCrosstalkDev.setItemText(0, _translate("MainWindow", "ER2200", None))
        self.comboBoxCrosstalkDev.setItemText(1, _translate("MainWindow", "ERM101", None))
        self.comboBoxCrosstalkCom.setItemText(0, _translate("MainWindow", "COM1", None))
        self.comboBoxCrosstalkCom.setItemText(1, _translate("MainWindow", "COM2", None))
        self.comboBoxCrosstalkCom.setItemText(2, _translate("MainWindow", "COM3", None))
        self.comboBoxCrosstalkCom.setItemText(3, _translate("MainWindow", "COM4", None))
        self.comboBoxThermDev.setItemText(0, _translate("MainWindow", "05038", None))
        self.comboBoxThermDev.setItemText(1, _translate("MainWindow", "20160417", None))
        self.comboBoxThermCom.setItemText(0, _translate("MainWindow", "COM1", None))
        self.comboBoxThermCom.setItemText(1, _translate("MainWindow", "COM2", None))
        self.comboBoxThermCom.setItemText(2, _translate("MainWindow", "COM3", None))
        self.comboBoxThermCom.setItemText(3, _translate("MainWindow", "COM4", None))
        self.lineEditRate.setText(_translate("MainWindow", "10", None))
        self.pushButtonStart.setText(_translate("MainWindow", "开始", None))
        self.pushButtonStop.setText(_translate("MainWindow", "结束", None))
        self.pushButtonExit.setText(_translate("MainWindow", "退出", None))

from mplwidget import MplWidget
