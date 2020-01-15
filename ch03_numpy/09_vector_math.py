import numpy as np

# -----------------transpose--------------------
arr35 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr35.shape)                              # (2, 3)
arr36 = arr35.transpose()
print(arr36.shape)                              # (3, 2)


# -----------------dot--------------------------
print(np.dot(arr35, arr36))                     # [[14 32][32 77]]

#-----------------cross-------------------------
print(np.cross(np.array([3, 2, -1]), np.array([1, 0, -5])))     # [-10 14 -2]

