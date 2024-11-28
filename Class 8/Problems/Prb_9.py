nums = [1,20,33,4,55,67,27,28,10]

mx = -999999999
for num in nums:
    if num > mx:
        mx = num

print(f"Max is {mx}")
