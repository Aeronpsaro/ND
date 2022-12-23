from ev3dev2.auto import *

#Función que devuelve la distancia medida por el sensor de ultrasonido

us = UltrasonicSensor(INPUT_1)
us.MODE_US_DIST_CM = 'US_DIST_CM'

def getDistance():
    dist=us.distance_centimeters
    return dist