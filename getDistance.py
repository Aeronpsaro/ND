#!/usr/bin/env python3

from ev3dev2.auto import *

#Función que devuelve la distancia medida por el sensor de ultrasonido

us = UltrasonicSensor(INPUT_1)
us.MODE_US_DIST_CM = 'US_DIST_CM'
print(us.value())
def getDistance():
    dist=us.value()
    return dist