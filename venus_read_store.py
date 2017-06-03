# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:35:38 2017

@author: smrak
"""

import sys
import glob
import serial
import getpass
import datetime
import os.path

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux'):
        ports = glob.glob('/dev/ttyUSB*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result
    
def createfile(fn):
	"""
	"""
	if not os.path.exists(fn):
		fw = open(fn, 'wb')
	else:
		c = 0
		while os.path.isfile(fn):
			c += 1
			fn = fn + '_' + str(c)
		fw = open(fn, 'wb')
	return fw
	
def newfile():
	"""
	"""
	fw.close()
	t = datetime.datetime.utcnow()
	tm = t.strftime('%Y%m%d')
	day = t.strftime('%d')
	fn = usr+'_'+tm
	fw = createfile(fn)
	return fw

# Open serial port
port = serial_ports()[0]
ser = serial.Serial()
ser.baudrate = 115200
ser.port = port
try:
    ser.open()
except (Exception, serial.SerialException):
    pass

# File name constitution
usr = getpass.getuser()
t = datetime.datetime.utcnow()
tm = t.strftime('%Y%m%d')
day = t.strftime('%d')
fn = usr+'_'+tm
fw = createfile(fn)


a = 0
while a < 1000:
	dd = datetime.datetime.utcnow().strftime('%d')
	if int(dd) > int(day):
		fw = newfile()
    #~ inline = ser.readline()
	fw.write(ser.readline())
	a+=1
ser.close()
fw.close()
