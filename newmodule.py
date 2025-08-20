# import math
# num = int(input("Enter a number for find squre : "))
# num1 = math.sqrt(num)
# print(num1)

# def add(a, b):
#     return a + b
# a = add(3,5)
# print(a)

def factorial(n):
    if n == 0 or n == 1:                             # we can use like : from newmodule import factorial
        return 1
    return n * factorial(n-1)
a = factorial(int(input("Enter a number for getting factorial : ")))
print(f"Your numbers factorial is :{a}")