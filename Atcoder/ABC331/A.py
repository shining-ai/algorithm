import io
import sys


def debug_input():
    _INPUT = """\
12 30
2012 6 20

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    M, D = map(int, input().split())
    y, m, d = map(int, input().split())

    d = d + 1
    if d > D:
        d = 1
        m += 1
    if m > M:
        m = 1
        y += 1

    print(y, m, d)


if __name__ == "__main__":
    # debug_input()
    main()
