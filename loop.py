#!/usr/bin/env python3

from spinTo import spinTo
from getDistance import getDistance
from getNorth import getNorth
from getValleys import getValleys
from getBestValley import getBestValley
from getRoute import getRoute
from move import move
import time
from ev3dev.ev3 import Sound
import sys
from ev3dev2.sensor.lego import TouchSensor

ts = TouchSensor()
MEASURE_WIDTH = 10
SPINS = 1
angles = list(range(0,181,MEASURE_WIDTH))


def loop(currentAngle):

    reverse = angles[0] > 90

    measurements = []
    #angles.append(0)

    ts.on_press = lambda: sys.exit()

    for angle in angles:
        #print(currentAngle, file=sys.stderr)
        #currentAngle = spinTo(90)
        currentAngle = spinTo(angle - currentAngle)
        measurements.append((currentAngle - 90, getDistance()))

    if reverse:
        measurements.reverse()
    
    print("RODOLFIN", file=sys.stderr)
    #time.sleep(3)
    north = getNorth() 
    #north = 0
    
    valleys = getValleys(measurements)
    chosenValley = getBestValley(valleys, north)
    if not chosenValley:
        if(abs(north - 90) < abs(north + 90)):
            phi = 90
        else:
            phi = -90

        move(0, phi)
    else:
        phi = getRoute(chosenValley, north)
        move(SPINS, phi)
        
    angles.reverse()
    return currentAngle
    
