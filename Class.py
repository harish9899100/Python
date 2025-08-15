# In this file we are practice about class and object in python

# class myclass:
#     x = 5
# p1 = myclass()
# print(p1.x)

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p1 = person("harish", 22)
# print("The name of Person is :",p1.name)
# print("The age of person is :",p1.age)

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = person("rohit", 23)
print("The name of person is :", p1.name)
print("The age of person is : ", p1.age)
p2 = person("vikash", 21)
print("The name of person is :", p2.name)
print("The age of person is :", p2.age)