# q1. write a function which takes any two numbers as the input and the operation as the input and return the solution

def operations(x,y,z):

    if z == 'add':
        result = x+y
    elif z == 'sub':
        result = x-y
    elif z == 'mul':
        result = x*y
    elif z == 'div':
        result = x/y
    else:
        result = 'Enter valid operator'

    return result

print(operations(2,3,'add'))
    

