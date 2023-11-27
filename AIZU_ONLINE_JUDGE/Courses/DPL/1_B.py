import io
import sys


def debug_input():
    _INPUT = """\
5 6
5 4
4 3
8 5
7 3
3 2
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, W = map(int, input().split())
    dp = [[-1] * (W + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for i_item in range(N):
        v, w = map(int, input().split())
        for j_kg in range(W + 1):
            if dp[i_item][j_kg] != -1:
                dp[i_item + 1][j_kg] = max(
                    dp[i_item][j_kg],
                    dp[i_item + 1][j_kg],
                )

                if j_kg + w <= W:
                    dp[i_item + 1][j_kg + w] = max(
                        dp[i_item][j_kg] + v,
                        dp[i_item + 1][j_kg + w],
                    )

    print(max(dp[N]))


if __name__ == "__main__":
    # debug_input()
    main()
