import numpy as np

# 2D array (3 rows, 3 columns)
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# 1D array (length = number of columns)
row_adjustment = np.array([1, 2, 3])

# 🔹 Row-wise addition
# NumPy "broadcasts" row_adjustment across each row
result_row = data + row_adjustment
print("Row-wise broadcast:\n", result_row)

# 1D array (length = number of rows)
column_multiplier = np.array([1, 2, 3]).reshape(-1, 1)

# 🔹 Column-wise multiplication
# Broadcasting works because shapes are compatible
result_column = data * column_multiplier
print("Column-wise broadcast:\n", result_column)

# 🔹 Intentional shape mismatch
try:
    wrong_shape = np.array([1, 2])  # incompatible shape
    print(data + wrong_shape)
except ValueError as e:
    print("Broadcasting error:", e)