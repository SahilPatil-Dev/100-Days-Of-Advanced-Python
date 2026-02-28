import numpy as np

# Create 2D array (3 rows, 4 columns)
data = np.array([
    [100, 200, 150, 300],
    [120, 180, 160, 310],
    [130, 190, 170, 320]
])

print("Original shape:", data.shape)

# Sum across rows (axis=1 → collapse columns)
row_sums = np.sum(data, axis=1)
print("Row sums:", row_sums)

# Sum across columns (axis=0 → collapse rows)
column_sums = np.sum(data, axis=0)
print("Column sums:", column_sums)

# Mean of entire array
mean_value = np.mean(data)
print("Overall mean:", mean_value)

# Reshape (flatten to 1D)
flattened1 = data.reshape(-1)
flattened2 = data.flatten()

print("Flattened shape:", flattened1.shape)
print("Flattened shape:", flattened2.shape)
