import io
import sys


def debug_input():
    _INPUT = """\
3 7
2 2 3
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N)
def main():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)

    dp = [[-1] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(1, N + 1):
        for i_sum in range(S + 1):
            if dp[i - 1][i_sum] != -1:
                dp[i][i_sum] = dp[i - 1][i_sum]
                if i_sum + A[i] <= S:
                    dp[i][i_sum + A[i]] = i

    ans = []
    if dp[N][S] != -1:
        while S > 0:
            ans.append(dp[N][S])
            S = S - A[dp[N][S]]
        print(len(ans))
        for a in reversed(ans):
            print(a, end=" ")
        print()
    else:
        print(-1)


if __name__ == "__main__":
    # debug_input()
    main()
