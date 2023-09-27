import io
import math
import sys


def debug_input():
    _INPUT = """\
    3 5
    1 2 5
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(XY+N)
def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    L = 0
    R = N - 1
    i = (L + R) // 2
    while A[i] != X:
        if A[i] > X:
            R = i
            i = math.floor((L + R) / 2)  # 切り捨て
        else:
            L = i
            i = math.ceil((L + R) / 2)  # 切り上げ

    print(i + 1)


if __name__ == "__main__":
    # debug_input()
    main()
