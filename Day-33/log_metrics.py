import numpy as np

# Simulated response times (milliseconds)
response_times = np.array([
    120, 200, -50, 300, np.nan,
    250, 180, 4000, 220, -10,
    210, np.nan, 190
], dtype=float)

print("Raw data:\n", response_times)

# Remove invalid entries (negative or NaN)
valid_mask = (~np.isnan(response_times)) & (response_times >= 0)

clean_data = response_times[valid_mask]

print("Clean data:\n", clean_data)

# Compute metrics
average = np.mean(clean_data)
percentile_95 = np.percentile(clean_data, 95)
maximum = np.max(clean_data)

print("Average response time:", average)
print("95th percentile:", percentile_95)
print("Maximum valid response:", maximum)