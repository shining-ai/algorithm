import io
import sys


def debug_input():
    _INPUT = """\
    2 3 100
    10 20
    1 2 3
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N + M)
def main():
    N, M, B = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ans = 0

    for i_a in A:
        ans += i_a * M

    ans += B * N * M

    for i_c in C:
        ans += i_c * N

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
