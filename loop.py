from spinTo import spinTo
from getDistance import getDistance
from getNorth import getNorth
from getValleys import getValleys
from getBestValley import getBestValley
from getRoute import getRoute
from move import move

MEASURE_WIDTH = 10
angles = range(-90,90,MEASURE_WIDTH)
SPINS = 3
def loop():
    measurements = []
    for angle in angles:
        measuredAngle = spinTo(angle)
        measurements.append((measuredAngle, getDistance()))
    north = getNorth()
    valleys = getValleys(measurements)
    chosenValley = getBestValley(valleys, north)
    phi = getRoute(chosenValley, north)
    move(SPINS, phi)
