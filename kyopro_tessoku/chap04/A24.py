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

    ans = 0
    L = []
    dp = [0] * N

    # 動的計画法
    for i in range(N):
        pos = bisect.bisect_left(L, A[i])
        dp[i] = pos

        # 配列 L を更新
        if dp[i] >= ans:
            L.append(A[i])
            ans += 1
        else:
            L[dp[i]] = A[i]

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
