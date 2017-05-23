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
c=1
id_idx = 4
raw_id = 'DD'
sv_idx = 7
snr_idx = 8
prn_idx = [9, 16]
l_idx = [17, 24]
f_idx = [25, 28]
indic_idx = 29
#if ser.is_open == True:
while c<10:
    inline = ser.readline()
    if inline[0] == 160:
        line = bytes(inline).splitlines()
        for l in line:
            if len(l) > 3:
#                b_length = b''.join([b'l[2]', b'l[3]'])
#                msg_length = int.from_bytes(b_length, byteorder='big')
#                msg_len = len(l)
#                l = l.split()
#                print (l)
#                print (hex(l[1]), l[1], l[2], hex(l[-1]))
#                print ('MSG Length: ', msg_length)
                unpacked = ['{:02X}'.format(b) for b in l]
#                uu = [str.encode(s) for s in unpacked]
#                print (l)
#                print (unpacked)
#                print (uu[id_idx])
                if unpacked[id_idx] == raw_id:
#                    print (unpacked)
                    sv = int(unpacked[sv_idx], 16)
                    snr = int(unpacked[snr_idx], 16)
#                    print ('BYTES: ', msg_length)
                    print ('SV: ', sv)
                    print ('SNR: ', snr)
#                    prn = b''.join( uu[prn_idx[0]:prn_idx[1]] )
                    prn = int(''.join(unpacked[prn_idx[0]:prn_idx[1]]), 16)
                    l = int(''.join(unpacked[l_idx[0]:l_idx[1]]), 16)
                    
#                    l = int.from_bytes(unpacked[l_idx[0]:l_idx[1]], byteorder='big')
#                    f = int.from_bytes(unpacked[f_idx[0]:f_idx[1]], byteorder='big')
                    print ('PRN: ', prn)
                    print ('L: ', l)
#                    print ('Phase: ', l)
#                    print ('Doppler: ', f)
                    print ('---------------------')
            
        
    c+=1
ser.close()
#        print (len(line))
#    print (line[0])
#    exit
#    l = struct.unpack('s',line)
#    print (line)
#    print ()
#