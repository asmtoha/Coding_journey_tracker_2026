from math import atan2, degrees

AB = int(input()) 
BC = int(input()) 
theta = atan2(AB,BC) 
degree = (round(degrees(theta))) 
print(str(degree) + chr(176))