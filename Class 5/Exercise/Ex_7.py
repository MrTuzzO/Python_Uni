class EmptyFileError(Exception):
    pass


try:
    with open('empty.txt', 'r') as file:
        content = file.read()
        if not content.strip():
            raise EmptyFileError("This file is empty.")
except EmptyFileError as e:
    print(e)
except FileNotFoundError:
    print("This file is not found.")