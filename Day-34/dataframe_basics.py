import pandas as pd

# Create DataFrame manually
data = {
    "name": ["Sahil", "Amit", "Neha", "Riya"],
    "age": [23, 30, 27, 22],
    "city": ["Mumbai", "Delhi", "Pune", "Bangalore"]
}

df = pd.DataFrame(data)

print("Full DataFrame:\n", df)
print("Shape:", df.shape)

# Column selection
print("\nAges column:")
print(df["age"])

# Row selection using .iloc (position-based)
print("\nFirst row using iloc:")
print(df.iloc[0])

# Row selection using .loc (label-based)
print("\nRow with index 1 using loc:")
print(df.loc[1])

# Filtering (age > 25)
filtered_df = df.loc[df["age"] > 25]
print("\nFiltered (age > 25):")
print(filtered_df)