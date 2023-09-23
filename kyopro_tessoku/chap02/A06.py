import io
import sys


def debug_input():
    _INPUT = """\
    10 5
    8 6 9 1 2 1 10 100 1000 10000
    2 3
    1 4
    3 9
    6 8
    1 10
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N + Q)
def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    prefix_sum = [0]

    for i_a in A:
        prefix_sum.append(prefix_sum[-1] + i_a)

    for i_q in range(Q):
        start_day, end_day = map(int, input().split())
        result = prefix_sum[end_day] - prefix_sum[start_day - 1]
        print(result)


if __name__ == "__main__":
    # debug_input()
    main()
