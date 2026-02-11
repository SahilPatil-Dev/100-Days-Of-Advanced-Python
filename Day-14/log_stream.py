from pathlib import Path
from typing import Iterator


def read_logs(path: Path) -> Iterator[str]:
    """
    Lazily reads a log file line-by-line.
    Never loads the full file into memory.
    """
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            yield line.rstrip("\n")


if __name__ == "__main__":
    log_file = Path(__file__).parent / "app.log"

    for log_line in read_logs(log_file):
        print(log_line)
