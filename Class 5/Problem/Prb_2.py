with open('shopping_list.txt', 'r') as f:
    for i, line in enumerate(f, start=1):
        print(i, line.strip())