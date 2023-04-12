string = input("Enter a string: ")

match_string = match string:
case _ if ' ' in string:
    print("Multiword string")
case _:
    print("Single word string")

