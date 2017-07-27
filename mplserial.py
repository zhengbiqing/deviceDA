# -*- coding:utf-8 -*-

u"""偏振消光比测试仪、温箱数据采集程序：QT主程序"""

__author__ = 'zhengbiqing 460356155@qq.com'

import sys
from time import sleep

from PyQt4.QtGui import QFileDialog
from PyQt4 import QtGui

from serial import Serial

from mpldesigner import Ui_MainWindow
from constant import *


class DaMainWindow(Ui_MainWindow):
    def __init__(self, parent=None):
        super(DaMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButtonExit.setHidden(True)
        self.pushButtonStop.setEnabled(False)
        self.pushButtonStart.setEnabled(True)

        self.pushButtonStart.clicked.connect(self.start_clicked)
        self.pushButtonStop.clicked.connect(self.stop_clicked)

    # 重定义closeEvent，等待数据采集线程退出，关闭modbus、串口，保存文件
    def closeEvent(self, event):
        self.mplWidget.threadquit = True

        self.mplWidget.modbus_master.close()
        self.mplWidget.ctser.close()
        if len(self.mplWidget.filename):
            self.mplWidget.excel_file.save(str(self.mplWidget.filename))
            self.mplWidget.excel_file.close()

        # 先隐藏窗口
        self.setHidden(True)
        # 等待线程退出
        self.mplWidget.dispThread.join()

    # 停止采集：本次采集结束，关闭modbus、串口，保存文件，停止采集数据，设置按钮使能
    def stop_clicked(self):
        self.mplWidget.modbus_master.close()
        self.mplWidget.ctser.close()
        if len(self.mplWidget.filename):
            self.mplWidget.excel_file.save(str(self.mplWidget.filename))
            self.mplWidget.excel_file.close()
            self.mplWidget.filename = ''

        self.mplWidget.excel_file.remove_sheet(self.mplWidget.excel_file.get_sheet_by_name(EXCEL_SHEET_NAME))

        self.mplWidget.threadstop = True

        self.pushButtonStop.setEnabled(False)
        self.pushButtonStart.setEnabled(True)
        self.comboBoxCrosstalkCom.setEnabled(True)
        self.comboBoxCrosstalkDev.setEnabled(True)
        self.comboBoxThermCom.setEnabled(True)
        self.comboBoxThermDev.setEnabled(True)

    # 开始采集：启动一次新采集，清空excel文件数据，初始化excel文件，获取保存的excel文件名、采集频率
    def start_clicked(self):
        # 如果未增加sheet，则增加
        try:
            self.mplWidget.excel_file.get_sheet_by_name(EXCEL_SHEET_NAME)
        except:
            self.mplWidget.sheet1 = self.mplWidget.excel_file.create_sheet(EXCEL_SHEET_NAME, 0)

        # 增加excel第一行
        self.mplWidget.sheet1.append(ROW0)

        self.mplWidget.filename = QFileDialog.getSaveFileName(self, 'save file', '.', 'excel files (*.xls)')
        self.mplWidget.gather_rate = int(self.lineEditRate.text())

        # 获取串音设备型号，并设置相关数据
        if self.comboBoxCrosstalkDev.currentText() == ER2200:
            self.mplWidget.ctser_name = ER2200
            self.mplWidget.ctser_baudrate = ER2200_SERIAL_BAUDRATE
            self.mplWidget.ctser_init_str = ER2200_INIT_STR
            self.mplWidget.ctser_write_str = ER2200_WRITE_STR
        else:
            # 新增类型在这添加代码
            return

        self.pushButtonStart.setEnabled(False)
        self.pushButtonStop.setEnabled(True)
        self.comboBoxCrosstalkCom.setEnabled(False)
        self.comboBoxCrosstalkDev.setEnabled(False)
        self.comboBoxThermCom.setEnabled(False)
        self.comboBoxThermDev.setEnabled(False)

        # print(str(self.comboBoxCrosstalkCom.currentText()))
        try:
            self.mplWidget.ctser = Serial(str(self.comboBoxCrosstalkCom.currentText()),
                                          self.mplWidget.ctser_baudrate, timeout=SERIAL_TIMEOUT)
            # 根据串音ER2200协议，采集数据前，需先写入初始化字符串
            self.mplWidget.ctser.write(self.mplWidget.ctser_init_str)
            print("write", self.mplWidget.ctser.isOpen())
            sleep(3)
        except Exception, e:
            print Exception, ":", e
            return

        self.mplWidget.threadstop = False


app = QtGui.QApplication(sys.argv)
window = DaMainWindow()
window.show()
sys.exit(app.exec_())
