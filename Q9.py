year = int(input("Enter a year: "))

match year:
    case x if x % 400 == 0:
        print(f"{year} is a century leap year")
    case x if x % 100 == 0:
        print(f"{year} is a century non leap year")
    case x if x % 4 == 0:
        print(f"{year} is a non century leap year")
    case _:
        print(f"{year} is a non century non leap year")
