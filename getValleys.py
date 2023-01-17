#!/usr/bin/env python3
import sys
INFINITY = 0
THRESHOLD = 30
def getValleys(measurements):
    print(measurements, file=sys.stderr)
    valleys = []
    inValley = False
    valleyBegin = (0, INFINITY)
    print(len(measurements[0]))
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
    
    return valleys
