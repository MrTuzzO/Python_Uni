import heapq

nums = [4, 1, 7, 3]
heapq.heapify(nums)
print(nums)
heapq.heappush(nums, 2)
print(nums)
print(heapq.heappop(nums))