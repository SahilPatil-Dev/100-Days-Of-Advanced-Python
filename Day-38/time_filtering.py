import pandas as pd
from datetime import datetime, timedelta

data = {
    "timestamp": [
        "2026-03-06 10:00:00",
        "2026-03-05 12:00:00",
        "2026-03-05 09:00:00",
        "2024-01-02 09:30:00",
        "2023-02-06 12:00:00"
    ],
    "endpoint": ["/login", "/orders", "/login", "/profile", "/orders"],
    "response_time": [120, 350, 140, 100, 150]
}

df = pd.DataFrame(data)

df["timestamp"] = pd.to_datetime(df["timestamp"])

# Filter last 24 hours
latest_time = df["timestamp"].max()
last_24h = df[df["timestamp"] >= latest_time - timedelta(hours=24)]

print("Logs from last 24 hours:")
print(last_24h)

# Filter specific date
specific_date = df[df["timestamp"].dt.date == datetime(2026, 3, 6).date()]

print("\nLogs for specific date:")
print(specific_date)

# Metrics
avg_response = specific_date["response_time"].mean()
total_requests = specific_date.shape[0]

print("\nAverage response time:", avg_response)
print("Total requests:", total_requests)