#write a python program to compute the height reached by the ladder on the wall for the following values : a)16feet,75degrees b)20feet,0degrees c)24feet,45degrees d)24feet,80degrees.
import math
length = int(input("enter the length of ladder(feet)"))
angle = int(input("enter the angle of ladder(degrees)"))
perpendicular = length*math.sin(math.radians(angle))
print("the height reached by the ladder=",round(perpendicular,2),"feet")



