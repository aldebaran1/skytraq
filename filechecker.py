# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:54:11 2017

@author: rinoc
"""

import RPi.GPIO as GPIO
import datetime
import os.path
import time
import socket

pin = 11

GPIO.cleanup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

"""following block is a test block, to be commented out after testing GPIO pin
GPIO.output(pin, GPIO.HIGH)
time.sleep(5)
GPIO.output(pin, GPIO.LOW)
block end"""


usr = socket.gethostname()        
t = datetime.datetime.utcnow()
#tm = t.strftime('%Y%m%d')
#dd1 = t.strftime('%d')
#mm1 = t.strftime('%m')
yy1 = t.strftime('%y')
day_in_year = t.timetuple().tm_yday
path = os.path.dirname(os.path.realpath(__file__))
fn = path+'/data/'+usr+'0'+str(day_in_year)+'.'+yy1+'r' 
sizeA =int( os.path.getsize(fn) )
time.sleep(60)
sizeB =int( os.path.getsize(fn) )

if sizeB > sizeA:
  GPIO.output(pin, GPIO.HIGH)
if sizeB <= sizeA:
  GPIO.output(pin, GPIO.LOW)
