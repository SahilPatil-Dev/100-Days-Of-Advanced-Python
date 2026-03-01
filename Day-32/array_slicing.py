import numpy as np

# Simulated sales data (rows = months, columns = regions)
sales = np.array([
    [100, 200, 150],
    [120, 180, 160],
    [130, 190, 170],
    [140, 210, 180]
])

print("Original shape:", sales.shape)

# First column (all rows, column 0)
first_column = sales[:, 0]
print("First column:\n", first_column)

# Last row
last_row = sales[-1, :]
print("Last row:\n", last_row)

# Sub-matrix (rows 1–2, columns 0–1)
sub_matrix = sales[1:3, 0:2]
print("Sub-matrix:\n", sub_matrix)

# Boolean filtering (values > 170)
filtered_values = sales[sales > 170]
print("Values > 170:\n", filtered_values)