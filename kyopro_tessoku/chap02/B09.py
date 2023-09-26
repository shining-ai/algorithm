import io
import sys


def debug_input():
    _INPUT = """\
    2
    1 1 3 3
    2 2 4 4
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(XY+N)
def main():
    X_MAX = 1501
    Y_MAX = 1501
    N = int(input())
    world = [[0] * (X_MAX + 2) for _ in range(Y_MAX + 2)]

    for _ in range(N):
        A, B, C, D = map(int, input().split())
        world[B][A] += 1
        world[D][C] += 1
        world[B][C] -= 1
        world[D][A] -= 1

    for i_y in range(Y_MAX + 1):
        for i_x in range(1, X_MAX + 1):
            world[i_y][i_x] += world[i_y][i_x - 1]

    for i_x in range(X_MAX + 1):
        for i_y in range(1, Y_MAX + 1):
            world[i_y][i_x] += world[i_y - 1][i_x]

    ans = 0
    for i_y in range(Y_MAX + 1):
        for i_x in range(X_MAX + 1):
            if world[i_y][i_x] > 0:
                ans += 1

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
