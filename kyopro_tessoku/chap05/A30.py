import io
import sys


def debug_input():
    _INPUT = """\
    4 2
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(30)
def main():
    n, r = map(int, input().split())
    m = (10**9) + 7

    a = 1
    for i_factorial in range(1, n + 1):
        a = (a * i_factorial) % m

    b = 1
    for i_factorial in range(1, r + 1):
        b = (b * i_factorial) % m
    for i_factorial in range(1, n - r + 1):
        b = (b * i_factorial) % m

    ans = 1
    p = b

    for i in range(30):
        wari = 2**i
        if (m - 2) // wari % 2 == 1:
            ans = ans * p % m
        p = p * p % m

    ans = a * ans % m

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
