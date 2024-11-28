str = "Hello World"
it = iter(str)

while True:
    char = next(it, None)
    if char is None or char == '\n':
        break

    print(char)
