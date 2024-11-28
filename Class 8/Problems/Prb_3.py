def cToF(celsius_list):
    return list(map(lambda c: 9/5 * c + 32, celsius_list))


cl = [0, 20, 30, 100]
fl = cToF(cl)
print(fl)

