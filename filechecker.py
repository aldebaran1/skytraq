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
import glob

pin = 11

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

dt = datetime.datetime.now()
t1 = time.mktime(dt.timetuple())

while True:
    usr = socket.gethostname()        
    t = datetime.datetime.utcnow()
    tm = t.strftime('%Y%m%d')
    dd1 = t.strftime('%d')
    mm1 = t.strftime('%m')
    yy1 = t.strftime('%y')
    day_in_year = t.timetuple().tm_yday
    path = os.path.dirname(os.path.realpath(__file__))     
   
    wlst = path+'/data/'+usr+'0'+str(day_in_year)+'*'
    flist =sorted(glob.glob(wlst))
       
    try:
	
        sizeA = int( os.path.getsize(flist[-1]) )
        dt = datetime.datetime.now()
        t2 = time.mktime(dt.timetuple())
        
        if (t1 + 30) <= t2:
            print (flist)
            print (t1, t2, sizeA)
            sizeB = int( os.path.getsize(flist[-1]) )
            t1 = t2    
            if sizeB > sizeA:
                GPIO.output(pin, GPIO.HIGH)        
            else:
                GPIO.output(pin, GPIO.LOW)
    except:
        print('There is no files in the directory')
