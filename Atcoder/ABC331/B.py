import io
import sys


def debug_input():
    _INPUT = """\
99 600 800 1200


    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, S, M, L = map(int, input().split())

    dp = [None] * 120
    dp[0] = 0
    ans = 10**9

    for i in range(120):
        if dp[i] == None:
            continue
        if i + 6 < 120:
            if dp[i + 6] == None:
                dp[i + 6] = dp[i] + S
            else:
                dp[i + 6] = min(
                    dp[i + 6],
                    dp[i] + S,
                )

    for i in range(120):
        if dp[i] == None:
            continue
        if i + 8 < 120:
            if dp[i + 8] == None:
                dp[i + 8] = dp[i] + M
            else:
                dp[i + 8] = min(
                    dp[i + 8],
                    dp[i] + M,
                )

    for i in range(120):
        if dp[i] == None:
            continue
        if i + 12 < 120:
            if dp[i + 12] == None:
                dp[i + 12] = dp[i] + L
            else:
                dp[i + 12] = min(
                    dp[i + 12],
                    dp[i] + L,
                )

    for i in range(N, 120):
        if dp[i] != None:
            ans = min(ans, dp[i])

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
