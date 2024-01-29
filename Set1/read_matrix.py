import numpy as np

loaded_matrix = np.loadtxt('matrix.txt')

# Convert it back to a NumPy matrix
loaded_matrix = np.matrix(loaded_matrix)

print(loaded_matrix)