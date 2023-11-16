import io
import sys


def debug_input():
    _INPUT = """\
3
10 40 70
20 50 80
30 60 90
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    happiness = [[0 for i in range(3)] for j in range(N + 1)]

    for i_day in range(1, N + 1):
        a, b, c = map(int, input().split())

        act_1 = happiness[i_day - 1][1] + a
        act_2 = happiness[i_day - 1][2] + a
        happiness[i_day][0] = max(act_1, act_2)

        act_1 = happiness[i_day - 1][0] + b
        act_2 = happiness[i_day - 1][2] + b
        happiness[i_day][1] = max(act_1, act_2)

        act_1 = happiness[i_day - 1][0] + c
        act_2 = happiness[i_day - 1][1] + c
        happiness[i_day][2] = max(act_1, act_2)

    print(max(happiness[N]))


if __name__ == "__main__":
    # debug_input()
    main()
