# age = int(input("Enter your age : "))
# mamber = bool(input("If you are member of this company then enter yes : \nOther-wise press enter : "))
# if age >= 60:
#     if mamber == True:
#         print("Your senior discount is : 40% ")
#     else:
#         print("Your senior discount is : 25% ")
# else:
#     print("Yor are not eligible for any discount.")



age = int(input("Enter your age :"))
mamber = input("Enter True if you are bember of this company :\nOtherwise press Enter :")
if age >= 60:
    if mamber.lower() == "yes":
        print("Your seniour discount is : 40% ")
    else:
        print("Your seniour discount is : 25% ")
else:
    ("You are not eligible for any type's of discount.")