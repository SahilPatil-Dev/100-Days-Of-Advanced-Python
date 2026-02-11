from typing import Iterator


def read_numbers(source: list[int]) -> Iterator[int]:
    for value in source:
        yield value


def filter_valid(numbers: Iterator[int]) -> Iterator[int]:
    for number in numbers:
        if number >= 0:
            yield number


def transform(numbers: Iterator[int]) -> Iterator[int]:
    for number in numbers:
        yield number * number


def consume(numbers: Iterator[int]) -> None:
    for number in numbers:
        print(f"Processed value: {number}")


if __name__ == "__main__":
    raw_data = [5, -2, 7, 0, -1, 3]

    pipeline = transform(
        filter_valid(
            read_numbers(raw_data)
        )
    )

    consume(pipeline)
