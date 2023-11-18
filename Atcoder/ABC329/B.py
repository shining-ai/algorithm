import io
import sys


def debug_input():
    _INPUT = """\
5
2 1 3 3 2
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = set(map(int, input().split()))

    A = list(A)
    A = sorted(A)

    print(A[-2])

if __name__ == "__main__":
    # debug_input()
    main()
