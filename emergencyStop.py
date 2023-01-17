#!/usr/bin/env python3

import sys
from ev3dev2.sensor.lego import TouchSensor

btn = Button()

if btn.escape:
   sys.exit()
