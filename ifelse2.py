# Given three angles of a triangle check if it is valid triangle

def checkTriangle(x,y,z):
    if x+y+z == 180:
        return "It is a valid triangle"
    else:
        return "Invalid Triangle"
    
print(checkTriangle(60,60,60))
