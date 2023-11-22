import io
import sys


def debug_input():
    _INPUT = """\
4
0 0
0 1
1 0
1 1
    """

    sys.stdin = io.StringIO(_INPUT)


def calc_dist(X, Y, from_pos, to_pos):
    dist = (
        (X[from_pos] - X[to_pos]) ** 2 + (Y[from_pos] - Y[to_pos]) ** 2
    ) ** 0.5
    return dist


# 計算量: O(ST)
def main():
    N = int(input())
    X = [None] * N
    Y = [None] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())

    dp = [[10**10] * N for i in range(2**N)]
    dp[0][0] = 0

    for i in range(2**N):
        for i_from in range(N):
            if dp[i][i_from] < 10**10:
                for i_to in range(N):
                    if (i // (2**i_to)) % 2 == 0:
                        dist = calc_dist(X, Y, i_from, i_to)
                        dp[i + (2**i_to)][i_to] = min(
                            dp[i + (2**i_to)][i_to],
                            dp[i][i_from] + dist,
                        )

    print(dp[(2**N) - 1][0])


if __name__ == "__main__":
    debug_input()
    main()
