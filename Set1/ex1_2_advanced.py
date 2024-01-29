import numpy as np

matrix = np.random.randint(0, 50, (5, 10))

for i in range(10):
    x, y = np.random.randint(0, 5, 2)
    matrix[x, y] = -100

# Create a masked array to handle the -100 values
masked_matrix = np.ma.masked_equal(matrix, -100)

# Replace every -100 with 0
masked_matrix = np.ma.filled(masked_matrix, 0)

# Print the original matrix and the masked matrix
print("Original matrix:")
print(matrix)
print("Masked matrix:")
print(masked_matrix)