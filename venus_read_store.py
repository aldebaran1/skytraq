# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:35:38 2017

@author: smrak
"""

import sys
import glob
import serial


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
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
    
port = serial_ports()[0]
ser = serial.Serial()
ser.baudrate = 115200
ser.port = port
try:
    ser.open()
except (Exception, serial.SerialException):
    pass

fw = open('test.sqr', 'w')
c=1
while c < 1000:
    inline = ser.readline()
    fw.write(str(inline)+'\n')
    c+=1
ser.close()
fw.close()