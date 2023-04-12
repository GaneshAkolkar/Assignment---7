def is_isosceles_triangle(a, b, c):
    """
    Returns True if a, b, c are the lengths of an isosceles triangle, False otherwise.
    """
    if a == b or b == c or c == a:
        return True
    else:
        return False

def is_right_angled_triangle(a, b, c):
    """
    Returns True if a, b, c are the lengths of a right-angled triangle, False otherwise.
    """
    sides = sorted([a, b, c])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

def is_equilateral_triangle(a, b, c):
    """
    Returns True if a, b, c are the lengths of an equilateral triangle, False otherwise.
    """
    if a == b and b == c:
        return True
    else:
        return False

while True:
    print("Please select an option:")
    print("a. Check whether a given set of three numbers are lengths of an isosceles triangle or not")
    print("b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not")
    print("c. Check whether a given set of three numbers are equilateral triangle or not")
    print("d. Exit")

    choice = input().lower()

    if choice == 'a':
        a, b, c = map(float, input("Enter the three lengths separated by spaces: ").split())
        if is_isosceles_triangle(a, b, c):
            print("Yes, these lengths form an isosceles triangle.")
        else:
            print("No, these lengths do not form an isosceles triangle.")

    elif choice == 'b':
        a, b, c = map(float, input("Enter the three lengths separated by spaces: ").split())
        if is_right_angled_triangle(a, b, c):
            print("Yes, these lengths form a right-angled triangle.")
        else:
            print("No, these lengths do not form a right-angled triangle.")

    elif choice == 'c':
        a, b, c = map(float, input("Enter the three lengths separated by spaces: ").split())
        if is_equilateral_triangle(a, b, c):
            print("Yes, these lengths form an equilateral triangle.")
        else:
            print("No, these lengths do not form an equilateral triangle.")

    elif choice == 'd':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
