with open('shopping_list.txt', 'r') as file:
    count = 0
    for line in file:
        for word in line.split():
            count+=1

    print(count)