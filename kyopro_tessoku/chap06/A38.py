import io
import sys


def debug_input():
    _INPUT = """\
    5 3
    1 2 22
    2 3 16
    3 5 23
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N*D)
def main():
    D, N = map(int, input().split())
    limit = [24] * (D + 1)
    limit[0] = 0

    for i_n in range(N):
        L, R, H = map(int, input().split())
        for i_d in range(L, R + 1):
            limit[i_d] = min(limit[i_d], H)

    ans = sum(limit)
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
