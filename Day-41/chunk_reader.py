import pandas as pd


def read_in_chunks(filepath: str, chunk_size: int = 5):
    """
    Read CSV file in chunks to avoid loading the entire dataset into memory.
    """

    for chunk_number, chunk in enumerate(
        pd.read_csv(filepath, chunksize=chunk_size)
    ):
        print(f"Processing chunk {chunk_number + 1}")
        print("Chunk size:", len(chunk))


if __name__ == "__main__":
    read_in_chunks("large_logs.csv", chunk_size=5)