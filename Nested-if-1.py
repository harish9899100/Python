age = int(input("Enter your age : "))
mamber = str(input("If you are member of this company then enter yes : \nOther-wise press enter : "))
if age >= 60:
    if mamber == True:
        print("Your senior discount is : 40% ")
    else:
        print("Your senior discount is : 25% ")
else:
    print("Yor are not eligible for any discount.")