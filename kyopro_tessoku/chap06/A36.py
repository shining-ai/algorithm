import io
import sys


def debug_input():
    _INPUT = """\
    5 10
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(1)
def main():
    N, K = map(int, input().split())

    if K >= 2 * N - 2:
        if K % 2 == 0:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    # debug_input()
    main()
