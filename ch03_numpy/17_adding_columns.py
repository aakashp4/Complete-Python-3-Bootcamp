import numpy as np

ones_arr = np.ones((3, 3))                                          # [[1 1 1] [1 1 1] [1 1 1]]
new_col0 = np.full((1, 3), 10)                                      # [10 10 10]
new_col4 = np.linspace(10, 30, 3)                                   # [10 20 30]
new_col5 = np.array([True, False, True], dtype=bool)                # creates a boolean array
new_arr = np.c_[new_col0.T, ones_arr, new_col4.T, new_col5.T]       # Transpose arrays so they become "columns"
print(new_arr)


new_row0 = np.array([10, 1, 1, 1, 40, 0])
new_row4 = np.array([10, 1, 1, 1, 50, 0])
new_arr = np.r_['0, 2', new_row0, new_arr, new_row4]

print(new_arr)                                          # [ [ 10.   1.   1.   1.  40.   0.]
                                                        #   [ 10.   1.   1.   1.  10.   1.]
                                                        #   [ 10.   1.   1.   1.  20.   0.]
                                                        #   [ 10.   1.   1.   1.  30.   1.]
                                                        #   [ 10.   1.   1.   1.  50.   0.] ]


# ----------------------------------------
#  Now removing rows and cols....
#
#
remaining = np.delete(new_arr, (1, 3), axis=1)
print(remaining)                                      # [[10 1 40 0] [10 1 10 1] [10 1 20 1] [10 1 30 1] [10 1 50 0]]

# this will delete a column where a particular value is encountered...
index = np.argwhere(remaining[:, 2] == 20)
remaining = np.delete(remaining, index, axis=0)
print(remaining)
