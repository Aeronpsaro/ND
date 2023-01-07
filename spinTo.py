#!/usr/bin/env python3

from ev3dev2.motor import MediumMotor, OUTPUT_C

def spinTo(angle):

  motor = MediumMotor(OUTPUT_C)
  motor.on_for_degrees(speed=1, degrees=angle, brake=True, block=True)
  
  return motor.position
