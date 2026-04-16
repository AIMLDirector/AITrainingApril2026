a = 10  # global variable 
print(a)


def func1():
    b = 20
    print(b)
    print(a)


func1()

print(a)
print("executing b value outside of the function:",b)
