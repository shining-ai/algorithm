import io
import sys


def debug_input():
    _INPUT = """\
15 6
1 2 7 8 12 50
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    dp = [50001] * (N + 1)
    dp[0] = 0

    for i_c in reversed(C):
        for i_n in range(N + 1):
            if i_n + i_c > N:
                break
            dp[i_n + i_c] = min(dp[i_n + i_c], dp[i_n] + 1)

    print(dp[N])


if __name__ == "__main__":
    # debug_input()
    main()
