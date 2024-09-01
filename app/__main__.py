# https://docs.python.org/3/howto/argparse.html#argparse-tutorial
import argparse
import sys

from . import operations


def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="operation", required=True)

    # https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_subparsers
    subparsers.add_parser("add")

    # Arguments common to all subcommands.
    parser.add_argument("x", type=int)
    parser.add_argument("y", type=int)

    args = parser.parse_args()
    x, y = args.x, args.y

    if args.operation == "add":
        result = operations.add(x, y)
    else:
        sys.exit(f"Unknown operation {args.operation}")

    print(f"{x} + {y} = {result}")


if __name__ == "__main__":
    main()
