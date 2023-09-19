import io
import sys


def debug_input():
    _INPUT = """\
    5 20
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(B - A + 1)
def main():
    A, B = map(int, input().split())

    for i in range(A, B + 1):
        if 100 % i == 0:
            print("Yes")
            exit()
    print("No")


if __name__ == "__main__":
    # debug_input()
    main()
