threshold = 10 #Tamaño mínimo del valle para que quepa el robot
minWidthCenter = 25 #Tamaño mínimo del robot para que el robot no tenga que ir por el centro
securityDist = 5 #Distancia de seguridad que tiene que dejar el robot con respecto a los obstáculos

#-------------------
# Función que obtiene la mejor ruta del robot
# - valley: array que contiene donde empieza y donde acaba el valle
# - north: donde se encuentra el objetivo
#------------------
def getRoute(valley, north):
    valleyWidth = valley[1] - valley[0]
    #Si el ancho del valle es mayor que el threshold, significa que puede caber
    if (valleyWidth > threshold ):
        #Si el norte está dentro del valle
        if (north < valley[1] and north > valley[0]):
            spinTo(north)
        else:
            #Comprobamos que si el ancho no es suficiente, el robot tiene que ir
            # por el centro del valle
            if (valleyWidth < minWidthCenter):
                spinTo(valleyWidth / 2)
                
            else:
                #Comprobamos de que lado del valle está más cerca north
                if (abs(north - valley[0]) < abs(north - valley[1])):
                    spinTo(valley[0] + securityDist)
                else:
                    spinTo(valley[1] + securityDist)
    else:
        #Si no hay ningún valle donde quepa el robot, que gire 90º
        spinTo(90)