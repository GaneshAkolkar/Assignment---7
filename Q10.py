color = input("Enter your favorite color: ").lower()

day = match color:
    case "yellow":
        "Monday"
    case "blue":
        "Tuesday"
    case "orange":
        "Wednesday"
    case "white":
        "Thursday"
    case "black":
        "Friday"
    case "red":
        "Saturday"
    case _:
        "Sunday"

    print(f"Your favorite color is {color} and the corresponding day is {day}")
