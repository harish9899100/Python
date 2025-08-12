#comparesion between two numbers and check number is graterthen, number is lessthen and number's are equal
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
if num1 > num2:
    print("The number ", num1 , "is grater then ", num2)
elif num1 < num2:
    print("The number ", num2 , "is grater then ", num1)
else:
    print("The both number ", num1 ,"and" , num2 ,"is equal")