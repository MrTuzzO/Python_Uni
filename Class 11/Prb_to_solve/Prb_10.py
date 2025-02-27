import numpy as np

rand_mat = np.random.randint(0,10,(3,3))

print("Original Matrix:")
print(rand_mat)

transposed_mat = rand_mat.T
print("\nTransposed Matrix:")
print(transposed_mat)
