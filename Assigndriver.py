# Allocate nearest driver
# import Distances
# def nearestDriver(c1,c2,dx1,dy1,dx2,dy2):

#     d1 = Distances.eucDistance(c1,c2,dx1,dy1)

#     d2 = Distances.eucDistance(c1,c2,dx2,dy2)

#     if d1 < d2:
#         print("Assign Driver1")
#     else:
#         print("Assign Driver2")

# nearestDriver(1,2,2,3,4,6)
import math

def dist(point_1,point_2):
    d = math.sqrt((point_2[0]-point_1[0])**2 + (point_2[1]-point_1[1])**2)
    return d

def AssignDriver(d1,d2,u):
    if dist(d1,u) < dist(d2,u):
        print("Assign driver 1")
    else:
        print("Assign driver 2")
d1 = (2,3)
d2 = (8,9)
u = (10,11)

AssignDriver(d1,d2,u)


