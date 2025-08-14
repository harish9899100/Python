# simple squares program
# num = int(input("Enter a number for check squares :"))
# print(num**2)

# num = int(input("Enter a number for print even number : "))            # find the even number
# for x in range(2, num, 2):
#     print(x)

# num = int(input("Enter a number for print odd number : "))              # find the odd number
# for x in range(1, num, 2):
#     print(x)

# name = str(input("Enter your name : "))                                  # print each charcter of the name
# for char in name:
#     print(char)


# While loop in python
# num = int(input("Whare to start print number : "))
# end = int(input("Whare to stop print number : "))
# while num <= end:
#     print(num)
#     num += 1

# num = 8
# while num >= 1:            # countdown form 8
#     print(num)
#     num -= 1

# while True:
#     pwd = input("Enter your password : ")
#     if pwd == "python":
#         print("Enter in your laptop : ")
#         break


# for x in range(1, 21):
#     if x % 5 == 0:
#         print("The 5 divisible numbers is : ", x)

number = int(input("Enter a number : "))
fact = 1
for i in range(1, number+1):
    fact *= i
print("The fectorial number of :",number, "is :", fact)

