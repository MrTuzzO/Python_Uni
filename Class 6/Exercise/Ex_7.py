def sum_of_evens(numbers):
    return sum(n for n in numbers if n % 2 == 0)


numbers = list(map(int, input("Enter numbers: ").split()))
print(sum_of_evens(numbers))