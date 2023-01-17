#!/usr/bin/env python3

from ev3dev2.sensor.lego import *

#Función que devuelve la distancia medida por el sensor de ultrasonido

us = UltrasonicSensor()
#us.mode = 'US_DIST_CM'

def getDistance():
    dist=us.distance_centimeters
    return dist