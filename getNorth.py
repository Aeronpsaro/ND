from ev3dev2.sensor.lego import CompassSensor 

# Inicializa el sensor de brújula conectado al puerto 1
compass = CompassSensor(INPUT_3)

# Obtiene el valor del compás en grados
bearing = compass.bearing

# Imprime el valor del compás
print(bearing)
