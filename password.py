#Write a function which takes password as input and it is a valid password if it follows the below rules
# 1. It has to be minimum 8 characters
# 2. Should be a mix of alphas and nums
# 3.It should contain atleast one special character
# 4. It should not have spaces
# 5. Should contain a mix of upper and lower cases

def testPassword(x):


    islong = len(x) >= 8
    isnum =  x.isdigit()== False
    isalpha = x.isalpha() == False
    isspace = x.count(" ") == 0
    isspecial = (x.count("@") == 0 and x.count("#") == 0 and x.count("$") == 0 and x.count("_") == 0)

    if  islong and (not (isnum and isalpha)) and (not isspace) and  (isspecial):
        return "Score is 1"
    
    elif islong and  (isnum and isalpha) and (not isspace) and  (isspecial):
        return "Score is 2"
    
    elif islong and  (isnum and isalpha) and  isspace and  (isspecial):
        return "Score is 3"
    
    elif islong and  (isnum and isalpha) and  isspace and  (not isspecial):
        return "Score is 4"
    else:
        return "Strong Password"


    # if len(x) < 8:
    #     return "Password must be 8 chars"
    
    # elif x.isalpha() == True or x.isdigit()== True:
    #     return "Password must contain both alpha and nums"
    
    # elif x.count(" ") >= 1:
    #     return "Password must not contain spaces"
    
    # elif x.isupper() == True or x.islower() == True:
    #     return "Password must contain both upper and lower cases"
    
    # elif x.count("@") == 0 and x.count("#") == 0 and x.count("$") == 0 and x.count("_") == 0:
    #     return "Password must contain special characters"
    # else:

    #     return "Strong Password"

    
print(testPassword("sa a"))


# Create 5 flags isnum , isalpha ,islong, isspacefree,isspecial

