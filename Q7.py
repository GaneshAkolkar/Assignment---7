num = int(input("Enter a number: "))

match num:
    case 0:
        print("The number is zero")
    case _ if num > 0:
        print("The number is positive")
    case _:
        print("The number is negative")
