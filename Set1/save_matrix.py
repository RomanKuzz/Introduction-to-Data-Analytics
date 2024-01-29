import numpy as np

# Create a 15x15 matrix
matrix = np.random.random((15, 15))

# Save the matrix to a file (matrix.txt)
np.savetxt('matrix.txt', matrix)