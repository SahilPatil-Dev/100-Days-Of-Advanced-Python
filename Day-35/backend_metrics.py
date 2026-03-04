import pandas as pd
import numpy as np

# Simulated server logs
data = {
    "endpoint": ["/login", "/login", "/orders", "/orders", "/orders", "/profile"],
    "response_time": [120, 200, 350, 400, 150, 100],
    "status_code": [200, 500, 200, 404, 200, 200]
}

df = pd.DataFrame(data)

# Average response time per endpoint
avg_response = df.groupby("endpoint")["response_time"].mean()

print("Average response time per endpoint:")
print(avg_response)

# Total errors per endpoint (status >= 400)
errors = (
    df[df["status_code"] >= 400]
    .groupby("endpoint")["status_code"]
    .count()
)

print("\nTotal errors per endpoint:")
print(errors)

# Slowest endpoint (highest average response time)
slowest_endpoint = avg_response.idxmax()

print("\nSlowest endpoint:", slowest_endpoint)