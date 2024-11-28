try:
    with open('data.txt', 'r') as f:
        contents = f.read()
        print(contents)
except IOError:
    print('An error occurred while reading the file.')