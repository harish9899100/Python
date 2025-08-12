day = input("Enter the day for check status of office :")
match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("In the ", day, "i am inside office ")
    case "saturday" | "sunday":
        print("The", day, "is weekends")
    case _:
        print("Enter valid day of week")