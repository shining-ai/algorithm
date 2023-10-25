import io
import sys


def debug_input():
    _INPUT = """\
    4 30
    20 30
    10 40
    50 10
    30 60
    """

    sys.stdin = io.StringIO(_INPUT)


def get_score(A, B, a, b, K):
    res = 0
    for i in range(len(A)):
        if a <= A[i] <= a + K and b <= B[i] <= b + K:
            res += 1
    return res


# 計算量: O(N)
def main():
    N, K = map(int, input().split())
    A = []
    B = []

    ans = 0

    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    for i_a in range(101):
        for j_b in range(101):
            res = get_score(A, B, i_a, j_b, K)
            ans = max(ans, res)

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
