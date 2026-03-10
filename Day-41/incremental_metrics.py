import pandas as pd


def compute_metrics(filepath: str, chunk_size: int = 1000):

    total_requests = 0
    total_latency = 0
    error_count = 0

    for chunk in pd.read_csv(filepath, chunksize=chunk_size):

        total_requests += len(chunk)

        total_latency += chunk["response_time"].sum()

        error_count += (chunk["status_code"] >= 400).sum()

    average_latency = total_latency / total_requests

    print("Total requests:", total_requests)
    print("Average response time:", average_latency)
    print("Error count:", error_count)


if __name__ == "__main__":
    compute_metrics("large_logs.csv")