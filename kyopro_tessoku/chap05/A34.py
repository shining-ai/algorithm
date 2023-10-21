import io
import sys


def debug_input():
    _INPUT = """\
    2 2 3
    7 8
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N)
def main():
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))

    groudy = [None] * 100001

    for i in range(100001):
        Transit = [False, False, False]
        if i - X >= 0:
            Transit[groudy[i - X]] = True
        if i - Y >= 0:
            Transit[groudy[i - Y]] = True

        if Transit[0] == False:
            groudy[i] = 0
        elif Transit[1] == False:
            groudy[i] = 1
        else:
            groudy[i] = 2

    XOR_sum = 0
    for i in range(N):
        XOR_sum ^= groudy[A[i]]

    if XOR_sum == 0:
        print("Second")
    else:
        print("First")


if __name__ == "__main__":
    # debug_input()
    main()
