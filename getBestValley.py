#!/usr/bin/env python3
import sys

def getBestValley(valleys, north):

    securityDist = 10
    
    openValleys = []

    for valley in valleys:
        if (abs(valley[0][0] - valley[1][0]) < securityDist):
            openValleys.append(valley)

    def distanceToNorth(valley):
        return min(abs(valley[0][0] - north) , abs(valley[1][0] - north))

    return sorted(valleys, key=distanceToNorth)[0]


