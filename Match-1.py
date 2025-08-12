# The match statment is same like switch statment in c
day = int(input("Enter the day number of week for getting day name :"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Please enter valid day number between 1 to 7:")