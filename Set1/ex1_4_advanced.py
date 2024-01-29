import numpy as np

# used chat GPT examples
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

arr_repeated = np.repeat(arr, 3)
print(arr_repeated)

arr_flattened = np.ravel(arr)
print(arr_flattened)

arr_hsplit = np.hsplit(arr, 2)
print(arr_hsplit)

arr_vsplit = np.vsplit(arr, 3)
print(arr_vsplit)

arr_hstack = np.hstack(arr_hsplit)
print(arr_hstack)

arr_vstack = np.vstack(arr_vsplit)
print(arr_vstack)

arr_transposed = np.transpose(arr)
print(arr_transposed)
