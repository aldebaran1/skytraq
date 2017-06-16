# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 12:14:51 2017

@author: smrak
"""
import requests
import urllib3
from datetime import datetime
import socket

def getIP():
    """
    Sebastijan Mrak:
        get & reteurn a public IP address
    """
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://ip.42.pl/raw')
    my_ip = r.data.decode('utf-8')
    return my_ip

def send_simple_message(dev_name, ip):
    dt = datetime.utcnow()
    time = dt.strftime("%d-%m %H:%M")
    return requests.post(
        "https://api.mailgun.net/v3/sandbox1b5516af304e4d3bbb4ce505c254cbca.mailgun.org/messages",
        auth=("api", "key-6e8d2a811ff2ea98114574c72dc988f6"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox1b5516af304e4d3bbb4ce505c254cbca.mailgun.org>",
              "to": "Sebastijan <sebastijan.mrak@gmail.com>",
              "subject": "Current IP address for device: " + dev_name,
              "text": "IP address of the HOST: " +dev_name+ "at a time "+str(time)+" is: "+str(ip)})
    
ip = getIP()
hostname = socket.gethostname()
#print (ip)
send_simple_message(hostname, ip)
