from typing import Iterator, List, Sequence, TypeVar
import time

T = TypeVar("T")


def paginate(data: Sequence[T], page_size: int) -> Iterator[List[T]]:
    """
    Yields data in pages instead of returning everything at once.
    """
    if page_size <= 0:
        raise ValueError("page_size must be greater than zero")

    for i in range(0, len(data), page_size):
        yield list(data[i : i + page_size])


if __name__ == "__main__":
    users = list(range(1, 51))

    for page in paginate(users, 10):
        print(page)
        time.sleep(1)
