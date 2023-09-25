import io
import sys


def debug_input():
    _INPUT = """\
    5 5
    2 0 0 5 1
    1 0 3 0 0
    0 8 5 0 2
    4 1 0 0 6
    0 9 2 7 0
    2
    2 2 4 5
    1 1 5 5
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(HW + Q)
def main():
    H, W = map(int, input().split())
    X_sum = [[0] * (W + 1) for _ in range(H + 1)]
    X = [list(map(int, input().split())) for _ in range(H)]

    for i_h in range(1, H + 1):
        for i_w in range(1, W + 1):
            X_sum[i_h][i_w] = X_sum[i_h][i_w - 1] + X[i_h - 1][i_w - 1]

    for i_w in range(1, W + 1):
        for i_h in range(1, H + 1):
            X_sum[i_h][i_w] += X_sum[i_h - 1][i_w]

    Q = int(input())
    for _ in range(Q):
        result = 0
        A, B, C, D = map(int, input().split())
        result = (
            X_sum[C][D]
            - X_sum[A - 1][D]
            - X_sum[C][B - 1]
            + X_sum[A - 1][B - 1]
        )
        print(result)


if __name__ == "__main__":
    # debug_input()
    main()
