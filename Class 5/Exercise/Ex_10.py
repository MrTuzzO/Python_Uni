try:
    with open('data.txt', 'r') as source_file:
        content = source_file.read()

    with open('backup.txt', 'w') as destination_file:
        destination_file.write(content)
except FileNotFoundError:
    print('File not found')
except IOError:
    print('An IO error occurred')