# class dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def bark(self):
#         print(f"{self.name} is bark ")
# dog1 = dog("joya", 4)
# dog1.bark()

# class calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def add(self):
#         return self.a + self.b
# a = int(input("Enter first number :"))
# b = int(input("Enter your second number :"))

# calc = calculator(a, b)
# print("Add = ", calc.add())







# class car:
#     def __init__(self, company, car_name):
#         self.company = company
#         self.car_name = car_name
#         self.meater = 0

#     def drive(self, kms):
#         print(f"drive the car {kms} kms...")
#         self.meater += kms
# car1 = car("Mahinda", "SUV 7OO")
# print(f"The car compeny is : {car1.company} and\nThe car model name is :{car1.car_name}")
# print(f"Initial car meater reading is {car1.meater}")
# car1.drive(50)
# car1.drive(200)
# print(f"Now the car total meater reading is {car1.meater}")

# question 1.
# Create a Student Class

# Attributes: name, age, grade

# Methods: display_info() to print student details

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#     def display_info(self):
#         print(f"\nThe name of student is : {self.name}\nThe age of student is : {self.age}\nThe grade of student is : {self.grade}\n")
# s = Student("Rohit", 23, "A++")
# s.display_info()
# s2 = Student("Rajendra", 25, "A")
# s2.display_info()


# question 2
# Bank Account Class

# Attributes: account_number, account_holder, balance

# Methods: deposit(amount), withdraw(amount), check_balance()

# class Bankaccount:
#     def __init__(self, account_number, account_holder, balance):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposite(self, amount):
#         self.amount = amount
#         self.deposi -= self.amount
#         print(f"The deposite balance is : {self.balance}")
    
#     def balance_check(self):
#         self.balance
#         print(f"Your account current balance is : {self.balance}")
# a1 = Bankaccount(1234567890123, "Dipak", 50000)
# a1.balance_check()
# a2 = Bankaccount(2353454564, "fdfs", 60000)
# a2.balance_check()


# Car Class

# Attributes: brand, model, year, speed

# Methods: accelerate(), brake(), display()


class Car:
    def __init__(self, brand, name, model):
        self.brand = brand
        self.name = name
        self.model = model
        self.speed = 0

    def accelater(self):
        self.speed += 10
        print(f"Now you press accelater and your speed is increase : {self.speed} km/h")
        
    
    def brake(self):
        if self.speed > 10:
            self.speed -= 10
        else:
            self.speed = 0
        print(f"Now you press the breke of car and speed is decrease : -10 km/h")

    def display(self):
        print(f"Your current speed is {self.speed} km/h\n")

a = Car("Toyota", "Fortuner", 2024)
print(f"The car brand is : {a.brand}\nThe car name is : {a.name}\nThe car model is :  {a.model}\nThe car speed  is : {a.speed}")
a.accelater()
a.brake()
a.display()
b = Car("Mercedes", "Mayback", 2024)
print(f"The car brand is : {b.brand}\nThe car name is : {b.name}\nThe car model is :  {b.model}\nThe car speed  is : {b.speed}")
b.accelater()
b.accelater()
b.accelater()
b.accelater()
b.accelater()
b.brake()
b.display()