numbers = []
while True:
    number = int(input("Enter a number (-1 to stop): "))
    if number == -1:
        break
    numbers.append(number)

if numbers:
    largest_number = max(numbers)
    print("Largest number:", largest_number)
else:
    print("No numbers were entered.")
