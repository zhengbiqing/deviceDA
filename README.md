# deviceDA
device data acquisition base on python2.7 pyqt4 serial modbus_tcp

depends on：
	numpy
	openpyxl
	pyqt4
	matplotlib
	modbus_tk
	serial
	threading
	
	
tools in tools dir can be used to debug when devices and interfaces are not ready:
1、install modbus slave and run
2、run vspdconfig.exe
3、run devSim.py

http://www.cnblogs.com/zhengbiqing/p/6910327.html can be refered.


pyuic4 mpldesigner.ui -o mpldesigner.py
pyinstaller -F mpldesigner.py