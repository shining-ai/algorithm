import io
import sys


def debug_input():
    _INPUT = """\
4
10 30 40 20
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    h = list(map(int, input().split()))

    h.insert(0, 0)
    cost = [0] * (N + 1)
    cost[2] = abs(h[2] - h[1])

    for i in range(3, N + 1):
        route1 = cost[i - 1] + abs(h[i - 1] - h[i])
        route2 = cost[i - 2] + abs(h[i - 2] - h[i])
        cost[i] = min(route1, route2)

    print(cost[N])


if __name__ == "__main__":
    # debug_input()
    main()
