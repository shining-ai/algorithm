import io
import sys


def debug_input():
    _INPUT = """\
    2
    5 8
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N)
def main():
    N = int(input())
    A = list(map(int, input().split()))

    XOR_sum = A[0]
    for i in range(1, N):
        XOR_sum ^= A[i]

    if XOR_sum == 0:
        print("Second")
    else:
        print("First")


if __name__ == "__main__":
    # debug_input()
    main()
