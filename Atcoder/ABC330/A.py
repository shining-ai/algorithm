import io
import sys


def debug_input():
    _INPUT = """\
5 60
60 20 100 90 40
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(2N)
def main():
    N, L = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    for i_a in A:
        if i_a >= L:
            ans += 1

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
