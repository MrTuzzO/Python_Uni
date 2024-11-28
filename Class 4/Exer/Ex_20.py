month = int(input("Enter a month number (1-12): "))
year = int(input("Enter a year number: "))
if month == 2:
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("February has 29 days.")
    else:
        print("February has 28 days.")
elif month in [4,6,9,11]:
    print(f"The month has 30 days.")
else:
    print(f"The month has 31 days.")
