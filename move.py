#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D

def move(spins, phi):
    large_motorA = LargeMotor(OUTPUT_A)
    large_motorD = LargeMotor(OUTPUT_D)
    
    #Pasamos de grados a radianes
    phi = (phi * 2 * 3.14) / 360
    
    degree = phi * 12 / (2 *2.75)
    
    degree = (degree * 180) / 3.14
    
    large_motorA.on_for_degrees(speed=20, degrees=degree, block=False)
    large_motorD.on_for_degrees(speed=20, degrees=-degree, block=True)
    
    large_motorA.on_for_degrees(speed=20, degrees=spins*360, block=False)
    large_motorD.on_for_degrees(speed=20, degrees=spins*360, block=True)

    return large_motorD.on_for_degrees(speed=0, degrees=0, block=True)
    
