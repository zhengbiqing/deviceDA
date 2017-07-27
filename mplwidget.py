# -*- coding:utf-8 -*-

u"""温箱数据采集程序：modbus tcp 读取数据，matplotlib显示图，保存为excel文件"""

__author__ = 'zhengbiqing 460356155@qq.com'

from time import sleep
import time
from datetime import datetime
import threading
import binascii
import random

import numpy as np
from openpyxl import Workbook
from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT  as NavigationToolbar
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import date2num, MinuteLocator, DateFormatter
import modbus_tk.modbus_tcp as modbus_tcp
import modbus_tk.defines as cst
from serial import Serial

from constant import *


class MplCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.ax_temp = self.fig.add_subplot(211)
        self.ax_ct = self.fig.add_subplot(212)

        self.ax_temp.set_ylabel('temperature')
        self.ax_ct.set_ylabel('crosstalk')
        self.ax_ct.set_xlabel("time")

        # 取消温度图表的时间刻度显示，只显示一个图的时间刻度显示
        self.ax_temp.axes.set_xticks([])

        # 每分钟一个刻度
        self.ax_ct.xaxis.set_major_locator(MinuteLocator())
        self.ax_ct.xaxis.set_major_formatter(DateFormatter('%H:%M'))
        self.ax_ct.legend()

        self.curveTemp = None
        self.curveCt = None

    def plot(self, datatempx, datatempy, datactx, datacty):
        if self.curveTemp is None:
            self.curveTemp, = self.ax_temp.plot_date(np.array(datatempx), np.array(datatempy), 'bo-')
            self.curveCt, = self.ax_ct.plot_date(np.array(datactx), np.array(datacty), 'bo-')
        else:
            # 更新数据
            self.curveTemp.set_data(np.array(datatempx), np.array(datatempy))
            self.curveCt.set_data(np.array(datactx), np.array(datacty))
            # 更新X、Y最大最小刻度
            self.ax_temp.set_xlim(datatempx[0], datatempx[-1])
            self.ax_temp.set_ylim(np.array(datatempy).min(), np.array(datatempy).max())
            self.ax_ct.set_xlim(datactx[0], datactx[-1])
            self.ax_ct.set_ylim(np.array(datacty).min(), np.array(datacty).max())

        self.draw()


class MplWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MplWidget, self).__init__(parent)
        self.canvas = MplCanvas()

        self.vbl = QtGui.QVBoxLayout()
        self.ntb = NavigationToolbar(self.canvas, parent)
        self.vbl.addWidget(self.ntb)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

        self.dataTempX = []
        self.dataTempY = []
        self.dataCtX = []
        self.dataCtY = []

        self.threadstop = True
        self.threadquit = False
        self.gather_rate = int()
        self.filename = str()

        # 串音串口参数初始化
        self.ctser = Serial()
        self.ctser_name = str()
        self.ctser_baudrate = int()
        self.ctser_init_str = str()
        self.ctser_write_str = str()

        # excel文件初始化
        self.excel_file = Workbook()
        self.sheet1 = self.excel_file.create_sheet(EXCEL_SHEET_NAME, 0)

        try:
            self.modbus_master = modbus_tcp.TcpMaster(host=IPADDR, port=MODBUS_PORT)
            self.modbus_master.set_verbose(True)
        except Exception, e:
            print Exception, ":", e
            return

        # 启动数据采集线程
        self.dispThread = threading.Thread(name="dispThread", target=self.display)
        self.dispThread.start()

    def display(self):
        count = 0
        ctData = str()
        crosstalk = float()
        temperature = float()

        while True:
            if self.threadquit is True:
                break

            if self.threadstop is True:
                sleep(THREAD_SLEEP)
                if count is not 0:
                    self.dataTempX = []
                    self.dataTempY = []
                    self.dataCtX = []
                    self.dataCtY = []
                    self.canvas.curveTemp = None
                    self.canvas.curveCt = None
                    count = 0
                continue

            try:
                tempData = self.modbus_master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 1)
                # 接收温度数据调试打印
                databinstr = '{0:016b}'.format(tempData[0])
                # print(databinstr)
                if databinstr[0] == '1':
                    # 负数
                    nodatabinstr = databinstr.replace('1', 'x')
                    nodatabinstr = nodatabinstr.replace('0', '1')
                    nodatabinstr = nodatabinstr.replace('x', '0')
                    # print(nodatabinstr, int(nodatabinstr,2), int(nodatabinstr,2)+1, -(int(nodatabinstr,2)+1))
                    temperature = 0 - (int(nodatabinstr, 2) + 1)
                else:
                    temperature = tempData[0]
                print(temperature)

            except Exception, e:
                print Exception, ":", e

            # 采集串音数据
            try:
                if self.ctser.isOpen():
                    self.ctser.write(self.ctser_write_str)
                    while self.ctser.inWaiting() < 7:
                        sleep(0.1)
                    # ctData = self.ctser.readline()
                    ctData = self.ctser.read_all()
                    # 接收串音数据调试打印
                    # print (binascii.b2a_hex(ctData), ctData)
            except Exception, e:
                print Exception, ":", e

            if self.ctser_name == ER2200:
                crosstalk = round(float(ctData.split(',')[0]), 2)
                polarizationangle = round(float(ctData.split(',')[1]), 2)
                power = round(float(ctData.split(',')[2]), 2)
            else:
                pass

            newTime = date2num(datetime.now())

            now = time.localtime(time.time())
            HMS = time.strftime('%H:%M:%S', now)
            YMD = time.strftime('%Y-%m-%d', now)

            temperature = temperature * 0.1 + 10 * (random.random() if DEBUG else 0)
            temperature = round(temperature, 2)
            print 'disp %s %s %.2f %.2f %.2f %.2f ' % (YMD, HMS, temperature, crosstalk, polarizationangle, power)
            self.dataTempX.append(newTime)
            self.dataTempY.append(temperature)
            self.dataCtX.append(newTime)
            self.dataCtY.append(crosstalk)

            # 把温度、串音数据保存到excel
            self.sheet1.append([YMD, HMS, temperature, crosstalk, polarizationangle, power])
            if count % 10 == 0:
                self.excel_file.save(str(self.filename))

            # 显示曲线图
            self.canvas.plot(self.dataTempX, self.dataTempY, self.dataCtX, self.dataCtY)

            # 图像最多保留MAXCOUNTER个点，多出的移除
            if count >= MAXCOUNTER:
                self.dataTempX.pop(0)
                self.dataTempY.pop(0)
                self.dataCtX.pop(0)
                self.dataCtY.pop(0)

            count += 1

            # 间隔gather_rate秒采集1次
            sleep(self.gather_rate)
