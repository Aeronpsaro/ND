import sys
from ev3dev2.button import Button

btn = Button()

if btn.escape:
   sys.exit()
