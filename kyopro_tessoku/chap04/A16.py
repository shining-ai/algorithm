import io
import sys


def debug_input():
    _INPUT = """\
    10
    1 19 75 37 17 16 33 18 22
    41 28 89 74 98 43 42 31
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N)
def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    arrive_time = [0] * N

    arrive_time[1] = A.pop(0)

    for i in range(N - 2):
        route_a = A[i] + arrive_time[i + 1]
        route_b = B[i] + arrive_time[i]
        arrive_time[i + 2] = min(route_a, route_b)

    print(arrive_time[-1])


if __name__ == "__main__":
    # debug_input()
    main()
