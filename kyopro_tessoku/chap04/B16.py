import io
import sys


def debug_input():
    _INPUT = """\
6
30 10 60 10 60 50
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N)
def main():
    N = int(input())
    h = list(map(int, input().split()))

    dp = [0] * N
    dp[1] = abs(h[1] - h[0])

    for i_pos in range(2, N):
        route_1 = dp[i_pos - 1] + abs(h[i_pos - 1] - h[i_pos])
        route_2 = dp[i_pos - 2] + abs(h[i_pos - 2] - h[i_pos])
        dp[i_pos] = min(route_1, route_2)

    print(dp[N-1])


if __name__ == "__main__":
    # debug_input()
    main()
