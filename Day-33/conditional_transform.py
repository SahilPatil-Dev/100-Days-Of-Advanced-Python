import numpy as np

data = np.array([10, -5, 30, 200, 15, -2, 400])

print("Original:", data)

# Replace negative values with 0
data[data < 0] = 0

# Cap values above threshold
threshold = 100
data[data > threshold] = threshold

print("Transformed:", data)