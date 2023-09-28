import io
import sys


def debug_input():
    _INPUT = """\
    15
    83 31 11 17 32 19 23 37 43 47 53 61 67 5 55
    5
    10
    20
    30
    40
    50
    """

    sys.stdin = io.StringIO(_INPUT)


def binary_search(N, A, X):
    L = 0
    R = N
    while L < R:
        mid = (L + R) // 2
        if A[mid] < X:
            L = mid + 1
        else:
            R = mid

    return L


# 計算量: O(logN+QlogN)
def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    A.sort()

    for _ in range(Q):
        X = int(input())
        ans = binary_search(N, A, X)
        print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
