#Build a module called areas inside this module 1. the function to calculate volume of a sphere = 4/3pir2 
# 2. volume of cuboid = l*w*h
# to get exact pi value math.pi
import math
def volumeSphere(r):
    result = (4/3)*math.pi*(r**2)
    return result

def volumeCuboid(l,w,h):
    result = l*w*h
    return result

