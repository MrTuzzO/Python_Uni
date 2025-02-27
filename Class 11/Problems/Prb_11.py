import numpy as np
array = np.array([1,2,3,4,5,6,7,8,9,10])
filtered_array = array[array % 2 == 0]
print(filtered_array)