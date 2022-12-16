executionTime = T
def loop():
	measurements = []
	for i in range(len(angles)):
		measuredAngle = spinTo(angle[i])
		measurements.append((measuredAngle, measure()))
	north = getNorth()
	valleys = getValleys(measurements)
	chosenValley = getBestValley(valleys, north)
	phi = getRoute(chosenValley, north)
	move(T, phi)
