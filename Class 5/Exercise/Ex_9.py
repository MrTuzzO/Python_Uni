with open('data.txt', 'r') as file:
    line_num = sum(1 for line in file)
    print(f"Total number of lines: {line_num}")