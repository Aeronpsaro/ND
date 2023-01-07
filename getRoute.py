#!/usr/bin/env python3

minWidthCenter = 25 #Tamaño mínimo del robot para que el robot no tenga que ir por el centro
securityDist = 5 #Distancia de seguridad que tiene que dejar el robot con respecto a los obstáculos

#-------------------
# Función que obtiene la mejor ruta del robot
# - valley: array que contiene donde empieza y donde acaba el valle
# - north: donde se encuentra el objetivo
#------------------
def getRoute(valley, north):
    valleyWidth = valley[1][0] - valley[0][0]
    #Si el norte está dentro del valle
    if (north < valley[1][0] and north > valley[0][0]):
        return north
    else:
        #Comprobamos que si el ancho no es suficiente, el robot tiene que ir
        # por el centro del valle
        if (valleyWidth < minWidthCenter):
            return valleyWidth / 2
            
        else:
            #Comprobamos de que lado del valle está más cerca north
            if (abs(north - valley[0][0]) < abs(north - valley[1][0])):
                return valley[0][0] + securityDist
            else:
                return valley[1][0] + securityDist