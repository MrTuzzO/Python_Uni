from collections import Counter

nums = [1, 2, 2, 2, 3, 3, 1, 4]
count = Counter(nums)
print(count)
print(count.most_common(1))