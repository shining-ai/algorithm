import io
import sys


def debug_input():
    _INPUT = """\
    5 23
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(30)
def main():
    a, b = map(int, input().split())
    p = a
    m = (10**9) + 7
    ans = 1

    for i in range(30):
        wari = 2**i
        if b // wari % 2 == 1:
            ans = ans * p % m
        p = p*p % m

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
