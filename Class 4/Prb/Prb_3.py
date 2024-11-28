evenCnt = 0
oddCnt = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    elif number % 2 == 0:
        evenCnt += 1
    else:
        oddCnt += 1

print("Even numbers:", evenCnt)
print("Odd numbers:", oddCnt)
