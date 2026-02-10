from pathlib import Path


def process_file(path: Path) -> tuple[int, int]:
    """
    Streams a file line-by-line.
    Returns total lines and non-empty lines.
    """
    total_lines = 0
    non_empty_lines = 0

    with path.open("r", encoding="utf-8") as file:
        for line in file:
            total_lines += 1
            if line.strip():
                non_empty_lines += 1

    return total_lines, non_empty_lines


if __name__ == "__main__":
    file_path = Path(__file__).parent / "sample.txt"

    total, non_empty = process_file(file_path)
    print(f"Total lines: {total}")
    print(f"Non-empty lines: {non_empty}")
