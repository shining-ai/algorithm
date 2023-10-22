import io
import sys


def debug_input():
    _INPUT = """\
    4
    20 10 30 40
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N^2)
def main():
    N = int(input())
    A = list(map(int, input().split()))

    dp = [[None] * (N + 1) for _ in range(N + 1)]

    for i, i_A in enumerate(A):
        dp[N][i + 1] = i_A

    for i in range(N - 1, 0, -1):
        for j in range(1, i + 1):
            if i % 2 == 1:
                dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1])
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1])

    print(dp[1][1])


if __name__ == "__main__":
    # debug_input()
    main()
