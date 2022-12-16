threshold = 10
def getValleys(measurements):
    valleys = []
    inValley = False
    firstIsValley = False
    if measurements[0][1] < threshold:
        firstIsValley = True
    inFirstValley = firstIsValley
    inValley = inFirstValley
    for measurement in measurements:
        if measurement[1] < threshold:
            if inValley:
                lastValley = measurement
                continue
            valleyBegin = measurement
            lastValley = measurement
            inValley = True
            continue
        if inFirstValley:
            lastFirstValley = lastValley
            inFirstValley = False
            inValley = False
            continue
        if inValley:
            inValley = False
            valleys.append((valleyBegin, lastValley))
    if inValley:
        if not firstIsValley:
            valleys.append((valleyBegin, valleyBegin))
            return valleys
        valleys.append((valleyBegin, lastFirstValley))
        return valleys
    valleys.append((measurements[0], lastFirstValley))
    return valleys
