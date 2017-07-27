# -*- coding:utf-8 -*-

u"""FIBERPRO偏振消光比测试仪ER2200模拟程序"""

__author__ = 'zhengbiqing 460356155@qq.com'

import binascii
import signal
import sys
from random import random
import time

import serial

ser = serial.Serial('COM4', 115200, timeout=1)

print 'Welcome to ', __doc__, ',', 'device is %s' % ('Ready' if ser.isOpen() else 'Error')
print 'Author is ', __author__


# ctrl+c处理函数
def signal_handler(signal, frame):
    ser.close()
    print 'You pressed Ctrl+C! ', 'device is %s' % ('Closed' if not ser.isOpen() else 'Error')
    print 'Goodbye!'
    sys.exit(0)


# 程序是死循环，通过ctrl+c退出，为了在退出时关闭串口，捕获该信号
signal.signal(signal.SIGINT, signal_handler)

while True:
    data = ser.read(7)
    if len(data):
        # 调试打印，b2a_hex(data)是把字符串data转换为十六进制数
        now = time.localtime(time.time())
        HMS = time.strftime('%H:%M:%S', now)
        print '%s <- %s(%r)' % (HMS, binascii.b2a_hex(data), data)

    if data == 'read?\r\n':
        # 三个数字分别表示被测光的消光比,偏振角度,和光功率
        classtalk = 19.35 + round(random(), 2)
        angle = 53.47 + round(random(), 2)
        power = -5.17 + round(random(), 2)
        sendstr = str(classtalk) + ',' + str(angle) + ',' + str(power) + '\r'
        now = time.localtime(time.time())
        HMS = time.strftime('%H:%M:%S', now)
        print '%s -> %s' % (HMS, sendstr)
        ser.write(sendstr)
