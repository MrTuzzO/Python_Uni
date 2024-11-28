try:
    with open('missing.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('File not found')