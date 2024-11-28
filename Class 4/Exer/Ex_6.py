num = int(input('Enter a number: '))
print(f"Multiples of {num} up to 100: ")
for i in range(1, 101):
    if i % num == 0:
        print(f'{i} ', end='')