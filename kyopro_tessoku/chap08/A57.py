import io
import sys


def debug_input():
    _INPUT = """\
    7 4
2 4 1 7 6 5 3
1 1
1 5
2 13
5 999999999
    """
    sys.stdin = io.StringIO(_INPUT)


# O(NlogN)
def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    LEVELS = 30
    dp = [[None] * N for i in range(LEVELS)]
    for i in range(0, N):
        dp[0][i] = A[i] - 1
    for d in range(1, LEVELS):
        for i in range(0, N):
            dp[d][i] = dp[d - 1][dp[d - 1][i]]

    for _ in range(Q):
        X, Y = map(int, input().split())
        current_pos = X - 1
        for d in range(LEVELS - 1, -1, -1):
            if (Y >> d) & 1:
                current_pos = dp[d][current_pos]

        print(current_pos + 1)


if __name__ == "__main__":
    # debug_input()
    main()
