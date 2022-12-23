from ev3dev2.sensor.lego import CompassSensor 

compass = CompassSensor(INPUT_3)

def getNorth():
    bearing = compass.bearing # Obtiene el valor del compás en grados
    return bearing