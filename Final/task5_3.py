temperatures = [28, 32, 35, 31, 29, 30, 33, 36, 27, 25, 34, 30, 29, 37, 38, 26, 31, 35, 33, 32, 36, 34, 29, 28, 27, 35, 32, 30, 31, 33]

avg_temp = sum(temperatures) / len(temperatures)
temp_differences = [temp - avg_temp for temp in temperatures]

print(temp_differences)
