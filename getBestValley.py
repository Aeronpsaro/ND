#!/usr/bin/env python3
import sys

def getBestValley(valleys, north):
    
    result = []
    dist_seguridad = 10
    accurateAngle = 0

    for i in range(len(valleys)):
        
        
        if valleys[i][1][0] > 95:
            accurateAngle = north + 90 - valleys[i][1][0]
        elif valleys[i][0][0] < 95:
            accurateAngle = north - 90 + valleys[i][0][0]
        difAngle = abs(north - accurateAngle)
        
        if difAngle > north:
            continue
        difDist = abs(valleys[i][1][1] - valleys[i][0][1])
        if valleys[i][1][1]==0 and valleys[i][0][1]==0:
            difDist = 255
        if difDist <= dist_seguridad:
            continue
        
        result.append((difDist, i))
    result.sort(key = lambda x: x[0])
    print([valleys[result[0][1]]], file = sys.stderr)

    return [valleys[result[0][1]]]


