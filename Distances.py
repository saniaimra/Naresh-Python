import math
def eucDistance(x1,y1,x2,y2):
    res = math.sqrt(((x2-x1)**2)+((y2-y2)**2))
    return res

def manDistance(x1,y1,x2,y2):
    res= abs(((x2-x1)**2)+((y2-y2)**2))
    return res

