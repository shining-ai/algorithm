import io
import sys


def debug_input():
    _INPUT = """\
ABC
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    S = input()
    for i in S:
        print(i, end=" ")


if __name__ == "__main__":
    # debug_input()
    main()
