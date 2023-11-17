import io
import sys


def debug_input():
    _INPUT = """\
3 8
3 30
4 50
5 60
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, W = map(int, input().split())
    dp = [[None for i in range(100000 + 1)] for j in range(N + 1)]
    dp[0][0] = 0

    for i_goods in range(1, N + 1):
        w, v = map(int, input().split())
        for i_value in range(100000 + 1):
            if dp[i_goods - 1][i_value] != None:
                if dp[i_goods][i_value] == None:
                    dp[i_goods][i_value] = dp[i_goods - 1][i_value]
                else:
                    dp[i_goods][i_value] = min(
                        dp[i_goods][i_value], dp[i_goods - 1][i_value]
                    )
                if i_value + v > 100000:
                    continue
                if dp[i_goods][i_value + v] != None:
                    dp[i_goods][i_value + v] = min(
                        dp[i_goods][i_value + v], dp[i_goods - 1][i_value] + w
                    )
                else:
                    dp[i_goods][i_value + v] = dp[i_goods - 1][i_value] + w

    for i in range(100000, -1, -1):
        if dp[N][i] != None and dp[N][i] <= W:
            print(i)
            break

    # print(dp[N])


if __name__ == "__main__":
    # debug_input()
    main()
