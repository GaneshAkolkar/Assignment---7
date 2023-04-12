str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

match (str1, str2):
    case (a, b) if a == b:
        print("The two strings are identical")
    case (a, b) if a < b:
        print("The first string comes before the second in dictionary order")
    case _:
        print("The first string comes after the second in dictionary order")
