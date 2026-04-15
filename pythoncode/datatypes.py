# # we are learning data types in python 
# ''' 
# Data types in python
# we are going to practice string, float, int, boolean data types in python
# '''
# a = "sameqr211@"  # string
# b ="123"
# c = 'i am learning python programming language'
# print(type(a))
# print(type(b))
# print(type(c))
# d = 20  
# e = 20.5  
# f = True  
# print(type(d), d)
# print(type(e),e)
# print(type(f),f)

# List Data types:  add the data, remove the data, update the data, sort the data, reverse the data, slicing the data, indexing the data
l1 = []  # empty list 
l2 = []
t1 = ()   # tuples
s1 = {}  # set
d1 = {"key": "value"} # dictionary 

# l3 = [1,2,40,3,10,4]   # index is the address/location where the data is present  [0,1,2,3,4,5] or [-6,-5,-4,-3,-2,-1]
# print(l3[0:3])
# print(l3[5])
# # print(l3)
# # print(l3[::-1])
# # print(l3[-1])
# # l3.reverse()
# # print(l3)
# l3.sort()
# print(l3)
# l3.append(50)
# print(l3)
# l3.insert(2, 100)
# print(l3)

# if 100 in l3:
#     idx = l3.index(100)
#     print(idx)
#     l3[idx] = 200
#     print(l3)

# 100 value is present in index -- 2    l3[2] = 200
# for i in  100,10,40:
#     if i in l3 and i == 100:
#         idx = l3.index(i)
#         print(idx)
#         l3[idx] = 200
#     elif i in l3 and i == 10:
#         idx = l3.index(i)
#         print(idx)
#         l3[idx] = 100
#     elif i in l3 and i == 40:
#         idx = l3.index(i)
#         print(idx)
#         l3[idx] = 400
# print(l3)   


# l3.remove(50)
# print(l3)
# l3.pop(2)
# print(l3)
# l3.clear()
# print(l3)

# l4 = []
# l4.extend([1,2,3,4,5])
# print(l4)
# l4.extend(l3)
# print(l4)

# t1 = (1,2,3,4,5,4,3,5)  # tuples are immutable(we cannot do any action like add, modify or delete) data types
# print(t1)
# a  = t1.count(4)  # count the number of times the value is present in the tuple
# print(a)
# b = t1.index(5)  # index of the first occurrence of the value in the tuple
# print(b)

# user_list = ("admin", "root", "user1")

# user_name = input("Enter your username: ")

# if user_name in user_list:
#     print("Welcome, ", user_name)
# else:
#     print("You are not authorized to access this system.")

s1 = {"sam", "arun","daniel"}   # set is a collection of unique elements, it is unordered and unindexed data type
print(s1)

l4 = [1,2,3,4,5,4,3,5]
print(l4)
l4 = set(l4)
print(l4)
l4 = list(l4)
print(l4)
# l4 = list(set(l4))  # convert the list to set and then back to list to remove duplicates
# print(l4)