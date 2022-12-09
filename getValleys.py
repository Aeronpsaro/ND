threshold = 10
def getValleys(measurements):
    valleys = []
    inValley = False
    for measurement in measurements:
        if measurement[1] < threshold:
            if inValley:
                lastValley = measurement
                continue
            valleyBegin = measurement
            continue
        if inValley:
            inValley = False
            valleys.append((valleyBegin, lastValley))
    return valleys
