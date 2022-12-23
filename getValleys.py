INFINITY = 99999999999999999999999999999
THRESHOLD = 10
def getValleys(measurements):
    valleys = []
    inValley = False
    valleyBegin = (0, INFINITY)
    for measurement in measurements:
        if measurement[1] < THRESHOLD:
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
