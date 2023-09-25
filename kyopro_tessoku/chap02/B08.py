import io
import sys


def debug_input():
    _INPUT = """\
    5
    1 3
    2 5
    3 4
    2 6
    3 3
    3
    1 3 3 6
    1 5 2 6
    1 3 3 5
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N+XY+Q)
def main():
    X_MAX = 1500
    Y_MAX = 1500

    world = [[0] * (X_MAX + 1) for _ in range(Y_MAX + 1)]
    world_sum = [[0] * (X_MAX + 1) for _ in range(Y_MAX + 1)]
    N = int(input())

    for _ in range(N):
        lx, ly = map(int, input().split())
        world[ly][lx] += 1

    for y in range(1, Y_MAX + 1):
        for x in range(1, X_MAX + 1):
            world_sum[y][x] = world_sum[y][x - 1] + world[y][x]

    for x in range(1, X_MAX + 1):
        for y in range(1, Y_MAX + 1):
            world_sum[y][x] += world_sum[y - 1][x]

    Q = int(input())
    for _ in range(Q):
        result = 0
        A, B, C, D = map(int, input().split())
        result = (
            world_sum[D][C]
            - world_sum[D][A - 1]
            - world_sum[B - 1][C]
            + world_sum[B - 1][A - 1]
        )
        print(result)


if __name__ == "__main__":
    # debug_input()
    main()
