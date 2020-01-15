import numpy as np

arr10 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
arr11 = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.], [10., 11., 12.]])
arr12 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], dtype=float)

print(arr10.dtype, arr11.dtype, arr12.dtype)

arr13 = np.float64([1, 3, 5])
print(arr13.dtype)
