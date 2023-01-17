#!/usr/bin/env python3


from loop import loop

import sys
from ev3dev2.sensor.lego import TouchSensor
from threading import Thread
from time import sleep


ts = TouchSensor()
pulsado = True
def main():    
    while pulsado: 
        loop()
        sleep(0.5)

pulsado = True
t = Thread(target=main)
t.start()
ts.wait_for_bump()
pulsado = False

    


