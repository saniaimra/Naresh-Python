# create 2 lists take an input from user and list 1 should be even numbers and list 2 should have odd numbers
x = int(input())
list_1 = []
list_2 = []

if x % 2 == 0:
    list_1.append(x)
else:
    list_2.append(x)

print("Even List:",list_1)
print("Odd List:",list_2)


# Check if an element is present inside the list 

x = input("Give the input:")

cities = ['Bucharest' , 'Monaco' , 'Brooklyn' , 'LA']

if cities.count(x) >= 1:
    print("Present")
else :
    print("Not Present")




