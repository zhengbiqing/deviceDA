# -*- coding:utf-8 -*-

u"""偏振消光比测试仪、温箱数据采集程序：全局变量"""

__author__ = 'zhengbiqing 460356155@qq.com'

MAXCOUNTER = 500
TEMP_IPADDR = '200.200.200.190'
LOOP_IPADDR = '127.0.0.1'
MODBUS_PORT = 3000
THREAD_SLEEP = 5

DEBUG = True
IPADDR = LOOP_IPADDR if DEBUG else TEMP_IPADDR

# 偏振消光比测试仪ER2200参数及通信协议
ER2200_SERIAL_BAUDRATE = 115200
# 通信初始化写入字符
ER2200_INIT_STR = 'rmt\r\n'
# 采集数据时发送的命令字符串
ER2200_WRITE_STR = 'read?\r\n'
SERIAL_TIMEOUT = 5
ER2200 = 'ER2200'

# excel文件相关
EXCEL_SHEET_NAME = 'Temp-Crosstalk'
ROW0 = [u'日期', u'时间', u'温度', u'消光比', u'角度', u'功率']
