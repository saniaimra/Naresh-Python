# try to store squares of even numbers


# list_ = []
# for i in range(11):
#     if i % 2 == 0:
#         list_.append(i**2)
# print(list_)


# generate a list of squares of all the numbers from 1 to 50

# list_ = []
# for i in range(51):
#     list_.append(i**2)
# print(list_)

# --------------List comprehension ----------------------

# squares = [i **2 for i in range(1,51)]

# dict_ = {}
# for i in range(21):
#     dict_[i] = i**2
# print(dict_)

# dict_ = {num : num**2 for num in range(21)}
# print(dict_)

# cities = ["Monaco","Baku","Singapore"]
# lower = []
# for i in cities:
#     lower.append(i.lower())
# print(lower)

# lower = [i.lower() for i in cities]
# print(lower)

# --------------------------break and continue---------------------------
# cities = ["Monaco","Baku","Singapore"]
# for i in cities:
#     print(i)
#     if i == "Baku":
#         continue


# Q1. input = [[10,20,30],50,[20,10],[20]]
output = [10,20,30,50,20,10,20]
input = [[10,20,30],50,[20,10],"tokyo",[20]]
output=[]
for i in input:
        if type(i) == int:
            output.append(i)
            continue
            for j in i:
                output.append(j)

print(output)


# input = [[10,20,30],50,[20,10],"tokyo",[20]]
# output=[]
# for i in input:
#         if type(i) == int:
#                 output.append(i)
#         elif type(i) == str:
#                 output.append(i)
#         else:
#             for j in i:
#                 output.append(j)

# print(output)