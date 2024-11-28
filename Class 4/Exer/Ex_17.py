num1 = int(input('Enter a number: '))
operator = input('Enter a operator (+, -, *, /): ')
num2 = int(input('Enter another number: '))
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2!=0:
        result = num1 / num2
    else:
        print('Division by zero not allowed')

print(f"The result is {result}")
