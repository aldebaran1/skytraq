#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  utilfunctions.py
#  
#  Copyright 2017  <pi@eclipsepi>
#  

def checksum(data):
	"""
	Calculate and return a checksum for skytraq binary protocol
	XOR
	"""
	checksum = 0
	for by in data:
		checksum ^= ord(by)
	#print (hex(checksum))
	return hex(checksum)
