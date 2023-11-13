import io
import math
import sys


def debug_input():
    _INPUT = """\
    2 3 4
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, M, K = map(int, input().split())
    # dp[i][j]: 前からi個を使って、合計がjになる組み合わせの数
    # (1 1)1, (1 2)1, (1 3)1, (1 4)0
    # (2 1)0, (2 2)1, (2 3)2, (2 4)3
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(K):
            for k in range(1, M + 1):
                if j + k <= K:
                    dp[i + 1][j + k] += dp[i][j]

    ans = 0
    for i in range(1, K + 1):
        ans += dp[N][i]
        ans %= 998244353
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
