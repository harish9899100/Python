month = input("Enter the month name for check weather :")
match month:
    case "january" | "febuary" |"march" | "april":
        print(month, "In this month mostly weather is could")
    case "may" | "june" | "july" | "august":
        print(month, "In this month mostly weather is rainy")
    case "september" | "octomber" | "november" | "december":
        print(month, "In this month mostly weather is hot and hard sunlight")
    case _:
        print("Please enter valid months name")