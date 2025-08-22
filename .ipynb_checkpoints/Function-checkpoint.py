# def add(a, b):
#     print(a + b)
# def sub(a, b):
#     print(a - b)
# def multyply(a, b):
#     print(a * b)
# def dev(a, b):
#     print(a / b)
# add(5, 5)
# sub(10, 8)
# multyply(4, 6)
# dev(10, 5)  

# def my_function(fname):
#     print(fname + " Hello")
# my_function("harish")
# my_function("sir")

# def my_function(fname, lname):
#     print(fname, "", lname)
# my_function("harish", "khileri")

# def my_function(*kids):
#     print("The youngest child is", kids[1])
# my_function("jone", "deo", "leo")


# def my_function(country = "Indai"):
#     print("I am from ", country)
# my_function()

# def my_function(food):
#     for x in food:
#       print(x)
# fruits = ["apple", "banana", "mango"]
# drinks = ["water", "coco-cola", "appy-fizz"]
# my_function(fruits)
# my_function(drinks)

# def my_function(x):
#     return x * 2
# print(my_function(5))
# print(my_function(8))
# print(my_function(15))
# print(my_function(10))

# def my_function(x):
#     print(x * 2)
# my_function(8)

# def my_function(fname, lname):
#     print("Enter you full name  : ", fname, lname)
# #my_function()
# my_function("harish", "khilery")

# def child(*kids):
#     print(kids[1])
# child("rohit", "raju", "manga")

# def myfunction(food):
#     for x in food:
#         print(x)
# fruits = ["mango", "apple", "papaya"]
# myfunction(fruits)

# def username(name):
#     print(f"Hello {name} have a greate coding practice ")
# username("harish")


# def company(employ):
#     print(f"{employ} is realy hardworker and progressible person. thank you {employ} sir")
# company("Harish Khileri")
# company("Vijay Choudhary")


# def name(name = "harish"):
#     print(f"hello {name}")
# name()
# name("rahul")

# def calculator(a, b):
#     sum = a + b
#     diff = a - b
#     multy = a * b
#     div = a / b
#     return sum, diff, multy, div
# sum, diff, multy, div = calculator(4, 8)
# print(sum, diff, multy, div)

# def square(x):
#     return x * x
# print(square(7))

# square = lambda x : x * x
# print(square(8))

# cube = lambda x : x * x * x
# print(cube(3))
 
# add = lambda x, y : x + y
# diff = lambda x, y: x - y
# mult = lambda x, y: x * y
# div = lambda x, y: x / y
# print(add(81, 9))
# print(diff(70, 35))
# print(mult(5, 10))
# print(div(10, 5))

# say_hello = lambda : "Hello"
# print(say_hello())


# how to use map() in lambda function
#n = [22,34,5,6,8]
# square = (list(map(lambda x, y: x * x, y)))
# print(square(5, 4))

# add = lambda a,b,c:a + b * c              # lambda arguments : expression
# print(add(3,4,5,))
# print(add(34,56,67))


def myfunction(n):
    return lambda a:a*n
my = myfunction(5)
print(my(10))