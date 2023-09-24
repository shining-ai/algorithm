import io
import sys


def debug_input():
    _INPUT = """\
    10
    7
    0 3
    2 4
    1 3
    0 3
    5 6
    5 6
    5 10
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N + T)
def main():
    T = int(input())
    N = int(input())

    workers = [0] * (T + 1)

    for _ in range(N):
        L, R = map(int, input().split())
        workers[L] += 1
        workers[R] -= 1

    for i_d in range(1, T + 1):
        workers[i_d] += workers[i_d - 1]

    workers.pop(-1)
    for i_worker in workers:
        print(i_worker)


if __name__ == "__main__":
    # debug_input()
    main()
