import io
import sys


def debug_input():
    _INPUT = """\
    5 5 2
    1 1 3 3
    2 2 4 4
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(HW + N)
def main():
    H, W, N = map(int, input().split())
    X = [[0] * (W + 2) for _ in range(H + 2)]

    for _ in range(N):
        A, B, C, D = map(int, input().split())
        X[A][B] += 1
        X[C + 1][D + 1] += 1
        X[A][D + 1] -= 1
        X[C + 1][B] -= 1

    for i_h in range(1, H + 1):
        for i_w in range(1, W + 1):
            X[i_h][i_w] += X[i_h][i_w - 1]

    for i_w in range(1, W + 1):
        for i_h in range(1, H + 1):
            X[i_h][i_w] += X[i_h - 1][i_w]

    for i_h in range(1, H + 1):
        for i_w in range(1, W + 1):
            print(X[i_h][i_w], end=" ")
        print()


if __name__ == "__main__":
    # debug_input()
    main()
