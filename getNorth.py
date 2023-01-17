#!/usr/bin/env python3

#from ev3dev2.sensor.lego import CompassSensor 

from ev3dev.ev3 import *
from ev3dev2.sensor import Sensor
import sys


def getNorth():

    seeker = Sensor(driver_name='ht-nxt-compass')
    seeker.mode = 'COMPASS'
    print(seeker.value(0), file = sys.stderr)
    # direction is 0 for no signal, or 1-9 for left-right direction
    direction = seeker.value(0)
    return direction