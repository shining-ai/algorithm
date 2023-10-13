import io
import sys


def debug_input():
    _INPUT = """\
    33 88
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N)
def main():
    A, B = map(int, input().split())
    big = max(A, B)
    small = min(A, B)

    while big % small != 0:
        big, small = small, big % small

    print(small)


if __name__ == "__main__":
    # debug_input()
    main()
