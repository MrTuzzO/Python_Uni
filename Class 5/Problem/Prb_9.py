try:
    with open('notes.txt', 'r') as mainfile:
        content = mainfile.read()
    with open('backup_file.txt', 'w') as backupfile:
        backupfile.write(content)
except FileNotFoundError:
    print('File not found')
except IOError:
    print('I/O Error')
