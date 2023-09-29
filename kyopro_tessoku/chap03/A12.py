import io
import sys


def debug_input():
    _INPUT = """\
    4 10
    1 2 3 4
    """

    sys.stdin = io.StringIO(_INPUT)


def count_flyer(A, sec):
    cnt = 0
    for i_a in A:
        cnt += sec // i_a

    return cnt


# 計算量: O(N+log10^9)
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    L = 0
    R = 10**9
    while L < R:
        mid = (L + R) // 2
        if count_flyer(A, mid) < K:
            L = mid + 1
        else:
            R = mid

    print(L)


if __name__ == "__main__":
    # debug_input()
    main()
