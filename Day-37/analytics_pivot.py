import pandas as pd

# Simulated web analytics dataset
data = {
    "date": [
        "2024-01-01", "2024-01-01", "2024-01-01",
        "2024-01-02", "2024-01-02", "2024-01-02"
    ],
    "endpoint": [
        "/login", "/orders", "/profile",
        "/login", "/orders", "/profile"
    ],
    "response_time": [120, 350, 100, 140, 400, 110],
    "requests": [200, 120, 80, 220, 140, 90]
}

df = pd.DataFrame(data)

# Create pivot-style aggregation
analytics = df.pivot_table(
    index="endpoint",
    values=["response_time", "requests"],
    aggfunc={
        "response_time": "mean",
        "requests": "sum"
    }
)

analytics = analytics.rename(
    columns={
        "response_time": "avg_response_time",
        "requests": "total_requests"
    }
)

print("Endpoint Analytics Dashboard:")
print(analytics)