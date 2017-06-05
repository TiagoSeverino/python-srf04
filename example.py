from srf04 import *

#Trigger, Echo Pins
sonar = SRF04(31, 32)

print sonar.getCM()