from ev3dev2.motor import MediumMotor

def spinTo(angle):

  motor = MediumMotor(port='C')
  motor.on_for_degrees(speed=1, degrees=angle, brake=True, block=True)
  
  return motor.position
