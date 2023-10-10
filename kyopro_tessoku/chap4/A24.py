import io
import sys


def debug_input():
    _INPUT = """\
6
2 3 1 6 4 5
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(2N)
def main():

    N = int(input())
    A = list(map(int, input().split()))

    dp = [0] * (N + 1)
    dp[0] = 1

    # 動的計画法
    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))

if __name__ == "__main__":
    # debug_input()
    main()
