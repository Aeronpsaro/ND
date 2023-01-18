#!/usr/bin/env python3
import sys
INFINITY = 0
THRESHOLD = 50
def getValleys(measurements):

    valleys = []
    inValley = False
    valleyBegin = (0, INFINITY)
    measurements.pop()
    for measurement in measurements:
        if measurement[1] > THRESHOLD:
            if inValley: continue
            inValley = True
            continue
        if inValley:
            inValley = False
            valleys.append((valleyBegin, measurement))
        valleyBegin = measurement
    if inValley:
        valleys.append((valleyBegin, (180, INFINITY)))
        
    print(measurements, file=sys.stderr)
    print(valleys, file=sys.stderr)
    return valleys
