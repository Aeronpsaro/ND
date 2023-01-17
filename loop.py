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

def loop():
    angles = list(range(0,181,MEASURE_WIDTH))
       
    currentAngle = 0
    measurements = []
    angles.append(0)

    ts.on_press = lambda: sys.exit()
        

    for angle in angles:
    # print(currentAngle, file=sys.stderr)
        currentAngle = spinTo(angle - currentAngle)
        measurements.append((currentAngle, getDistance()))
    
    print("RODOLFIN", file=sys.stderr)
    #time.sleep(3)
    north = getNorth() 
    #north = 0
    
    valleys = getValleys(measurements)
    chosenValley = getBestValley(valleys, north)
    phi = getRoute(chosenValley, north)
    move(SPINS, phi)
    sorted(angles, reverse=True)