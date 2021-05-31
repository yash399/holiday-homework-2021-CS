#a python program to find the volume of spheres with radius 7cm,12cm,16cm respectively.
import math
radius = int(input("enter the value of radius(cm)"))
volume = 4/3*math.pi*math.pow(radius,3)
print(round(volume,3),"cm")



