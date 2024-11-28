number = int(input("Enter a positive integer: "))
res = sum(int(digit) for digit in str(number))
print("Sum of digits:", res)
