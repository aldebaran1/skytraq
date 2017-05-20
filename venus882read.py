# -*- coding: utf-8 -*-
"""
Created on Sat May 20 09:10:34 2017

@author: smrak
"""

#import numpy as np
import serial as ps
import struct

ser = ps.Serial()
ser.baudrate = 115200
ser.port = 'COM3'

ser.open()
#if ser.is_open == True:
while 1:
    line = ser.readline()
    print (line[0])
#    exit
#    l = struct.unpack('s',line)
#    print (line)
#    print ()
