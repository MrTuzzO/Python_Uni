from functools import reduce

nums = [1,2,3,4,5,6]
product = reduce(lambda x,y:x*y,nums)
print(product)