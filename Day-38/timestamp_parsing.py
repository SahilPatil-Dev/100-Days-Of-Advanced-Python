import pandas as pd

# Simulated API log dataset
data = {
    "timestamp": [
        "2024-01-01 10:00:00",
        "2024-01-01 10:05:00",
        "2024-01-01 11:00:00",
        "2024-01-02 09:30:00"
    ],
    "endpoint": ["/login", "/orders", "/login", "/profile"],
    "response_time": [120, 350, 140, 100]
}

df = pd.DataFrame(data)

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Extract hour and day
df["hour"] = df["timestamp"].dt.hour
df["day"] = df["timestamp"].dt.day

# Sort by timestamp
df = df.sort_values(by="timestamp")

print(df)