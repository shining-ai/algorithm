import io
import sys


def debug_input():
    _INPUT = """\
    7
    2 4 4 7 6 7
    3 5 6 7 7 7
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(2N)
def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.insert(0, 0)
    B.insert(0, 0)

    # dp = [0] * (N + 1)
    dp = [-(10**9)] * (N + 1)
    dp[1] = 0

    for i_pos in range(1, N):
        dp[A[i_pos]] = max(dp[A[i_pos]], dp[i_pos] + 100)
        dp[B[i_pos]] = max(dp[B[i_pos]], dp[i_pos] + 150)

    print(dp[N])



if __name__ == "__main__":
    # debug_input()
    main()
