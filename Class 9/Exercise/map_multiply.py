def multiply(lst, factor):
    return list(map(lambda x: x * factor, lst))


lst = [1, 2, 3, 4, 5]
factor = 2

result = multiply(lst, factor)
print(result)
