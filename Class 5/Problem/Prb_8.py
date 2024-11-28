class FileEmptyError(Exception):
    pass

try:
    with open('notes.txt', 'r') as notes:
        content = notes.read()
        if not content.strip():
            raise FileEmptyError("This File is Empty.")
        else:
            print(content)
except FileNotFoundError as e:
    print(e)
except FileNotFoundError:
    print("File Not Found")