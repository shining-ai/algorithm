import io
import sys


def debug_input():
    _INPUT = """\
11
programming
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(ST)
def main():
    N = int(input())
    S = input()

    dp = [[None] * N for i in range(N)]
    for i in range(N):
        dp[i][i] = 1
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            dp[i][i + 1] = 2
        else:
            dp[i][i + 1] = 1

    for LEN in range(2, N):
        for l in range(N - LEN):
            r = l + LEN
            if S[l] == S[r]:
                dp[l][r] = max(
                    dp[l + 1][r - 1] + 2, dp[l + 1][r], dp[l][r - 1]
                )
            else:
                dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])

    print(dp[0][N - 1])


if __name__ == "__main__":
    debug_input()
    main()
