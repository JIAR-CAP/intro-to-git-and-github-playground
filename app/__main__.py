# https://docs.python.org/3/howto/argparse.html#argparse-tutorial
import argparse

from . import operations


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int)
    parser.add_argument("y", type=int)
    args = parser.parse_args()

    x, y = args.x, args.y
    result = operations.add(x, y)
    print(f"{x} + {y} = {result}")


if __name__ == "__main__":
    main()
