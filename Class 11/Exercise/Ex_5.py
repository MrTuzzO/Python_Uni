import numpy as np

data = np.array([1,2,3,4,5])
normalized_data = (data - np.min(data)) / (np.max(data) - np.min(data))

print(normalized_data)