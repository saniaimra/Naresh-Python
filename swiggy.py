
def swiggy(res_loc,user_loc,radius):
    if (res_loc[0]-user_loc[0])**2 + (res_loc[1]-res_loc[1])**2 <= radius**2:
        print("Please select your order")
    else:
        print("Restaurant not in your area")

swiggy((4,5),(18,19),7)

# import math

# def rangeCheck(user_loc, res_loc, radius):

#     if math.dist(user_loc, res_loc) >= radius:

#         return "Not in Range"
    
#     else:

#         return "In Range"
    

# u_ = (10, 30)
# r_ = (2,3)
# print(rangeCheck(u_, r_, 7))