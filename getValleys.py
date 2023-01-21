#!/usr/bin/env python3
import sys
BEGIN = 0
THRESHOLD = 25
def getValleys(measurements):
    valleys = []
    inValley = False
    valleyBegin = (-90, BEGIN)
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
        valleys.append((valleyBegin, (90, BEGIN)))
        
    print(measurements, file=sys.stderr)
    print(valleys, file=sys.stderr)
    return valleys
