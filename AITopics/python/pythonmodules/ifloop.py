# if condition:
#     action


# if <condition>:  
#     <action>
# else:   
#     <action>


# if condition:
#     action
# elif condition:
#     action
# else:
#     action


# if condition:
#     action
# elif condition:
#     action
# elif condition:
#     action
# elif condition:
#     action
# else:
#     action

a = 10
b = 20

if a > b:
    print("a is greater than b")

if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")


if a > b:
    print("a is greater than b")
elif a < b:
    print("b is greater than a")
else:
    print("a and b are equal")

c = 30
d = 40
e = 50


if a > b and a > c and a > d and a > e:  # all the condition should be true
    print("a is greatest")
elif b > a and b > c and b > d and b > e:
    print("b is greatest")
elif c > a and c > b and c > d and c > e:
    print("c is greatest")
elif d > a and d > b and d > c and d > e:
    print("d is greatest")
elif e > a and e > b and e > c and e > d:
    print("e is greatest")
else:
    print("all are equal")

if a > b or a > c :  # any one condition should be true
    print("a is greatest")

s1 = 'daniel'

if 'd' in s1:
    print("d is present in s1")

if len(s1) > 5:
    print("length of s1 is greater than 5 characters")

l1 = [10,20,30,40,50,20]

if 20 in l1:
    print("20 is present in l1")

count = 0

for i in l1:
    if i == 20:
        count += 1

print(f"20 is present in l1 for {count} times")





