import io
import sys


def debug_input():
    _INPUT = """\
6 15
6 5
5 6
6 4
6 6
3 5
7 2
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, W = map(int, input().split())
    dp = [[-1 for i in range(W + 1)] for j in range(N + 1)]
    dp[0][0] = 0

    for i_goods in range(1, N + 1):
        w, v = map(int, input().split())
        for i_weight in range(W + 1):
            if dp[i_goods - 1][i_weight] != -1:
                dp[i_goods][i_weight] = max(
                    dp[i_goods - 1][i_weight], dp[i_goods][i_weight]
                )
                if i_weight + w <= W:
                    dp[i_goods][i_weight + w] = max(
                        dp[i_goods - 1][i_weight] + v,
                        dp[i_goods][i_weight + w],
                    )

    print(max(dp[N]))


if __name__ == "__main__":
    # debug_input()
    main()
