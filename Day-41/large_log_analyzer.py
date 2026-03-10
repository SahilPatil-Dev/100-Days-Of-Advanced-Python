import pandas as pd
from collections import defaultdict


def analyze_large_logs(filepath: str, chunk_size: int = 1000):

    request_counts = defaultdict(int)
    latency_sums = defaultdict(float)
    error_counts = defaultdict(int)

    for chunk in pd.read_csv(filepath, chunksize=chunk_size):

        grouped = chunk.groupby("endpoint")

        for endpoint, group in grouped:

            request_counts[endpoint] += len(group)

            latency_sums[endpoint] += group["response_time"].sum()

            error_counts[endpoint] += (group["status_code"] >= 400).sum()

    print("\nFinal Metrics\n")

    for endpoint in request_counts:

        avg_latency = latency_sums[endpoint] / request_counts[endpoint]

        error_rate = error_counts[endpoint] / request_counts[endpoint]

        print(endpoint)
        print("  requests:", request_counts[endpoint])
        print("  avg latency:", round(avg_latency, 2))
        print("  error rate:", round(error_rate, 3))
        print()


if __name__ == "__main__":
    analyze_large_logs("large_logs.csv")