import io
import sys


def debug_input():
    _INPUT = """\
    8 2 3
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(30)
def main():
    N, A, B = map(int, input().split())

    dp = [None] * (N + 1)

    for i in range(N + 1):
        if i < A:
            dp[i] = False
        elif not dp[i - A]:
            dp[i] = True
        elif i >= B and dp[i - B] == False:
            dp[i] = True
        else:
            dp[i] = False

    # 出力
    if dp[N]:
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    # debug_input()
    main()
