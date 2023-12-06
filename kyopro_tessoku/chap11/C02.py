import io
import sys


def debug_input():
    _INPUT = """\
5
120 150 100 200 100
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()

    print(A[-1] + A[-2])


if __name__ == "__main__":
    # debug_input()
    main()
