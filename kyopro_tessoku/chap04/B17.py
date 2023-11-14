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

    ans = [N]

    i = N - 1
    while i > 0:
        if dp[i] == dp[i - 1] + abs(h[i] - h[i - 1]):
            ans.insert(0, i)
            i -= 1
        else:
            ans.insert(0, i - 1)
            i -= 2

    print(len(ans))
    for i in ans:
        print(i, end=" ")
    print()

if __name__ == "__main__":
    # debug_input()
    main()
