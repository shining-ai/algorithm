import io
import sys


def debug_input():
    _INPUT = """\
    4
    + 57
    + 43
    * 100
    - 1
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(2N)
def main():
    N = int(input())
    result = 0

    for _ in range(N):
        T, A = input().split()
        if T == "+":
            result += int(A)
        elif T == "-":
            result -= int(A)
        elif T == "*":
            result *= int(A)

        if result < 0:
            result += 10000
        result %= 10000
        print(result)


if __name__ == "__main__":
    # debug_input()
    main()
