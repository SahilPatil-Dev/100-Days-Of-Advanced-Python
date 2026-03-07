import pandas as pd

# Simulated API log dataset
data = {
    "timestamp": [
        "2024-01-01 10:00:00",
        "2024-01-01 10:10:00",
        "2024-01-01 11:00:00",
        "2024-01-01 11:20:00",
        "2024-01-01 12:00:00"
    ],
    "endpoint": ["/login", "/orders", "/login", "/orders", "/profile"],
    "response_time": [120, 350, 140, 400, 100],
    "status_code": [200, 200, 500, 200, 200]
}

df = pd.DataFrame(data)

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Set timestamp as index
df = df.set_index("timestamp")

# Requests per hour
requests_per_hour = df.resample("h").size()

# Average response time per hour
avg_response_time = df["response_time"].resample("h").mean()

print("Requests per hour:")
print(requests_per_hour)

print("\nAverage response time per hour:")
print(avg_response_time)