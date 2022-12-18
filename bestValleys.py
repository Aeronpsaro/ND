def getBestValley(valleys, north):
    valleys.sort(key = lambda x: x[0], reverse = True)
    return valleys[0]
    