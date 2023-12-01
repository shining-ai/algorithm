import io
import sys


def debug_input():
    _INPUT = """\
2 20
5 9
4 10
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, W = map(int, input().split())

    dp = [[W + 1] * ((N + 1) * 100) for _ in range(N + 1)]
    dp[0][0] = 0

    for i_item in range(1, N + 1):
        v, w = map(int, input().split())
        for i_value in range((N + 1) * 100):
            if dp[i_item - 1][i_value] != W + 1:
                dp[i_item][i_value] = min(
                    dp[i_item - 1][i_value],
                    dp[i_item][i_value],
                )
                if dp[i_item - 1][i_value] + w <= W:
                    dp[i_item][i_value + v] = min(
                        dp[i_item - 1][i_value] + w,
                        dp[i_item][i_value + v],
                    )

    for i in range(N * 100, -1, -1):
        if dp[N][i] <= W:
            print(i)
            break


if __name__ == "__main__":
    # debug_input()
    main()
