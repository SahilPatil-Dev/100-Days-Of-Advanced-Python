import argparse
import sys
from typing import Dict

from Day_09.user_schema import User, ValidationError


def create_user(data: Dict[str, str]) -> User:
    return User.from_dict(data)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a user via CLI"
    )

    parser.add_argument("--email", required=True)
    parser.add_argument("--age", required=True)

    args = parser.parse_args()

    try:
        user = create_user({
            "email": args.email,
            "age": args.age,
        })

        print({
            "success": True,
            "email": user.email,
            "age": user.age
        })

    except ValidationError as e:
        print({
            "success": False,
            "error": str(e)
        })
        sys.exit(1)


if __name__ == "__main__":
    main()
