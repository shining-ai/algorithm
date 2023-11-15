import io
import sys


def debug_input():
    _INPUT = """\
10 4
40 10 20 70 80 10 20 70 80 60
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))

    h.insert(0, 0)
    cost = [10**9] * (N + 1)
    cost[1] = 0

    for i_next in range(2, N + 1):
        for i_jump in range(1, K + 1):
            if i_next - i_jump <= 0:
                break
            route = cost[i_next - i_jump] + abs(h[i_next - i_jump] - h[i_next])
            cost[i_next] = min(route, cost[i_next])

    print(cost[N])


if __name__ == "__main__":
    # debug_input()
    main()
