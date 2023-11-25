import io
import math
import sys


def debug_input():
    _INPUT = """\
21
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(2N)
def main():
    D = int(input())

    r = math.isqrt(D) + 1
    ans = D
    for i_x in range(1, r + 1):
        C = i_x**2 - D
        if C == 0:
            ans = 0
            break
        elif C > 0:
            ans = min(ans, C)
        else:
            y_1 = math.isqrt(-C)
            y_2 = y_1 + 1
            ans = min(ans, abs(y_1**2 + C))
            ans = min(ans, abs(y_2**2 + C))
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
