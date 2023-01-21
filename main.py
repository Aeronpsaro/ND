#!/usr/bin/env python3


from loop import loop

from spinTo import spinTo

import sys
from ev3dev2.sensor.lego import TouchSensor
from threading import Thread
from time import sleep


ts = TouchSensor()
noPulsado = True

def main():  
    #spinTo(-90)
    currentAngle = 0  
    while noPulsado: 
        currentAngle = loop(currentAngle)
        sleep(0.5)

noPulsado = True
t = Thread(target=main)
t.start()
ts.wait_for_bump()
noPulsado = False

    


