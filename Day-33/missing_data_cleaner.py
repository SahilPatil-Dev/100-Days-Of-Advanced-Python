import numpy as np

# Simulated dataset (rows = users, columns = metrics)
data = np.array([
    [100.0, 200.0, np.nan],
    [120.0, np.nan, 250.0],
    [np.nan, 180.0, 230.0],
    [130.0, 190.0, 240.0]
])

print("Original data:\n", data)

# Column-wise mean ignoring NaN
column_means = np.nanmean(data, axis=0)
print("Column means (ignoring NaN):\n", column_means)

# Find where values are NaN
nan_mask = np.isnan(data)

# Replace NaN with corresponding column mean
# Broadcasting applies column means correctly
data[nan_mask] = np.take(column_means, np.where(nan_mask)[1])

print("Cleaned data:\n", data)