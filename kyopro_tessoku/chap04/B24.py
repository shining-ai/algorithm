import bisect
import io
import sys


def debug_input():
    _INPUT = """\
5
30 50
10 30
40 60
50 20
40 70
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(2N)
def main():
    N = int(input())

    ans = 0
    L = [0]
    dp = [0] * (N + 1)

    X_Y = [list(map(int, input().split())) for _ in range(N)]
    X_Y.sort(key=lambda x: (x[0], -x[1]))
    X_Y.insert(0, [0, 0])

    # 動的計画法
    for i in range(1, N + 1):
        combo = bisect.bisect_left(L, X_Y[i][1])
        dp[i] = combo

        if combo > ans:
            L.append(X_Y[i][1])
            ans = combo
        else:
            L[combo] = min(L[combo], X_Y[i][1])

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
