try:
    with open('shopping_list.txt', 'r') as source:
        content = source.read()
    with open('list_backup.txt', 'w') as destination:
        destination.write(content)

except FileNotFoundError:
    print('File not found')
except IOError:
    print('I/O Error occurred')