cities = ['Venice','Monaco','Abu Dhabi','Dubai']
numbers_=[1,2,3,4,5]

# the style of building structures which can accomodate multiple types of values is called object oriented programming
#these structures are called objects even strings and ints

# ---------------OOPS------------------------------
# An object has multiple functions in it
#class is a keyword that is used before specifying the object

# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth = breadth
#     def getLength(self):
#         return self.length
    
#     def getBreadth(self):
#         return self.breadth
    
#     def areaRect(self):
#         return self.breadth*self.length
    
# my_rect = Rectangle(10,10)  
# oth_rect = Rectangle(5,5)

# print(my_rect.areaRect())
''' python reads it as Rectangle(my_rect,10,10)
                                #(self,length,breadth)
                                #my_rect.getLength() == len(my_rect)'''


#Q1. Create a point which consists x , y coordinate and have methods to show x and y values

# class Point:
#     def __init__(self,x_cood,y_cood):
#         self.x_cood = x_cood
#         self.y_cood = y_cood

#     def get_x(self):
#         return self.x_cood
#     def get_y(self):
#         return self.y_cood
    
# x_coordinate = Point(3,4)
# y_coordinate = Point(6,7)
# print(x_coordinate.get_x())
# print(y_coordinate.get_y())



class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self, oth_point):
        return ((oth_point.x-self.x)**2 + (oth_point.y - self.y)**2)**0.5
    
p1 = Point(1,2)
p2 = Point(3,5)

print(p1.distance(p2))

