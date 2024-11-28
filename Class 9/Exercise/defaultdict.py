from collections import defaultdict

dd = defaultdict(list)
dd['a'].append(1)
dd['b'].append(2)

print(dd['c'])
print(dd['a'])