import io
import sys


def debug_input():
    _INPUT = """\
    7 10
    11 12 16 22 27 28 31
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N+log10^9)
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    tmp = 1
    for i in range(N - 1):
        for j in range(tmp, N):
            if A[j] - A[i] > K:
                ans += j - i - 1
                tmp = j
                break
            elif j == N - 1:
                ans += j - i
                tmp = j
                break

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
