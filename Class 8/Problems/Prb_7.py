try:
    str = input("Enter a number: ")
    number = int(str)
    print(f"The number you entered is {number}.")
except ValueError as e:
    print(f"Invalid input: {e}")
