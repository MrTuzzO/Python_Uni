try:
    with open('grocery.txt', 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print('File not found')
