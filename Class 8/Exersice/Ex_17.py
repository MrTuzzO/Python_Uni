import pdb

def factorial(n):
    pdb.set_trace()
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(5))