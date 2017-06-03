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

def newfile(fw, day):
    """
    """
    fw.close()
    t = datetime.datetime.utcnow()
    tm = t.strftime('%Y%m%d')
    day = t.strftime('%d')
    path = os.path.dirname(os.path.realpath(__file__))
    fn = path+'/data/'+usr+'_'+tm
    fw = createfile(fn)
    return fw

def setModuleMore(ser):
#    prefix = '\xa0\xa1\x00\x03'
#    data = '\x09\x02\x01'
#    cs = chr(sum(map(ord, data)))
#    sufix = '\x0d\x0a'
    message = '\xa0\xa1\x00\x03\x09\x02\x01\x0c\x0d\x0a'
    ser.write(message)
    ack = ser.readline()
    return ack
#    print (message)

def readPositionDataRate(ser):
    message = '\xa0\xa1\x00\x01\x10\x10\x0d\x0a'
    ser.write(message)
    ack = ser.readline()
    msg = ser.readline()
    return [ack, msg]

def readBinaryDataRate(ser):
#    prefix = '\xa0\xa1\x00\x01'
#    data = '\x1f'
#    cs = chr(sum(map(ord, data)))
#    sufix = '\x0d\x0a'
    message = '\xa0\xa1\x00\x01\x1f\x1f\x0d\x0a'
    ser.write(message)
    ack = ser.readline()
    msg = ser.readline()
    return [ack, msg]

def setDataOutput(ser):
    # 'A0 A1 00 09 1E'
    # 04 == 10Hz
    # 00 00 01 00
    # 01 GPS only
    # 00 01
    # 37
    # 0D 0A
    data = '\x1E\x04\x00\x00\x01\x00\x01\x00\x01'
    message = '\xA0\xA1\x00\x09\x1E\x04\x01\x01\x01\x01\x01\x00\x01\x1a\x0D\x0A'
#    message = '\xA0\xA1\x00\x09\x1E\x00\x00\x00\x01\x01\x03\x01\x01\x1d\x0D\x0A'
    ser.write(message)
    ack = ser.readline()
    return ack

# Open serial port
try:
    port = serial_ports()[0]
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = port
    ser.open()
except (Exception, serial.SerialException):
    raise EnvironmentError('No ports found')

# File name constitution
usr = getpass.getuser()
t = datetime.datetime.utcnow()
tm = t.strftime('%Y%m%d')
day = t.strftime('%d')
path = os.path.dirname(os.path.realpath(__file__))
fn = path+'/data/'+usr+'_'+tm
fw = createfile(fn)

# Main script
a = 0
#ack1 = setModuleMore(ser)
#ack2 = setDataOutput(ser)
#pos_rate = readPositionDataRate(ser)
bin_rate = readBinaryDataRate(ser)
#print ('Data return ack: ', ack2)
#print ('Query return: ', pos_rate)
print ('Query return binary: ', bin_rate)
#while a < 10:
#    dd = datetime.datetime.utcnow().strftime('%d')
#    if int(dd) > int(day):
#        fw = newfile(fw, day)
#    fw.write(ser.readline())
#    a+=1
#print ('to je to')
ser.close()
fw.close()
