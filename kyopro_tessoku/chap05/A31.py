import io
import sys


def debug_input():
    _INPUT = """\
    10
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(3)
def main():
    n = int(input())

    multiple_3 = n // 3
    multiple_5 = n // 5
    multiple_15 = n // 15

    ans = multiple_3 + multiple_5 - multiple_15
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
