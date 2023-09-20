import io
import sys


def debug_input():
    _INPUT = """\
10000000
"""

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N)
def main():
    N = input()
    result = 0
    bit = len(N)

    for i in range(bit):
        result += int(N[bit - i - 1]) * 2**i

    print(result)


if __name__ == "__main__":
    # debug_input()
    main()
