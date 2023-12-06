import io
import sys


def debug_input():
    _INPUT = """\
800
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())

    print(int(N * 1.1))


if __name__ == "__main__":
    # debug_input()
    main()
