import numpy as np

print("Matrix Tool\n")

# Input matrix
matrix = np.array([[1, 2], [3, 4]])

print("Matrix:\n", matrix)

# Transpose
print("\nTranspose:\n", matrix.T)

# Determinant
print("\nDeterminant:", np.linalg.det(matrix))

# Inverse
print("\nInverse:\n", np.linalg.inv(matrix))