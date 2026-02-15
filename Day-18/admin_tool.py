import argparse
import sys


def create_user(email: str, age: str) -> None:
    print(f"Creating user with email={email}, age={age}")


def delete_user(email: str) -> None:
    print(f"Deleting user with email={email}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Admin utility tool"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Create user command
    create_parser = subparsers.add_parser("create-user")
    create_parser.add_argument("--email", required=True)
    create_parser.add_argument("--age", required=True)

    # Delete user command
    delete_parser = subparsers.add_parser("delete-user")
    delete_parser.add_argument("--email", required=True)

    args = parser.parse_args()

    try:
        if args.command == "create-user":
            create_user(args.email, args.age)
        elif args.command == "delete-user":
            delete_user(args.email)

    except Exception as e:
        print(f"Operation failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
