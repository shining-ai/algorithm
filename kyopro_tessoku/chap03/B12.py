import io
import sys


def debug_input():
    _INPUT = """\
    1010
    """

    sys.stdin = io.StringIO(_INPUT)


def measure(X):
    res = X**3 + X

    return res


# 計算量: O(logN)
def main():
    N = int(input())

    L = 0
    R = 100
    ans = 0
    x3x = 0
    while (N - 0.001) > x3x or x3x > (N + 0.001):
        ans = (L + R) / 2
        x3x = measure(ans)
        if x3x > N:
            R = ans
        else:
            L = ans

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
