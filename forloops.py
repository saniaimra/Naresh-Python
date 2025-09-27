# iteration is a process in which we go through every value in a data struture
# A data structure is iterable if it alllows iteration using iterator

#Q1. write a python functionwhich takes input of a number and calculates the sum till that point

# def sum_num(x):
#     sum_ = 0
#     for i in range(x+1):
#         sum_ += i
#     print(sum_)

# sum_num(10)

# Q2 . input l1 = [1,2,5,7,10],l2 = [8,12,9,20,50]
# output = [9,14,14,27,60]

# l1 =[1,2,5,7,10]
# l2 = [8,12,9,20,50]
# def sum_index(l1,l2):
#     res = []

#     for i in range(len(l1)):
#         res.append(l1[i] + l2[i])
#     print(res)

# sum_index([1,2,5,7,10],[8,12,9,20,50])

#Q3. input = "Mississippi"
# output = {M : 1 , i : 4, s: 4, p : 2}

# input = "Mississippi"
# list_ = list(input)
# dict_ = {}
# for i in list_:
#     dict_[i] = list_.count(i) 
# print(dict_)

# input = "Mississippi"
# list_ = list(input)
# dict_ = {}
# for i in range(len(list_)):
#     dict_[list_[i]] = list_.count(list_[i]) 
# print(dict_)


# Q4. input = ["Dog","F","Horn","Fight"]
#output = {"Dog":3,}

input = ["Dog","F","Horn","Fight"]
dict_ = {}
for i in input:
    dict_[i] = len(i)

print (dict_)



