import bisect
import io
import sys


def debug_input():
    _INPUT = """\
6
2 3 1 6 4 5
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(2N)
def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.insert(0, 0)
    ans = 0
    L = [0]
    dp = [0] * (N + 1)

    # 動的計画法
    for i in range(1, N + 1):
        combo = bisect.bisect_left(L, A[i])
        dp[i] = combo

        if combo > ans:
            L.append(A[i])
            ans = combo
        else:
            L[combo] = min(L[combo], A[i])

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
