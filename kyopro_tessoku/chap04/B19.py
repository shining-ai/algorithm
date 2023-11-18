import io
import sys


def debug_input():
    _INPUT = """\
3 100
55 2
75 3
40 2

    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N)
def main():
    N, W = map(int, input().split())
    dp = [[10**10] * (100001) for _ in range(N + 1)]

    dp[0][0] = 0
    for i_item in range(1, N + 1):
        w, v = map(int, input().split())
        for i_value in range(100001):
            if dp[i_item - 1][i_value] <= 10**9:
                dp[i_item][i_value] = min(
                    dp[i_item - 1][i_value], dp[i_item][i_value]
                )
            if i_value + v > 100000:
                continue
            else:
                dp[i_item][i_value + v] = min(
                    dp[i_item - 1][i_value] + w, dp[i_item][i_value + v]
                )

    for i in range(100000, 0, -1):
        if dp[N][i] <= W:
            print(i)
            break


if __name__ == "__main__":
    # debug_input()
    main()
