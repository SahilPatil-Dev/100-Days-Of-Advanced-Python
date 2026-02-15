import argparse
import sys
from pathlib import Path


def count_lines(file_path: Path) -> int:
    with file_path.open("r", encoding="utf-8") as file:
        return sum(1 for _ in file)


def print_uppercase(file_path: Path) -> None:
    with file_path.open("r", encoding="utf-8") as file:
        for line in file:
            print(line.upper(), end="")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="File processing utility"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to input file"
    )

    parser.add_argument(
        "--mode",
        required=True,
        choices=["count", "uppercase"],
        help="Processing mode"
    )

    args = parser.parse_args()

    file_path = Path(args.input)

    if not file_path.exists():
        print("Error: Input file does not exist.")
        sys.exit(1)

    try:
        if args.mode == "count":
            total = count_lines(file_path)
            print(f"Total lines: {total}")
        elif args.mode == "uppercase":
            print_uppercase(file_path)

    except Exception as e:
        print(f"Processing failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
