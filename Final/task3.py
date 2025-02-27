import numpy as np

A = np.array([[2, 4, 6], [1, 3, 5], [7, 9, 11]])
B = np.array([[8, 5, 2], [7, 4, 1], [6, 3, 0]])

sum_AB = A + B

product_AB = A * B

dot_product = np.dot(A, B.T)

det_A = np.linalg.det(A)

print("Element-wise sum:\n", sum_AB)
print("\nElement-wise product:\n", product_AB)
print("\nDot product:\n", dot_product)
print("\nDeterminant of A:", det_A)
