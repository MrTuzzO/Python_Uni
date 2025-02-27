import numpy as np

data = np.random.randn(10000)

# Task 1
mean_val = np.mean(data)
median_val = np.median(data)
std_dev = np.std(data)

print(f'Mean: {mean_val}, Median: {median_val}, Standard Deviation: {std_dev}')

# Task 2
min_val = np.min(data)
max_val = np.max(data)

print(f'Min: {min_val}, Max: {max_val}')

# Task 3
count_greater_than_mean = np.sum(data > mean_val)

print(f'Greater than mean: {count_greater_than_mean}')

# Task 4
normalized_data = (data - min_val) / (max_val - min_val)

print(normalized_data[:20])


