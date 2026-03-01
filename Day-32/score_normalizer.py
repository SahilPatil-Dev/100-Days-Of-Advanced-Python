import numpy as np

# Rows = students, Columns = subjects
scores = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [90, 95, 100],
    [50, 65, 70]
])

# 🔹 Compute column-wise mean
mean = np.mean(scores, axis=0)

# 🔹 Compute column-wise standard deviation
std = np.std(scores, axis=0)

# 🔹 Normalize (vectorized)
normalized_scores = (scores - mean) / std

print("Mean:\n", mean)
print("Standard deviation:\n", std)
print("Normalized scores:\n", normalized_scores)