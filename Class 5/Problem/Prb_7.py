try:
    with open('notes.txt', 'r') as f:
        contents = f.read()
        print(contents)
except FileNotFoundError:
    print('File not found')
except IOError:
    print('I/O error to read file')